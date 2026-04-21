"""RobotLoader subclasses for ANYbotics ANYmal B quadruped."""

from .utils import RobotLoader


class AnymalBLoader(RobotLoader):
    """Loader for the ANYbotics ANYmal B quadruped."""

    robot_name = "anymal_b"
    robot_subdir = "anymal_b_simple_description"
    urdf_relpath = "robots/anymal.urdf"
    srdf_relpath = "srdf/anymal.srdf"
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class AnymalBKinovaLoader(RobotLoader):
    """Loader for ANYmal B with Kinova arm attachment."""

    robot_name = "anymal_b_kinova"
    robot_subdir = "anymal_b_simple_description"
    urdf_relpath = "robots/anymal-kinova.urdf"
    srdf_relpath = "srdf/anymal-kinova.srdf"
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


__all__ = [
    "AnymalBLoader",
    "AnymalBKinovaLoader",
]
