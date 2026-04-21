"""ToolLoader subclasses for Schunk grippers."""

from .utils import ToolLoader


class SchunkEgpLoader(ToolLoader):
    """Loader for the Schunk EGP parallel gripper."""

    tool_name = "schunk_egp"
    tool_subdir = "schunk/egp_description"
    urdf_relpath = "urdf/egp.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"


class SchunkEgu50Loader(ToolLoader):
    """Loader for the Schunk EGU 50 parallel gripper."""

    tool_name = "schunk_egu_50"
    tool_subdir = "schunk/egu_description"
    urdf_relpath = "urdf/egu_50.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"


class SchunkPznPlusLoader(ToolLoader):
    """Loader for the Schunk PZN Plus 3-finger gripper."""

    tool_name = "schunk_pzn_plus"
    tool_subdir = "schunk/pzn_plus_description"
    urdf_relpath = "urdf/pzn_plus.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"


class SchunkPzv64Loader(ToolLoader):
    """Loader for the Schunk PZV 64 vacuum gripper."""

    tool_name = "schunk_pzv_64"
    tool_subdir = "schunk/pzv_64_description"
    urdf_relpath = "urdf/pzv_64.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"


__all__ = [
    "SchunkEgpLoader",
    "SchunkEgu50Loader",
    "SchunkPznPlusLoader",
    "SchunkPzv64Loader",
]
