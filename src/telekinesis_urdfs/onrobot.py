"""ToolLoader subclasses for OnRobot end-effectors."""

from .utils import ToolLoader


class OnRobotRg6Loader(ToolLoader):
    """Loader for the OnRobot RG6 parallel gripper."""

    tool_name = "onrobot_rg6"
    tool_subdir = "onrobot/onrobot_rg_description"
    urdf_relpath = "urdf/onrobot_rg6_model.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"


__all__ = [
    "OnRobotRg6Loader",
]
