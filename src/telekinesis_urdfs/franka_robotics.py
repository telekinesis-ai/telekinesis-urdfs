"""RobotLoader subclasses for Franka Robotics arms."""

from .utils import RobotLoader


class FrankaPandaLoader(RobotLoader):
    """Loader for the Franka Robotics Panda research arm."""

    robot_name = "franka_panda"
    robot_subdir = "franka_robotics/panda_description"
    urdf_relpath = "urdf/panda.urdf"
    srdf_relpath = "srdf/panda.srdf"
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


__all__ = [
    "FrankaPandaLoader",
]
