#  Demo: Using ospCaseBuilder to build house-demo

This demo employs osp's house-demo to build up a caseDict what can be used by a subsequent farn process.
The main steps are
* gather information from a provides "OspSystemStructure.xml"
* manually adaptation of the required source directory (where the fmu's are),
* manual adaptation of the readen input values as farn variables (if required),
* building up the cosim case and
* run / post.

## Prepare

We assume that the folder structure looks like this:
~~~
|-- README.md
|-- farnDict
|-- src
|   |-- Clock.fmu
|   |-- InnerWall.fmu
|   |-- OspSystemStructure.xml
|   |-- OuterWall1.fmu
|   |-- OuterWall2.fmu
|   |-- PlotConfig.json
|   |-- Room1.fmu
|   |-- Room2.fmu
|   |-- SystemStructure.ssd
|   `-- TempController.fmu
`-- template
    |-- README.md
    `-- resetDemo.bat
~~~
and we are currently inside the "template" folder.
Then run
~~~ps
importSystemStructure.py ..\src\OspSystemStructure.xml
~~~
to generate a "OspSystemStructure.xml-Dict".

Edit "OspSystemStructure.xml-Dict" and adjust the libSource variable to point to the library folder containing the fmu's according following example:
~~~cpp
_environment
{
    libSource                 'C:\Dev\farn-demo\library';  //adjust this path to point to the library folder containing the fmu's
    root                     ..\src;
}
~~~
If there is a "paramDict" to be used, substitute the given values from the source "..\src\OspSystemStructure.xml" into the farn variables:
~~~xml
<Simulator name="COMPONENTNAME" source="FMUNAME.fmu">
    <InitialValues>
        <InitialValue variable="VARIABLENAME">
            <Real value="VALUE"/>
        </InitialValue>
    </InitialValues>
</Simulator>
~~~
==
~~~cpp
COMPONENTNAME
{
    connectors
    {
        PORTNAME {...}
    }
    initialize
    {
        VARIABLENAME
        {
            causality     parameter;
            start         VALUE;
            variability   fixed;
        }
    }
    fmu             FMUNAME.fmu;
~~~
to
~~~cpp
COMPONENTNAME
{
    connectors
    {
        PORTNAME {...}
    }
    initialize
    {
        VARIABLENAME
        {
            causality     parameter;
            start         $VALUEREFERENCE;
            variability   fixed;
        }
    }
    fmu             FMUNAME.fmu;
~~~
Make sure that the entires are matching the full-qualified "paramDict" variables. Insert the include directive at the beginning of "OspSystemStructure.xml-Dict".
#include '.\paramDict'
~~~cpp
#include '.\paramDict'
~~~

## Inspect fmu's

Run
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


## Build the OSP case

To build the OSP case, i.e. the ModelDescription and OspSystemStructure XML files, run

~~~ps
ospCaseBuilder caseDict --verbose
~~~

Optionally you can create a dependency graph image using graphviz
~~~ps
ospCaseBuilder caseDict --graph
~~~

## Run the OSP case with cosim
Run the simulation
~~~ps
cosim run OspSystemStructure.xml -b 0 -d 360 --log-level=debug
~~~
and wait for results.

## Watch cosim
run

~~~ps
watchCosim --help
~~~

to get all options.

Optionally watch the progress of a long lasting simulation (second terminal needed)
with
~~~ps
watchCosim watchDict -c
~~~
For a collection of results and to plot:
~~~ps
watchCosim watchDict -pd
~~~