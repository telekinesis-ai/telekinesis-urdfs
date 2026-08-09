# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2026-08-03

### Added

- Epson CX4-A601S robot loader (`epsoncx4a601s`)
- Piab piCOBOT Electric vacuum gripper loader (`piabpicobotelectric`)
- `scripts/convert_glb_fbx_to_meshes.py` — Blender utility to convert an FBX/GLB source model into visual/collision meshes
- "Adding a New Model" section in `DEVELOPMENT.md` documenting the mesh-conversion workflow

### Changed

- Moved `verify_model.py` to `scripts/verify_model.py`

## [0.1.1] - 2026-07-01

### Added

- Robotiq Hand-E gripper loader (`robotiqhande`)
- OnRobot RG2 gripper loader (`onrobotrg2`)
- `CONTRIBUTING.md` documenting how to add a robot or tool (folder layout, mesh-path convention, naming, loader registration, xacro flattening)

### Changed

- Standardized tool folder structure (`robotiq`, `onrobot`, `schunk`) to `urdf/` + `meshes/{visual,collision}/<model>/`, with raw ROS/xacro sources under `ros/`
- Rewrote all gripper `package://` mesh paths to true `example-robot-data/<robots|tools>/...` paths so they resolve with the same rule as robots (no downstream patching/search needed)
- Renamed Robotiq URDFs to drop the `_gripper` suffix (`robotiq_2f_85.urdf`, `robotiq_2f_140.urdf`) and gave each a unique `<robot name>`
- Rebuilt the UR5 + Robotiq 2F-85 gripper subtree to use the current 2F-85 mesh set and kinematics

### Fixed

- Corrected Schunk PZV-64 mesh filename typo (`pvz_*` → `pzv_*`)

### Removed

- Robotiq 2F-85 Legacy loader (`robotiq2f85legacy`) and its `robotiq_2f_85_gripper_visualization_old` assets

## [0.1.0] - 2026-04-17

### Added

- Unified `ModelDescription` dataclass covering robots and tools — fields: `name`, `root_dir`, `model_dir`, `urdf_path`, `srdf_path`, `mesh_dir`, `ref_posture`, `free_flyer`
- `load(name)` and `load_as_dict(name)` public helpers for resolving any registered robot or tool by registry key
- `ROBOTS`, `TOOLS`, and `REGISTRY` dictionaries exposing all registered loaders
- Robot loaders for 21 manufacturers (164 robots total):
  ABB, Agibot, Agility Robotics, Allegro Hand, ANYmal B, ANYmal C, Bitcraze, Boston Dynamics, Fanuc, Franka Robotics, Google, Hector, Husky, KUKA, Motoman, Neura Robotics, PAL Robotics, Simple Humanoid, Unitree, Universal Robots, and a custom mobile robot base
- Tool loaders for grippers and end-effectors (8 tools total):
  OnRobot RG6, Robotiq 2F-85, Robotiq 2F-140, Robotiq 2F-85 Legacy, Schunk EGP, Schunk EGU 50, Schunk PZN+, Schunk PZV 64
- Bundled URDF, SRDF, and mesh assets for all registered robots and tools
- `robot_loader.py` example script with `--robot` and `--brand` CLI flags
