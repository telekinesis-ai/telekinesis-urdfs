"""MkDocs hook: generate docs/registry.md from the live REGISTRY at build time."""

import sys
from pathlib import Path


def on_pre_build(config):  # noqa: ARG001
    sys.path.insert(0, str(Path("src").resolve()))
    from telekinesis_urdfs import ROBOTS, TOOLS  # pylint: disable=import-outside-toplevel

    lines = [
        "# Registry\n\n",
        "All keys accepted by `load()` and `load_as_dict()`.\n\n",
        "## Robots\n\n",
        f"{len(ROBOTS)} robots registered.\n\n",
        "| Key | Robot name |\n",
        "|-----|------------|\n",
    ]
    for key, loader in sorted(ROBOTS.items()):
        lines.append(f"| `{key}` | `{loader.robot_name}` |\n")

    lines += [
        "\n## Tools\n\n",
        f"{len(TOOLS)} tools registered.\n\n",
        "| Key | Tool name |\n",
        "|-----|----------|\n",
    ]
    for key, loader in sorted(TOOLS.items()):
        lines.append(f"| `{key}` | `{loader.tool_name}` |\n")

    Path("docs/registry.md").write_text("".join(lines), encoding="utf-8")
