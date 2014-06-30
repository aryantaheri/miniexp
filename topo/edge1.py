from mininet.topo import Topo

class edge1(Topo):
    "Edge topo"

    def __init__( self, enable_all = True ):
        "Create custom topo for edge switches."
        Topo.__init__( self )

        h1 = self.addHost("h1",
                          ip="10.0.0.10/24")

        h2 = self.addHost("h2",
                          ip="10.0.0.11/24")



        sA = self.addSwitch("s5")
#        sB = self.addSwitch("s6")
#        sC = self.addSwitch("s7")
#        sD = self.addSwitch("s8")

        self.addLink(h1, sA)
        self.addLink(h2,sA)
#        self.addLink(h2, sB)
#        self.addLink(h3, sC)
#        self.addLink(h4, sD)
#        self.addLink(sA, sB)
#        self.addLink(sB, sD)
#        self.addLink(sD, sC)
#        self.addLink(sC, sA)
#        self.addLink(sA, sD)

class edge2(Topo):
    "Edge topo"

    def __init__( self, enable_all = True ):
        "Create custom topo for edge switches."
        Topo.__init__( self )

        h1 = self.addHost("h1",
                          ip="10.0.0.20/24")

        h2 = self.addHost("h2",
                          ip="10.0.0.21/24")



        sA = self.addSwitch("s5")
#        sB = self.addSwitch("s6")                                                                                                                                                                                  
#        sC = self.addSwitch("s7")                                                                                                                                                                                  
#        sD = self.addSwitch("s8")                                                                                                                                                                                  

        self.addLink(h1, sA)
        self.addLink(h2,sA)

topos = { 'edge1': ( lambda: edge1() ), 'edge2': ( lambda: edge2() ) }
