"""Shared utilities, base classes, and data types for robot and tool loaders."""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional
from importlib.resources import files


def _get_root_model_dir() -> Path:
    """Return the root directory of the bundled models.

    Returns:
        Absolute path to the ``models/`` directory inside the package.
    """
    return Path(files("telekinesis_urdfs") / "models")


def _get_model_root(robot_subdir: Optional[str] = None) -> Path:
    """Return the robots root, optionally scoped to a robot subdirectory.

    Args:
        robot_subdir: Relative path under ``robots/``, e.g.
            ``"universal_robots"``. If ``None``, the ``robots/`` root is
            returned.

    Returns:
        Absolute path to the requested directory.

    Raises:
        FileNotFoundError: If ``robot_subdir`` is given but does not exist.
    """
    robots_root = _get_root_model_dir() / "example-robot-data" / "robots"

    if robot_subdir:
        candidate = robots_root / robot_subdir
        if candidate.is_dir():
            return candidate
        raise FileNotFoundError(f"Robot subdir not found: {candidate}")

    return robots_root


def _get_tool_model_root(tool_subdir: Optional[str] = None) -> Path:
    """Return the tools root, optionally scoped to a tool subdirectory.

    Args:
        tool_subdir: Relative path under ``tools/``, e.g.
            ``"robotiq"``. If ``None``, the ``tools/`` root is returned.

    Returns:
        Absolute path to the requested directory.

    Raises:
        FileNotFoundError: If ``tool_subdir`` is given but does not exist.
    """
    tools_root = _get_root_model_dir() / "example-robot-data" / "tools"

    if tool_subdir:
        candidate = tools_root / tool_subdir
        if candidate.is_dir():
            return candidate
        raise FileNotFoundError(f"Tool subdir not found: {candidate}")

    return tools_root


@dataclass(frozen=True)
class ModelDescription:
    """Immutable snapshot of all resolved paths for a robot or tool.

    Attributes:
        name: Canonical name (e.g. ``"ur10e"``, ``"robotiq_2f_85"``).
        root_dir: Root of the bundled models or tools directory.
        model_dir: Robot- or tool-specific subdirectory.
        urdf_path: Absolute path to the URDF file.
        srdf_path: Absolute path to the SRDF file, or ``None``.
        mesh_dir: Absolute path to the mesh directory, or ``None``.
        ref_posture: Named reference joint configuration, or ``None``.
        free_flyer: ``True`` if the robot has an unactuated floating base.
    """

    name: str
    root_dir: Path
    model_dir: Path
    urdf_path: Path
    srdf_path: Optional[Path]
    mesh_dir: Optional[Path]
    ref_posture: Optional[str] = None
    free_flyer: bool = False


class RobotLoader:
    """Base class for all robot loaders.

    Subclasses declare class-level attributes that describe where a robot's
    URDF, SRDF, and meshes live relative to the bundled model data.

    Attributes:
        robot_name: Canonical name for the robot.
        robot_subdir: Path relative to ``robots/`` for this robot's data.
        urdf_relpath: URDF file path relative to ``model_dir``.
        srdf_relpath: SRDF file path relative to ``model_dir``, or ``None``.
        mesh_relpath: Mesh directory relative to ``model_dir``, or ``None``.
        ref_posture: Named reference joint configuration, or ``None``.
        free_flyer: ``True`` for robots with an unactuated floating base.
    """

    robot_name: str = ""
    robot_subdir: str = ""
    urdf_relpath: str = ""
    srdf_relpath: Optional[str] = None
    mesh_relpath: Optional[str] = None
    ref_posture: Optional[str] = None
    free_flyer: bool = False

    @classmethod
    def get_root_model_dir(cls) -> Path:
        """Return the root of the bundled models directory.

        Returns:
            Absolute path to ``models/``.
        """
        return _get_root_model_dir()

    @classmethod
    def get_model_dir(cls) -> Path:
        """Return the robot-specific model directory.

        Returns:
            Absolute path to the robot's model directory.

        Raises:
            ValueError: If ``robot_subdir`` is not set on the subclass.
        """
        if not cls.robot_subdir:
            raise ValueError(f"{cls.__name__}.robot_subdir must be set")
        return _get_model_root(cls.robot_subdir)

    @classmethod
    def get_urdf_path(cls) -> Path:
        """Return the absolute path to the robot's URDF file.

        Returns:
            Resolved absolute path to the URDF.

        Raises:
            ValueError: If ``urdf_relpath`` is not set on the subclass.
        """
        if not cls.urdf_relpath:
            raise ValueError(f"{cls.__name__}.urdf_relpath must be set")
        return (cls.get_model_dir() / cls.urdf_relpath).resolve()

    @classmethod
    def get_srdf_path(cls) -> Optional[Path]:
        """Return the absolute path to the robot's SRDF file, or ``None``.

        Returns:
            Resolved absolute path to the SRDF, or ``None`` if not set.
        """
        if cls.srdf_relpath is None:
            return None
        return (cls.get_model_dir() / cls.srdf_relpath).resolve()

    @classmethod
    def get_mesh_dir(cls) -> Optional[Path]:
        """Return the absolute path to the robot's mesh directory, or ``None``.

        Returns:
            Resolved absolute path to the mesh directory, or ``None``.
        """
        if cls.mesh_relpath is None:
            return None
        return (cls.get_model_dir() / cls.mesh_relpath).resolve()

    @classmethod
    def get_description(cls) -> ModelDescription:
        """Build and return a fully resolved ModelDescription.

        Returns:
            Populated, immutable ModelDescription for this robot.
        """
        return ModelDescription(
            name=cls.robot_name or cls.__name__,
            root_dir=cls.get_root_model_dir(),
            model_dir=cls.get_model_dir(),
            urdf_path=cls.get_urdf_path(),
            srdf_path=cls.get_srdf_path(),
            mesh_dir=cls.get_mesh_dir(),
            ref_posture=cls.ref_posture,
            free_flyer=cls.free_flyer,
        )


class ToolLoader:
    """Base class for all tool/end-effector loaders.

    Subclasses declare class-level attributes that describe where a tool's
    URDF, SRDF, and meshes live relative to the bundled tool data.

    Attributes:
        tool_name: Canonical name for the tool.
        tool_subdir: Path relative to ``tools/`` for this tool's data.
        urdf_relpath: URDF file path relative to ``model_dir``.
        srdf_relpath: SRDF file path relative to ``model_dir``, or ``None``.
        mesh_relpath: Mesh directory relative to ``model_dir``, or ``None``.
    """

    tool_name: str = ""
    tool_subdir: str = ""
    urdf_relpath: str = ""
    srdf_relpath: Optional[str] = None
    mesh_relpath: Optional[str] = None

    @classmethod
    def get_root_tool_dir(cls) -> Path:
        """Return the root of the bundled models directory.

        Returns:
            Absolute path to ``models/``.
        """
        return _get_root_model_dir()

    @classmethod
    def get_tool_dir(cls) -> Path:
        """Return the tool-specific directory.

        Returns:
            Absolute path to the tool's directory.

        Raises:
            ValueError: If ``tool_subdir`` is not set on the subclass.
        """
        if not cls.tool_subdir:
            raise ValueError(f"{cls.__name__}.tool_subdir must be set")
        return _get_tool_model_root(cls.tool_subdir)

    @classmethod
    def get_urdf_path(cls) -> Path:
        """Return the absolute path to the tool's URDF file.

        Returns:
            Resolved absolute path to the URDF.

        Raises:
            ValueError: If ``urdf_relpath`` is not set on the subclass.
        """
        if not cls.urdf_relpath:
            raise ValueError(f"{cls.__name__}.urdf_relpath must be set")
        return (cls.get_tool_dir() / cls.urdf_relpath).resolve()

    @classmethod
    def get_srdf_path(cls) -> Optional[Path]:
        """Return the absolute path to the tool's SRDF file, or ``None``.

        Returns:
            Resolved absolute path to the SRDF, or ``None`` if not set.
        """
        if cls.srdf_relpath is None:
            return None
        return (cls.get_tool_dir() / cls.srdf_relpath).resolve()

    @classmethod
    def get_mesh_dir(cls) -> Optional[Path]:
        """Return the absolute path to the tool's mesh directory, or ``None``.

        Returns:
            Resolved absolute path to the mesh directory, or ``None``.
        """
        if cls.mesh_relpath is None:
            return None
        return (cls.get_tool_dir() / cls.mesh_relpath).resolve()

    @classmethod
    def get_description(cls) -> ModelDescription:
        """Build and return a fully resolved ModelDescription.

        Returns:
            Populated, immutable ModelDescription for this tool.
        """
        return ModelDescription(
            name=cls.tool_name or cls.__name__,
            root_dir=cls.get_root_tool_dir(),
            model_dir=cls.get_tool_dir(),
            urdf_path=cls.get_urdf_path(),
            srdf_path=cls.get_srdf_path(),
            mesh_dir=cls.get_mesh_dir(),
        )
