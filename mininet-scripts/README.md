## How to run script?

There are two scripts: ***automatic_script_16.py*** and ***automatic_script_32.py***, that can be run to analyze convergence time of network topology. Each script need to specify 2 parameters. The first parameter is the link delay (-d) in miliseconds and the second parameter specify bandwith (-b).

Example of running script:

```
sudo python ./automatic_script_16.py -d 2ms -b 1000
```

The output of the script is reditected to the file /tmp/ping16.txt
