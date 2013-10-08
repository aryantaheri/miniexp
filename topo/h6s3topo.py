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
        hs1 = self.addHost( 'hs1' )
        hs2 = self.addHost( 'hs2' )
        ss1 = self.addSwitch( 'ss1' )

        ht1 = self.addHost( 'ht1' )
        ht2 = self.addHost( 'ht2' )
        st1 = self.addSwitch( 'st1' )

        hk1 = self.addHost( 'hk1' )
        hk2 = self.addHost( 'hk2' )
        sk1 = self.addSwitch( 'sk1' )


        # Add links
        self.addLink( hs1, ss1 )
        self.addLink( hs2, ss1 )

        self.addLink( ht1, st1 )
        self.addLink( ht2, st1 )

        self.addLink( hk1, sk1 )
        self.addLink( hk2, sk1 )

        self.addLink( ss1, st1 )
        self.addLink( ss1, sk1 )
        self.addLink( st1, sk1 )


topos = { 'h6s3topo': ( lambda: H6S3Topo() ) }
