"""RobotLoader subclasses for simple reference humanoid models."""

from .utils import RobotLoader


class SimpleHumanoidLoader(RobotLoader):
    """Loader for the simple humanoid reference model."""

    robot_name = "simple_humanoid"
    robot_subdir = "simple_humanoid_description"
    urdf_relpath = "urdf/simple_humanoid.urdf"
    srdf_relpath = "srdf/simple_humanoid.srdf"
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class SimpleHumanoidClassicalLoader(RobotLoader):
    """Loader for the classical simple humanoid reference model."""

    robot_name = "simple_humanoid_classical"
    robot_subdir = "simple_humanoid_description"
    urdf_relpath = "urdf/simple_humanoid_classical.urdf"
    srdf_relpath = "srdf/simple_humanoid_classical.srdf"
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


__all__ = [
    "SimpleHumanoidLoader",
    "SimpleHumanoidClassicalLoader",
]
