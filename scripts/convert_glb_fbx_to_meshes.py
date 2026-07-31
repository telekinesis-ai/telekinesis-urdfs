"""Convert an FBX/GLB source model into visual/collision meshes for a tool.

Usage (run with Blender's bundled Python):
    blender --background --python convert_glb_fbx_to_meshes.py -- \\
        --input "src/telekinesis_urdfs/models/example-robot-data/tools/piab/meshes/PCOE.U3.M01.E1.R111PD.X.C.E.XXX v1.fbx" \\
        --output-dir "src/telekinesis_urdfs/models/example-robot-data/tools/piab/meshes" \\
        --name picobot_electric \\
        --collision-ratio 0.1
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import bpy


def _script_args() -> list[str]:
    """Return CLI args after the ``--`` separator, stripping Blender's own."""
    argv = sys.argv
    if "--" in argv:
        return argv[argv.index("--") + 1 :]
    return []


def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)


def import_model(input_path: Path) -> None:
    suffix = input_path.suffix.lower()

    if suffix == ".fbx":
        bpy.ops.import_scene.fbx(filepath=str(input_path))
    elif suffix in {".glb", ".gltf"}:
        bpy.ops.import_scene.gltf(filepath=str(input_path))
    else:
        raise ValueError(f"Unsupported input format: {suffix}")


def prepare_meshes() -> None:
    mesh_objects = [obj for obj in bpy.context.scene.objects if obj.type == "MESH"]

    if not mesh_objects:
        raise RuntimeError("No mesh objects found in imported file")

    for obj in mesh_objects:
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj

        # Apply object rotation and scale to the mesh data.
        bpy.ops.object.transform_apply(
            location=False,
            rotation=True,
            scale=True,
        )

        obj.select_set(False)


def join_meshes(name: str) -> bpy.types.Object:
    mesh_objects = [obj for obj in bpy.context.scene.objects if obj.type == "MESH"]

    bpy.ops.object.select_all(action="DESELECT")

    for obj in mesh_objects:
        obj.select_set(True)

    bpy.context.view_layer.objects.active = mesh_objects[0]
    bpy.ops.object.join()

    joined = bpy.context.active_object
    joined.name = name
    return joined


def export_visual_stl(output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    bpy.ops.wm.stl_export(
        filepath=str(output_path),
        export_selected_objects=True,
        ascii_format=False,
    )


def _collada_export_available() -> bool:
    if hasattr(bpy.types, "WM_OT_collada_export"):
        return True
    try:
        bpy.ops.preferences.addon_enable(module="io_scene_dae")
    except Exception:
        pass
    return hasattr(bpy.types, "WM_OT_collada_export")


def export_visual_dae(output_path: Path) -> None:
    if not _collada_export_available():
        print(
            "Skipping DAE export: Collada exporter is not available in this "
            "Blender install (bundled by default only up to Blender 4.1; "
            "install the 'Collada (.dae)' extension to enable it)."
        )
        return

    output_path.parent.mkdir(parents=True, exist_ok=True)

    bpy.ops.wm.collada_export(
        filepath=str(output_path),
        selected=True,
        apply_modifiers=True,
    )


def create_collision_mesh(
    source_object: bpy.types.Object,
    name: str,
    ratio: float,
) -> bpy.types.Object:
    collision = source_object.copy()
    collision.data = source_object.data.copy()
    collision.name = name

    bpy.context.collection.objects.link(collision)

    bpy.ops.object.select_all(action="DESELECT")
    collision.select_set(True)
    bpy.context.view_layer.objects.active = collision

    modifier = collision.modifiers.new(
        name="Decimate",
        type="DECIMATE",
    )
    modifier.ratio = ratio

    bpy.ops.object.modifier_apply(modifier=modifier.name)

    return collision


def export_collision_stl(
    collision_object: bpy.types.Object,
    output_path: Path,
) -> None:
    bpy.ops.object.select_all(action="DESELECT")
    collision_object.select_set(True)
    bpy.context.view_layer.objects.active = collision_object

    output_path.parent.mkdir(parents=True, exist_ok=True)

    bpy.ops.wm.stl_export(
        filepath=str(output_path),
        export_selected_objects=True,
        ascii_format=False,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument(
        "--name",
        default=None,
        help="Base name for the joined mesh and exported files. "
        "Defaults to the input file's stem.",
    )
    parser.add_argument(
        "--collision-ratio",
        type=float,
        default=0.1,
    )
    args = parser.parse_args(_script_args())

    input_path = Path(args.input).resolve()
    output_dir = Path(args.output_dir).resolve()
    name = args.name or input_path.stem

    clear_scene()
    import_model(input_path)
    prepare_meshes()

    visual = join_meshes(name)

    bpy.ops.object.select_all(action="DESELECT")
    visual.select_set(True)
    bpy.context.view_layer.objects.active = visual

    export_visual_dae(output_dir / "visual" / f"{name}.dae")
    export_visual_stl(output_dir / "visual" / f"{name}.stl")

    collision = create_collision_mesh(
        visual,
        name=f"{name}_collision",
        ratio=args.collision_ratio,
    )

    export_collision_stl(
        collision,
        output_dir / "collision" / f"{name}_collision.stl",
    )

    print(f"Meshes exported to: {output_dir}")


if __name__ == "__main__":
    main()
