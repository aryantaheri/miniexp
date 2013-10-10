"""Custom topology example

Two directly connected switches plus a host for each switch:

   hs1,hs2 --- ss1 --- st1 --- ht1,ht2
                |       |
                -- sk1 --
                    |
                 hk1,hk2

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=h6s3topo' from the command line.
"""

from mininet.topo import Topo

class H6S3Topo( Topo ):
    "Simple UNINETT SDN Lab topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        s7 = self.addSwitch( 's7' )

        h3 = self.addHost( 'h3' )
        h4 = self.addHost( 'h4' )
        s8 = self.addSwitch( 's8' )

        h5 = self.addHost( 'h5' )
        h6 = self.addHost( 'h6' )
        s9 = self.addSwitch( 's9' )


        # Add links
        self.addLink( h1, s7 )
        self.addLink( h2, s7 )

        self.addLink( h3, s8 )
        self.addLink( h4, s8 )

        self.addLink( h5, s9 )
        self.addLink( h6, s9 )

        self.addLink( s7, s8 )
        self.addLink( s7, s9 )
        self.addLink( s8, s9 )


topos = { 'h6s3topo': ( lambda: H6S3Topo() ) }
