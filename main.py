#!/usr/bin/env python3
"""Sum up 24 November's world news in one image — writes entry.png.

Copies the front page this repository holds (drawn by draw.py) to the
output directory. No network, no randomness: every run writes the same bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    src = os.path.join(HERE, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dest)
    print(f"wrote {dest} ({os.path.getsize(dest)} bytes)")


if __name__ == "__main__":
    main()
