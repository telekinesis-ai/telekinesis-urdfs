"""RobotLoader subclasses for Universal Robots collaborative arms."""

from .utils import RobotLoader


class UR3Loader(RobotLoader):
    """Loader for the Universal Robots UR3 collaborative arm."""

    robot_name = "ur3"
    robot_subdir = "universal_robots"
    urdf_relpath = "urdf/ur3.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes_description/ur3"
    ref_posture = None
    free_flyer = False


class UR5Loader(RobotLoader):
    """Loader for the Universal Robots UR5 collaborative arm."""

    robot_name = "ur5"
    robot_subdir = "universal_robots"
    urdf_relpath = "urdf/ur5.urdf"
    srdf_relpath = "srdf/ur5.srdf"
    mesh_relpath = "meshes_description/ur5"
    ref_posture = None
    free_flyer = False


class UR10Loader(RobotLoader):
    """Loader for the Universal Robots UR10 collaborative arm."""

    robot_name = "ur10"
    robot_subdir = "universal_robots"
    urdf_relpath = "urdf/ur10.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes_description/ur10"
    ref_posture = None
    free_flyer = False


class UR10eLoader(RobotLoader):
    """Loader for the Universal Robots UR10e collaborative arm."""

    robot_name = "ur10e"
    robot_subdir = "universal_robots"
    urdf_relpath = "urdf/ur10e.urdf"
    srdf_relpath = "srdf/ur10e.srdf"
    mesh_relpath = "meshes_description/ur10e"
    ref_posture = None
    free_flyer = False


class UR3eLoader(RobotLoader):
    """Loader for the Universal Robots UR3e collaborative arm."""

    robot_name = "ur3e"
    robot_subdir = "universal_robots"
    urdf_relpath = "urdf/ur3e.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes_description/ur3e"
    ref_posture = None
    free_flyer = False


class UR5eLoader(RobotLoader):
    """Loader for the Universal Robots UR5e collaborative arm."""

    robot_name = "ur5e"
    robot_subdir = "universal_robots"
    urdf_relpath = "urdf/ur5e.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes_description/ur5e"
    ref_posture = None
    free_flyer = False


class UR7eLoader(RobotLoader):
    """Loader for the Universal Robots UR7e collaborative arm."""

    robot_name = "ur7e"
    robot_subdir = "universal_robots"
    urdf_relpath = "urdf/ur7e.urdf"
    srdf_relpath = None
    mesh_relpath = None
    ref_posture = None
    free_flyer = False


class UR12eLoader(RobotLoader):
    """Loader for the Universal Robots UR12e collaborative arm."""

    robot_name = "ur12e"
    robot_subdir = "universal_robots"
    urdf_relpath = "urdf/ur12e.urdf"
    srdf_relpath = None
    mesh_relpath = None
    ref_posture = None
    free_flyer = False


class UR15Loader(RobotLoader):
    """Loader for the Universal Robots UR15 collaborative arm."""

    robot_name = "ur15"
    robot_subdir = "universal_robots"
    urdf_relpath = "urdf/ur15.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes_description/ur15"
    ref_posture = None
    free_flyer = False


class UR16eLoader(RobotLoader):
    """Loader for the Universal Robots UR16e collaborative arm."""

    robot_name = "ur16e"
    robot_subdir = "universal_robots"
    urdf_relpath = "urdf/ur16e.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes_description/ur16e"
    ref_posture = None
    free_flyer = False


class UR20Loader(RobotLoader):
    """Loader for the Universal Robots UR20 collaborative arm."""

    robot_name = "ur20"
    robot_subdir = "universal_robots"
    urdf_relpath = "urdf/ur20.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes_description/ur20"
    ref_posture = None
    free_flyer = False


class UR30Loader(RobotLoader):
    """Loader for the Universal Robots UR30 collaborative arm."""

    robot_name = "ur30"
    robot_subdir = "universal_robots"
    urdf_relpath = "urdf/ur30.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes_description/ur30"
    ref_posture = None
    free_flyer = False


class UR3GripperLoader(RobotLoader):
    """Loader for the UR3 with gripper SRDF configuration."""

    robot_name = "ur3_gripper"
    robot_subdir = "universal_robots"
    urdf_relpath = "urdf/ur3.urdf"
    srdf_relpath = "srdf/ur3_gripper.srdf"
    mesh_relpath = "meshes_description/ur3"
    ref_posture = None
    free_flyer = False


class UR5GripperLoader(RobotLoader):
    """Loader for the UR5 with gripper SRDF configuration."""

    robot_name = "ur5_gripper"
    robot_subdir = "universal_robots"
    urdf_relpath = "urdf/ur5.urdf"
    srdf_relpath = "srdf/ur5_gripper.srdf"
    mesh_relpath = "meshes_description/ur5"
    ref_posture = None
    free_flyer = False


class UR5JointLimitedLoader(RobotLoader):
    """Loader for the UR5 with joint-limited SRDF."""

    robot_name = "ur5_joint_limited_robot"
    robot_subdir = "universal_robots"
    urdf_relpath = "urdf/ur5.urdf"
    srdf_relpath = "srdf/ur5_joint_limited_robot.srdf"
    mesh_relpath = "meshes_description/ur5"
    ref_posture = None
    free_flyer = False


class UR5Robotiq2F85Loader(RobotLoader):
    """Loader for the UR5 with Robotiq 2F-85 gripper."""

    robot_name = "ur5_robotiq_2f_85"
    robot_subdir = "universal_robots"
    urdf_relpath = "urdf/ur5_robotiq_2f_85.urdf"
    srdf_relpath = "srdf/ur5_robotiq_2f_85.srdf"
    mesh_relpath = "meshes_description/ur5"
    ref_posture = None
    free_flyer = False


class UR10eFactoryCalibrationLoader(RobotLoader):
    """Loader for UR10e with factory calibration URDF."""

    robot_name = "ur10e_factory_calibration"
    robot_subdir = "universal_robots"
    urdf_relpath = "urdf/ur10e_factory_calibration.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes_description/ur10e"
    ref_posture = None
    free_flyer = False


class UR10eNewFactoryCalibrationLoader(RobotLoader):
    """Loader for UR10e with updated factory calibration."""

    robot_name = "ur10e_new_factory_calibration"
    robot_subdir = "universal_robots"
    urdf_relpath = "urdf/ur10e_new_factory_calibration.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes_description/ur10e"
    ref_posture = None
    free_flyer = False


__all__ = [
    "UR3Loader",
    "UR5Loader",
    "UR10Loader",
    "UR3eLoader",
    "UR5eLoader",
    "UR7eLoader",
    "UR10eLoader",
    "UR12eLoader",
    "UR15Loader",
    "UR16eLoader",
    "UR20Loader",
    "UR30Loader",
    "UR3GripperLoader",
    "UR5GripperLoader",
    "UR5JointLimitedLoader",
    "UR5Robotiq2F85Loader",
    "UR10eFactoryCalibrationLoader",
    "UR10eNewFactoryCalibrationLoader",
]
