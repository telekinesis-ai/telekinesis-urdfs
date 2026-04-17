from typing import Dict, Type

from synapse_robot_data.loaders.robots._base_loader import RobotDescription, RobotLoader
from synapse_robot_data.loaders.robots._universal_robots_loader import (
    UR3eLoader,
    UR3GripperLoader,
    UR3Loader,
    UR5eLoader,
    UR5GripperLoader,
    UR5JointLimitedLoader,
    UR5Loader,
    UR5Robotiq2F85Loader,
    UR7eLoader,
    UR10eFactoryCalibrationLoader,
    UR10eLoader,
    UR10eNewFactoryCalibrationLoader,
    UR10Loader,
    UR12eLoader,
    UR15Loader,
    UR16eLoader,
    UR20Loader,
    UR30Loader,
)



ROBOTS: Dict[str, Type[RobotLoader]] = {
    # Class-name style aliases for easy synapse support (input is normalized to lowercase in load()).
    "universalrobotsur3": UR3Loader,
    "universalrobotsur5": UR5Loader,
    "universalrobotsur10": UR10Loader,
    "universalrobotsur3e": UR3eLoader,
    "universalrobotsur5e": UR5eLoader,
    "universalrobotsur7e": UR7eLoader,
    "universalrobotsur10e": UR10eLoader,
    "universalrobotsur12e": UR12eLoader,
    "universalrobotsur15": UR15Loader,
    "universalrobotsur16e": UR16eLoader,
    "universalrobotsur20": UR20Loader,
    "universalrobotsur30": UR30Loader,

    # Backward-compatible short aliases.
    "ur3": UR3Loader,
    "ur5": UR5Loader,
    "ur10": UR10Loader,
    "ur3e": UR3eLoader,
    "ur5e": UR5eLoader,
    "ur7e": UR7eLoader,
    "ur10e": UR10eLoader,
    "ur12e": UR12eLoader,
    "ur15": UR15Loader,
    "ur16e": UR16eLoader,
    "ur20": UR20Loader,
    "ur30": UR30Loader,
    "ur3_gripper": UR3GripperLoader,
    "ur5_gripper": UR5GripperLoader,
    "ur5_joint_limited_robot": UR5JointLimitedLoader,
    "ur5_robotiq_2f_85": UR5Robotiq2F85Loader,
    "ur10e_factory_calibration": UR10eFactoryCalibrationLoader,
    "ur10e_new_factory_calibration": UR10eNewFactoryCalibrationLoader,
}

def load(name: str) -> RobotDescription:
    """
    Return basic file paths and metadata for a known robot.
    """
    key = name.lower()
    if key not in ROBOTS:
        available = ", ".join(sorted(ROBOTS))
        raise ValueError(f"Unknown robot '{name}'. Available robots: {available}")

    loader_cls = ROBOTS[key]
    desc = loader_cls.describe()

    if not desc.urdf_path.exists():
        raise FileNotFoundError(
            f"URDF file not found for robot '{name}': {desc.urdf_path}"
        )

    if desc.srdf_path is not None and not desc.srdf_path.exists():
        raise FileNotFoundError(
            f"SRDF file not found for robot '{name}': {desc.srdf_path}"
        )

    return desc


def load_full(name: str) -> dict:
    """
    Slightly richer form, useful if later you want more metadata.
    """
    desc = load(name)
    return {
        "name": desc.name,
        "root_model_dir": desc.root_model_dir,
        "model_dir": desc.model_dir,
        "urdf_path": desc.urdf_path,
        "srdf_path": desc.srdf_path,
        "mesh_dir": desc.mesh_dir,
        "ref_posture": desc.ref_posture,
        "free_flyer": desc.free_flyer,
    }


__all__ = ["ROBOTS", "load", "load_full", "RobotDescription", "RobotLoader"]