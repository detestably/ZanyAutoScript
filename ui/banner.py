"""Logo ASCII centralizada exibida no topo de todas as telas."""
from __future__ import annotations

from rich.align import Align
from rich.console import Console, Group
from rich.text import Text

LOGO_LINES = [
    "███████╗          █████╗ ██╗   ██╗████████╗ ██████╗ ",
    "╚════██║         ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗",
    "  ███╔═╝  █████╗ ███████║██║   ██║   ██║   ██║   ██║",
    "██╔══╝    ╚════╝ ██╔══██║██║   ██║   ██║   ██║   ██║",
    "███████╗         ██║  ██║╚██████╔╝   ██║   ╚██████╔╝",
    "╚══════╝         ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ "
]

TITLE = "Z - A U T O"
TAGLINE = "Automação Inteligente de Bot"

def banner_renderable(subtitle: str | None = None, compact: bool = False) -> Group:
    width = max(len(line) for line in LOGO_LINES)
    logo = Text(justify="left", no_wrap=True)
    
    # Degradê de roxo para rosa por exemplo
    colors = ["magenta", "magenta", "deep_pink3", "deep_pink3", "hot_pink", "hot_pink"]
    for line, color in zip(LOGO_LINES, colors):
        logo.append(line.ljust(width) + "\n", style=f"bold {color}")
    logo.rstrip()

    parts = [Align.center(logo), Align.center(Text(TITLE, style="bold white"))]
    if not compact:
        parts.append(Align.center(Text(TAGLINE, style="dim")))
    if subtitle:
        parts.append(Align.center(Text(f"─── {subtitle} ───", style="bold magenta")))
    parts.append(Text(""))
    return Group(*parts)


def show_banner(console: Console, subtitle: str | None = None) -> None:
    console.clear()
    console.print(banner_renderable(subtitle))
