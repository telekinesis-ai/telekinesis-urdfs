"""RobotLoader subclasses for Yaskawa Motoman industrial arms."""

from .utils import RobotLoader


class MotomanBmda3Loader(RobotLoader):
    """Loader for the Motoman BMDA3 dual-arm assembly robot."""

    robot_name = "motoman_bmda3"
    robot_subdir = "motoman/bmda3_description"
    urdf_relpath = "urdf/bmda3.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class MotomanBmda3WeEfssLoader(RobotLoader):
    """Loader for the Motoman BMDA3 with end-effectors."""

    robot_name = "motoman_bmda3_w_effs"
    robot_subdir = "motoman/bmda3_description"
    urdf_relpath = "urdf/bmda3_w_effs.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class MotomanMh5Loader(RobotLoader):
    """Loader for the Motoman MH5 industrial arm."""

    robot_name = "motoman_mh5"
    robot_subdir = "motoman/mh5_description"
    urdf_relpath = "urdf/mh5.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class MotomanSia10dLoader(RobotLoader):
    """Loader for the Motoman SIA10D 7-DOF arm."""

    robot_name = "motoman_sia10d"
    robot_subdir = "motoman/sia10d_description"
    urdf_relpath = "urdf/sia10d.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class MotomanSia10fLoader(RobotLoader):
    """Loader for the Motoman SIA10F 7-DOF arm."""

    robot_name = "motoman_sia10f"
    robot_subdir = "motoman/sia10f_description"
    urdf_relpath = "urdf/sia10f.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class MotomanSia20dLoader(RobotLoader):
    """Loader for the Motoman SIA20D 7-DOF arm."""

    robot_name = "motoman_sia20d"
    robot_subdir = "motoman/sia20d_description"
    urdf_relpath = "urdf/sia20d.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class MotomanSia5dLoader(RobotLoader):
    """Loader for the Motoman SIA5D 7-DOF arm."""

    robot_name = "motoman_sia5d"
    robot_subdir = "motoman/sia5d_description"
    urdf_relpath = "urdf/sia5d.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


__all__ = [
    "MotomanBmda3Loader",
    "MotomanBmda3WeEfssLoader",
    "MotomanMh5Loader",
    "MotomanSia10dLoader",
    "MotomanSia10fLoader",
    "MotomanSia20dLoader",
    "MotomanSia5dLoader",
]
