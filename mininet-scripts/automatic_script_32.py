"""Custom topology with 32 nodes and 2 hosts

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.

resources: 
	https://mailman.stanford.edu/pipermail/mininet-discuss/2011-July/000420.html
	https://github.com/mininet/mininet/wiki/Introduction-to-Mininet
"""

from mininet.topo import Topo
from mininet.log import setLogLevel, info
from mininet.node import RemoteController
from mininet.net import Mininet
from mininet.link import TCLink
from time import sleep
import sys

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self, delay, bw ):
        "Create custom topo."
        self.delay = delay
        self.bw = bw

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
        switch1 = self.addSwitch( 's1' )
        switch2 = self.addSwitch( 's2' )
        switch3 = self.addSwitch( 's3' )
        switch4 = self.addSwitch( 's4' )
        switch5 = self.addSwitch( 's5' )
        switch6 = self.addSwitch( 's6' )
        switch7 = self.addSwitch( 's7' )
        switch8 = self.addSwitch( 's8' )
        switch9 = self.addSwitch( 's9' )
        switch10 = self.addSwitch( 's10' )
        switch11 = self.addSwitch( 's11' )
        switch12 = self.addSwitch( 's12' )
        switch13 = self.addSwitch( 's13' )
        switch14 = self.addSwitch( 's14' )
        switch15 = self.addSwitch( 's15' )
        switch16 = self.addSwitch( 's16' )
        switch17 = self.addSwitch( 's17' )
        switch18 = self.addSwitch( 's18' )
        switch19 = self.addSwitch( 's19' )
        switch20 = self.addSwitch( 's20' )
        switch21 = self.addSwitch( 's21' )
        switch22 = self.addSwitch( 's22' )
        switch23 = self.addSwitch( 's23' )
        switch24 = self.addSwitch( 's24' )
        switch25 = self.addSwitch( 's25' )
        switch26 = self.addSwitch( 's26' )
        switch27 = self.addSwitch( 's27' )
        switch28 = self.addSwitch( 's28' )
        switch29 = self.addSwitch( 's29' )
        switch30 = self.addSwitch( 's30' )
        switch31 = self.addSwitch( 's31' )
        switch32 = self.addSwitch( 's32' )
        

        # Add links
        self.addLink( leftHost, switch1, bw=self.bw, delay=self.delay )
        self.addLink( switch1, switch2, bw=self.bw, delay=self.delay )
        self.addLink( switch2, switch3, bw=self.bw, delay=self.delay )
        self.addLink( switch2, switch4, bw=self.bw, delay=self.delay )
        self.addLink( switch3, switch7, bw=self.bw, delay=self.delay )
        self.addLink( switch3, switch4, bw=self.bw, delay=self.delay )
        self.addLink( switch4, switch6, bw=self.bw, delay=self.delay )
        self.addLink( switch4, switch5, bw=self.bw, delay=self.delay )
        self.addLink( switch7, switch6, bw=self.bw, delay=self.delay )
        self.addLink( switch7, switch8, bw=self.bw, delay=self.delay )
        self.addLink( switch6, switch8, bw=self.bw, delay=self.delay )
        self.addLink( switch6, switch5, bw=self.bw, delay=self.delay )
        self.addLink( switch5, switch9, bw=self.bw, delay=self.delay )
        self.addLink( switch8, switch9, bw=self.bw, delay=self.delay )
        self.addLink( switch8, switch10, bw=self.bw, delay=self.delay )
        self.addLink( switch9, switch13, bw=self.bw, delay=self.delay )
        self.addLink( switch10, switch11, bw=self.bw, delay=self.delay )
        self.addLink( switch10, switch12, bw=self.bw, delay=self.delay )
        self.addLink( switch11, switch12, bw=self.bw, delay=self.delay )
        self.addLink( switch13, switch12, bw=self.bw, delay=self.delay )
        self.addLink( switch13, switch14, bw=self.bw, delay=self.delay )
        self.addLink( switch12, switch15, bw=self.bw, delay=self.delay )
        self.addLink( switch14, switch15, bw=self.bw, delay=self.delay )
        self.addLink( switch14, switch19, bw=self.bw, delay=self.delay )
        self.addLink( switch14, switch20, bw=self.bw, delay=self.delay )
        self.addLink( switch15, switch16, bw=self.bw, delay=self.delay )
        self.addLink( switch16, switch17, bw=self.bw, delay=self.delay )
        self.addLink( switch16, switch18, bw=self.bw, delay=self.delay )
        self.addLink( switch17, switch18, bw=self.bw, delay=self.delay )
        self.addLink( switch17, switch21, bw=self.bw, delay=self.delay )
        self.addLink( switch18, switch19, bw=self.bw, delay=self.delay )
        self.addLink( switch18, switch22, bw=self.bw, delay=self.delay )
        self.addLink( switch19, switch20, bw=self.bw, delay=self.delay )
        self.addLink( switch19, switch23, bw=self.bw, delay=self.delay )
        self.addLink( switch21, switch24, bw=self.bw, delay=self.delay )
        self.addLink( switch21, switch25, bw=self.bw, delay=self.delay )
        self.addLink( switch22, switch25, bw=self.bw, delay=self.delay )
        self.addLink( switch23, switch25, bw=self.bw, delay=self.delay )
        self.addLink( switch23, switch26, bw=self.bw, delay=self.delay )
        self.addLink( switch24, switch29, bw=self.bw, delay=self.delay )
        self.addLink( switch25, switch27, bw=self.bw, delay=self.delay )
        self.addLink( switch26, switch28, bw=self.bw, delay=self.delay )
        self.addLink( switch26, switch31, bw=self.bw, delay=self.delay )
        self.addLink( switch27, switch29, bw=self.bw, delay=self.delay )
        self.addLink( switch28, switch30, bw=self.bw, delay=self.delay )
        self.addLink( switch29, switch30, bw=self.bw, delay=self.delay )
        self.addLink( switch30, switch31, bw=self.bw, delay=self.delay )
        self.addLink( switch31, switch32, bw=self.bw, delay=self.delay )
        self.addLink( switch32, rightHost, bw=self.bw, delay=self.delay )


def fileOperation(text, i):
    try:
    	f = open('/tmp/ping32.txt', 'a')
	f.write("%s %s\n" % (text, i))
	f.close()
    except IOError:
	print "a je to v ****"

def runPingTest(delay, bw):
    c = RemoteController('c', '172.16.197.137', 6653)
    net = Mininet(topo=MyTopo(delay, bw), link=TCLink, controller=None)
    net.addController(c)
    net.start()
    print "running pingAll() command"
    sleep(5)
    net.pingAll()
    print "httping from h1 to h2"
    h1 = net.get('h1')
    h2 = net.get('h2')
    fileOperation("Starting tests", "")
    i = 15
    while(i > 0):
	print "starting/restating httpserver on host h2"
    	h2.cmd('python -m SimpleHTTPServer 80 &')
    	sleep(2)
	fileOperation("Test number ", i)
	print "printing to the output /tmp/ping32.txt"
    	h1.cmd('httping %s >> /tmp/ping32.txt &' %h2.IP())
    	#result = h1.cmd('httping %s' %h2.IP())
	#fileOperation(result, "")
    	sleep(5)
	fileOperation("Link down", "")
    	print "Link going down"
    	net.configLinkStatus('s2','s4','down')
	#print >>f, "after link down"
    	fileOperation("After link down", "")
    	sleep(20)
    	print "Link going up"
    	fileOperation("After link up", "")
    	net.configLinkStatus('s2','s4','up')
	h1.cmd('kill %httping')
	i = i - 1
	sleep(5)
    print("end of script")
    net.stop()

if __name__ == '__main__':
    if sys.argv[1] == '-h':
        print("Usage: automaticScript.py [OPTION]\n"
            "\t -h \t print this help\n"
            "\t -b \t use bandwith in Mbit/s\n"
            "\t -d \t use delay in ms")
        exit(0)
    elif sys.argv[1] == '-d' and sys.argv[3] == '-b':
        delay = sys.argv[2]
        bw = float(sys.argv[4])
    else:
        print("Invalid command. You must specify both delay (-d) and bandwith (-b). Run -h to see help.")
        exit(0)	
    setLogLevel('info')
    runPingTest(delay, bw)
