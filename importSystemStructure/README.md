#  importSystemStructure Demo

Demo showing the usage of importSystemStructure to import the OspSystemStructure.xml from the OSP house-demo.

After the import is done, the demo will also show how to parameterize the caseDict and set up farn to generate, build and execute multiple OSP simulation cases.


# Import System Structure from OSP house demo

The main steps are
* Prepare
* Import OspSystemStructure.xml
* Adjust library source directory in caseDict
* Use a paramDict to make input values parameterizable (optional)
* Build the OSP case
* Run cosim
* Watch cosim


## Prepare

We assume the folder structure looks like this:
~~~
|-- README.md
|-- farnDict
|-- resetDemo.bat
|-- house
|   |-- Clock.fmu
|   |-- InnerWall.fmu
|   |-- OspSystemStructure.xml
|   |-- OuterWall1.fmu
|   |-- OuterWall2.fmu
|   |-- Room1.fmu
|   |-- Room2.fmu
|   |-- SystemStructure.ssd
|   `-- TempController.fmu
`-- template
    |-- cleanUpTemplateFolder.bat
    |-- paramDict
    `-- winjob.cmd
~~~


## Import OspSystemStructure.xml

For the import of the house demo system structure, jump into the template folder:

~~~sh
$ cd template
~~~

Run

~~~sh
$ importSystemStructure ..\house\OspSystemStructure.xml
~~~

to generate the imported caseDict. It will be named "caseDict_imported_from_OspSystemStructure_xml".

Rename "caseDict_imported_from_OspSystemStructure_xml" to simply "caseDict".


## Adjust library source directory in caseDict

Edit caseDict and adjust the libSource variable to point to the library folder containing the fmu's
and set root to '.' (current directory), see following example:

~~~cpp
_environment
{
    libSource                 'C:\Dev\farn-demo\house-demo\house';  //adjust this path to point to the library folder containing the fmu's
    root                     .;
}
~~~


## Use a paramDict

Optionally, you can now make hardcoded values in the caseDict parameterizable by referencing variables defined in a paramDict.
( This in fact is one of the core strengths of farn, so let's exercise it here ;-) )

If you look into the OspSystemStructure.xml file that you imported above, you will find a hardcoded initial value of "5.3" for the variable "T_outside":

~~~xml
<Simulator name="OuterWall1" source="OuterWall1.fmu">
    <InitialValues>
        <InitialValue variable="T_outside">
            <Real value="5.3"/>
        </InitialValue>
    </InitialValues>
</Simulator>
~~~

You will see this hardcoded initial value for "T_outside" transferred 1:1 by the importer into the caseDict:

~~~cpp
OuterWall1
{
    connectors
    {
        ...
    }
    fmu               OuterWall1.fmu;
    initialize
    {
        T_outside
        {
            causality       parameter;
            variability     fixed;
            start           5.3;
        }
    }
}
~~~

Now, create a paramDict file (or take the one prepared for you in this demo).

In the paramDict, define a variable OuterWall1_T_outside and set its value to 5.3:

~~~cpp
OuterWall1_T_outside    5.3;
~~~

Add following #include directive in the caseDict to include the paramDict:

~~~cpp
/*---------------------------------*- C++ -*----------------------------------*\
filetype dictionary; coding utf-8; version 0.1; local --; purpose --;
\*----------------------------------------------------------------------------*/
#include '.\paramDict'

_environment
{
    ...
~~~

Now you can replace the formerly hardcoded value in the caseDict with a reference to the variable defines in the included paramDict:

~~~cpp
OuterWall1
{
    connectors
    {
        ...
    }
    fmu               OuterWall1.fmu;
    initialize
    {
        T_outside
        {
            causality       parameter;
            variability     fixed;
            start           $OuterWall1_T_outside;
        }
    }
}
~~~

Repeat the same steps for the initial value of "T_outside" of the "OuterWall2" component.

Make sure that the $xyz references exactly match the fully qualified names of the referenced variables in the paramDict.


## Create a dependency graph image using graphviz (optional)

Optionally, you can call ospCaseBuilder with the --graph option to optionally create a pdf image with the system structure dependency graph:

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

Run the following command to execute cosim:

~~~sh
$ cosim run OspSystemStructure.xml -b 0 -d 360 --log-level=debug
~~~


## Watch cosim

watchCosim allows you to monitor a running simulation, dump results and plot a graph.

Run

~~~sh
$ watchCosim --help
~~~

to get all options.

Run

~~~sh
$ watchCosim watchDict -pd
~~~

to plot and dump the results.


## Clean up the template folder

~~~sh
$ cleanUpTemplateFolder
~~~


# farn

After you successfully imported the system structure of the OSP house demo and prepared the caseDict for parameterization,
you can now use farn to generate, build and execute multiple parameterized simulation cases of the house demo.

## Prepare

Change dir from template folder back to the house-demo root folder:

~~~sh
$ cd ..
~~~

Run

~~~sh
$ farn --help
~~~

to see all options.

run with --test option to generate/process only the first case for debug purposes.

add -v or --verbose to log INFO and DEBUG messages to console.


## Create samples

~~~sh
$ farn farnDict --sample
~~~

## Generate case folder structure

~~~sh
$ farn sampled.farnDict --generate
~~~

## Execute 'copy' command

Execute the 'copy' command to copy specified files from \template folder to all case folders:

~~~sh
$ farn sampled.farnDict --execute copy
~~~

## Execute 'parse' command

Execute the 'parse' command to parse the caseDict file in all case folders:

~~~sh
$ farn sampled.farnDict --execute parse
~~~

Note that the 'parse' step is optional:
ospCaseBuilder will read also a non-parsed caseDict and include a paramDict specified therein (if so) on-the-fly.


## Execute 'build' command

Execute the 'build' command to build the OSP files in all case folders:

~~~sh
$ farn sampled.farnDict --execute build
~~~

Note that the 'build' command in farnDict needs to be adapted depending on whether you have a distinct 'parse' step or not:

If you include the 'parse' step, the 'build' command in farnDict should point to the parsed. version of the caseDict file.

If you omit the 'parse' step, the 'build' command in farnDict should point to the the non-parsed caseDict file:

~~~cpp
_commands
{
    ...
    build
    (
        'ospCaseBuilder parsed.caseDict'  // use parsed.caseDict if you explicitely executed the 'parse' step before
        'ospCaseBuilder caseDict'         // use caseDict if you did NOT execute the 'parse' step before
    );
~~~


## Execute 'run' or 'runjob' command

Execute the 'run' command to run cosim in all case folders:

~~~sh
$ farn sampled.farnDict --execute run
~~~

Alternatively, use the 'runjob' command instead to run cosim in a separate cmd shell via winjob.cmd:

~~~sh
$ farn sampled.farnDict --execute runjob
~~~

## Execute 'post' command

Execute the 'post' command to run any postprocessing jobs or, as in this demo case, i.e. the watchDict commandline script:
(Be aware this step takes a bit longer.  Be patient ;-) )

~~~sh
$ farn sampled.farnDict --execute post
~~~
