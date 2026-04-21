"""Combined registry of all robots and tools with unified load helpers."""

from typing import Dict, Type, Union

from .utils import ModelDescription, RobotLoader, ToolLoader
from .abb import (
    ABBCrb15000595Loader,
    ABBIrb1200590Loader,
    ABBIrb1200770Loader,
    ABBIrb120358Loader,
    ABBIrb120t358Loader,
    ABBIrb1600612Loader,
    ABBIrb16008145Loader,
    ABBIrb2400Loader,
    ABBIrb260012165Loader,
    ABBIrb4400l30243Loader,
    ABBIrb460020250Loader,
    ABBIrb460040255Loader,
    ABBIrb460060205Loader,
    ABBIrb527120Loader,
    ABBIrb527145Loader,
    ABBIrb5400Loader,
    ABBIrb6600Loader,
    ABBIrb6640185280Loader,
    ABBIrb6650s90390Loader,
    ABBIrb6650s125350Loader,
    ABBIrb6700200260Loader,
    ABBIrb6700235265Loader,
    ABBIrb7600150350Loader,
)
from .agibot import AgibotX1Loader
from .agility_robotics import AgilityDigitLoader
from .allegro_hand import AllegroLeftHandLoader, AllegroRightHandLoader
from .anymal_b import AnymalBLoader, AnymalBKinovaLoader
from .anymal_c import AnymalCLoader
from .bitcraze import (
    BitcrazeCf2xLoader,
    BitcrazeCf2pLoader,
    BitcrazeCrazyflieRacerLoader,
    BitcrazeCrazyflieArchitravelLoader,
    BitcrazeCrazyflieBoxLoader,
)
from .boston_dynamics import SpotLoader, SpotWithArmLoader
from .custom_mobile_robots import CustomMobileRobotLoader
from .fanuc import (
    FanucCr35iaLoader,
    FanucCr7iaLoader,
    FanucCr7ialLoader,
    FanucCrx10ialLoader,
    FanucLrmate200iLoader,
    FanucLrmate200ibLoader,
    FanucLrmate200ib3lLoader,
    FanucLrmate200icLoader,
    FanucLrmate200ic5fLoader,
    FanucLrmate200ic5hLoader,
    FanucLrmate200ic5hsLoader,
    FanucLrmate200ic5lLoader,
    FanucLrmate200idLoader,
    FanucLrmate200id4sLoader,
    FanucLrmate200id4scLoader,
    FanucLrmate200id4shLoader,
    FanucLrmate200id7hLoader,
    FanucLrmate200id7lLoader,
    FanucLrmate200id7lcLoader,
    FanucM10iaLoader,
    FanucM10ia7lLoader,
    FanucM16ib20Loader,
    FanucM20iaLoader,
    FanucM20ia10lLoader,
    FanucM20ib25Loader,
    FanucM430ia2fLoader,
    FanucM430ia2pLoader,
    FanucM6ibLoader,
    FanucM6ib6sLoader,
    FanucM710ic45mLoader,
    FanucM710ic50Loader,
    FanucM900ia260lLoader,
    FanucM900ib700Loader,
    FanucR1000ia80fLoader,
    FanucR2000ib210fLoader,
    FanucR2000ic125lLoader,
    FanucR2000ic165fLoader,
    FanucR2000ic210fLoader,
    FanucR2000ic210lLoader,
    FanucR2000ic270fLoader,
)
from .franka_robotics import FrankaPandaLoader
from .google import BarkourV0Loader, BarkourVbLoader
from .hector import HectorQuadrotorLoader
from .husky import HuskyLoader
from .kuka import (
    KukaKr10r1100sixxLoader,
    KukaKr10r1420Loader,
    KukaKr10r9002Loader,
    KukaKr120r2500proLoader,
    KukaKr1502Loader,
    KukaKr150r31002Loader,
    KukaKr162Loader,
    KukaKr210l150Loader,
    KukaKr3r540Loader,
    KukaKr5ArcLoader,
    KukaKr6r700sixxLoader,
    KukaKr6r9002Loader,
    KukaKr6r900sixxLoader,
    KukaLbrIiwa14R820Loader,
)
from .motoman import (
    MotomanBmda3Loader,
    MotomanBmda3WeEfssLoader,
    MotomanMh5Loader,
    MotomanSia10dLoader,
    MotomanSia10fLoader,
    MotomanSia20dLoader,
    MotomanSia5dLoader,
)
from .neura_robotics import (
    NeuraLara3Loader,
    NeuraLara8Loader,
    NeuraMaira7MLoader,
)
from .pal_robotics import (
    PalSoloLoader,
    PalSolo12Loader,
    PalTalosFullV2Loader,
    PalTalosFullV2BoxLoader,
    PalTalosLeftArmLoader,
    PalTalosReducedLoader,
    PalTalosReducedBoxLoader,
    PalTalosReducedCorrectedLoader,
    PalTiagoLoader,
    PalTiagoDualLoader,
    PalTiagoNoHandLoader,
)
from .simple_humanoid import (
    SimpleHumanoidLoader,
    SimpleHumanoidClassicalLoader,
)
from .unitree import (
    UnitreeA1Loader,
    UnitreeAliengoLoader,
    UnitreeB1Loader,
    UnitreeB1Z1Loader,
    UnitreeB2Loader,
    UnitreeB2wLoader,
    UnitreeGo1Loader,
    UnitreeGo2Loader,
    UnitreeGo2DescriptionLoader,
    UnitreeGo2wLoader,
    UnitreeG123dofLoader,
    UnitreeG123dofRev10Loader,
    UnitreeG129dofLoader,
    UnitreeG129dofLockWaistLoader,
    UnitreeG129dofLockWaistRev10Loader,
    UnitreeG129dofRev10Loader,
    UnitreeG129dofWithHandLoader,
    UnitreeG129dofWithHandRev10Loader,
    UnitreeG1DualArmLoader,
    UnitreeDex31LLoader,
    UnitreeDex31RLoader,
    UnitreeH1Loader,
    UnitreeH1WithHandLoader,
    UnitreeH12Loader,
    UnitreeH12HandlessLoader,
    UnitreeZ1Loader,
)
from .universal_robots import (
    UR3Loader,
    UR3eLoader,
    UR3GripperLoader,
    UR5Loader,
    UR5eLoader,
    UR5GripperLoader,
    UR5JointLimitedLoader,
    UR5Robotiq2F85Loader,
    UR7eLoader,
    UR10Loader,
    UR10eLoader,
    UR10eFactoryCalibrationLoader,
    UR10eNewFactoryCalibrationLoader,
    UR12eLoader,
    UR15Loader,
    UR16eLoader,
    UR20Loader,
    UR30Loader,
)
from .onrobot import OnRobotRg6Loader
from .robotiq import (
    Robotiq2F85Loader,
    Robotiq2F140Loader,
    Robotiq2F85LegacyLoader,
)
from .schunk import (
    SchunkEgpLoader,
    SchunkEgu50Loader,
    SchunkPznPlusLoader,
    SchunkPzv64Loader,
)


ROBOTS: Dict[str, Type[RobotLoader]] = {
    # ── ABB ──────────────────────────────────────────────────────────────────
    "abbcrb15000595": ABBCrb15000595Loader,
    "abbirb1200590": ABBIrb1200590Loader,
    "abbirb1200770": ABBIrb1200770Loader,
    "abbirb120358": ABBIrb120358Loader,
    "abbirb120t358": ABBIrb120t358Loader,
    "abbirb1600612": ABBIrb1600612Loader,
    "abbirb16008145": ABBIrb16008145Loader,
    "abbirb2400": ABBIrb2400Loader,
    "abbirb260012165": ABBIrb260012165Loader,
    "abbirb4400l30243": ABBIrb4400l30243Loader,
    "abbirb460020250": ABBIrb460020250Loader,
    "abbirb460040255": ABBIrb460040255Loader,
    "abbirb460060205": ABBIrb460060205Loader,
    "abbirb527120": ABBIrb527120Loader,
    "abbirb527145": ABBIrb527145Loader,
    "abbirb5400": ABBIrb5400Loader,
    "abbirb6600": ABBIrb6600Loader,
    "abbirb6640185280": ABBIrb6640185280Loader,
    "abbirb6650s90390": ABBIrb6650s90390Loader,
    "abbirb6650s125350": ABBIrb6650s125350Loader,
    "abbirb6700200260": ABBIrb6700200260Loader,
    "abbirb6700235265": ABBIrb6700235265Loader,
    "abbirb7600150350": ABBIrb7600150350Loader,
    # ── Agibot ───────────────────────────────────────────────────────────────
    "agibotx1": AgibotX1Loader,
    # ── Agility Robotics ─────────────────────────────────────────────────────
    "agilitydigit": AgilityDigitLoader,
    # ── Allegro Hand ─────────────────────────────────────────────────────────
    "allegrolefthand": AllegroLeftHandLoader,
    "allegrorighthand": AllegroRightHandLoader,
    # ── ANYmal ───────────────────────────────────────────────────────────────
    "anymalb": AnymalBLoader,
    "anymalbkinova": AnymalBKinovaLoader,
    "anymalc": AnymalCLoader,
    # ── Bitcraze ─────────────────────────────────────────────────────────────
    "bitcrazecf2x": BitcrazeCf2xLoader,
    "bitcrazecf2p": BitcrazeCf2pLoader,
    "bitcrazecrazyflieracer": BitcrazeCrazyflieRacerLoader,
    "bitcrazecrazyfliearchitravel": BitcrazeCrazyflieArchitravelLoader,
    "bitcrazecrazyfliebox": BitcrazeCrazyflieBoxLoader,
    # ── Boston Dynamics ──────────────────────────────────────────────────────
    "bostondynamicsspot": SpotLoader,
    "bostondynamicsspotwitharm": SpotWithArmLoader,
    # ── Custom Mobile Robot ──────────────────────────────────────────────────
    "custommobilerobot": CustomMobileRobotLoader,
    # ── Fanuc ────────────────────────────────────────────────────────────────
    "fanuccr35ia": FanucCr35iaLoader,
    "fanuccr7ia": FanucCr7iaLoader,
    "fanuccr7ial": FanucCr7ialLoader,
    "fanuccrx10ial": FanucCrx10ialLoader,
    "fanuclrmate200i": FanucLrmate200iLoader,
    "fanuclrmate200ib": FanucLrmate200ibLoader,
    "fanuclrmate200ib3l": FanucLrmate200ib3lLoader,
    "fanuclrmate200ic": FanucLrmate200icLoader,
    "fanuclrmate200ic5f": FanucLrmate200ic5fLoader,
    "fanuclrmate200ic5h": FanucLrmate200ic5hLoader,
    "fanuclrmate200ic5hs": FanucLrmate200ic5hsLoader,
    "fanuclrmate200ic5l": FanucLrmate200ic5lLoader,
    "fanuclrmate200id": FanucLrmate200idLoader,
    "fanuclrmate200id4s": FanucLrmate200id4sLoader,
    "fanuclrmate200id4sc": FanucLrmate200id4scLoader,
    "fanuclrmate200id4sh": FanucLrmate200id4shLoader,
    "fanuclrmate200id7h": FanucLrmate200id7hLoader,
    "fanuclrmate200id7l": FanucLrmate200id7lLoader,
    "fanuclrmate200id7lc": FanucLrmate200id7lcLoader,
    "fanucm10ia": FanucM10iaLoader,
    "fanucm10ia7l": FanucM10ia7lLoader,
    "fanucm16ib20": FanucM16ib20Loader,
    "fanucm20ia": FanucM20iaLoader,
    "fanucm20ia10l": FanucM20ia10lLoader,
    "fanucm20ib25": FanucM20ib25Loader,
    "fanucm430ia2f": FanucM430ia2fLoader,
    "fanucm430ia2p": FanucM430ia2pLoader,
    "fanucm6ib": FanucM6ibLoader,
    "fanucm6ib6s": FanucM6ib6sLoader,
    "fanucm710ic45m": FanucM710ic45mLoader,
    "fanucm710ic50": FanucM710ic50Loader,
    "fanucm900ia260l": FanucM900ia260lLoader,
    "fanucm900ib700": FanucM900ib700Loader,
    "fanucr1000ia80f": FanucR1000ia80fLoader,
    "fanucr2000ib210f": FanucR2000ib210fLoader,
    "fanucr2000ic125l": FanucR2000ic125lLoader,
    "fanucr2000ic165f": FanucR2000ic165fLoader,
    "fanucr2000ic210f": FanucR2000ic210fLoader,
    "fanucr2000ic210l": FanucR2000ic210lLoader,
    "fanucr2000ic270f": FanucR2000ic270fLoader,
    # ── Franka Robotics ──────────────────────────────────────────────────────
    "frankapanda": FrankaPandaLoader,
    # ── Google ───────────────────────────────────────────────────────────────
    "googlebarkourv0": BarkourV0Loader,
    "googlebarkouvb": BarkourVbLoader,
    # ── Hector ───────────────────────────────────────────────────────────────
    "hectorquadrotor": HectorQuadrotorLoader,
    # ── Clearpath ────────────────────────────────────────────────────────────
    "clearpathusky": HuskyLoader,
    # ── KUKA ─────────────────────────────────────────────────────────────────
    "kukakr10r1100sixx": KukaKr10r1100sixxLoader,
    "kukakr10r1420": KukaKr10r1420Loader,
    "kukakr10r9002": KukaKr10r9002Loader,
    "kukakr120r2500pro": KukaKr120r2500proLoader,
    "kukakr1502": KukaKr1502Loader,
    "kukakr150r31002": KukaKr150r31002Loader,
    "kukakr162": KukaKr162Loader,
    "kukakr210l150": KukaKr210l150Loader,
    "kukakr3r540": KukaKr3r540Loader,
    "kukakr5arc": KukaKr5ArcLoader,
    "kukakr6r700sixx": KukaKr6r700sixxLoader,
    "kukakr6r9002": KukaKr6r9002Loader,
    "kukakr6r900sixx": KukaKr6r900sixxLoader,
    "kukalbriiwa14r820": KukaLbrIiwa14R820Loader,
    # ── Motoman ──────────────────────────────────────────────────────────────
    "motomanbmda3": MotomanBmda3Loader,
    "motomanbmda3weffs": MotomanBmda3WeEfssLoader,
    "motomanmh5": MotomanMh5Loader,
    "motomansia10d": MotomanSia10dLoader,
    "motomansia10f": MotomanSia10fLoader,
    "motomansia20d": MotomanSia20dLoader,
    "motomansia5d": MotomanSia5dLoader,
    # ── Neura Robotics ───────────────────────────────────────────────────────
    "neuraroboticslara3": NeuraLara3Loader,
    "neuraroboticslara8": NeuraLara8Loader,
    "neuraroboticsmaira7m": NeuraMaira7MLoader,
    # ── PAL Robotics ─────────────────────────────────────────────────────────
    "palroboticssolo": PalSoloLoader,
    "palroboticssolo12": PalSolo12Loader,
    "palroboticstalos": PalTalosFullV2Loader,
    "palroboticstalosfullv2box": PalTalosFullV2BoxLoader,
    "palroboticstalosieftarm": PalTalosLeftArmLoader,
    "palroboticstalosreduced": PalTalosReducedLoader,
    "palroboticstalosreducedbox": PalTalosReducedBoxLoader,
    "palroboticstalosreducedcorrected": (
        PalTalosReducedCorrectedLoader
    ),
    "palroboticstiago": PalTiagoLoader,
    "palroboticstiagodual": PalTiagoDualLoader,
    "palroboticstiagonohand": PalTiagoNoHandLoader,
    # ── Simple Humanoid ──────────────────────────────────────────────────────
    "simplehumanoid": SimpleHumanoidLoader,
    "simplehumanoidclassical": SimpleHumanoidClassicalLoader,
    # ── Unitree ──────────────────────────────────────────────────────────────
    "unitreea1": UnitreeA1Loader,
    "unitreealiengo": UnitreeAliengoLoader,
    "unitreeb1": UnitreeB1Loader,
    "unitreeb1z1": UnitreeB1Z1Loader,
    "unitreeb2": UnitreeB2Loader,
    "unitreeb2w": UnitreeB2wLoader,
    "unitreego1": UnitreeGo1Loader,
    "unitreego2": UnitreeGo2Loader,
    "unitreego2description": UnitreeGo2DescriptionLoader,
    "unitreego2w": UnitreeGo2wLoader,
    "unitreeg123dof": UnitreeG123dofLoader,
    "unitreeg123dofrev10": UnitreeG123dofRev10Loader,
    "unitreeg129dof": UnitreeG129dofLoader,
    "unitreeg129doflockwaist": UnitreeG129dofLockWaistLoader,
    "unitreeg129doflockwaistrev10": (
        UnitreeG129dofLockWaistRev10Loader
    ),
    "unitreeg129dofrev10": UnitreeG129dofRev10Loader,
    "unitreeg129dofwithhand": UnitreeG129dofWithHandLoader,
    "unitreeg129dofwithhandrev10": (
        UnitreeG129dofWithHandRev10Loader
    ),
    "unitreeg1dualarm": UnitreeG1DualArmLoader,
    "unitreedex31l": UnitreeDex31LLoader,
    "unitreedex31r": UnitreeDex31RLoader,
    "unitreeh1": UnitreeH1Loader,
    "unitreeh1withhand": UnitreeH1WithHandLoader,
    "unitreeh12": UnitreeH12Loader,
    "unitreeh12handless": UnitreeH12HandlessLoader,
    "unitreez1": UnitreeZ1Loader,
    # ── Universal Robots ─────────────────────────────────────────────────────
    "universalrobotsur3": UR3Loader,
    "universalrobotsur3e": UR3eLoader,
    "universalrobotsur3gripper": UR3GripperLoader,
    "universalrobotsur5": UR5Loader,
    "universalrobotsur5e": UR5eLoader,
    "universalrobotsur5gripper": UR5GripperLoader,
    "universalrobotsur5jointlimitedrobot": UR5JointLimitedLoader,
    "universalrobotsur5robotiq2f85": UR5Robotiq2F85Loader,
    "universalrobotsur7e": UR7eLoader,
    "universalrobotsur10": UR10Loader,
    "universalrobotsur10e": UR10eLoader,
    "universalrobotsur10efactorycalibration": (
        UR10eFactoryCalibrationLoader
    ),
    "universalrobotsur10enewfactorycalibration": (
        UR10eNewFactoryCalibrationLoader
    ),
    "universalrobotsur12e": UR12eLoader,
    "universalrobotsur15": UR15Loader,
    "universalrobotsur16e": UR16eLoader,
    "universalrobotsur20": UR20Loader,
    "universalrobotsur30": UR30Loader,
}

TOOLS: Dict[str, Type[ToolLoader]] = {
    # ── OnRobot ───────────────────────────────────────────────────────────────
    "onrobotrg6": OnRobotRg6Loader,
    # ── Robotiq ───────────────────────────────────────────────────────────────
    "robotiq2f85": Robotiq2F85Loader,
    "robotiq2f140": Robotiq2F140Loader,
    "robotiq2f85legacy": Robotiq2F85LegacyLoader,
    # ── Schunk ────────────────────────────────────────────────────────────────
    "schunkegp": SchunkEgpLoader,
    "schunkegu50": SchunkEgu50Loader,
    "schunkpznplus": SchunkPznPlusLoader,
    "schunkpzv64": SchunkPzv64Loader,
}

REGISTRY: Dict[str, Union[Type[RobotLoader], Type[ToolLoader]]] = {
    **ROBOTS,
    **TOOLS,
}


def load(name: str) -> ModelDescription:
    """Load and validate a description by registry key.

    Looks up ``name`` in the combined robot and tool registry.

    Args:
        name: A key from REGISTRY (case-insensitive).

    Returns:
        Fully resolved ModelDescription for the requested robot or tool.

    Raises:
        ValueError: If ``name`` is not found in the registry.
        FileNotFoundError: If the URDF or SRDF path does not exist on disk.
    """
    key = name.lower()
    if key not in REGISTRY:
        available = ", ".join(sorted(REGISTRY))
        raise ValueError(
            f"Unknown name '{name}'. Available: {available}"
        )
    desc = REGISTRY[key].get_description()
    if not desc.urdf_path.exists():
        raise FileNotFoundError(f"URDF not found: {desc.urdf_path}")
    if desc.srdf_path is not None and not desc.srdf_path.exists():
        raise FileNotFoundError(f"SRDF not found: {desc.srdf_path}")
    return desc


def load_as_dict(name: str) -> dict:
    """Load a description and return it as a plain dictionary.

    Args:
        name: A key from REGISTRY (case-insensitive).

    Returns:
        Dictionary with all ModelDescription fields as string-keyed entries.

    Raises:
        ValueError: If ``name`` is not found in the registry.
        FileNotFoundError: If the URDF or SRDF path does not exist on disk.
    """
    desc = load(name)
    return {
        "name": desc.name,
        "root_dir": desc.root_dir,
        "model_dir": desc.model_dir,
        "urdf_path": desc.urdf_path,
        "srdf_path": desc.srdf_path,
        "mesh_dir": desc.mesh_dir,
        "ref_posture": desc.ref_posture,
        "free_flyer": desc.free_flyer,
    }


__all__ = ["REGISTRY", "ROBOTS", "TOOLS", "load", "load_as_dict"]
