from mininet.topo import Topo

class Edge1(Topo):
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

class Edge2(Topo):
    "Edge topo"

    def __init__( self, enable_all = True ):
        "Create custom topo for edge switches."
        Topo.__init__( self )

        h1 = self.addHost("h1",
                          ip="10.0.0.20/24")

        h2 = self.addHost("h2",
                          ip="10.0.0.21/24")



        sA = self.addSwitch("s6")
#        sB = self.addSwitch("s6") 
#        sC = self.addSwitch("s7") 
#        sD = self.addSwitch("s8")                                                                                                                                                                                 
        self.addLink(h1, sA)
        self.addLink(h2,sA)


class Edge3(Topo):
    "Edge topo"

    def __init__( self, enable_all = True ):
        "Create custom topo for edge switches."
        Topo.__init__( self )

        h1 = self.addHost("h1",
                          ip="10.0.0.30/24")

        h2 = self.addHost("h2",
                          ip="10.0.0.31/24")

        sA = self.addSwitch("s7")
        sB = self.addSwitch("s8")
#        sC = self.addSwitch("s7")
#        sD = self.addSwitch("s8")
        self.addLink(h1, sA)
        self.addLink(h2, sB)
        self.addLink(sA, sB)


class Edge4(Topo):
    "Edge topo"

    def __init__( self, enable_all = True ):
        "Create custom topo for edge switches."
        Topo.__init__( self )

        h1 = self.addHost("h1", ip="10.0.0.40/24")
        sA = self.addSwitch("s104")
        self.addLink(h1, sA)

class Edge5(Topo):
    "Edge topo"

    def __init__( self, enable_all = True ):
        "Create custom topo for edge switches."
        Topo.__init__( self )

        h1 = self.addHost("h1", ip="10.0.0.50/24")
        sA = self.addSwitch("s105")
        self.addLink(h1, sA)


topos = { 'edge1': ( lambda: Edge1() ), 'edge2': ( lambda: Edge2() ), 'edge3': ( lambda: Edge3() ), 'edge4': ( lambda: Edge4() ), 'edge5': ( lambda: Edge5() ) }
