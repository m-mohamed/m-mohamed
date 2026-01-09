#!/usr/bin/env python3
"""Generate retro terminal GIF for GitHub profile."""

import gifos


def main():
    # Create terminal (smaller = no play button on GitHub)
    t = gifos.Terminal(width=600, height=320, xpad=10, ypad=10)

    # Header
    t.gen_text(
        text="\x1b[36mm-mohamed\x1b[0m@\x1b[36mgithub\x1b[0m",
        row_num=1
    )
    t.gen_text(text="-" * 25, row_num=2)

    # Stats (neofetch style)
    t.gen_text(text="\x1b[34mStack:\x1b[0m Rust, TypeScript, Python", row_num=3)
    t.gen_text(text="\x1b[34mEditor:\x1b[0m Neovim", row_num=4)
    t.gen_text(text="\x1b[34mTerminal:\x1b[0m WezTerm", row_num=5)
    t.gen_text(text="\x1b[34mTheme:\x1b[0m Tokyo Night", row_num=6)
    t.gen_text(text="\x1b[34mShell:\x1b[0m zsh 5.9", row_num=7)
    t.gen_text(text="", row_num=8)

    # Building section
    t.gen_text(text="\x1b[35mBuilding:\x1b[0m", row_num=9)
    t.gen_text(text="\x1b[32m->\x1b[0m rehoboam   TUI for Claude Code", row_num=10)
    t.gen_text(text="\x1b[32m->\x1b[0m dotfiles   macOS, <100ms shell", row_num=11)

    # Generate GIF
    t.gen_gif()
    print("Generated terminal.gif")


if __name__ == "__main__":
    main()
