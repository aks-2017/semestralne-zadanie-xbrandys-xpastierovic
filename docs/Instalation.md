# Performance of SDN Routing in Comparison with Legacy Routing Protocols
#### Matúš Brandýs, Dominik Pastierovič
#### Instalation process 

## Requirements
 - Mininet vestion 2.2.2

The basic instalation of mininet doesn't know all unix command as it is just lighweithed version of Ubuntu (check uname -a or less /etc/issue). 

First things we will need to instal floodlight controller. This controller run as java applicaton, so we weil need also run JDK.

You will need to add this repository 
```
sudo add-apt-repository ppa:webupd8team/java
```

run update and install java 8

```
sudo apt-get update
sudo apt-get install oracle-java8-installer
```

Check if instalaton of java finished successfuly by typing:

```
java -version
```

Notice
while adding repository the system doesn't know command: add-apt-repository, it's give error add-apt-repository: command not found. In this case you have to install some basic packages that aren't icluded in basic instalation.

You have to run:

```
sudo apt-get install software-properties-common
```

apt-get install software-properties-common


## Floodlight instalation

Floodlight is simple to download from Github and build. You will need follow thos steps:

```
git clone git://github.com/floodlight/floodlight.git
cd floodlight
git submodule init
git submodule update
ant
 
sudo mkdir /var/lib/floodlight
sudo chmod 777 /var/lib/floodlight
```

# How to run toppology

First we will need to run Floodlight controller

```
cd ~/floodlight
java -jar target/floodlight.jar
```
Next, we will run python script of our custom topology with parameters of our remote controller. Remote floodlight contr listen on port 6653.

```
 sudo mn --controller=remote,ip=IP_OF_CONTROLLER,port=6653 --custom SCRIPT.PY --topo mytopo
```

# Additional instalation

During qour testing we will also use http-ping. For that we will need instal library in mininet.

```
sudo apt-get install httping
```


