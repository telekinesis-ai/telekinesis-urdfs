"""RobotLoader subclasses for Agibot humanoid robots."""

from .utils import RobotLoader


class AgibotX1Loader(RobotLoader):
    """Loader for the Agibot X1 humanoid robot."""

    robot_name = "agibot_x1"
    robot_subdir = "agibot/x1_description"
    urdf_relpath = "urdf/x1.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


__all__ = [
    "AgibotX1Loader",
]
