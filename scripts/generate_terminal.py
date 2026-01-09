#!/usr/bin/env python3
"""Generate retro terminal GIF for GitHub profile."""

import os
import gifos

def main():
    username = os.getenv("GITHUB_REPOSITORY_OWNER", "m-mohamed")

    # Create terminal (800x400 for a nice wide format)
    t = gifos.Terminal(width=800, height=400, xpad=15, ypad=15)

    # Boot sequence
    t.gen_text(text="BIOS v3.0.1 (2026/01/08)", row_num=1)
    t.gen_text(text="Initializing system...", row_num=2)
    t.gen_text(text="Loading profile data...", row_num=3)
    t.gen_text(text="", row_num=4)

    # Fetch GitHub stats
    try:
        stats = gifos.utils.fetch_github_stats(user_name=username)

        # Header
        t.gen_text(
            text=f"\x1b[36m{username}\x1b[0m@\x1b[36mgithub\x1b[0m",
            row_num=5
        )
        t.gen_text(text="-" * 30, row_num=6)

        # Stats (neofetch style)
        t.gen_text(
            text=f"\x1b[34mStack:\x1b[0m Rust, TypeScript, Python",
            row_num=7
        )
        t.gen_text(
            text=f"\x1b[34mEditor:\x1b[0m Neovim",
            row_num=8
        )
        t.gen_text(
            text=f"\x1b[34mTerminal:\x1b[0m WezTerm",
            row_num=9
        )
        t.gen_text(
            text=f"\x1b[34mTheme:\x1b[0m Tokyo Night",
            row_num=10
        )
        t.gen_text(
            text=f"\x1b[34mShell:\x1b[0m zsh 5.9",
            row_num=11
        )
        t.gen_text(text="", row_num=12)

        # GitHub stats
        t.gen_text(
            text=f"\x1b[34mRepos:\x1b[0m {stats.public_repos}",
            row_num=13
        )
        t.gen_text(
            text=f"\x1b[34mFollowers:\x1b[0m {stats.followers}",
            row_num=14
        )
        t.gen_text(text="", row_num=15)

        # Building section
        t.gen_text(text="\x1b[35mBuilding:\x1b[0m", row_num=16)
        t.gen_text(
            text="\x1b[32m->\x1b[0m rehoboam   TUI for Claude Code",
            row_num=17
        )
        t.gen_text(
            text="\x1b[32m->\x1b[0m dotfiles   macOS, <100ms shell",
            row_num=18
        )

    except Exception as e:
        print(f"Warning: Could not fetch GitHub stats: {e}")
        t.gen_text(text=f"\x1b[31mError:\x1b[0m Could not fetch stats", row_num=5)

    # Generate GIF
    t.gen_gif()
    print("Generated terminal.gif")


if __name__ == "__main__":
    main()
