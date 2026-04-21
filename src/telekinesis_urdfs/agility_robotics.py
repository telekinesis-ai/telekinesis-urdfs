"""RobotLoader subclasses for Agility Robotics bipedal robots."""

from .utils import RobotLoader


class AgilityDigitLoader(RobotLoader):
    """Loader for the Agility Robotics Digit bipedal robot."""

    robot_name = "agility_digit"
    robot_subdir = "agility_robotics/digit_description"
    urdf_relpath = "urdf/digit_model.urdf"
    srdf_relpath = None
    mesh_relpath = None
    ref_posture = None
    free_flyer = False


__all__ = [
    "AgilityDigitLoader",
]
