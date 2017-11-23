from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.log import setLogLevel, info
from time import sleep
from mininet.node import RemoteController
import sys

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self , delay, be):
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

        # Add links
        self.addLink( leftHost, switch1 , bw=self.bw, delay=self.delay)
        self.addLink( switch1, switch2 , bw=self.bw, delay=self.delay)
        self.addLink( switch2, switch3 , bw=self.bw, delay=self.delay)
        self.addLink( switch2, switch4 , bw=self.bw, delay=self.delay)   
        self.addLink( switch3, switch7 , bw=self.bw, delay=self.delay)
        self.addLink( switch3, switch4 , bw=self.bw, delay=self.delay)
        self.addLink( switch4, switch6 , bw=self.bw, delay=self.delay)
        self.addLink( switch4, switch5 , bw=self.bw, delay=self.delay)
        self.addLink( switch7, switch6 , bw=self.bw, delay=self.delay)
        self.addLink( switch7, switch8 , bw=self.bw, delay=self.delay)
        self.addLink( switch6, switch8 , bw=self.bw, delay=self.delay)
        self.addLink( switch6, switch5 , bw=self.bw, delay=self.delay)
        self.addLink( switch5, switch9 , bw=self.bw, delay=self.delay)
        self.addLink( switch8, switch9 , bw=self.bw, delay=self.delay)
        self.addLink( switch8, switch10 , bw=self.bw, delay=self.delay)
        self.addLink( switch9, switch13 , bw=self.bw, delay=self.delay)
        self.addLink( switch10, switch11 , bw=self.bw, delay=self.delay)
        self.addLink( switch10, switch12 , bw=self.bw, delay=self.delay)
        self.addLink( switch11, switch12 , bw=self.bw, delay=self.delay)
        self.addLink( switch13, switch12 , bw=self.bw, delay=self.delay)
        self.addLink( switch13, switch14 , bw=self.bw, delay=self.delay)
        self.addLink( switch12, switch15 , bw=self.bw, delay=self.delay)
        self.addLink( switch14, switch15 , bw=self.bw, delay=self.delay)
        self.addLink( switch15, switch16 , bw=self.bw, delay=self.delay)
        self.addLink( switch16, rightHost , bw=self.bw, delay=self.delay)

def fileOperation(text, i):
    try:
    	f = open('/tmp/ping32.txt', 'a')
	f.write("%s %s\n" % (text, i))
	f.close()
    except IOError:
	print "File cannot be opened"

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
    	net.configLinkStatus('s9','s13','down')
	#print >>f, "after link down"
    	fileOperation("After link down", "")
    	sleep(20)
    	print "Link going up"
    	fileOperation("After link up", "")
    	net.configLinkStatus('s9','s13','up')
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
