"""RobotLoader subclasses for Clearpath Husky mobile robot."""

from .utils import RobotLoader


class HuskyLoader(RobotLoader):
    """Loader for the Clearpath Husky wheeled mobile robot."""

    robot_name = "husky"
    robot_subdir = "husky_description"
    urdf_relpath = "urdf/clearpathHusky.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


__all__ = [
    "HuskyLoader",
]
