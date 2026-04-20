"""RobotLoader subclasses for Unitree robots (quadrupeds, humanoids, arms)."""

from .utils import RobotLoader


# ── Quadrupeds ────────────────────────────────────────────────────────────────

class UnitreeA1Loader(RobotLoader):
    """Loader for the Unitree A1 quadruped."""

    robot_name = "unitree_a1"
    robot_subdir = "unitree/a1_description"
    urdf_relpath = "urdf/a1.urdf"
    srdf_relpath = "srdf/a1.srdf"
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class UnitreeAliengoLoader(RobotLoader):
    """Loader for the Unitree Aliengo quadruped."""

    robot_name = "unitree_aliengo"
    robot_subdir = "unitree/aliengo_description"
    urdf_relpath = "urdf/aliengo.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class UnitreeB1Loader(RobotLoader):
    """Loader for the Unitree B1 quadruped."""

    robot_name = "unitree_b1"
    robot_subdir = "unitree/b1_description"
    urdf_relpath = "urdf/b1.urdf"
    srdf_relpath = "srdf/b1.srdf"
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class UnitreeB1Z1Loader(RobotLoader):
    """Loader for Unitree B1 with Z1 arm."""

    robot_name = "unitree_b1_z1"
    robot_subdir = "unitree/b1_description"
    urdf_relpath = "urdf/b1-z1.urdf"
    srdf_relpath = "srdf/b1-z1.srdf"
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class UnitreeB2Loader(RobotLoader):
    """Loader for the Unitree B2 quadruped."""

    robot_name = "unitree_b2"
    robot_subdir = "unitree/b2_description"
    urdf_relpath = "urdf/b2_description.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class UnitreeB2wLoader(RobotLoader):
    """Loader for the Unitree B2W wheeled quadruped."""

    robot_name = "unitree_b2w"
    robot_subdir = "unitree/b2w_description"
    urdf_relpath = "urdf/b2w_description.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class UnitreeGo1Loader(RobotLoader):
    """Loader for the Unitree Go1 quadruped."""

    robot_name = "unitree_go1"
    robot_subdir = "unitree/go1_description"
    urdf_relpath = "urdf/go1.urdf"
    srdf_relpath = "srdf/go1.srdf"
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class UnitreeGo2Loader(RobotLoader):
    """Loader for the Unitree Go2 quadruped."""

    robot_name = "unitree_go2"
    robot_subdir = "unitree/go2_description"
    urdf_relpath = "urdf/go2.urdf"
    srdf_relpath = "srdf/go2.srdf"
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class UnitreeGo2DescriptionLoader(RobotLoader):
    """Loader for the Unitree Go2 description variant."""

    robot_name = "unitree_go2_description"
    robot_subdir = "unitree/go2_description"
    urdf_relpath = "urdf/go2_description.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class UnitreeGo2wLoader(RobotLoader):
    """Loader for the Unitree Go2W wheeled quadruped."""

    robot_name = "unitree_go2w"
    robot_subdir = "unitree/go2w_description"
    urdf_relpath = "urdf/go2w_description.urdf"
    srdf_relpath = None
    mesh_relpath = "dae"
    ref_posture = None
    free_flyer = False


# ── Humanoids ─────────────────────────────────────────────────────────────────

class UnitreeG123dofLoader(RobotLoader):
    """Loader for the Unitree G1 humanoid (23 DOF)."""

    robot_name = "unitree_g1_23dof"
    robot_subdir = "unitree/g1_description"
    urdf_relpath = "g1_23dof.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class UnitreeG123dofRev10Loader(RobotLoader):
    """Loader for the Unitree G1 humanoid (23 DOF, rev 1.0)."""

    robot_name = "unitree_g1_23dof_rev_1_0"
    robot_subdir = "unitree/g1_description"
    urdf_relpath = "g1_23dof_rev_1_0.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class UnitreeG129dofLoader(RobotLoader):
    """Loader for the Unitree G1 humanoid (29 DOF)."""

    robot_name = "unitree_g1_29dof"
    robot_subdir = "unitree/g1_description"
    urdf_relpath = "g1_29dof.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class UnitreeG129dofLockWaistLoader(RobotLoader):
    """Loader for Unitree G1 29 DOF with locked waist."""

    robot_name = "unitree_g1_29dof_lock_waist"
    robot_subdir = "unitree/g1_description"
    urdf_relpath = "g1_29dof_lock_waist.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class UnitreeG129dofLockWaistRev10Loader(RobotLoader):
    """Loader for Unitree G1 29 DOF locked-waist rev 1.0."""

    robot_name = "unitree_g1_29dof_lock_waist_rev_1_0"
    robot_subdir = "unitree/g1_description"
    urdf_relpath = "g1_29dof_lock_waist_rev_1_0.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class UnitreeG129dofRev10Loader(RobotLoader):
    """Loader for the Unitree G1 humanoid (29 DOF, rev 1.0)."""

    robot_name = "unitree_g1_29dof_rev_1_0"
    robot_subdir = "unitree/g1_description"
    urdf_relpath = "g1_29dof_rev_1_0.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class UnitreeG129dofWithHandLoader(RobotLoader):
    """Loader for Unitree G1 29 DOF with hands."""

    robot_name = "unitree_g1_29dof_with_hand"
    robot_subdir = "unitree/g1_description"
    urdf_relpath = "g1_29dof_with_hand.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class UnitreeG129dofWithHandRev10Loader(RobotLoader):
    """Loader for Unitree G1 29 DOF with hands, rev 1.0."""

    robot_name = "unitree_g1_29dof_with_hand_rev_1_0"
    robot_subdir = "unitree/g1_description"
    urdf_relpath = "g1_29dof_with_hand_rev_1_0.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class UnitreeG1DualArmLoader(RobotLoader):
    """Loader for the Unitree G1 dual-arm configuration."""

    robot_name = "unitree_g1_dual_arm"
    robot_subdir = "unitree/g1_description"
    urdf_relpath = "g1_dual_arm.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class UnitreeDex31LLoader(RobotLoader):
    """Loader for the Unitree Dex3-1 left dexterous hand."""

    robot_name = "unitree_dex3_1_l"
    robot_subdir = "unitree/g1_description"
    urdf_relpath = "dex3_1_l.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class UnitreeDex31RLoader(RobotLoader):
    """Loader for the Unitree Dex3-1 right dexterous hand."""

    robot_name = "unitree_dex3_1_r"
    robot_subdir = "unitree/g1_description"
    urdf_relpath = "dex3_1_r.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class UnitreeH1Loader(RobotLoader):
    """Loader for the Unitree H1 humanoid."""

    robot_name = "unitree_h1"
    robot_subdir = "unitree/h1_description"
    urdf_relpath = "urdf/h1.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class UnitreeH1WithHandLoader(RobotLoader):
    """Loader for the Unitree H1 humanoid with hands."""

    robot_name = "unitree_h1_with_hand"
    robot_subdir = "unitree/h1_description"
    urdf_relpath = "urdf/h1_with_hand.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class UnitreeH12Loader(RobotLoader):
    """Loader for the Unitree H1-2 humanoid."""

    robot_name = "unitree_h1_2"
    robot_subdir = "unitree/h1_2_description"
    urdf_relpath = "h1_2.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class UnitreeH12HandlessLoader(RobotLoader):
    """Loader for the Unitree H1-2 humanoid without hands."""

    robot_name = "unitree_h1_2_handless"
    robot_subdir = "unitree/h1_2_description"
    urdf_relpath = "h1_2_handless.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


# ── Arms ──────────────────────────────────────────────────────────────────────

class UnitreeZ1Loader(RobotLoader):
    """Loader for the Unitree Z1 robotic arm."""

    robot_name = "unitree_z1"
    robot_subdir = "unitree/z1_description"
    urdf_relpath = "urdf/z1.urdf"
    srdf_relpath = "srdf/z1.srdf"
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


__all__ = [
    # Quadrupeds
    "UnitreeA1Loader",
    "UnitreeAliengoLoader",
    "UnitreeB1Loader",
    "UnitreeB1Z1Loader",
    "UnitreeB2Loader",
    "UnitreeB2wLoader",
    "UnitreeGo1Loader",
    "UnitreeGo2Loader",
    "UnitreeGo2DescriptionLoader",
    "UnitreeGo2wLoader",
    # Humanoids
    "UnitreeG123dofLoader",
    "UnitreeG123dofRev10Loader",
    "UnitreeG129dofLoader",
    "UnitreeG129dofLockWaistLoader",
    "UnitreeG129dofLockWaistRev10Loader",
    "UnitreeG129dofRev10Loader",
    "UnitreeG129dofWithHandLoader",
    "UnitreeG129dofWithHandRev10Loader",
    "UnitreeG1DualArmLoader",
    "UnitreeDex31LLoader",
    "UnitreeDex31RLoader",
    "UnitreeH1Loader",
    "UnitreeH1WithHandLoader",
    "UnitreeH12Loader",
    "UnitreeH12HandlessLoader",
    # Arms
    "UnitreeZ1Loader",
]
