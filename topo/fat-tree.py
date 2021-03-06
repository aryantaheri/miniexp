"""
@article{Al-Fares:2008:SCD:1402946.1402967,
 author = {Al-Fares, Mohammad and Loukissas, Alexander and Vahdat, Amin},
 title = {A Scalable, Commodity Data Center Network Architecture},
 journal = {SIGCOMM Comput. Commun. Rev.},
 issue_date = {October 2008},
 volume = {38},
 number = {4},
 month = aug,
 year = {2008},
 issn = {0146-4833},
 pages = {63--74},
 numpages = {12},
 url = {http://doi.acm.org/10.1145/1402946.1402967},
 doi = {10.1145/1402946.1402967},
 acmid = {1402967},
 publisher = {ACM},
 address = {New York, NY, USA},
 keywords = {data center topology, equal-cost routing},
} 

Paper:
http://ccr.sigcomm.org/online/files/p63-alfares.pdf

Info:
+ k-port switch
+ k pods
+ each pod contains two layers of k/2 switches (k k-port switch)
+ each lower layer switch connected to k/2 hosts

+ #core switches: (k/2)^2 k-port switches
+ #pod switches: k^2
+ #hosts: k^3/4
+ each core switch has one link to each pod

@author Aryan
"""

from mininet.topo import Topo
import math

class FatTree1(Topo):
    "FatTree1 Topo"

    def __init__( self, k = 4, create_hosts = False, enable_all = True ):
        "Create custom FatTree from Al-fares et al. ."

        Topo.__init__( self )

        num_switches = int(5*math.pow(k, 2)/4)
        num_cores = int(math.pow(k, 2)/4)
        num_aggrs = int(math.pow(k, 2)/2)
        num_edges = int(math.pow(k, 2)/2)
        num_hosts = int(math.pow(k, 3)/4)
        

        cores = []
        aggrs = []
        edges = []
        hid = 0
        sid = 0

        # Create Core switches
        for i in range(num_cores):
            sid += 1
            cores.append(self.addSwitch('s%s' % sid))
            
        # Create K pods
        for i in range(k):
            # Create pod's Aggrs
            pod_aggrs = []
            for j in range(k/2):
                sid += 1
                aggr_sw = self.addSwitch('s%s' % sid)
                pod_aggrs.append(aggr_sw)
                aggrs.append(aggr_sw)
                
                # Connect Aggr to Cores
                # j*(k/2): # previously filled ports = connected core switches to this pod
                #        : index of first core switch to be connected to this aggr switch
                # (j+1)*(k/2): index of last core switch to be connected to this aggr switch
                for l in range(j*(k/2), (j+1)*(k/2)):
                    self.addLink(aggr_sw, cores[l])

            # Create pod's Edges
            for j in range(k/2):
                sid += 1
                edge_sw = self.addSwitch('s%s' % sid)
                edges.append(edge_sw)
                
                # Connects Edge to Aggrs, and Hosts to Edge
                for l in range(k/2):
                    # Connects Edge to Aggrs
                    self.addLink(edge_sw, pod_aggrs[l])
                    
                    if (create_hosts):
                        # Create and connect hosts
                        hid += 1
                        host = self.addHost('h%s' % hid)
                        self.addLink(edge_sw, host)

                
class FatTree2(Topo):
    "FatTree2 Topo: 2 layers of K-port switches (Aggregation, Edge)"
    "author: Haichen Shen (haichen@cs.washington.edu)"

    def __init__( self, k = 4, create_hosts = False, enable_all = True):
        "Simple fat tree"
        Topo.__init__( self )

        aggrs = []
        hid = 0
        sid = 0

        # Create Aggr switches
        for i in range(k/2):
            sid += 1
            aggrs.append(self.addSwitch('s%s' % sid))
            
        # Create Edge switches
        for i in range(k):
            sid += 1
            edge_sw = self.addSwitch('s%s' % sid)

            # Connect Edge to Aggrs
            for j in range(k/2):
                self.addLink(edge_sw, aggrs[j])

            if (create_hosts):
                # Create hosts and connect
                for j in range(k/2):
                    hid += 1
                    host = self.addHost('h%s' % hid)
                    self.addLink(edge_sw, host)

# Note: create_hosts is a boolean, while using mn to create this topology 0 means False, and any other value will be interepreted as create_hosts=True
topos = { 'ft1': ( lambda k, create_hosts: FatTree1(k, create_hosts) ), 'ft2': ( lambda k, create_hosts: FatTree2(k, create_hosts) ) }
