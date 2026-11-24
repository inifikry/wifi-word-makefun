#!/usr/bin/env python3
"""One Word for Your Wi-Fi — make.fun bounty entry.

Writes a single word describing home Wi-Fi to /output/entry.txt.
The word must be 1-20 UTF-8 characters, not only whitespace.
"""

import os

# The word: "Ghosting".
# Home Wi-Fi vanishes mid-call, mid-game, mid-download — no warning,
# no goodbye — exactly like being ghosted. It is the funniest and truest
# one-word description of Wi-Fi as it is actually lived: it does not just
# get slow, it disappears on you. A fresh angle (Wi-Fi as a bad date)
# instead of the words everyone reaches for (slow, laggy, flaky), and
# instantly understood with no context. As a network name it is perfect.
WORD = "Ghosting"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate check, mirroring the bounty scorer: 1-20 UTF-8 characters,
    # not only whitespace.
    text = WORD
    assert 1 <= len(text) <= 20, "word must be 1-20 characters"
    assert text.strip(), "word must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
