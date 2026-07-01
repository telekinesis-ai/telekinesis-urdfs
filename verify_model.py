"""Verify a registered model loads and all its mesh refs resolve.

Usage:
    python verify_model.py <registry_key>
    python verify_model.py robotiq2f85
"""

import sys
import xml.etree.ElementTree as ET

from telekinesis_urdfs import load
from telekinesis_urdfs.utils import _get_root_model_dir


def main() -> int:
    key = sys.argv[1] if len(sys.argv) > 1 else "robotiq2f85"
    d = load(key)  # raises if URDF/SRDF missing

    ex_root = _get_root_model_dir() / "example-robot-data"
    prefix = "package://example-robot-data/"

    missing = []
    for m in ET.parse(d.urdf_path).getroot().iter("mesh"):
        fn = m.get("filename", "")
        if not fn.startswith(prefix):
            missing.append(f"bad prefix: {fn}")
        elif not (ex_root / fn[len(prefix):]).exists():
            missing.append(f"missing: {fn}")

    if missing:
        print(f"{key}: FAIL")
        for x in missing:
            print("  ", x)
        return 1
    print(f"{key}: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
