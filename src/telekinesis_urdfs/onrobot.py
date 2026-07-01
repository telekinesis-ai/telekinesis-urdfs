"""ToolLoader subclasses for OnRobot end-effectors."""

from .utils import ToolLoader


class OnRobotRg2Loader(ToolLoader):
    """Loader for the OnRobot RG2 parallel gripper."""

    tool_name = "onrobot_rg2"
    tool_subdir = "onrobot"
    urdf_relpath = "urdf/onrobot_rg2_model.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"


class OnRobotRg6Loader(ToolLoader):
    """Loader for the OnRobot RG6 parallel gripper."""

    tool_name = "onrobot_rg6"
    tool_subdir = "onrobot"
    urdf_relpath = "urdf/onrobot_rg6_model.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"


__all__ = [
    "OnRobotRg2Loader",
    "OnRobotRg6Loader",
]
