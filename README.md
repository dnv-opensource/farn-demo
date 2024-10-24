# farn-demo
demo cases to get started with [farn][farn_docs]


## Development Setup

### 1. Install uv
This project uses `uv` as package manager.
If you haven't already, install [uv](https://docs.astral.sh/uv), preferably using it's ["Standalone installer"](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_2) method: <br>
..on Windows:
```sh
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
..on MacOS and Linux:
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```
(see [docs.astral.sh/uv](https://docs.astral.sh/uv/getting-started/installation/) for all / alternative installation methods.)

Once installed, you can update `uv` to its latest version, anytime, by running:
```sh
uv self update
```

### 2. Install Python
This project requires Python 3.10 or later. <br>
If you don't already have a compatible version installed on your machine, the probably most comfortable way to install Python is through `uv`:
```sh
uv python install
```
This will install the latest stable version of Python into the uv Python directory, i.e. as a uv-managed version of Python.

Alternatively, and if you want a standalone version of Python on your machine, you can install Python either via `winget`:
```sh
winget install --id Python.Python
```
or you can download and install Python from the [python.org](https://www.python.org/downloads/) website.

### 3. Install Graphviz system library

* Download from https://www.graphviz.org/download/
* Run the .exe file
* Choose 'Add Graphviz to the system PATH for current user'

Make sure Graphviz is properly added to your system PATH variables.
The following entry needs to exist in the USER PATH environment variable - add or adjust it if necessary:

```sh
%ProgramFiles%\Graphviz\bin
```


### 4. Install OSP cosim

* Download the latest cosim release (cosim-v0.x.0-win64.zip) from GitHub
* https://github.com/open-simulation-platform/cosim-cli/releases

Unzip the archive and copy its content into a suitable folder of your choice, e.g.
```sh
C:\path\of\your\choice\osp\cosim\
```

Add the bin path to USER PATH environment variable:
```sh
C:\path\of\your\choice\osp\cosim\bin
```


### 5. Clone the repository
Clone the farn-demo repository into your local development directory:
```sh
git clone https://github.com/dnv-innersource/farn-demo path/to/your/dev/farn-demo
```

### 6. Install dependencies
Run `uv sync` to create a virtual environment and install all project dependencies into it:
```sh
uv sync
```

### 7. (Optional) Install CUDA support
Run `uv sync` with option `--extra cuda` to in addition install torch with CUDA support:
```sh
uv sync --extra cuda
```

Alternatively, you can manually install torch with CUDA support.
_Note 1_: Do this preferably _after_ running `uv sync`. That way you ensure a virtual environment exists, which is a prerequisite before you install torch with CUDA support using below `uv pip install` command.

To manually install torch with CUDA support, generate a `uv pip install` command matching your local machine's operating system using the wizard on the official [PyTorch website](https://pytorch.org/get-started/locally/).
_Note_: As we use `uv` as package manager, remember to replace `pip` in the command generated by the wizard with `uv pip`.

If you are on Windows, the resulting `uv pip install` command will most likely look something like this:
```sh
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```

_Hint:_ If you are unsure which cuda version to indicate in above `uv pip install .. /cuXXX` command, you can use the shell command `nvidia-smi` on your local system to find out the cuda version supported by the current graphics driver installed on your system. When then generating the `uv pip install` command with the wizard from the [PyTorch website](https://pytorch.org/get-started/locally/), select the cuda version that matches the major version of what your graphics driver supports (major version must match, minor version may deviate).


### 8. (Optional) Activate the virtual environment
When using `uv`, there is in almost all cases no longer a need to manually activate the virtual environment. <br>
`uv` will find the `.venv` virtual environment in the working directory or any parent directory, and activate it on the fly whenever you run a command via `uv` inside your project folder structure:
```sh
uv run <command>
```

However, you still _can_ manually activate the virtual environment if needed.
When developing in an IDE, for instance, this can in some cases be necessary depending on your IDE settings.
To manually activate the virtual environment, run one of the "known" legacy commands: <br>
..on Windows:
```sh
.venv\Scripts\activate.bat
```
..on Linux:
```sh
source .venv/bin/activate
```


## farn Documentation on GitHub

For more examples and usage, please refer to farn's [documentation][farn_docs].



<!-- Markdown link & img dfn's -->
[dictIO_docs]: https://dnv-opensource.github.io/dictIO/README.html
[ospx_docs]: https://dnv-opensource.github.io/ospx/README.html
[farn_docs]: https://dnv-opensource.github.io/farn/README.html