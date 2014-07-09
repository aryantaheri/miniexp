"""
Core1: 
       h1 --- sA      sB --- h2  
               | \  /  |
               |  \/   |         
               |  /\   |    
               | /  \  |
              sC ---- sD

Core2: 

h1 --- sA ----- sB --- sD ----- sF --- h2
        |                        |
        |                        |
          ----- sC --- sE ----- 



"""

from mininet.topo import Topo

class Core1(Topo):
    "Core1 Topo"

    def __init__( self, enable_all = True ):
        "Create custom topo."

        Topo.__init__( self )

#        h1 = self.addHost("h1")
#        h2 = self.addHost("h2")
#        h3 = self.addHost("h3",                                                                                                                                                                                  
#                          ip="172.31.3.100/24",                                                                                                                                                                  
#                          defaultRoute="gw 172.31.3.1")                                                                                                                                                          
#        h4 = self.addHost("h4",                                                                                                                                                                                  
#                          ip="172.31.4.100/24",                                                                                                                                                                  
#                          defaultRoute="gw 172.31.4.1") 

        sA = self.addSwitch("s1")
        sB = self.addSwitch("s2")
        sC = self.addSwitch("s3")
        sD = self.addSwitch("s4")

#        self.addLink(h1, sA)
#        self.addLink(h2, sB)
#        self.addLink(h3, sC)                           
#        self.addLink(h4, sD) 

        self.addLink(sB, sD)
        self.addLink(sB, sC)
        self.addLink(sD, sC)
        self.addLink(sC, sA)
        self.addLink(sA, sD)


class Core2(Topo):
    "Core2 Topo"

    def __init__( self, enable_all = True ):
        "Create custom topo."

        Topo.__init__( self )
#        h1 = self.addHost("h1")                                                                                                                                                                                   
#        h2 = self.addHost("h2")                                                                                                                                                                                   
#        h3 = self.addHost("h3",                                                                                                                                                                                  
#                          ip="172.31.3.100/24",                                                                                                                                                                  
#                          defaultRoute="gw 172.31.3.1")                                                                                                                                                           
#        h4 = self.addHost("h4",                                                                                                                                                                                  
#                          ip="172.31.4.100/24",                                                                                                                                                                   
#                          defaultRoute="gw 172.31.4.1")                                                                                                                                                           

        sA = self.addSwitch("s21")
        sB = self.addSwitch("s22")
        sC = self.addSwitch("s23")
        sD = self.addSwitch("s24")
        sE = self.addSwitch("s25")
        sF = self.addSwitch("s26")

#        self.addLink(h1, sA)                                                                                                                                                                                     
#        self.addLink(h2, sB)                                                                                                                                                                                     
#        self.addLink(h3, sC)                                                                                                                                                                                     
#        self.addLink(h4, sD)                                                                                                                                                                                       

        self.addLink(sA, sB)
        self.addLink(sA, sC)
        self.addLink(sB, sD)
        self.addLink(sC, sE)
        self.addLink(sD, sF)
        self.addLink(sE, sF)


topos = { 'core1': ( lambda: Core1() ), 'core2': ( lambda: Core2() )}
