## Comparing the eouting convergebce time

The second test, we will measure the convergence time in different network scales with 2ms delay.

First we have to run our custom topology in mininet.

```
sudo mn --link tc,delay=2ms --controller=remote,ip=IP_OF_CONTROLLER,port=6653 --custom TOPOLOGY.py --topo mytopo
```

Then we will start http server on h2, because we will be testing httping from host h1. So in mininet, we type:

```
h2 python -m SimpleHTTPServer 80
```

Then, connect to console of node h1, and run the httping command to destination of host h2. 

```
xterm h1
httpping h2
```

When httpping is working we choose some link and put it down. To be sure that we are putting the right interface down (interface that is either ingress or egress port) we can allways run tcp dump on that interface:

example

```
tcpdump -i s2-eth3 src 10.0.0.1
```

when we are shure about interface than we shut that link down

exapmle
```
link s2 s4 down
```

Than we measure the response time in conslole of host h1.

