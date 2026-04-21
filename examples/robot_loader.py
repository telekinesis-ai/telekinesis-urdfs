"""Example demonstrating how to load any robot descriptions from 
telekinesis_urdfs.

Supports loading a single robot by name, all robots for a given brand, or
every registered robot (default when no arguments are provided).

Example:
    python robot_loader.py
    python robot_loader.py --robot universalrobotsur5
    python robot_loader.py --brand abb
"""

import argparse
from pathlib import Path
from typing import Optional, Type

import telekinesis_urdfs
from telekinesis_urdfs import utils


def get_brand(loader: Type[utils.RobotLoader]) -> str:
    """Return a human-readable brand name from the loader's robot_subdir.

    Args:
        loader: A RobotLoader subclass.

    Returns:
        Brand name string, e.g. ``"abb"``, ``"universal_robots"``.
    """
    top = loader.robot_subdir.split("/")[0]
    return top.removesuffix("_description").removesuffix("_simple")


def get_robot_description(
    loader: Type[utils.RobotLoader],
) -> utils.ModelDescription:
    """Resolve and return the ModelDescription for a loader.

    Args:
        loader: A RobotLoader subclass.

    Returns:
        Populated ModelDescription instance.
    """
    return loader.get_description()


def get_filesystem_path(path: Optional[Path]) -> str:
    """Return the last component of a path, or ``"-"`` if None.

    Args:
        path: A filesystem path, or None.

    Returns:
        The path's final component as a string, or ``"-"``.
    """
    return path.name if path is not None else "-"


def print_table(rows: list[tuple[str, utils.ModelDescription]]) -> None:
    """Print an ASCII table with all ModelDescription fields as columns.

    Args:
        rows: List of ``(brand, description)`` tuples, one per robot.
    """
    headers = [
        "Robot", "Brand", "URDF", "SRDF", "Meshes", "Ref Posture",
        "Free Flyer",
    ]

    data = [
        (
            desc.name,
            brand,
            get_filesystem_path(desc.urdf_path),
            get_filesystem_path(desc.srdf_path),
            get_filesystem_path(desc.mesh_dir),
            desc.ref_posture or "-",
            str(desc.free_flyer),
        )
        for brand, desc in rows
    ]

    widths = [
        max(len(headers[i]), max(len(row[i]) for row in data))
        for i in range(len(headers))
    ]
    sep = "+" + "+".join("-" * (w + 2) for w in widths) + "+"

    def fmt_row(cells: tuple[str, ...]) -> str:
        return (
            "|"
            + "|".join(f" {c.ljust(w)} " for c, w in zip(cells, widths))
            + "|"
        )

    print(f"\n{sep}")
    print(fmt_row(tuple(headers)))
    print(sep)
    for row in data:
        print(fmt_row(row))
    print(sep)
    print(f"  {len(rows)} robots total")


def unique_loaders() -> dict[str, tuple[Type[utils.RobotLoader], str]]:
    """Build a deduplicated mapping of robot_name -> (loader, brand).

    Multiple ROBOTS keys may point to the same loader (aliases). This
    function returns each physical robot exactly once, keyed by its
    canonical ``robot_name``.

    Returns:
        Dict mapping ``robot_name`` to ``(loader, brand)``.
    """
    seen: dict[str, tuple[Type[utils.RobotLoader], str]] = {}
    for loader in telekinesis_urdfs.ROBOTS.values():
        robot_name = loader.robot_name
        if robot_name not in seen:
            seen[robot_name] = (loader, get_brand(loader))
    return seen


def show_all() -> None:
    """Display every registered robot grouped by brand, then a table."""
    robots = unique_loaders()
    current_brand = None
    for robot_name, (_, brand) in sorted(
        robots.items(), key=lambda x: (x[1][1], x[0])
    ):
        if brand != current_brand:
            print(f"\n=== {brand.replace('_', ' ').title()} ===")
            current_brand = brand
        print(f"  {robot_name}")

    rows = sorted(
        [
            (brand, get_robot_description(loader))
            for _, (loader, brand) in robots.items()
        ],
        key=lambda r: (r[0], r[1].name),
    )
    print_table(rows)


def show_brand(brand: str) -> None:
    """Display all robots that belong to a given brand.

    Args:
        brand: Brand identifier, e.g. ``"abb"``, ``"fanuc"``,
            ``"universal_robots"``.

    Raises:
        SystemExit: If no robots match the requested brand.
    """
    robots = unique_loaders()
    matches = {
        robot_name: (loader, b)
        for robot_name, (loader, b) in robots.items()
        if b == brand
    }
    if not matches:
        available = sorted({b for _, b in robots.values()})
        brands_str = ", ".join(available)
        raise SystemExit(
            f"Brand '{brand}' not found.\n"
            f"Available brands: {brands_str}\n"
            f"Usage: python robot_loader.py --brand BRAND\n"
            f"Example: python robot_loader.py --brand abb"
        )

    print(f"=== {brand.replace('_', ' ').title()} ===")
    rows = sorted(
        [
            (brand, get_robot_description(loader))
            for _, (loader, _) in matches.items()
        ],
        key=lambda r: r[1].name,
    )
    print_table(rows)


def show_robot(robot_key: str) -> None:
    """Display a single robot looked up by its ROBOTS key.

    Args:
        robot_key: A key registered in ROBOTS, e.g.
            ``"universalrobotsur5"``, ``"frankapanda"``.

    Raises:
        SystemExit: If the key is not found in ROBOTS.
    """
    key = robot_key.lower()
    if key not in telekinesis_urdfs.ROBOTS:
        available = ", ".join(sorted(telekinesis_urdfs.ROBOTS))
        raise SystemExit(
            f"Robot '{robot_key}' not found.\n"
            f"Available robots: {available}\n"
            f"Usage: python robot_loader.py --robot NAME\n"
            f"Example: python robot_loader.py --robot universalrobotsur5"
        )
    loader = telekinesis_urdfs.ROBOTS[key]
    brand = get_brand(loader)
    print(f"=== {loader.robot_name} ===")
    print_table([(brand, get_robot_description(loader))])


def main() -> None:
    """Parse CLI arguments and dispatch to the appropriate display function."""
    parser = argparse.ArgumentParser(
        description=(
            "Load and display robot descriptions from telekinesis_urdfs."
        ),
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--robot", metavar="NAME",
        help="Key of a single robot (e.g. universalrobotsur5, abbir2400).",
    )
    group.add_argument(
        "--brand", metavar="BRAND",
        help="Brand to filter by (e.g. abb, fanuc, universal_robots).",
    )
    args = parser.parse_args()

    if args.robot:
        show_robot(args.robot)
    elif args.brand:
        show_brand(args.brand)
    else:
        show_all()


if __name__ == "__main__":
    main()
