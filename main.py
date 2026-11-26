"""Write one funny patch note to the make.fun output directory."""

import os

LINE = "v2.4.1: fixed a bug where hiccups ignored the mute button and kept playing on every conference call."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/tmp/out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
