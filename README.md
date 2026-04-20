<div align="center">
  <p>
    <a align="center" href="" target="_blank">
      <img
        width="100%"
        src="https://telekinesis-public-assets.s3.us-east-1.amazonaws.com/Telekinesis+Banner.png"
      >
    </a>
  </p>

  <br>

  [Telekinesis Examples](https://github.com/telekinesis-ai/telekinesis-examples) | [Telekinesis Data](https://gitlab.com/telekinesis/telekinesis-data)
  <br>

[![PyPI version](https://img.shields.io/pypi/v/telekinesis-urdfs)](https://pypi.org/project/telekinesis-urdfs/)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![Python versions](https://img.shields.io/pypi/pyversions/telekinesis-urdfs)](https://pypi.org/project/telekinesis-urdfs/)

</div>

<p align="center">
  <a href="https://github.com/telekinesis-ai">GitHub</a>
  &nbsp;•&nbsp;
  <a href="https://www.linkedin.com/company/telekinesis-ai/">LinkedIn</a>
  &nbsp;•&nbsp;
  <a href="https://x.com/telekinesis_ai">X</a>
  &nbsp;•&nbsp;
  <a href="https://discord.gg/7NnQ3bQHqm">Discord</a>
</p>


# Telekinesis URDFs

Telekinesis URDFs is a Python package of robot and tool model assets bundled with lightweight path loaders for the Telekinesis ecosystem.
It includes:
- Robot descriptions: URDFs, SRDFs, and mesh directories for 20+ manufacturers
- Tool descriptions: end-effectors and grippers with the same unified interface
- Zero-dependency loading: all paths resolved from installed package data — no ROS, no environment variables
- Typed API: a single `ModelDescription` dataclass covering robots and tools alike

This library is used internally by the Telekinesis SDKS and frameworks as the canonical source of robot and tool model assets across simulation, planning, and learning components.

**Telekinesis URDFs is currently in its early development phase (pre-1.0). There will be continuous minor version updates that may introduce new models and improvements. To ensure compatibility and have the latest features, please always install or upgrade to the latest version of the package.**

## Installation

1. Create an isolated environment so that there are no dependency conflicts. We recommend installing `Miniconda` by following instructions from [here](https://docs.conda.io/en/latest/miniconda.html#installing).

2. Create a new `conda` environment called `telekinesis`:
    ```bash
    conda create -n telekinesis-urdfs python=3.11
    ```

3. Activate the environment:
    ```bash
    conda activate telekinesis-urdfs
    ```

4. Install the package using `pip`:

    **We currently support Python versions 3.11 and 3.12. Ensure your environment is in one of these Python versions.**

    ```bash
    pip install telekinesis-urdfs
    ```

    Note: The Python module is called `telekinesis_urdfs`, while the package published on PyPI is `telekinesis-urdfs`.

## Example

Run a sample Python script to quickly test your installation.

1. Create a file named `ur10e_loader_example.py` in a directory of your choice and copy paste the below:

    ```python
    from telekinesis_urdfs import load, load_as_dict

    # Load a robot — returns a typed, frozen Description dataclass
    desc = load("universalrobotsur10e")

    print(f"Name       : {desc.name}")
    print(f"Root dir   : {desc.root_dir}")
    print(f"Model dir  : {desc.model_dir}")
    print(f"URDF       : {desc.urdf_path}")
    print(f"SRDF       : {desc.srdf_path or 'N/A'}")
    print(f"Meshes     : {desc.mesh_dir or 'N/A'}")
    print(f"Ref posture: {desc.ref_posture or 'N/A'}")
    print(f"Free flyer : {desc.free_flyer}")

    # Same data as a plain dict — useful when passing to other libraries
    desc_dict = load_as_dict("universalrobotsur10e")
    print(desc_dict)
    ```

2. On a terminal, navigate to the directory where `urdfs_example.py` was created and run:

    ```bash
    python urdfs_example.py
    ```

    Expected output:
    ```
    Name       : ur10e
    Root dir   : /path/to/site-packages/telekinesis_urdfs/models
    Model dir  : /path/to/site-packages/telekinesis_urdfs/models/example-robot-data/robots/universal_robots
    URDF       : /path/to/.../ur10e.urdf
    SRDF       : /path/to/.../ur10e.srdf
    Meshes     : /path/to/.../ur10e
    Ref posture: N/A
    Free flyer : False
    {'name': 'ur10e', ...}
    ```

You are now set up with Telekinesis URDFs.

## Resources

- Examples  
  Runnable usage examples for Telekinesis URDFs: [Telekinesis Examples](https://github.com/telekinesis-ai/telekinesis-examples)

- Documentation  
  Full SDK documentation and usage details: [Telekinesis Documentation](https://docs.telekinesis.ai)

- Sample Data  
  Datasets used across the examples: [Telekinesis Data](https://gitlab.com/telekinesis/telekinesis-data)

## Support

For issues and questions:
- Create an [issue](https://github.com/telekinesis-ai/telekinesis-urdfs/issues) in the GitHub repository.
- Contact the Telekinesis development team at support@telekinesis.ai or on [Discord](https://discord.com/invite/7NnQ3bQHqm).
