#  farn Demo

Demo showing the usage of farn to generate, build and execute multiple OSP simulation cases.


## Help

Run

~~~sh
$ farn --help
~~~

to see all options.

run with --test option to generate/process only the first case for debug purposes.

add -v or --verbose to log INFO and DEBUG messages to console.


## Create samples

<table><tr><td>

(farnDict in dictIO native file format)
~~~sh
$ farn farnDict --sample
~~~

</td><td>

(farnDict in JSON format)
~~~sh
$ farn farnDict.json --sample
~~~

</td></tr></table>


## Generate case folder structure

<table><tr><td>

(farnDict in dictIO native file format)
~~~sh
$ farn sampled.farnDict --generate
~~~

</td><td>

(farnDict in JSON format)
~~~sh
$ farn sampled.farnDict.json --generate
~~~

</td></tr></table>


## Execute 'prepare' command set

Executing the 'copy' command, will execute multiple shell commands (as set specified in farnDict) that do the following preparatory work for all case folders:
* copy specified files from \template folder
* parse the caseDict file
* build the OSP files

<table><tr><td>

(farnDict in dictIO native file format)
~~~sh
$ farn sampled.farnDict --execute prepare
~~~

</td><td>

(farnDict in JSON format)
~~~sh
$ farn sampled.farnDict.json --execute prepare
~~~

</td></tr></table>


Notes:
* The 'parse' shell command is optional. ospCaseBuilder will read also a non-parsed caseDict and include a paramDict specified therein (if so) on-the-fly.
* The 'build' shell command in farnDict needs to be adapted depending on whether you included the 'parse' command or not: <br>
If you included the 'parse' command, the 'build' command in farnDict should point to the parsed. version of the caseDict file. <br>
If you omitted the 'parse' command, the 'build' command in farnDict should point to the the non-parsed caseDict file:


<table><tr><td>

(dictIO native file format)
~~~cpp
_commands
{
    ...
    prepare
    (
        ...
        'ospCaseBuilder parsed.caseDict'  // use parsed.caseDict if you explicitely executed the 'parse' step before
        'ospCaseBuilder caseDict'         // use caseDict if you omitted the explicit 'parse' step before
        ...
    );
    ...
}
~~~

</td><td>

(JSON format)
~~~json
"_commands":
{
    ...
    "prepare":
    [
        ...
        "ospCaseBuilder parsed.caseDict.json",
        "ospCaseBuilder caseDict.json"
        ...
    ],
    ...
{
~~~

</td></tr></table>


## Execute 'run' command set

Execute the 'run' command set to run cosim in all case folders:

<table><tr><td>

(farnDict in dictIO native file format)
~~~sh
$ farn sampled.farnDict --execute run
~~~

</td><td>

(farnDict in JSON format)
~~~sh
$ farn sampled.farnDict.json --execute run
~~~

</td></tr></table>

Alternatively, use the 'runjob' command set instead to run cosim in a separate cmd shell via winjob.cmd:

<table><tr><td>

(farnDict in dictIO native file format)
~~~sh
$ farn sampled.farnDict --execute runjob
~~~

</td><td>

(farnDict in JSON format)
~~~sh
$ farn sampled.farnDict.json --execute runjob
~~~

</td></tr></table>


## Execute 'post' command set

Execute the 'post' command set to run any postprocessing jobs or, as in this demo case, i.e. the watchDict commandline script:
(Be aware this step takes a bit longer.  Be patient ;-) )

<table><tr><td>

(farnDict in dictIO native file format)
~~~sh
$ farn sampled.farnDict --execute post
~~~

</td><td>

(farnDict in JSON format)
~~~sh
$ farn sampled.farnDict.json --execute post
~~~

</td></tr></table>
