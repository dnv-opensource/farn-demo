# farn-demo
demo cases to get started with farn


## Install Python 3.9

* Download from https://www.python.org/downloads/release/python-399/
* Install

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

Create virtual environment:
~~~sh
$ python -m venv .venv
~~~

Activate the virtual environment:
~~~sh
$ .venv\Scripts\activate
~~~

Update pip and setuptools:
~~~sh
$ python -m pip install --upgrade pip setuptools
~~~


## pip install farn

~~~sh
$ pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ farn
~~~


## farn Documentation on GitHub

https://crispy-tribble-285142b5.pages.github.io
