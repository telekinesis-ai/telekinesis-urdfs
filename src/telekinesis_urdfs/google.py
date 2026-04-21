"""RobotLoader subclasses for Google Barkour quadrupeds."""

from .utils import RobotLoader


class BarkourV0Loader(RobotLoader):
    """Loader for the Google Barkour v0 quadruped."""

    robot_name = "barkour_v0"
    robot_subdir = "google/barkour_v0_description"
    urdf_relpath = "barkour_v0.urdf"
    srdf_relpath = None
    mesh_relpath = "assets"
    ref_posture = None
    free_flyer = False


class BarkourVbLoader(RobotLoader):
    """Loader for the Google Barkour vB quadruped."""

    robot_name = "barkour_vb"
    robot_subdir = "google/barkour_vb_description"
    urdf_relpath = "barkour_vb_rev_1_0_head_straight.urdf"
    srdf_relpath = None
    mesh_relpath = "assets"
    ref_posture = None
    free_flyer = False


__all__ = [
    "BarkourV0Loader",
    "BarkourVbLoader",
]
