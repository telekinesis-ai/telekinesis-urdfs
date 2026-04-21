"""RobotLoader subclasses for Bitcraze Crazyflie drones."""

from .utils import RobotLoader


class BitcrazeCf2xLoader(RobotLoader):
    """Loader for the Bitcraze Crazyflie CF2X quadrotor."""

    robot_name = "crazyflie_cf2x"
    robot_subdir = "bitcraze/crazyflie_description"
    urdf_relpath = "cf2x.urdf"
    srdf_relpath = None
    mesh_relpath = None
    ref_posture = None
    free_flyer = True


class BitcrazeCf2pLoader(RobotLoader):
    """Loader for the Bitcraze Crazyflie CF2+ quadrotor."""

    robot_name = "crazyflie_cf2p"
    robot_subdir = "bitcraze/crazyflie_description"
    urdf_relpath = "cf2p.urdf"
    srdf_relpath = None
    mesh_relpath = None
    ref_posture = None
    free_flyer = True


class BitcrazeCrazyflieRacerLoader(RobotLoader):
    """Loader for the Bitcraze Crazyflie Racer drone."""

    robot_name = "crazyflie_racer"
    robot_subdir = "bitcraze/crazyflie_description"
    urdf_relpath = "racer.urdf"
    srdf_relpath = None
    mesh_relpath = None
    ref_posture = None
    free_flyer = True


class BitcrazeCrazyflieArchitravelLoader(RobotLoader):
    """Loader for the Bitcraze Crazyflie Architrave fixture."""

    robot_name = "crazyflie_architrave"
    robot_subdir = "bitcraze/crazyflie_description"
    urdf_relpath = "architrave.urdf"
    srdf_relpath = None
    mesh_relpath = None
    ref_posture = None
    free_flyer = False


class BitcrazeCrazyflieBoxLoader(RobotLoader):
    """Loader for the Bitcraze Crazyflie Box fixture."""

    robot_name = "crazyflie_box"
    robot_subdir = "bitcraze/crazyflie_description"
    urdf_relpath = "box.urdf"
    srdf_relpath = None
    mesh_relpath = None
    ref_posture = None
    free_flyer = False


__all__ = [
    "BitcrazeCf2xLoader",
    "BitcrazeCf2pLoader",
    "BitcrazeCrazyflieRacerLoader",
    "BitcrazeCrazyflieArchitravelLoader",
    "BitcrazeCrazyflieBoxLoader",
]
