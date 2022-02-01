#  Demo: Using ospCaseBuilder to build an OSP simulation case

## Prepare

edit caseDict and adjust libSource variable to point to the library folder containing the fmu's

~~~cpp
_environment
{
    libSource                 'C:\Dev\farn-demo\library';  //adjust this path to point to the library folder containing the fmu's
    root                     .;
}
~~~

run

~~~ps
ospCaseBuilder --help
~~~

to see all options.


## Inspect fmu's
run

~~~ps
ospCaseBuilder --inspect caseDict --verbose
~~~

with
* --inspect: to inspect the connectors of the fmu'
* --log: optional log file name
* --log-level=INFO: log all informational output into log file
* --verbose: see all INFO (DEBUG) on the screen


## Detail out the caseDict
* populate "connectors" and "connections" elements in the caseDict
* use references to variables defined in an included paramDict, if so


## Build the OSP simulation case
run

~~~ps
ospCaseBuilder caseDict --verbose
~~~


## Run the OSP case with cosim
run

~~~ps
cosim help
cosim run --help
cosim run OspSystemStructure.xml -b 0 -d 10 --real-time --log-level=debug
cosim run OspSystenStructure.xml -b 0 -d 10
~~~

and wait for results.

Optionally, open a second terminal and

## Watch cosim
run

~~~ps
watchCosim --help
~~~

to get all options.

run

~~~ps
watchCosim watchDict -pd
~~~

to plot and dump the results.