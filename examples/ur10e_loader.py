"""
Minimal example showing how to load the UR10e robot description.

Loads the UR10e from the telekinesis_urdfs package and prints the
resolved paths to its URDF, SRDF, and mesh directory.

Example:
    python ur10e_loader.py
"""

from telekinesis_urdfs import load, load_as_dict


def main() -> None:
    """Load the UR10e description and print its resolved file paths."""

    # Calling load() resolves all paths relative to the installed
    # package data and returns a frozen ModelDescription dataclass.
    desc = load("universalrobotsur10e")

    print(f"Name       : {desc.name}")
    print(f"Root dir   : {desc.root_dir}")
    print(f"Model dir  : {desc.model_dir}")
    print(f"URDF       : {desc.urdf_path}")
    print(f"SRDF       : {desc.srdf_path or 'N/A'}")
    print(f"Meshes     : {desc.mesh_dir or 'N/A'}")
    print(f"Ref posture: {desc.ref_posture or 'N/A'}")
    print(f"Free flyer : {desc.free_flyer}")

    # Load full
    desc_full = load_as_dict("universalrobotsur10e")

    print("\nFull description as dictionary")
    print(f"{desc_full}")


if __name__ == "__main__":
    main()
