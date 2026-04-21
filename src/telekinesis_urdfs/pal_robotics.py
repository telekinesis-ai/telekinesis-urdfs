"""RobotLoader subclasses for PAL Robotics platforms."""

from .utils import RobotLoader


# ── Solo (quadruped) ──────────────────────────────────────────────────────────

class PalSoloLoader(RobotLoader):
    """Loader for the PAL Robotics Solo quadruped."""

    robot_name = "pal_solo"
    robot_subdir = "pal_robotics/solo_description"
    urdf_relpath = "robots/solo.urdf"
    srdf_relpath = "srdf/solo.srdf"
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class PalSolo12Loader(RobotLoader):
    """Loader for the PAL Robotics Solo12 quadruped."""

    robot_name = "pal_solo12"
    robot_subdir = "pal_robotics/solo_description"
    urdf_relpath = "robots/solo12.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


# ── Talos (humanoid) ──────────────────────────────────────────────────────────

class PalTalosFullV2Loader(RobotLoader):
    """Loader for the PAL Robotics Talos full humanoid v2."""

    robot_name = "pal_talos_full_v2"
    robot_subdir = "pal_robotics/talos_data_description"
    urdf_relpath = "robots/talos_full_v2.urdf"
    srdf_relpath = "srdf/talos.srdf"
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class PalTalosFullV2BoxLoader(RobotLoader):
    """Loader for Talos full v2 with box hand."""

    robot_name = "pal_talos_full_v2_box"
    robot_subdir = "pal_robotics/talos_data_description"
    urdf_relpath = "robots/talos_full_v2_box.urdf"
    srdf_relpath = "srdf/talos.srdf"
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class PalTalosLeftArmLoader(RobotLoader):
    """Loader for the Talos left arm only."""

    robot_name = "pal_talos_left_arm"
    robot_subdir = "pal_robotics/talos_data_description"
    urdf_relpath = "robots/talos_left_arm.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class PalTalosReducedLoader(RobotLoader):
    """Loader for Talos with a reduced kinematic tree."""

    robot_name = "pal_talos_reduced"
    robot_subdir = "pal_robotics/talos_data_description"
    urdf_relpath = "robots/talos_reduced.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class PalTalosReducedBoxLoader(RobotLoader):
    """Loader for Talos reduced with box hand."""

    robot_name = "pal_talos_reduced_box"
    robot_subdir = "pal_robotics/talos_data_description"
    urdf_relpath = "robots/talos_reduced_box.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class PalTalosReducedCorrectedLoader(RobotLoader):
    """Loader for Talos reduced with corrected inertias."""

    robot_name = "pal_talos_reduced_corrected"
    robot_subdir = "pal_robotics/talos_data_description"
    urdf_relpath = "robots/talos_reduced_corrected.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


# ── Tiago (mobile manipulator) ────────────────────────────────────────────────

class PalTiagoLoader(RobotLoader):
    """Loader for the PAL Robotics TIAGo mobile manipulator."""

    robot_name = "pal_tiago"
    robot_subdir = "pal_robotics/tiago_description"
    urdf_relpath = "robots/tiago.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class PalTiagoDualLoader(RobotLoader):
    """Loader for TIAGo with dual-arm configuration."""

    robot_name = "pal_tiago_dual"
    robot_subdir = "pal_robotics/tiago_description"
    urdf_relpath = "robots/tiago_dual.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class PalTiagoNoHandLoader(RobotLoader):
    """Loader for TIAGo without end-effectors."""

    robot_name = "pal_tiago_no_hand"
    robot_subdir = "pal_robotics/tiago_description"
    urdf_relpath = "robots/tiago_no_hand.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


__all__ = [
    "PalSoloLoader",
    "PalSolo12Loader",
    "PalTalosFullV2Loader",
    "PalTalosFullV2BoxLoader",
    "PalTalosLeftArmLoader",
    "PalTalosReducedLoader",
    "PalTalosReducedBoxLoader",
    "PalTalosReducedCorrectedLoader",
    "PalTiagoLoader",
    "PalTiagoDualLoader",
    "PalTiagoNoHandLoader",
]
