"""RobotLoader subclasses for custom mobile robot platforms."""

from .utils import RobotLoader


class CustomMobileRobotLoader(RobotLoader):
    """Loader for the generic custom mobile robot."""

    robot_name = "custom_mobile_robot"
    robot_subdir = "custom_mobile_robots/custom_mobile_robot_description"
    urdf_relpath = "urdf/custom_mobile_robot.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


__all__ = [
    "CustomMobileRobotLoader",
]
