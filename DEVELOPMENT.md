# Development Guide — Telekinesis URDFs

<details>
    <summary>Table of Contents</summary>

- [Getting Started](#getting-started)
   - [Conda Environment](#conda-environment)
   - [Installation](#installation)
- [Workflow](#workflow)
- [Deployment](#deployment)
   - [Build Package](#build-package)
   - [Upload to Test PyPI](#upload-to-test-pypi)
   - [Upload to Main PyPI](#upload-to-main-pypi)
- [Project Structure](#project-structure)
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
│ PR to main: lint + version availability check   │
└─────────────────────────────────────────────────┘
                    ↓
┌───────────────────── MAIN ──────────────────────┐
│ main                                            │
│ Merge: build → test PyPI → verify → PyPI        │
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
        - Wait until the pre-merge checks (lint + version availability) pass.
    - On PR to `main`:
        - Lint and version availability on PyPI are validated.
        - Merge succeeds only if the above passes.

3. **Main Branch**
    - On merge, the full release pipeline runs automatically:
        1. Package is built and checked.
        2. Published to Test PyPI.
        3. Installation is verified on Python 3.11 and 3.12.
        4. Published to PyPI.
        5. Git tag `v<version>` is created and pushed.
        6. Patch version is bumped on `develop` automatically.
    - Verify the release on [PyPI](https://pypi.org/project/telekinesis-urdfs/).
    - Continue development from `develop` with:
        ```bash
        git checkout develop
        git pull --rebase
        ```
        The next release version is automatically added to `pyproject.toml`.

Artifacts per branch:
- Feature — no builds
- Develop — GitHub Actions artifact `telekinesis-urdfs:<version>.devN`
- Main — PyPI package `telekinesis-urdfs:<version>`

## Deployment
**CI is already setup for this package**

Below steps are for **manual** deployment. With CI, ignore the below and refer to the CI setup in Release Management in Telekinesis Archiecture Documentation.

### Build Package

1. Ensure you are in the project directory with the correct conda environment active:
    ```bash
    conda activate telekinesis-urdfs
    cd telekinesis-urdfs
    ```

2. Change the `version` in `pyproject.toml`. Increment as per the entry in `CHANGELOG.md`.

    Versioning guidelines (`MAJOR.MINOR.PATCH`):
    - `PATCH` — bug fixes, no API change
    - `MINOR` — backward-compatible new features
    - `MAJOR` — breaking API changes

    Additional suffixes:
    - `devN` for development/unstable versions
    - `aN`, `bN` for alpha, beta versions
    - `rcN` for release candidates

    Pip precedence: `0.2.0.dev1 < 0.2.0a1 < 0.2.0b1 < 0.2.0rc1 < 0.2.0`

    **Important: Do NOT reuse a version number once uploaded to PyPI.**

3. Ensure `README.md` and `CHANGELOG.md` are up to date.

4. Ensure `pip` and build tools are upgraded:
    ```bash
    python -m pip install --upgrade pip build twine
    ```

5. Build the package:

    > **Important: Delete previous `dist/` files before building if they exist.**

    ```bash
    rm -rf dist/ build/ src/*.egg-info
    python -m build
    ```

    Expected output:
    ```
    Successfully built telekinesis_urdfs-<version>.tar.gz and telekinesis_urdfs-<version>-py3-none-any.whl
    ```

    Folder `dist/` is created with:
    ```
    dist/
    ├── telekinesis_urdfs-<version>-py3-none-any.whl
    └── telekinesis_urdfs-<version>.tar.gz
    ```

### Upload to Test PyPI

1. Upload to Test PyPI. Enter your Test PyPI API token when prompted:
    ```bash
    python -m twine upload --repository testpypi dist/*
    ```

    Expected output:
    ```
    Uploading distributions to https://test.pypi.org/legacy/
    ...
    View at: https://test.pypi.org/project/telekinesis-urdfs/<version>
    ```

2. Create a clean test environment:
    ```bash
    conda create -n telekinesis-urdfs-test python=3.11
    conda activate telekinesis-urdfs-test
    ```

3. Install from Test PyPI, replacing `<version>`:
    ```bash
    pip install \
      --index-url https://test.pypi.org/simple/ \
      --extra-index-url https://pypi.org/simple \
      telekinesis-urdfs==<version>
    ```

4. Verify the installation:
    ```bash
    python -c "from telekinesis_urdfs import load; d = load('universalrobotsur10e'); print(d.name)"
    ```

    Expected output:
    ```
    ur10e
    ```

    > Note: The PyPI package name is `telekinesis-urdfs`. The Python import namespace is `telekinesis_urdfs`.

### Upload to Main PyPI

1. Once Test PyPI verification passes, upload to the main PyPI. Enter your PyPI API token when prompted:
    ```bash
    python -m twine upload dist/*
    ```

    Expected output:
    ```
    View at: https://pypi.org/project/telekinesis-urdfs/<version>
    ```

2. Uninstall the test package and install the live release:
    ```bash
    pip uninstall telekinesis-urdfs
    pip install telekinesis-urdfs==<version>
    ```

3. Verify by running the example:
    ```bash
    python examples/robot_loader.py --robot universalrobotsur10e
    ```

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
├── docs/                        # MkDocs documentation source
├── .github/
│   └── workflows/
│       ├── verify.yml           # Lint + version checks on pull requests
│       ├── develop.yml          # Dev build artifact on push to develop
│       └── release.yml          # Full release pipeline on push to main
├── CHANGELOG.md
├── DEVELOPMENT.md
├── pyproject.toml
└── README.md
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

2. **Version already exists on PyPI**

    The pre-merge check will fail if the version in `pyproject.toml` is already published. Bump the version before merging.

3. **Test PyPI install fails**

    Test PyPI propagation can take a few minutes. The CI pipeline retries up to 3 times automatically. For manual installs, wait a minute and retry.

## Support

For issues and questions:
- Create an [issue](https://github.com/telekinesis-ai/telekinesis-urdfs/issues) in the GitHub repository.
- Contact the Telekinesis development team at support@telekinesis.ai or on [Discord](https://discord.com/invite/7NnQ3bQHqm).
