# farn-demo
demo cases to get started with [farn][farn_docs]


## Install Python

* Install Python 3.9 or higher, i.e. [Python 3.9](https://www.python.org/downloads/release/python-3912/) or [Python 3.10](https://www.python.org/downloads/release/python-3104/)

## Install Graphviz system library

* Download from https://www.graphviz.org/download/
* Run the .exe file
* Choose 'Add Graphviz to the system PATH for current user'

Make sure Graphviz is properly added to your system PATH variables.
The following entry needs to exist in the USER PATH environment variable - add or adjust it if necessary:

~~~sh
%ProgramFiles%\Graphviz\bin
~~~


## Install OSP cosim

* Download the latest cosim release (cosim-v0.x.0-win64.zip) from GitHub
* https://github.com/open-simulation-platform/cosim-cli/releases

Unzip the archive and copy its content into a suitable folder of your choice, e.g.
~~~sh
C:\path\of\your\choice\osp\cosim\
~~~

Add the bin path to USER PATH environment variable:
~~~sh
C:\path\of\your\choice\osp\cosim\bin
~~~


## Clone the farn-demo repository

Change dir to the location where you want farn-demo to be cloned and created in:
~~~sh
$ cd C:\path\to\my\dev
~~~

Clone the farn-demo repository from GitHub:
~~~sh
$ git clone https://github.com/dnv-opensource/farn-demo
~~~

this should create the 'farn-demo' project inside path/to/my/dev:
~~~sh
C:\path\to\my\dev\farn-demo
~~~

Change dir into it:
~~~sh
$ cd farn-demo
~~~

You should now be here, in the root folder of the 'farn-demo' project:
~~~sh
C:\path\to\my\dev\farn-demo
~~~


## Create project specific virtual environment

Convention:
	1. Create the virtual environment in the project root folder, so that it resides with the project it is created for.
	2. Name it '.venv'

Update pip and setuptools on your system Python:
~~~sh
$ python -m pip install --upgrade pip setuptools
~~~

Create virtual environment:
~~~sh
$ python -m venv .venv
~~~

Activate the virtual environment: <br>
..on Windows:
~~~sh
> .venv\Scripts\activate.bat
~~~
..on Linux:
~~~sh
$ source .venv/bin/activate
~~~

Update pip and setuptools in the virtual environment:
~~~sh
$ python -m pip install --upgrade pip setuptools
~~~


## pip install farn

~~~sh
$ pip install farn
~~~


## farn Documentation on GitHub

https://dnv-opensource.github.io/farn/


<!-- Markdown link & img dfn's -->
[dictIO_docs]: https://dnv-opensource.github.io/dictIO/
[ospx_docs]: https://dnv-opensource.github.io/ospx/
[farn_docs]: https://dnv-opensource.github.io/farn/
