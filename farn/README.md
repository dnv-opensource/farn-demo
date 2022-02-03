#  Demo: Using farn to generate, build and execute multiple OSP simulation cases

## Prepare

edit farnDict.

run

~~~ps
farn --help
~~~

to see all options.

run with the --test option to generate/process only the first case for debug purposes


## Create samples

~~~ps
farn farnDict --sample
~~~

## Generate case folder structure

~~~ps
farn sampled.farnDict --generate
~~~

## Execute 'copy' command

Execute the 'copy' command to copy necessary files from \template folder to all case folders:

~~~ps
farn sampled.farnDict --execute copy
~~~

## Execute 'parse' command

Execute the 'parse' command to parse the caseDict file in all case folders:

~~~ps
farn sampled.farnDict --execute parse
~~~

Note that executing the 'parse' command is optional.
ospCaseBuilder will read also a non-parsed caseDict and include a paramDict specified therein (if so) on-the-fly.

However, the 'build' command defined in farnDict will need to reflect one or the other case:

If you include the 'parse' step, the 'build' command in farnDict should point to the parsed. version of the caseDict file:

~~~cpp
_commands
{
    ...
    build
    (
        'ospCaseBuilder parsed.caseDict --verbose --log logs\ospCaseBuilder.log '
    );
~~~

If you omit the 'parse' step, the 'build' command in farnDict should point to the the non-parsed caseDict file:

~~~cpp
_commands
{
    ...
    build
    (
        'ospCaseBuilder caseDict --verbose --log logs\ospCaseBuilder.log'
    );
~~~


## Execute 'build' command

Execute the 'build' command to build the OSP files in all case folders:

~~~ps
farn sampled.farnDict --execute build
~~~


## Execute 'run' or 'runjob' command

Execute the 'run' command to run cosim in all case folders:

~~~ps
farn sampled.farnDict --execute run
~~~

Alternatively, use the 'runjob' command instead to run cosim in a separate cmd shell via winjob.cmd:

~~~ps
farn sampled.farnDict --execute runjob
~~~

## Execute 'post' command

Execute the 'post' command to run any postprocessing jobs or, as in this demo case, i.e. the watchDict commandline script:

~~~ps
farn sampled.farnDict --execute post
~~~
