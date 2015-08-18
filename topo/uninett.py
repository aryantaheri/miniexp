"""
Read graphs in Pajek format.

See http://vlado.fmf.uni-lj.si/pub/networks/pajek/doc/draweps.htm
for format information.

This implementation handles only directed and undirected graphs including
those with self loops and parallel edges.  

Adapted by Morten Knutsen (morten.knutsen@uninett.no).
Adapted by Aryan for Mininet
"""
__author__ = """Aric Hagberg (hagberg@lanl.gov)"""
#    Copyright (C) 2008 by 
#    Aric Hagberg <hagberg@lanl.gov>
#    Dan Schult <dschult@colgate.edu>
#    Pieter Swart <swart@lanl.gov>
#    Distributed under the terms of the GNU Lesser General Public License
#    http://www.gnu.org/copyleft/lesser.html
import networkx
import math
import urllib
from functools import partial
from networkx.utils import is_string_like
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.link import TCLink

class Uninett(Topo):
    "Uninett Topo"

    uninett_switches = {}
    graph = None

    def __init__( self, update_topo = False, url = 'https://drift.uninett.no/nett/ip-nett/isis-uninett.net' ):
        Topo.__init__( self )
        
        if (update_topo):
            topo_file_path = download_topo(url)
        else:
            topo_file_path = '/tmp/isis-uninett.net'
        
        global graph 
        self.graph = self.read_pajek(topo_file_path)
        #self.set_switch_config(G)
        
    def get_graph(self):
        return self.graph

    def read_pajek(self, path):
        """Read graph in pajek format from path. Returns an XGraph or XDiGraph.
        """
        fh=open(path,mode='r')
        lines = fh.readlines()
        G=self.parse_pajek(lines)
        return G

    def parse_pajek(self, lines):
        """Parse pajek format graph from string or iterable.."""
        import shlex
        if is_string_like(lines): lines=iter(lines.split('\n'))
        lines = iter([line.rstrip('\n') for line in lines])
        G=networkx.DiGraph() # are multiedges allowed in Pajek?
        G.node_attr={} # dictionary to hold node attributes
        directed=True # assume this is a directed network for now
        while lines:
            try:
                l=lines.next()
                l=l.lower()
            except: #EOF
                break
            if l.startswith("#"):
                continue
            if l.startswith("*network"):
                label,name=l.split()
                G.name=name
            if l.startswith("*vertices"):
                nodelabels={}
                l,nnodes=l.split()
                while not l.startswith("*arcs"):
                    if l.startswith('#'):
                        l = lines.next()
                        l = l.lower()
                        continue
                    if l.startswith('*'):
                        l = lines.next()
                        l = l.lower()
                        continue
                    splitline=shlex.split(l)
                    #print splitline
                    id, label = splitline[0:2]
                    G.add_node(label)
                    nodelabels[id]=label
                    G.node_attr[label]={'id':id}                
                    if len(splitline) > 2:
                        id,label,x,y=splitline[0:4]                
                        G.node_attr[label]={'id':id,'x':x,'y':y}
                    extra_attr=zip(splitline[4::2],splitline[5::2])
                    #print extra_attr
                    G.node_attr[label].update(extra_attr)
                    self.add_switch(id, label, x, y)
                    l = lines.next()
                    l = l.lower()
            if l.startswith("*arcs"):
                for l in lines:
                    if not l: break
                    if l.startswith('#'): continue
                    splitline=shlex.split(l)
                    ui,vi,w=splitline[0:3]
                    bw=splitline[6]
                    u=nodelabels.get(ui,ui)
                    v=nodelabels.get(vi,vi)
                    edge_data={'value':float(w)}
                    extra_attr=zip(splitline[3::2],splitline[4::2])
                    edge_data.update(extra_attr)
                    self.add_switch_link(ui, vi, w, bw)
                    if G.has_edge(u,v):
                        if G[u][v]['value'] > float(w):
                            G.add_edge(u,v,edge_data)
                    else:
                        G.add_edge(u,v,edge_data)
        if not G.name:
            raise Exception("No graph definition found")
        if len(G.nodes()) == 0:
            raise Exception("No graph definition found")
        return G

    def add_switch(self, id, label, x, y):
        sw = self.addSwitch('s%s' % id)
#        sw.vsctl('set', sw, 'other_config:label=%s' % label)
        print 'Added Sw ', id, sw, {id: sw}
        self.uninett_switches.update({id: sw})
        self.add_host(sw, id)
    
    def add_host(self, sw, host_id):
        host = self.addHost('h%s' % host_id)
        self.addLink(host, sw)
        print 'Added Host %s to Switch %s' % (host, sw)


    def add_switch_link(self, src_id, dst_id, weight, bw):
        src = self.uninett_switches.get(src_id)
        dst = self.uninett_switches.get(dst_id)
        # print src_id, dst_id
        # Mininet bw is specified in Mbps
        # UNINETT topo link capacity is in Kbps
        # Scale: 1:100
        if bw:
            linkopts = dict(bw=int(bw)/100000)
        print 'Added inter-switch link: %s -> %s (options: %s)' %(src, dst, linkopts) 
        if not src or not dst:
            print 'src %s or dst %s not available' % (src, dst)
            return
        self.addLink(src, dst, **linkopts)
        

    def set_link_load( self ):
        print 'Not there'
        

def set_switch_config(net, cli, topo, G):
#        print 'Node attributes: '                                                                                   
#        print G.node_attr 
    for node in topo.nodes():
        if topo.isSwitch(node):
            print node
            print topo.nodeInfo(node)
            node_obj = net.get(node)
            print node_obj
            print node_obj.bridgeOpts()
#        for sw_label in G.node_attr:
#            self.do_sh('ovs-vsctl set bridge %s other_config:{label=%s,x=%s,y=%s}' % (G.node_attr[sw_label][id], sw_label, G.node_attr[sw_label][x], G.node_attr[sw_label][y])) 

def download_topo( url = 'https://drift.uninett.no/nett/ip-nett/isis-uninett.net' ):
    filename = urllib.urlretrieve ( url, "/tmp/isis-uninett.net")
    print filename
    return filename[0]

def download_link_load( url = 'https://drift.uninett.no/nett/ip-nett/load-now' ):
    filename = urllib.urlretrieve ( url, "/tmp/uninett-load-now")
    print filename
    return filename[0]

if __name__ == '__main__':
    topology = Uninett()
    net = Mininet( topo=topology, link=TCLink, controller=partial( RemoteController, ip='192.168.10.15', port=6633 ), switch=OVSSwitch)
    net.start()
#    set_switch_config(net, None, topology, topology.get_graph())
    CLI( net )
    net.stop()


topos = { 'uninett': Uninett }
