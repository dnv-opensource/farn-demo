#  ospCaseBuilder Demo

Demo showing the usage of ospCaseBuilder to build an OSP simulation case.

## Prepare

Edit caseDict and adjust libSource variable to point to the library folder containing the fmu's.

~~~cpp
_environment
{
    libSource                 'C:\Dev\farn-demo\library';  //adjust this path to point to the library folder containing the fmu's
}
~~~

Run

~~~sh
$ ospCaseBuilder --help
~~~

to see all options.

add -v or --verbose to log INFO and DEBUG messages to console.


## Inspect fmu's

~~~sh
$ ospCaseBuilder --inspect caseDict --log inspect.log --log-level INFO
~~~

with
* --inspect: to inspect the connectors of the fmu'
* --log: optional log file name
* --log-level: log level to be used for the log file [DEBUG, INFO, WARNING, ERROR]


## Detail out the caseDict
* populate "connectors" and "connections" elements in the caseDict
* use references to variables defined in an included paramDict, if so


## Create a dependency graph image using graphviz

You can call ospCaseBuilder with the --graph option to optionally create a pdf image with the system structure dependency graph:

~~~sh
$ ospCaseBuilder caseDict --graph
~~~


## Build the OSP case

~~~sh
$ ospCaseBuilder caseDict
~~~


## Run the OSP case with cosim

Run

~~~sh
$ cosim help
$ cosim run --help
~~~

to get all options.

Run one of the following commands to execute cosim:

~~~sh
$ cosim run OspSystemStructure.xml -b 0 -d 10 --real-time --log-level info
$ cosim run OspSystemStructure.xml -b 0 -d 10
~~~


## Watch cosim

watchCosim allows you to monitor a running simulation, dump results and plot a graph.

Run

~~~sh
$ watchCosim --help
~~~

to get all options.

Optionally, to watch the progress of a long lasting simulation you can run watchCosim with option -c:
(Important: Use a separate, second Terminal to run this command.)

~~~ps
$ watchCosim watchDict -c
~~~

Finally, run

~~~sh
$ watchCosim watchDict -pd
~~~

to plot and dump the results.