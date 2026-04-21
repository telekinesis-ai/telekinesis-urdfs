"""RobotLoader subclasses for ANYbotics ANYmal C quadruped."""

from .utils import RobotLoader


class AnymalCLoader(RobotLoader):
    """Loader for the ANYbotics ANYmal C quadruped."""

    robot_name = "anymal_c"
    robot_subdir = "anymal_c_simple_description"
    urdf_relpath = "urdf/anymal.urdf"
    srdf_relpath = "srdf/anymal.srdf"
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


__all__ = [
    "AnymalCLoader",
]
