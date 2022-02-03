#  farn Demo

Demo showing the usage of farn to generate, build and execute multiple OSP simulation cases.


## Prepare

run

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

~~~sh
$ farn sampled.farnDict --execute post
~~~
