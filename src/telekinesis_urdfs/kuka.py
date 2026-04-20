"""RobotLoader subclasses for KUKA industrial arms."""

from .utils import RobotLoader


class KukaKr10r1100sixxLoader(RobotLoader):
    """Loader for the KUKA KR 10 R1100 SIXX industrial arm."""

    robot_name = "kuka_kr10r1100sixx"
    robot_subdir = "kuka/kr10_description"
    urdf_relpath = "urdf/kr10r1100sixx.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class KukaKr10r1420Loader(RobotLoader):
    """Loader for the KUKA KR 10 R1420 industrial arm."""

    robot_name = "kuka_kr10r1420"
    robot_subdir = "kuka/kr10_description"
    urdf_relpath = "urdf/kr10r1420.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class KukaKr10r9002Loader(RobotLoader):
    """Loader for the KUKA KR 10 R900-2 industrial arm."""

    robot_name = "kuka_kr10r900_2"
    robot_subdir = "kuka/kr10_description"
    urdf_relpath = "urdf/kr10r900_2.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class KukaKr120r2500proLoader(RobotLoader):
    """Loader for the KUKA KR 120 R2500 pro industrial arm."""

    robot_name = "kuka_kr120r2500pro"
    robot_subdir = "kuka/kr120_description"
    urdf_relpath = "urdf/kr120r2500pro.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class KukaKr1502Loader(RobotLoader):
    """Loader for the KUKA KR 150-2 industrial arm."""

    robot_name = "kuka_kr150_2"
    robot_subdir = "kuka/kr150_description"
    urdf_relpath = "urdf/kr150_2.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class KukaKr150r31002Loader(RobotLoader):
    """Loader for the KUKA KR 150 R3100-2 industrial arm."""

    robot_name = "kuka_kr150r3100_2"
    robot_subdir = "kuka/kr150_description"
    urdf_relpath = "urdf/kr150r3100_2.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class KukaKr162Loader(RobotLoader):
    """Loader for the KUKA KR 16-2 industrial arm."""

    robot_name = "kuka_kr16_2"
    robot_subdir = "kuka/kr16_description"
    urdf_relpath = "urdf/kr16_2.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class KukaKr210l150Loader(RobotLoader):
    """Loader for the KUKA KR 210 L150 industrial arm."""

    robot_name = "kuka_kr210l150"
    robot_subdir = "kuka/kr210_description"
    urdf_relpath = "urdf/kr210l150.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class KukaKr3r540Loader(RobotLoader):
    """Loader for the KUKA KR 3 R540 industrial arm."""

    robot_name = "kuka_kr3r540"
    robot_subdir = "kuka/kr3_description"
    urdf_relpath = "urdf/kr3r540.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class KukaKr5ArcLoader(RobotLoader):
    """Loader for the KUKA KR 5 ARC industrial arm."""

    robot_name = "kuka_kr5_arc"
    robot_subdir = "kuka/kr5_description"
    urdf_relpath = "urdf/kr5_arc.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class KukaKr6r700sixxLoader(RobotLoader):
    """Loader for the KUKA KR 6 R700 SIXX industrial arm."""

    robot_name = "kuka_kr6r700sixx"
    robot_subdir = "kuka/kr6_description"
    urdf_relpath = "urdf/kr6r700sixx.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class KukaKr6r9002Loader(RobotLoader):
    """Loader for the KUKA KR 6 R900-2 industrial arm."""

    robot_name = "kuka_kr6r900_2"
    robot_subdir = "kuka/kr6_description"
    urdf_relpath = "urdf/kr6r900_2.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class KukaKr6r900sixxLoader(RobotLoader):
    """Loader for the KUKA KR 6 R900 SIXX industrial arm."""

    robot_name = "kuka_kr6r900sixx"
    robot_subdir = "kuka/kr6_description"
    urdf_relpath = "urdf/kr6r900sixx.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class KukaLbrIiwa14R820Loader(RobotLoader):
    """Loader for the KUKA LBR iiwa 14 R820 research arm."""

    robot_name = "kuka_lbr_iiwa_14_r820"
    robot_subdir = "kuka/lbr_iiwa_description"
    urdf_relpath = "urdf/lbr_iiwa_14_r820.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


__all__ = [
    "KukaKr10r1100sixxLoader",
    "KukaKr10r1420Loader",
    "KukaKr10r9002Loader",
    "KukaKr120r2500proLoader",
    "KukaKr1502Loader",
    "KukaKr150r31002Loader",
    "KukaKr162Loader",
    "KukaKr210l150Loader",
    "KukaKr3r540Loader",
    "KukaKr5ArcLoader",
    "KukaKr6r700sixxLoader",
    "KukaKr6r9002Loader",
    "KukaKr6r900sixxLoader",
    "KukaLbrIiwa14R820Loader",
]
