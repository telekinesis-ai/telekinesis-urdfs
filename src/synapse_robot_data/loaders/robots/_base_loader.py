from dataclasses import dataclass
import os
from pathlib import Path
from typing import Optional
import importlib.resources as resources


@dataclass(frozen=True)
class RobotDescription:
    name: str
    root_model_dir: Path
    model_dir: Path
    urdf_path: Path
    srdf_path: Optional[Path]
    mesh_dir: Optional[Path]
    ref_posture: Optional[str] = None
    free_flyer: bool = False


def _package_root() -> Path:
    """Return the installed/imported package root for synapse_robot_data."""
    return Path(str(resources.files("synapse_robot_data"))).resolve()


def _source_checkout_root_model_dir() -> Optional[Path]:
    """
    Best-effort fallback for editable/source checkouts.

    Expected source layout:
      <repo>/
        pyproject.toml
        src/
          synapse_robot_data/
                models/
                    example-robot-data/
                        robots/
                        tools/
    """
    this_file = Path(__file__).resolve()

    # Look upwards for a repository root containing both pyproject.toml and src/synapse_robot_data
    for parent in [this_file.parent, *this_file.parents]:
        if not (parent / "pyproject.toml").is_file():
            continue
        if not (parent / "src" / "synapse_robot_data").is_dir():
            continue

        models_root = parent / "models"
        if (models_root / "example-robot-data" / "robots").is_dir():
            return models_root.resolve()

    return None


def get_root_model_dir() -> Path:
    """
    Resolve the top-level models directory that contains robots/, tools/, etc.

    Search order:
            1) SYNAPSE_MODELS_DIR env var (either <dir> or <dir>/robots)
            2) Installed package data: <site-packages>/synapse_robot_data/models
            3) Source checkout fallback: <repo>/models
    """
    candidates: list[Path] = []

    env_models_dir = os.environ.get("SYNAPSE_MODELS_DIR")
    if env_models_dir:
        env_path = Path(env_models_dir).expanduser().resolve()
        candidates.append(env_path)
        if env_path.name == "robots":
            candidates.append(env_path.parent)
        if env_path.name == "example-robot-data":
            candidates.append(env_path.parent)

    try:
        pkg_root = _package_root()
        candidates.append(pkg_root / "models")
    except ModuleNotFoundError:
        pass

    source_root = _source_checkout_root_model_dir()
    if source_root is not None:
        candidates.append(source_root)

    seen: set[Path] = set()
    ordered_candidates: list[Path] = []
    for candidate in candidates:
        candidate = candidate.resolve()
        if candidate not in seen:
            ordered_candidates.append(candidate)
            seen.add(candidate)

    for candidate in ordered_candidates:
        if candidate.is_dir() and (candidate / "robots").is_dir():
            return candidate

    for candidate in ordered_candidates:
        if candidate.is_dir():
            return candidate

    checked = "\n".join(f"  - {path}" for path in ordered_candidates) or "  - <no candidates>"
    raise FileNotFoundError(
        "Could not locate root models directory. Checked:\n"
        f"{checked}\n"
        "Set SYNAPSE_MODELS_DIR to a valid models directory if needed."
    )


def get_model_root(robot_subdir: Optional[str] = None) -> Path:
    """
    Resolve the models root directory that contains robot descriptions.

    Search order:
      1) SYNAPSE_MODELS_DIR env var (either <dir> or <dir>/robots)
            2) Installed package data: <site-packages>/synapse_robot_data/models/example-robot-data/robots
            3) Source checkout fallback: <repo>/models/example-robot-data/robots
    """
    root_model_dir = get_root_model_dir()
    candidates: list[Path] = [
                root_model_dir / "example-robot-data" / "robots",
        root_model_dir,
    ]

    try:
        pkg_root = _package_root()
        candidates.append(pkg_root / "robots")  # legacy fallback
    except ModuleNotFoundError:
        pass

    seen: set[Path] = set()
    ordered_candidates: list[Path] = []
    for candidate in candidates:
        candidate = candidate.resolve()
        if candidate not in seen:
            ordered_candidates.append(candidate)
            seen.add(candidate)

    for candidate in ordered_candidates:
        if not candidate.is_dir():
            continue
        if robot_subdir is not None and not (candidate / robot_subdir).is_dir():
            continue
        return candidate

    checked = "\n".join(f"  - {path}" for path in ordered_candidates) or "  - <no candidates>"
    raise FileNotFoundError(
        "Could not locate robot models directory. Checked:\n"
        f"{checked}\n"
        "Set SYNAPSE_MODELS_DIR to a valid models directory if needed."
    )


class RobotLoader:
    """
    Base class for robot-specific loaders.
    Subclasses should set class attributes.
    """

    robot_name: str = ""
    robot_subdir: str = ""
    urdf_relpath: str = ""
    srdf_relpath: Optional[str] = None
    mesh_relpath: Optional[str] = None
    ref_posture: Optional[str] = None
    free_flyer: bool = False

    @classmethod
    def root_model_dir(cls) -> Path:
        return get_root_model_dir()

    @classmethod
    def model_dir(cls) -> Path:
        if not cls.robot_subdir:
            raise ValueError(f"{cls.__name__}.robot_subdir must be set")
        return (get_model_root(cls.robot_subdir) / cls.robot_subdir).resolve()

    @classmethod
    def urdf_path(cls) -> Path:
        if not cls.urdf_relpath:
            raise ValueError(f"{cls.__name__}.urdf_relpath must be set")
        return (cls.model_dir() / cls.urdf_relpath).resolve()

    @classmethod
    def srdf_path(cls) -> Optional[Path]:
        if cls.srdf_relpath is None:
            return None
        return (cls.model_dir() / cls.srdf_relpath).resolve()

    @classmethod
    def mesh_dir(cls) -> Optional[Path]:
        if cls.mesh_relpath is None:
            return None
        return (cls.model_dir() / cls.mesh_relpath).resolve()

    @classmethod
    def exists(cls) -> bool:
        return cls.urdf_path().is_file()

    @classmethod
    def describe(cls) -> RobotDescription:
        return RobotDescription(
            name=cls.robot_name or cls.__name__,
            root_model_dir=cls.root_model_dir(),
            model_dir=cls.model_dir(),
            urdf_path=cls.urdf_path(),
            srdf_path=cls.srdf_path(),
            mesh_dir=cls.mesh_dir(),
            ref_posture=cls.ref_posture,
            free_flyer=cls.free_flyer,
        )