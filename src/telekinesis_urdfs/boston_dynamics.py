"""RobotLoader subclasses for Boston Dynamics robots."""

from .utils import RobotLoader


class SpotLoader(RobotLoader):
    """Loader for the Boston Dynamics Spot quadruped."""

    robot_name = "spot"
    robot_subdir = "boston_dynamics/spot_base_description"
    urdf_relpath = "spot.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class SpotWithArmLoader(RobotLoader):
    """Loader for Boston Dynamics Spot with arm attachment."""

    robot_name = "spot_with_arm"
    robot_subdir = "boston_dynamics/spot_with_arm_description"
    urdf_relpath = "spot_with_arm.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


__all__ = [
    "SpotLoader",
    "SpotWithArmLoader",
]
