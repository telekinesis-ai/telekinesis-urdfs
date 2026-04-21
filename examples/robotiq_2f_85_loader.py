"""Minimal example showing how to load the Robotiq 2F-85 tool description.

Example:
    python robotiq_2f_85_loader.py
"""

from telekinesis_urdfs import load, load_as_dict


def main() -> None:
    """Load and print the Robotiq 2F-85 tool description.

    Demonstrates both the typed ModelDescription object and the plain
    dictionary form returned by load_as_dict.
    """
    # Load via the full brandmodel key registered in TOOLS
    desc = load("robotiq2f85")

    # Print each field from the ModelDescription dataclass
    print(f"Name       : {desc.name}")
    print(f"Root dir   : {desc.root_dir}")
    print(f"Model dir  : {desc.model_dir}")
    print(f"URDF       : {desc.urdf_path}")
    print(f"SRDF       : {desc.srdf_path or 'N/A'}")
    print(f"Meshes     : {desc.mesh_dir or 'N/A'}")
    print(f"Ref posture: {desc.ref_posture or 'N/A'}")
    print(f"Free flyer : {desc.free_flyer}")

    # Same data as a plain dict — useful when passing to other libraries
    desc_dict = load_as_dict("robotiq2f85")
    print("\nFull description as dictionary")
    print(f"{desc_dict}")


if __name__ == "__main__":
    main()
