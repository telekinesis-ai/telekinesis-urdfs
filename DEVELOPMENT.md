# Development Guide — Telekinesis URDFs

<details>
    <summary>Table of Contents</summary>

- [Development Guide — Telekinesis URDFs](#development-guide--telekinesis-urdfs)
  - [Getting Started](#getting-started)
    - [Conda Environment](#conda-environment)
    - [Installation](#installation)
  - [Workflow](#workflow)
  - [Project Structure](#project-structure)
  - [Adding a New Model](#adding-a-new-model)
    - [Converting Source Meshes](#converting-source-meshes)
  - [Contributing](#contributing)
    - [Format Checks](#format-checks)
    - [Linting Checks](#linting-checks)
  - [Troubleshooting](#troubleshooting)
  - [Support](#support)

</details>

## Getting Started

### Conda Environment

It is highly recommended to install a Miniconda environment before setting up the project. You can install Miniconda by following instructions from [here](https://docs.conda.io/en/latest/miniconda.html#installing).

Create a new Conda environment called `telekinesis-urdfs`:
```bash
conda create -n telekinesis-urdfs python=3.11
```

To activate the environment:
```bash
conda activate telekinesis-urdfs
```

To deactivate the environment:
```bash
conda deactivate
```

### Installation

1. Clone the repository:
    ```bash
    git clone -b develop https://github.com/telekinesis-ai/telekinesis-urdfs.git
    cd telekinesis-urdfs
    ```

2. Install the package in editable mode with dev dependencies:
    ```bash
    pip install -e ".[dev,docs]"
    ```

## Workflow

Below is the workflow for this repository:

```
┌──────────────────── FEATURE ────────────────────┐
│ feature/<name>                                  │
│ Develop, test, lint                             │
│ Push: no automatic build                        │
│ PR to develop: lint validation                  │
└─────────────────────────────────────────────────┘
                    ↓
┌──────────────────── DEVELOP ────────────────────┐
│ develop                                         │
│ Holds next release version                      │
│ Push: build <version>.devN artifact             │
│ PR to main: lint validation                     │
└─────────────────────────────────────────────────┘
                    ↓
┌───────────────────── MAIN ──────────────────────┐
│ main                                            │
│ Merge: build → tag release                      │
│ Post-merge: tag release + bump develop version  │
└─────────────────────────────────────────────────┘
```

Progress of pipelines can be checked on [GitHub Actions](https://github.com/telekinesis-ai/telekinesis-urdfs/actions).

1. **Feature Branch**
    - Create a new branch named `feature/<feature_name>` from the latest `develop` branch.
    - Implement and test locally.
    - Run linting/formatting using [Contributing](#contributing) steps.
    - Push to branch. No automatic build runs.
    - Steps to merge into develop:
        ```bash
        git checkout develop
        git pull --rebase
        ```
        ```bash
        git checkout feature/<name>
        git merge develop
        ```
        Resolve conflicts carefully if any.
        ```bash
        git commit -m "chore: merge develop"
        ```
        ```bash
        git checkout develop
        git merge feature/<name>
        ```
        Resolve conflicts carefully if any.
        ```bash
        git commit -m "chore: merge feature <name>"
        ```
    - On PR to `develop`:
        - Lint (ruff + pylint) is validated on Python 3.11 and 3.12.
        - Merge succeeds only if the above passes.

2. **Develop Branch**
    - `develop` holds the next release version. The version in `pyproject.toml` should not contain `.devN`.
    - Every push builds the package and uploads a `.devN` artifact to GitHub Actions.
    - Run linting/formatting using [Contributing](#contributing) steps.
    - Update `CHANGELOG.md` with the latest changes before merging to `main`.
    - Steps to merge into main:
        - Go to [Pull Requests](https://github.com/telekinesis-ai/telekinesis-urdfs/pulls).
        - Select source branch `develop` and target branch `main`.
        - Enter title as `feat: release version <version>`.
        - Enable `Squash and merge`.
        - Wait until the pre-merge lint check passes.
    - On PR to `main`:
        - Lint is validated.
        - Merge succeeds only if the above passes.

3. **Main Branch**
    - On merge, the release pipeline runs automatically:
        1. Package is built and checked.
        2. Git tag `v<version>` is created and pushed.
        3. Patch version is bumped on `develop` automatically.
    - Continue development from `develop` with:
        ```bash
        git checkout develop
        git pull --rebase
        ```
        The next release version is automatically added to `pyproject.toml`.

Artifacts per branch:
- Feature — no builds
- Develop — GitHub Actions artifact `telekinesis-urdfs:<version>.devN`
- Main — Git tag `v<version>` on GitHub

## Project Structure

```
telekinesis-urdfs/
├── src/
│   └── telekinesis_urdfs/
│       ├── __init__.py          # Public API: load, load_as_dict, ROBOTS, TOOLS, REGISTRY
│       ├── loader.py            # Combined registry and load helpers
│       ├── utils.py             # ModelDescription dataclass, RobotLoader, ToolLoader base classes
│       ├── <manufacturer>.py    # Per-manufacturer loader modules (abb.py, fanuc.py, ...)
│       └── models/              # Bundled URDF, SRDF, and mesh assets
├── examples/
│   └── robot_loader.py          # CLI example: load by robot name or brand
├── scripts/
│   └── convert_glb_fbx_to_meshes.py  # Blender: FBX/GLB source model -> visual/collision meshes
├── docs/                        # MkDocs documentation source
├── .github/
│   └── workflows/
│       ├── verify.yml           # Lint checks on pull requests
│       ├── develop.yml          # Dev build artifact on push to develop
│       └── release.yml          # Build, tag, and bump version on push to main
├── CHANGELOG.md
├── DEVELOPMENT.md
├── pyproject.toml
└── README.md
```

## Adding a New Model

A new model — a robot under `models/example-robot-data/robots/<company>/` or a tool under `models/example-robot-data/tools/<company>/` — needs three things before it's usable via `telekinesis_urdfs.load()`:

1. A URDF referencing visual/collision meshes via `package://example-robot-data/<robots|tools>/<company>/meshes/...`.
2. A `<company>.py` loader module in `src/telekinesis_urdfs/` defining a `RobotLoader`/`ToolLoader` subclass (e.g. `tool_subdir`/`robot_subdir`, `urdf_relpath`, `mesh_relpath`).
3. A registry entry for it in the `ROBOTS`/`TOOLS` dict in `loader.py`.

### Converting Source Meshes

Vendors often only provide a single combined FBX or GLB model rather than the split visual/collision STL/DAE meshes the URDF pipeline expects (see `onrobot`, `robotiq`, `schunk` for the expected layout: `meshes/visual/<model>/...` and `meshes/collision/<model>/...`).

Any `.fbx`/`.glb`/`.gltf` source model — robot or tool — should be converted with `scripts/convert_glb_fbx_to_meshes.py` into a visual mesh (`.stl` + `.dae`) and a decimated collision mesh (`.stl`). It runs inside Blender's bundled Python, so invoke it with the `blender` CLI:

```bash
blender --background --python scripts/convert_glb_fbx_to_meshes.py -- \
  --input "src/telekinesis_urdfs/models/example-robot-data/<robots|tools>/<company>/meshes/<source_file>.fbx" \
  --output-dir "src/telekinesis_urdfs/models/example-robot-data/<robots|tools>/<company>/meshes" \
  --name <model_name> \
  --collision-ratio 0.1
```

Arguments:
- `--input`: path to the source `.fbx`, `.glb`, or `.gltf` file.
- `--output-dir`: directory that will receive `visual/` and `collision/` subfolders.
- `--name` (optional): base name for the joined mesh and output files. Defaults to the input file's stem.
- `--collision-ratio` (optional): Decimate modifier ratio applied to the collision mesh (default `0.1`, i.e. ~10% of the original triangle count).

This produces:
```
<output-dir>/visual/<model_name>.stl
<output-dir>/visual/<model_name>.dae
<output-dir>/collision/<model_name>_collision.stl
```

After conversion, author the URDF by hand (referencing the exported mesh paths) and wire up the loader and registry entry as described above. Verify the result with:
```bash
python verify_model.py <registry_key>
```

## Contributing

### Format Checks

1. Check for format errors:
    ```bash
    ruff format --check .
    ```
    Expected output:
    ```
    N files already formatted
    ```

2. Correct format errors:
    ```bash
    ruff format .
    ```

### Linting Checks

1. Check for linting errors:
    ```bash
    ruff check .
    ```
    Expected output:
    ```
    All checks passed!
    ```

2. Correct auto-fixable lint errors:
    ```bash
    ruff check . --fix
    ```

3. If not auto-fixable, correct the errors manually.

4. Run pylint:
    ```bash
    pylint src/
    ```
    Expected output:
    ```
    Your code has been rated at 10.00/10
    ```

## Troubleshooting

1. **Merge conflict (develop → main)**

    If the PR shows merge conflicts, resolve them locally:
    ```bash
    git checkout main
    git pull
    git checkout develop
    git merge main
    ```
    Resolve all conflicts using changes from `develop`.
    ```bash
    git commit -m "fix: resolve merge conflict"
    git push
    ```


## Support

For issues and questions:
- Create an [issue](https://github.com/telekinesis-ai/telekinesis-urdfs/issues) in the GitHub repository.
- Contact the Telekinesis development team at support@telekinesis.ai or on [Discord](https://discord.com/invite/7NnQ3bQHqm).
