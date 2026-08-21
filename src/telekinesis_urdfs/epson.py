"""RobotLoader subclasses for Epson industrial arms."""

from .utils import RobotLoader


class EpsonCx4a601sLoader(RobotLoader):
    """Loader for the Epson CX4-A601S industrial arm."""

    robot_name = "epson_cx4a601s"
    robot_subdir = "epson/cx4a601s_description"
    urdf_relpath = "urdf/cx4a601s.urdf"
    srdf_relpath = "srdf/epson_robot.srdf"
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


__all__ = [
    "EpsonCx4a601sLoader",
]
