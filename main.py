#!/usr/bin/env python3
"""Rejected Olympic Sports — one funny single-line sport the Olympics turned down.

The program writes a single line to /output/entry.txt: a made-up event that
sounds like a real broadcast, absurd enough to be funny, and short enough to
fit inside 200 characters.
"""

import os

# Final line: a minimarket queue sprint — concrete human scene (7 a.m. line),
# one specific physical object (the rice shelf), and the turn lands in the
# last words, when the elbowing athlete suddenly turns polite.
LINE = (
    "Competitive queue-jumping: four athletes sprint a 100-metre minimarket "
    "line at 7 a.m., baskets full, elbows out \u2014 gold to whoever reaches "
    "the rice shelf first and still says \u201csilakan dulu, Pak\u201d."
)


def main():
    # The grader mounts the output directory; locally it arrives through
    # MAKEFUN_OUTPUT_DIR, and on the grading image it is /output.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
