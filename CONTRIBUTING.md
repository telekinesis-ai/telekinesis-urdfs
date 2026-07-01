# Contributing

How to add a **robot** or **tool** so it loads through the unified API.
See [DEVELOPMENT.md](DEVELOPMENT.md) for setup, workflow, and lint.

## Add a robot or tool

### 1. Location

- Robot → `src/telekinesis_urdfs/models/example-robot-data/robots/`
- Tool → `src/telekinesis_urdfs/models/example-robot-data/tools/`

### 2. Brand folder

Lowercase brand name (`tools/robotiq/`, `robots/universal_robots/`). Reuse it if it already exists.

### 3. Assets

```
<brand>/
├── urdf/<brand>_<model>.urdf            # "urdf" singular, flattened .urdf only
└── meshes/
    ├── visual/<model>/...               # per-model subdir (2f_85, rg2, ...)
    └── collision/<model>/...
```

Keep raw `.xacro` / ROS sources in an optional `ros/` folder (never loaded).

#### Convert xacro → URDF

Loaders serve flattened `.urdf`, so flatten any `.xacro` first.

1. Install: `pip install xacro`
2. If from ROS, fix `$(find …)` includes first. A `$(find <pkg>)` include needs a sourced ROS workspace, else the flatten fails with:
   ```
   substitution args not supported:  No module named 'ament_index_python'
   ```
   Put all `.xacro` files in one directory and drop the `$(find <pkg>)/urdf/` prefix so includes are relative:
   ```xml
   <xacro:include filename="onrobot_rg2_model_macro.xacro"/>   <!-- was $(find onrobot_rg_description)/urdf/... -->
   ```
   Repeat for every `$(find …)` include (macro, transmission, gazebo, …).
3. Flatten: `xacro <model>.xacro -o <brand>_<model>.urdf`
4. Move the `.urdf` into `urdf/`.

### 4. Fix mesh paths

Every `package://` mesh ref must be the real path under the `example-robot-data/` root, with `example-robot-data` as the package name:

```xml
<mesh filename="package://example-robot-data/tools/<brand>/meshes/visual/<model>/<file>"/>
```

The resolver maps `example-robot-data` → `.../models/example-robot-data/` and appends
the rest verbatim, so it must be the on-disk path. Don't leave vendor package names
(`robotiq_description`, `end_effectors/...`) — they don't resolve. Rewrite every prefix
up to `/meshes/`.

### 5. Naming

| Item | Rule | Example |
|---|---|---|
| Brand folder | lowercase brand | `robotiq` |
| URDF file | `<brand>_<model>.urdf` | `robotiq_2f_85.urdf` |
| `<robot name>` | unique per model | `robotiq_2f_85` (not `robotiq_gripper`) |
| Mesh subdir | lowercase model key | `2f_85`, `rg2` |
| Loader class | `BrandModelLoader` | `Robotiq2F85Loader` |
| Registry key | lowercase `brand`+`model`, no separators | `robotiq2f85` |

### 6. Loader class

Add to `<brand>.py` (create the module if missing) and its `__all__`.

Tool:
```python
from .utils import ToolLoader

class AcmeG100Loader(ToolLoader):
    tool_name = "acme_g100"
    tool_subdir = "acme"                  # brand folder under tools/
    urdf_relpath = "urdf/acme_g100.urdf"
    srdf_relpath = None
    mesh_relpath = "meshes"
```

Robot — use `RobotLoader` with `robot_name`, `robot_subdir`, `urdf_relpath`, `srdf_relpath`, `mesh_relpath`, plus optional `ref_posture` and `free_flyer` (True for floating-base).

### 7. Register in `loader.py`

```python
from .acme import AcmeG100Loader

TOOLS = {                    # or ROBOTS for a robot
    "acmeg100": AcmeG100Loader,
}
```

## Verify

```python
from telekinesis_urdfs import load, REGISTRY
from telekinesis_urdfs.utils import _get_root_model_dir
import xml.etree.ElementTree as ET

key = "acmeg100"
d = load(key)                              # raises if URDF/SRDF missing
ex_root = _get_root_model_dir() / "example-robot-data"
prefix = "package://example-robot-data/"
for m in ET.parse(d.urdf_path).getroot().iter("mesh"):
    fn = m.get("filename", "")
    assert fn.startswith(prefix), f"bad prefix: {fn}"
    assert (ex_root / fn[len(prefix):]).exists(), f"missing: {fn}"
print("OK")
```
