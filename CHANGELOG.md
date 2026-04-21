# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
