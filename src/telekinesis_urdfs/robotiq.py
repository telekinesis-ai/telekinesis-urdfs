"""ToolLoader subclasses for Robotiq grippers."""

from .utils import ToolLoader


class Robotiq2F85Loader(ToolLoader):
    """Loader for the Robotiq 2F-85 parallel gripper."""

    tool_name = "robotiq_2f_85"
    tool_subdir = "robotiq"
    urdf_relpath = "urdf/robotiq_2f_85.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"


class Robotiq2F140Loader(ToolLoader):
    """Loader for the Robotiq 2F-140 parallel gripper."""

    tool_name = "robotiq_2f_140"
    tool_subdir = "robotiq"
    urdf_relpath = "urdf/robotiq_2f_140.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"


class RobotiqHandELoader(ToolLoader):
    """Loader for the Robotiq Hand-E parallel gripper."""

    tool_name = "robotiq_hande"
    tool_subdir = "robotiq"
    urdf_relpath = "urdf/robotiq_hande.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"


__all__ = [
    "Robotiq2F85Loader",
    "Robotiq2F140Loader",
    "RobotiqHandELoader",
]
