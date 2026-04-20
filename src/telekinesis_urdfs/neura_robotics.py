"""RobotLoader subclasses for Neura Robotics collaborative arms."""

from .utils import RobotLoader


class NeuraLara3Loader(RobotLoader):
    """Loader for the Neura Robotics Lara3 collaborative arm."""

    robot_name = "neura_lara3"
    robot_subdir = "neura_robotics/neura_robot_description-devel-lara3"
    urdf_relpath = "lara3/urdf/lara3.urdf"
    srdf_relpath = None
    mesh_relpath = "lara3/meshes"
    ref_posture = None
    free_flyer = False


class NeuraLara8Loader(RobotLoader):
    """Loader for the Neura Robotics Lara8 collaborative arm."""

    robot_name = "neura_lara8"
    robot_subdir = "neura_robotics/neura_robot_description-devel-lara8"
    urdf_relpath = "lara8/urdf/lara8.urdf"
    srdf_relpath = None
    mesh_relpath = "lara8/meshes"
    ref_posture = None
    free_flyer = False


class NeuraMaira7MLoader(RobotLoader):
    """Loader for the Neura Robotics Maira7M mobile arm."""

    robot_name = "neura_maira7m"
    robot_subdir = "neura_robotics/neura_robot_description-devel-maira7M"
    urdf_relpath = "maira7M/urdf/maira7M.urdf"
    srdf_relpath = None
    mesh_relpath = "maira7M/meshes"
    ref_posture = None
    free_flyer = False


__all__ = [
    "NeuraLara3Loader",
    "NeuraLara8Loader",
    "NeuraMaira7MLoader",
]
