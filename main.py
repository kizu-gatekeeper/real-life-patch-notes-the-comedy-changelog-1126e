"""Write one funny patch note to the make.fun output directory."""

import os
from pathlib import Path

LINE = "v2.4.1: fixed a bug where hiccups ignored the mute button and kept playing on every conference call."


def main():
    # Keep the entry a single non-empty line so the 1..200-char gate holds.
    if not LINE.strip():
        raise SystemExit("entry line must not be empty")
    out_path = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/tmp/out"))
    out_path.mkdir(parents=True, exist_ok=True)
    with open(out_path / "entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
