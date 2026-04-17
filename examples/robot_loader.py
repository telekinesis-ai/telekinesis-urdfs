"""Example of consuming synapse-robot-data from another repository.

In a downstream project, install this package as a dependency and then import the
public compatibility module directly.
"""

from synapse_robot_data.loaders.robots import loader


if __name__ == "__main__":
    # Load a robot description by name.
    # The name is normalized to lowercase and looked up in the ROBOTS dict in loader.py.
    # See that file for supported names and aliases.

    robot = loader.load("ur5e")

    print("Name      :", robot.name)
    print("Root Model Dir:", robot.root_model_dir)
    print("Model dir :", robot.model_dir)
    print("URDF      :", robot.urdf_path)
    print("SRDF      :", robot.srdf_path)
    print("Meshes    :", robot.mesh_dir)
    print("FreeFlyer :", robot.free_flyer)
