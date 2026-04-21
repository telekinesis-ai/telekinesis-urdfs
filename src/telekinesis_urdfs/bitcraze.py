"""RobotLoader subclasses for Bitcraze Crazyflie drones."""

from .utils import RobotLoader


class CrazyflieCf2xLoader(RobotLoader):
    """Loader for the Bitcraze Crazyflie CF2X quadrotor."""

    robot_name = "crazyflie_cf2x"
    robot_subdir = "bitcraze/crazyflie_description"
    urdf_relpath = "cf2x.urdf"
    srdf_relpath = None
    mesh_relpath = None
    ref_posture = None
    free_flyer = True


class CrazyflieCf2pLoader(RobotLoader):
    """Loader for the Bitcraze Crazyflie CF2+ quadrotor."""

    robot_name = "crazyflie_cf2p"
    robot_subdir = "bitcraze/crazyflie_description"
    urdf_relpath = "cf2p.urdf"
    srdf_relpath = None
    mesh_relpath = None
    ref_posture = None
    free_flyer = True


class CrazyflieRacerLoader(RobotLoader):
    """Loader for the Bitcraze Crazyflie Racer drone."""

    robot_name = "crazyflie_racer"
    robot_subdir = "bitcraze/crazyflie_description"
    urdf_relpath = "racer.urdf"
    srdf_relpath = None
    mesh_relpath = None
    ref_posture = None
    free_flyer = True


class CrazyflieArchitravelLoader(RobotLoader):
    """Loader for the Bitcraze Crazyflie Architrave fixture."""

    robot_name = "crazyflie_architrave"
    robot_subdir = "bitcraze/crazyflie_description"
    urdf_relpath = "architrave.urdf"
    srdf_relpath = None
    mesh_relpath = None
    ref_posture = None
    free_flyer = False


class CrazyflieBoxLoader(RobotLoader):
    """Loader for the Bitcraze Crazyflie Box fixture."""

    robot_name = "crazyflie_box"
    robot_subdir = "bitcraze/crazyflie_description"
    urdf_relpath = "box.urdf"
    srdf_relpath = None
    mesh_relpath = None
    ref_posture = None
    free_flyer = False


__all__ = [
    "CrazyflieCf2xLoader",
    "CrazyflieCf2pLoader",
    "CrazyflieRacerLoader",
    "CrazyflieArchitravelLoader",
    "CrazyflieBoxLoader",
]
