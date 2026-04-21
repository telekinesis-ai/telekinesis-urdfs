"""RobotLoader subclasses for Fanuc industrial arms."""

from .utils import RobotLoader


class FanucCr35iaLoader(RobotLoader):
    """Loader for the Fanuc CR-35iA collaborative arm."""

    robot_name = "fanuc_cr35ia"
    robot_subdir = "fanuc/cr35ia_description"
    urdf_relpath = "urdf/cr35ia.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucCr7iaLoader(RobotLoader):
    """Loader for the Fanuc CR-7iA collaborative arm."""

    robot_name = "fanuc_cr7ia"
    robot_subdir = "fanuc/cr7ia_description"
    urdf_relpath = "urdf/cr7ia.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucCr7ialLoader(RobotLoader):
    """Loader for the Fanuc CR-7iA/L collaborative arm."""

    robot_name = "fanuc_cr7ial"
    robot_subdir = "fanuc/cr7ia_description"
    urdf_relpath = "urdf/cr7ial.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucCrx10ialLoader(RobotLoader):
    """Loader for the Fanuc CRX-10iA/L collaborative arm."""

    robot_name = "fanuc_crx10ial"
    robot_subdir = "fanuc/crx10ia_description"
    urdf_relpath = "urdf/crx10ial.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucLrmate200iLoader(RobotLoader):
    """Loader for the Fanuc LR Mate 200i industrial arm."""

    robot_name = "fanuc_lrmate200i"
    robot_subdir = "fanuc/lrmate200i_description"
    urdf_relpath = "urdf/lrmate200i.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucLrmate200ibLoader(RobotLoader):
    """Loader for the Fanuc LR Mate 200iB industrial arm."""

    robot_name = "fanuc_lrmate200ib"
    robot_subdir = "fanuc/lrmate200ib_description"
    urdf_relpath = "urdf/lrmate200ib.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucLrmate200ib3lLoader(RobotLoader):
    """Loader for the Fanuc LR Mate 200iB/3L industrial arm."""

    robot_name = "fanuc_lrmate200ib3l"
    robot_subdir = "fanuc/lrmate200ib_description"
    urdf_relpath = "urdf/lrmate200ib3l.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucLrmate200icLoader(RobotLoader):
    """Loader for the Fanuc LR Mate 200iC industrial arm."""

    robot_name = "fanuc_lrmate200ic"
    robot_subdir = "fanuc/lrmate200ic_description"
    urdf_relpath = "urdf/lrmate200ic.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucLrmate200ic5fLoader(RobotLoader):
    """Loader for the Fanuc LR Mate 200iC/5F industrial arm."""

    robot_name = "fanuc_lrmate200ic5f"
    robot_subdir = "fanuc/lrmate200ic_description"
    urdf_relpath = "urdf/lrmate200ic5f.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucLrmate200ic5hLoader(RobotLoader):
    """Loader for the Fanuc LR Mate 200iC/5H industrial arm."""

    robot_name = "fanuc_lrmate200ic5h"
    robot_subdir = "fanuc/lrmate200ic_description"
    urdf_relpath = "urdf/lrmate200ic5h.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucLrmate200ic5hsLoader(RobotLoader):
    """Loader for the Fanuc LR Mate 200iC/5HS industrial arm."""

    robot_name = "fanuc_lrmate200ic5hs"
    robot_subdir = "fanuc/lrmate200ic_description"
    urdf_relpath = "urdf/lrmate200ic5hs.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucLrmate200ic5lLoader(RobotLoader):
    """Loader for the Fanuc LR Mate 200iC/5L industrial arm."""

    robot_name = "fanuc_lrmate200ic5l"
    robot_subdir = "fanuc/lrmate200ic_description"
    urdf_relpath = "urdf/lrmate200ic5l.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucLrmate200idLoader(RobotLoader):
    """Loader for the Fanuc LR Mate 200iD industrial arm."""

    robot_name = "fanuc_lrmate200id"
    robot_subdir = "fanuc/lrmate200id_description"
    urdf_relpath = "urdf/lrmate200id.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucLrmate200id4sLoader(RobotLoader):
    """Loader for the Fanuc LR Mate 200iD/4S industrial arm."""

    robot_name = "fanuc_lrmate200id4s"
    robot_subdir = "fanuc/lrmate200id_description"
    urdf_relpath = "urdf/lrmate200id4s.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucLrmate200id4scLoader(RobotLoader):
    """Loader for the Fanuc LR Mate 200iD/4SC industrial arm."""

    robot_name = "fanuc_lrmate200id4sc"
    robot_subdir = "fanuc/lrmate200id_description"
    urdf_relpath = "urdf/lrmate200id4sc.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucLrmate200id4shLoader(RobotLoader):
    """Loader for the Fanuc LR Mate 200iD/4SH industrial arm."""

    robot_name = "fanuc_lrmate200id4sh"
    robot_subdir = "fanuc/lrmate200id_description"
    urdf_relpath = "urdf/lrmate200id4sh.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucLrmate200id7hLoader(RobotLoader):
    """Loader for the Fanuc LR Mate 200iD/7H industrial arm."""

    robot_name = "fanuc_lrmate200id7h"
    robot_subdir = "fanuc/lrmate200id_description"
    urdf_relpath = "urdf/lrmate200id7h.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucLrmate200id7lLoader(RobotLoader):
    """Loader for the Fanuc LR Mate 200iD/7L industrial arm."""

    robot_name = "fanuc_lrmate200id7l"
    robot_subdir = "fanuc/lrmate200id_description"
    urdf_relpath = "urdf/lrmate200id7l.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucLrmate200id7lcLoader(RobotLoader):
    """Loader for the Fanuc LR Mate 200iD/7LC industrial arm."""

    robot_name = "fanuc_lrmate200id7lc"
    robot_subdir = "fanuc/lrmate200id_description"
    urdf_relpath = "urdf/lrmate200id7lc.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucM10iaLoader(RobotLoader):
    """Loader for the Fanuc M-10iA industrial arm."""

    robot_name = "fanuc_m10ia"
    robot_subdir = "fanuc/m10ia_description"
    urdf_relpath = "urdf/m10ia.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucM10ia7lLoader(RobotLoader):
    """Loader for the Fanuc M-10iA/7L industrial arm."""

    robot_name = "fanuc_m10ia7l"
    robot_subdir = "fanuc/m10ia_description"
    urdf_relpath = "urdf/m10ia7l.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucM16ib20Loader(RobotLoader):
    """Loader for the Fanuc M-16iB/20 industrial arm."""

    robot_name = "fanuc_m16ib20"
    robot_subdir = "fanuc/m16ib_description"
    urdf_relpath = "urdf/m16ib20.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucM20iaLoader(RobotLoader):
    """Loader for the Fanuc M-20iA industrial arm."""

    robot_name = "fanuc_m20ia"
    robot_subdir = "fanuc/m20ia_description"
    urdf_relpath = "urdf/m20ia.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucM20ia10lLoader(RobotLoader):
    """Loader for the Fanuc M-20iA/10L industrial arm."""

    robot_name = "fanuc_m20ia10l"
    robot_subdir = "fanuc/m20ia_description"
    urdf_relpath = "urdf/m20ia10l.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucM20ib25Loader(RobotLoader):
    """Loader for the Fanuc M-20iB/25 industrial arm."""

    robot_name = "fanuc_m20ib25"
    robot_subdir = "fanuc/m20ib_description"
    urdf_relpath = "urdf/m20ib25.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucM430ia2fLoader(RobotLoader):
    """Loader for the Fanuc M-430iA/2F industrial arm."""

    robot_name = "fanuc_m430ia2f"
    robot_subdir = "fanuc/m430ia_description"
    urdf_relpath = "urdf/m430ia2f.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucM430ia2pLoader(RobotLoader):
    """Loader for the Fanuc M-430iA/2P industrial arm."""

    robot_name = "fanuc_m430ia2p"
    robot_subdir = "fanuc/m430ia_description"
    urdf_relpath = "urdf/m430ia2p.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucM6ibLoader(RobotLoader):
    """Loader for the Fanuc M-6iB industrial arm."""

    robot_name = "fanuc_m6ib"
    robot_subdir = "fanuc/m6ib_description"
    urdf_relpath = "urdf/m6ib.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucM6ib6sLoader(RobotLoader):
    """Loader for the Fanuc M-6iB/6S industrial arm."""

    robot_name = "fanuc_m6ib6s"
    robot_subdir = "fanuc/m6ib_description"
    urdf_relpath = "urdf/m6ib6s.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucM710ic45mLoader(RobotLoader):
    """Loader for the Fanuc M-710iC/45M industrial arm."""

    robot_name = "fanuc_m710ic45m"
    robot_subdir = "fanuc/m710ic_description"
    urdf_relpath = "urdf/m710ic45m.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucM710ic50Loader(RobotLoader):
    """Loader for the Fanuc M-710iC/50 industrial arm."""

    robot_name = "fanuc_m710ic50"
    robot_subdir = "fanuc/m710ic_description"
    urdf_relpath = "urdf/m710ic50.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucM900ia260lLoader(RobotLoader):
    """Loader for the Fanuc M-900iA/260L industrial arm."""

    robot_name = "fanuc_m900ia260l"
    robot_subdir = "fanuc/m900ia_description"
    urdf_relpath = "urdf/m900ia260l.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucM900ib700Loader(RobotLoader):
    """Loader for the Fanuc M-900iB/700 industrial arm."""

    robot_name = "fanuc_m900ib700"
    robot_subdir = "fanuc/m900ib_description"
    urdf_relpath = "urdf/m900ib700.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucR1000ia80fLoader(RobotLoader):
    """Loader for the Fanuc R-1000iA/80F industrial arm."""

    robot_name = "fanuc_r1000ia80f"
    robot_subdir = "fanuc/r1000ia_description"
    urdf_relpath = "urdf/r1000ia80f.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucR2000ib210fLoader(RobotLoader):
    """Loader for the Fanuc R-2000iB/210F industrial arm."""

    robot_name = "fanuc_r2000ib210f"
    robot_subdir = "fanuc/r2000ib_description"
    urdf_relpath = "urdf/r2000ib210f.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucR2000ic125lLoader(RobotLoader):
    """Loader for the Fanuc R-2000iC/125L industrial arm."""

    robot_name = "fanuc_r2000ic125l"
    robot_subdir = "fanuc/r2000ic_description"
    urdf_relpath = "urdf/r2000ic125l.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucR2000ic165fLoader(RobotLoader):
    """Loader for the Fanuc R-2000iC/165F industrial arm."""

    robot_name = "fanuc_r2000ic165f"
    robot_subdir = "fanuc/r2000ic_description"
    urdf_relpath = "urdf/r2000ic165f.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucR2000ic210fLoader(RobotLoader):
    """Loader for the Fanuc R-2000iC/210F industrial arm."""

    robot_name = "fanuc_r2000ic210f"
    robot_subdir = "fanuc/r2000ic_description"
    urdf_relpath = "urdf/r2000ic210f.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucR2000ic210lLoader(RobotLoader):
    """Loader for the Fanuc R-2000iC/210L industrial arm."""

    robot_name = "fanuc_r2000ic210l"
    robot_subdir = "fanuc/r2000ic_description"
    urdf_relpath = "urdf/r2000ic210l.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class FanucR2000ic270fLoader(RobotLoader):
    """Loader for the Fanuc R-2000iC/270F industrial arm."""

    robot_name = "fanuc_r2000ic270f"
    robot_subdir = "fanuc/r2000ic_description"
    urdf_relpath = "urdf/r2000ic270f.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


__all__ = [
    "FanucCr35iaLoader",
    "FanucCr7iaLoader",
    "FanucCr7ialLoader",
    "FanucCrx10ialLoader",
    "FanucLrmate200iLoader",
    "FanucLrmate200ibLoader",
    "FanucLrmate200ib3lLoader",
    "FanucLrmate200icLoader",
    "FanucLrmate200ic5fLoader",
    "FanucLrmate200ic5hLoader",
    "FanucLrmate200ic5hsLoader",
    "FanucLrmate200ic5lLoader",
    "FanucLrmate200idLoader",
    "FanucLrmate200id4sLoader",
    "FanucLrmate200id4scLoader",
    "FanucLrmate200id4shLoader",
    "FanucLrmate200id7hLoader",
    "FanucLrmate200id7lLoader",
    "FanucLrmate200id7lcLoader",
    "FanucM10iaLoader",
    "FanucM10ia7lLoader",
    "FanucM16ib20Loader",
    "FanucM20iaLoader",
    "FanucM20ia10lLoader",
    "FanucM20ib25Loader",
    "FanucM430ia2fLoader",
    "FanucM430ia2pLoader",
    "FanucM6ibLoader",
    "FanucM6ib6sLoader",
    "FanucM710ic45mLoader",
    "FanucM710ic50Loader",
    "FanucM900ia260lLoader",
    "FanucM900ib700Loader",
    "FanucR1000ia80fLoader",
    "FanucR2000ib210fLoader",
    "FanucR2000ic125lLoader",
    "FanucR2000ic165fLoader",
    "FanucR2000ic210fLoader",
    "FanucR2000ic210lLoader",
    "FanucR2000ic270fLoader",
]
