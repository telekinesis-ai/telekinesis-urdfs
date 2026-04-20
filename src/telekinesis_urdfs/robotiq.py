"""ToolLoader subclasses for Robotiq grippers."""

from .utils import ToolLoader


class Robotiq2F85Loader(ToolLoader):
    """Loader for the Robotiq 2F-85 parallel gripper."""

    tool_name = "robotiq_2f_85"
    tool_subdir = "robotiq"
    urdf_relpath = "urdf/robotiq_2f_85_gripper.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"


class Robotiq2F140Loader(ToolLoader):
    """Loader for the Robotiq 2F-140 parallel gripper."""

    tool_name = "robotiq_2f_140"
    tool_subdir = "robotiq"
    urdf_relpath = "urdf/robotiq_2f_140_gripper.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"


class Robotiq2F85LegacyLoader(ToolLoader):
    """Loader for the Robotiq 2F-85 legacy visualization model."""

    tool_name = "robotiq_2f_85_legacy"
    tool_subdir = "robotiq/robotiq_2f_85_gripper_visualization_old"
    urdf_relpath = "urdf/robotiq_arg2f_85_model.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"


__all__ = [
    "Robotiq2F85Loader",
    "Robotiq2F140Loader",
    "Robotiq2F85LegacyLoader",
]
