"""ToolLoader subclasses for Piab end-effectors."""

from .utils import ToolLoader


class PiabPicobotElectricLoader(ToolLoader):
    """Loader for the Piab piCOBOT Electric vacuum gripper."""

    tool_name = "piab_picobot_electric"
    tool_subdir = "piab"
    urdf_relpath = "urdf/picobot_electric.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"


__all__ = [
    "PiabPicobotElectricLoader",
]
