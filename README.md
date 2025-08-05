# farn-demo
Demo cases to get started with [farn][farn_docs].


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
git clone https://github.com/dnv-opensource/farn-demo path/to/your/dev/farn-demo
```
Change into the project directory after cloning:
```sh
cd farn-demo
```

### 6. Install dependencies
Run `uv sync` to create a virtual environment and install all project dependencies into it:
```sh
uv sync
```
> **Note**: Using `--no-dev` will omit installing development dependencies.

> **Note**: `uv` will create a new virtual environment called `.venv` in the project root directory when running
> `uv sync` the first time. Optionally, you can create your own virtual environment using e.g. `uv venv`, before running
> `uv sync`.

### 7. (Optional) Activate the virtual environment
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

### 8. Install pre-commit hooks
The `.pre-commit-config.yaml` file in the project root directory contains a configuration for pre-commit hooks.
To install the pre-commit hooks defined therein in your local git repository, run:
```sh
uv run pre-commit install
```

All pre-commit hooks configured in `.pre-commit-config.yaml` will now run each time you commit changes.

pre-commit can also manually be invoked, at anytime, using:
```sh
uv run pre-commit run --all-files
```

To skip the pre-commit validation on commits (e.g. when intentionally committing broken code), run:
```sh
uv run git commit -m <MSG> --no-verify
```

To update the hooks configured in `.pre-commit-config.yaml` to their newest versions, run:
```sh
uv run pre-commit autoupdate
```

## Meta

Copyright (c) 2024 [DNV](https://www.dnv.com) SE. All rights reserved.

Frank Lumpitzsch - [@LinkedIn](https://www.linkedin.com/in/frank-lumpitzsch-23013196/) - frank.lumpitzsch@dnv.com

Claas Rostock - [@LinkedIn](https://www.linkedin.com/in/claasrostock/?locale=en_US) - claas.rostock@dnv.com

Seunghyeon Yoo - [@LinkedIn](https://www.linkedin.com/in/seunghyeon-yoo-3625173b/) - seunghyeon.yoo@dnv.com

Distributed under the MIT license. See [LICENSE](LICENSE.md) for more information.

[https://github.com/dnv-opensource/farn-demo](https://github.com/dnv-opensource/farn-demo)

## Contributing

1. Fork it (<https://github.com/dnv-opensource/farn-demo/fork>)
2. Create an issue in your GitHub repo
3. Create your branch based on the issue number and type (`git checkout -b issue-name`)
4. Evaluate and stage the changes you want to commit (`git add -i`)
5. Commit your changes (`git commit -am 'place a descriptive commit message here'`)
6. Push to the branch (`git push origin issue-name`)
7. Create a new Pull Request in GitHub


## farn Documentation on GitHub

For more examples and usage, please refer to farn's [documentation][farn_docs].



<!-- Markdown link & img dfn's -->
[dictIO_docs]: https://dnv-opensource.github.io/dictIO/README.html
[ospx_docs]: https://dnv-opensource.github.io/ospx/README.html
[farn_docs]: https://dnv-opensource.github.io/farn/README.html