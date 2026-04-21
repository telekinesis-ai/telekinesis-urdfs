"""RobotLoader subclasses for ABB industrial and collaborative arms."""

from .utils import RobotLoader


class ABBCrb15000595Loader(RobotLoader):
    """Loader for the ABB CRB 15000 5/0.95 collaborative arm."""

    robot_name = "abb_crb15000_5_95"
    robot_subdir = "abb/crb15000_description"
    urdf_relpath = "urdf/crb15000_5_95.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class ABBIrb1200590Loader(RobotLoader):
    """Loader for the ABB IRB 1200 5/90 industrial arm."""

    robot_name = "abb_irb1200_5_90"
    robot_subdir = "abb/irb1200_description"
    urdf_relpath = "urdf/irb1200_5_90.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class ABBIrb1200770Loader(RobotLoader):
    """Loader for the ABB IRB 1200 7/70 industrial arm."""

    robot_name = "abb_irb1200_7_70"
    robot_subdir = "abb/irb1200_description"
    urdf_relpath = "urdf/irb1200_7_70.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class ABBIrb120358Loader(RobotLoader):
    """Loader for the ABB IRB 120 3/58 industrial arm."""

    robot_name = "abb_irb120_3_58"
    robot_subdir = "abb/irb120_description"
    urdf_relpath = "urdf/irb120_3_58.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class ABBIrb120t358Loader(RobotLoader):
    """Loader for the ABB IRB 120T 3/58 industrial arm."""

    robot_name = "abb_irb120t_3_58"
    robot_subdir = "abb/irb120_description"
    urdf_relpath = "urdf/irb120t_3_58.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class ABBIrb1600612Loader(RobotLoader):
    """Loader for the ABB IRB 1600 6/1.2 industrial arm."""

    robot_name = "abb_irb1600_6_12"
    robot_subdir = "abb/irb1600_description"
    urdf_relpath = "urdf/irb1600_6_12.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class ABBIrb16008145Loader(RobotLoader):
    """Loader for the ABB IRB 1600 8/1.45 industrial arm."""

    robot_name = "abb_irb1600_8_145"
    robot_subdir = "abb/irb1600_description"
    urdf_relpath = "urdf/irb1600_8_145.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class ABBIrb2400Loader(RobotLoader):
    """Loader for the ABB IRB 2400 industrial arm."""

    robot_name = "abb_irb2400"
    robot_subdir = "abb/irb2400_description"
    urdf_relpath = "urdf/irb2400.urdf"
    srdf_relpath = "srdf/abb_irb2400.srdf"
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class ABBIrb260012165Loader(RobotLoader):
    """Loader for the ABB IRB 2600 12/1.65 industrial arm."""

    robot_name = "abb_irb2600_12_165"
    robot_subdir = "abb/irb2600_description"
    urdf_relpath = "urdf/irb2600_12_165.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class ABBIrb4400l30243Loader(RobotLoader):
    """Loader for the ABB IRB 4400L 30/2.43 industrial arm."""

    robot_name = "abb_irb4400l_30_243"
    robot_subdir = "abb/irb4400_description"
    urdf_relpath = "urdf/irb4400l_30_243.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class ABBIrb460020250Loader(RobotLoader):
    """Loader for the ABB IRB 4600 20/2.50 industrial arm."""

    robot_name = "abb_irb4600_20_250"
    robot_subdir = "abb/irb4600_description"
    urdf_relpath = "urdf/irb4600_20_250.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class ABBIrb460040255Loader(RobotLoader):
    """Loader for the ABB IRB 4600 40/2.55 industrial arm."""

    robot_name = "abb_irb4600_40_255"
    robot_subdir = "abb/irb4600_description"
    urdf_relpath = "urdf/irb4600_40_255.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class ABBIrb460060205Loader(RobotLoader):
    """Loader for the ABB IRB 4600 60/2.05 industrial arm."""

    robot_name = "abb_irb4600_60_205"
    robot_subdir = "abb/irb4600_description"
    urdf_relpath = "urdf/irb4600_60_205.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class ABBIrb527120Loader(RobotLoader):
    """Loader for the ABB IRB 52 7/1.20 industrial arm."""

    robot_name = "abb_irb52_7_120"
    robot_subdir = "abb/irb52_description"
    urdf_relpath = "urdf/irb52_7_120.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class ABBIrb527145Loader(RobotLoader):
    """Loader for the ABB IRB 52 7/1.45 industrial arm."""

    robot_name = "abb_irb52_7_145"
    robot_subdir = "abb/irb52_description"
    urdf_relpath = "urdf/irb52_7_145.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class ABBIrb5400Loader(RobotLoader):
    """Loader for the ABB IRB 5400 industrial arm."""

    robot_name = "abb_irb5400"
    robot_subdir = "abb/irb5400_description"
    urdf_relpath = "urdf/irb5400.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class ABBIrb6600Loader(RobotLoader):
    """Loader for the ABB IRB 6600 industrial arm."""

    robot_name = "abb_irb6600"
    robot_subdir = "abb/irb6600_description"
    urdf_relpath = "urdf/irb6600.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class ABBIrb6640185280Loader(RobotLoader):
    """Loader for the ABB IRB 6640 185/2.80 industrial arm."""

    robot_name = "abb_irb6640_185_280"
    robot_subdir = "abb/irb6640_description"
    urdf_relpath = "urdf/irb6640_185_280.urdf"
    srdf_relpath = "srdf/abb_irb6640_185_280.srdf"
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class ABBIrb6650s90390Loader(RobotLoader):
    """Loader for the ABB IRB 6650S 90/3.90 industrial arm."""

    robot_name = "abb_irb6650s_90_390"
    robot_subdir = "abb/irb6650s_description"
    urdf_relpath = "urdf/irb6650s_90_390.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class ABBIrb6650s125350Loader(RobotLoader):
    """Loader for the ABB IRB 6650S 125/3.50 industrial arm."""

    robot_name = "abb_irb6650s_125_350"
    robot_subdir = "abb/irb6650s_description"
    urdf_relpath = "urdf/irb6650s_125_350.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class ABBIrb6700200260Loader(RobotLoader):
    """Loader for the ABB IRB 6700 200/2.60 industrial arm."""

    robot_name = "abb_irb6700_200_260"
    robot_subdir = "abb/irb6700_description"
    urdf_relpath = "urdf/irb6700_200_260.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class ABBIrb6700235265Loader(RobotLoader):
    """Loader for the ABB IRB 6700 235/2.65 industrial arm."""

    robot_name = "abb_irb6700_235_265"
    robot_subdir = "abb/irb6700_description"
    urdf_relpath = "urdf/irb6700_235_265.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class ABBIrb7600150350Loader(RobotLoader):
    """Loader for the ABB IRB 7600 150/3.50 industrial arm."""

    robot_name = "abb_irb7600_150_350"
    robot_subdir = "abb/irb7600_description"
    urdf_relpath = "urdf/irb7600_150_350.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


__all__ = [
    "ABBCrb15000595Loader",
    "ABBIrb1200590Loader",
    "ABBIrb1200770Loader",
    "ABBIrb120358Loader",
    "ABBIrb120t358Loader",
    "ABBIrb1600612Loader",
    "ABBIrb16008145Loader",
    "ABBIrb2400Loader",
    "ABBIrb260012165Loader",
    "ABBIrb4400l30243Loader",
    "ABBIrb460020250Loader",
    "ABBIrb460040255Loader",
    "ABBIrb460060205Loader",
    "ABBIrb527120Loader",
    "ABBIrb527145Loader",
    "ABBIrb5400Loader",
    "ABBIrb6600Loader",
    "ABBIrb6640185280Loader",
    "ABBIrb6650s90390Loader",
    "ABBIrb6650s125350Loader",
    "ABBIrb6700200260Loader",
    "ABBIrb6700235265Loader",
    "ABBIrb7600150350Loader",
]
