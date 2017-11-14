## Node forwarding speed

In this first test, we will measure the response time of ping command between two hosts in network to analyze the forwarding speed of network node.

First we have to run our custom topology in mininet.

```
sudo mn --link tc,delay=2ms --controller=remote,ip=IP_OF_CONTROLLER,port=6653 --custom TOPOLOGY.py --topo mytopo
```

Connect to console of node h1, and run the ping command to destination host h2. To find out ip addresses of h1 and h2 hosts, we can execute:

```
dump
```
To run console of host h1 and run ping we have to type:

```
xterm h1
ping h2
```

Now observe the response time of ping.
