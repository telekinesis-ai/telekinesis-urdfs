"""Example demonstrating how to load any tool descriptions from
telekinesis_urdfs.

Supports loading a single tool by name, all tools for a given brand, or
every registered tool (default when no arguments are provided).

Example:
    python tool_loader.py
    python tool_loader.py --tool robotiq2f85
    python tool_loader.py --brand robotiq
"""

import argparse
from pathlib import Path
from typing import Optional, Type

import telekinesis_urdfs
from telekinesis_urdfs import utils


def get_brand(loader: Type[utils.ToolLoader]) -> str:
    """Return a human-readable brand name from the loader's tool_subdir.

    Args:
        loader: A ToolLoader subclass.

    Returns:
        Brand name string, e.g. ``"robotiq"``, ``"schunk"``.
    """
    return loader.tool_subdir.split("/")[0]


def get_tool_description(
    loader: Type[utils.ToolLoader],
) -> utils.ModelDescription:
    """Resolve and return the ModelDescription for a loader.

    Args:
        loader: A ToolLoader subclass.

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
        rows: List of ``(brand, description)`` tuples, one per tool.
    """
    headers = ["Tool", "Brand", "URDF", "SRDF", "Meshes"]

    data = [
        (
            desc.name,
            brand,
            get_filesystem_path(desc.urdf_path),
            get_filesystem_path(desc.srdf_path),
            get_filesystem_path(desc.mesh_dir),
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
    print(f"  {len(rows)} tools total")


def unique_loaders() -> dict[str, tuple[Type[utils.ToolLoader], str]]:
    """Build a deduplicated mapping of tool_name -> (loader, brand).

    Multiple TOOLS keys may point to the same loader (aliases). This
    function returns each physical tool exactly once, keyed by its
    canonical ``tool_name``.

    Returns:
        Dict mapping ``tool_name`` to ``(loader, brand)``.
    """
    seen: dict[str, tuple[Type[utils.ToolLoader], str]] = {}
    for loader in telekinesis_urdfs.TOOLS.values():
        tool_name = loader.tool_name
        if tool_name not in seen:
            seen[tool_name] = (loader, get_brand(loader))
    return seen


def show_all() -> None:
    """Display every registered tool grouped by brand, then a table."""
    tools = unique_loaders()
    current_brand = None
    for tool_name, (_, brand) in sorted(
        tools.items(), key=lambda x: (x[1][1], x[0])
    ):
        if brand != current_brand:
            print(f"\n=== {brand.replace('_', ' ').title()} ===")
            current_brand = brand
        print(f"  {tool_name}")

    rows = sorted(
        [
            (brand, get_tool_description(loader))
            for _, (loader, brand) in tools.items()
        ],
        key=lambda r: (r[0], r[1].name),
    )
    print_table(rows)


def show_brand(brand: str) -> None:
    """Display all tools that belong to a given brand.

    Args:
        brand: Brand identifier, e.g. ``"robotiq"``, ``"schunk"``.

    Raises:
        SystemExit: If no tools match the requested brand.
    """
    tools = unique_loaders()
    matches = {
        tool_name: (loader, b)
        for tool_name, (loader, b) in tools.items()
        if b == brand
    }
    if not matches:
        available = sorted({b for _, b in tools.values()})
        brands_str = ", ".join(available)
        raise SystemExit(
            f"Brand '{brand}' not found.\n"
            f"Available brands: {brands_str}\n"
            f"Usage: python tool_loader.py --brand BRAND\n"
            f"Example: python tool_loader.py --brand robotiq"
        )

    print(f"=== {brand.replace('_', ' ').title()} ===")
    rows = sorted(
        [
            (brand, get_tool_description(loader))
            for _, (loader, _) in matches.items()
        ],
        key=lambda r: r[1].name,
    )
    print_table(rows)


def show_tool(tool_key: str) -> None:
    """Display a single tool looked up by its TOOLS key.

    Args:
        tool_key: A key registered in TOOLS, e.g.
            ``"robotiq2f85"``, ``"onrobotrg6"``.

    Raises:
        SystemExit: If the key is not found in TOOLS.
    """
    key = tool_key.lower()
    if key not in telekinesis_urdfs.TOOLS:
        available = ", ".join(sorted(telekinesis_urdfs.TOOLS))
        raise SystemExit(
            f"Tool '{tool_key}' not found.\n"
            f"Available tools: {available}\n"
            f"Usage: python tool_loader.py --tool NAME\n"
            f"Example: python tool_loader.py --tool robotiq2f85"
        )
    loader = telekinesis_urdfs.TOOLS[key]
    brand = get_brand(loader)
    print(f"=== {loader.tool_name} ===")
    print_table([(brand, get_tool_description(loader))])


def main() -> None:
    """Parse CLI arguments and dispatch to the appropriate display function."""
    parser = argparse.ArgumentParser(
        description=(
            "Load and display tool descriptions from telekinesis_urdfs."
        ),
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--tool", metavar="NAME",
        help="Key of a single tool (e.g. robotiq2f85, onrobotrg6).",
    )
    group.add_argument(
        "--brand", metavar="BRAND",
        help="Brand to filter by (e.g. robotiq, schunk, onrobot).",
    )
    args = parser.parse_args()

    if args.tool:
        show_tool(args.tool)
    elif args.brand:
        show_brand(args.brand)
    else:
        show_all()


if __name__ == "__main__":
    main()
