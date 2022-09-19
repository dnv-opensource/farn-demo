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

~~~sh
$ farn farnDict --sample
~~~

## Generate case folder structure

~~~sh
$ farn sampled.farnDict --generate
~~~

## Execute 'prepare' command set

Executing the 'copy' command, will execute multiple shell commands (as set specified in farnDict) that do the following preparatory work for all case folders:
* copy specified files from \template folder
* parse the caseDict file
* build the OSP files


~~~sh
$ farn sampled.farnDict --execute prepare
~~~

Notes:
* The 'parse' shell command is optional. ospCaseBuilder will read also a non-parsed caseDict and include a paramDict specified therein (if so) on-the-fly.
* The 'build' shell command in farnDict needs to be adapted depending on whether you included the 'parse' command or not: <br>
If you included the 'parse' command, the 'build' command in farnDict should point to the parsed. version of the caseDict file. <br>
If you omitted the 'parse' command, the 'build' command in farnDict should point to the the non-parsed caseDict file:

~~~cpp
_commands
{
    ...
    prepare
    (
        ...
        'ospCaseBuilder parsed.caseDict'  // use parsed.caseDict if you explicitely executed the 'parse' step before
        'ospCaseBuilder caseDict'         // use caseDict if you did NOT execute the 'parse' step before
        ...
    );
~~~


## Execute 'run' command set

Execute the 'run' command set to run cosim in all case folders:

~~~sh
$ farn sampled.farnDict --execute run
~~~

Alternatively, use the 'runjob' command set instead to run cosim in a separate cmd shell via winjob.cmd:

~~~sh
$ farn sampled.farnDict --execute runjob
~~~

## Execute 'post' command set

Execute the 'post' command set to run any postprocessing jobs or, as in this demo case, i.e. the watchDict commandline script:
(Be aware this step takes a bit longer.  Be patient ;-) )

~~~sh
$ farn sampled.farnDict --execute post
~~~
