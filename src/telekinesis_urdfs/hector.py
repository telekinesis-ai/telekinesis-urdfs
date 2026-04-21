"""RobotLoader subclasses for Hector aerial robots."""

from .utils import RobotLoader


class HectorQuadrotorLoader(RobotLoader):
    """Loader for the Hector quadrotor UAV."""

    robot_name = "hector_quadrotor"
    robot_subdir = "hector_description"
    urdf_relpath = "robots/quadrotor_base.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = True


__all__ = [
    "HectorQuadrotorLoader",
]
