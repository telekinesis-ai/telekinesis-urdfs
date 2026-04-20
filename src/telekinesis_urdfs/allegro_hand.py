"""RobotLoader subclasses for Allegro Hand dexterous hands."""

from .utils import RobotLoader


class AllegroLeftHandLoader(RobotLoader):
    """Loader for the Allegro left dexterous hand."""

    robot_name = "allegro_left_hand"
    robot_subdir = "allegro_hand_description"
    urdf_relpath = "urdf/allegro_left_hand.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


class AllegroRightHandLoader(RobotLoader):
    """Loader for the Allegro right dexterous hand."""

    robot_name = "allegro_right_hand"
    robot_subdir = "allegro_hand_description"
    urdf_relpath = "urdf/allegro_right_hand.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
    ref_posture = None
    free_flyer = False


__all__ = [
    "AllegroLeftHandLoader",
    "AllegroRightHandLoader",
]
