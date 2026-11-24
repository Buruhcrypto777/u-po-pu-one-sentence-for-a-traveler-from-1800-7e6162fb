"""One Sentence for a Traveler from 1800.

Writes a single sentence (at most 200 characters) explaining the modern
internet to a time traveler from 1800, using only things a person from
that year already knows: libraries, letters, rooms, tea.

Pure stdlib. Deterministic: the same bytes on every run.
"""

import os

SENTENCE = (
    "The internet is every library on earth folded into one room, "
    "where a letter to a stranger in China is answered before your "
    "tea cools."
)


def main():
    text = SENTENCE.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError("sentence must be 1-200 characters, got %d" % len(text))
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(SENTENCE + "\n")
    except OSError:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "out", "entry.txt")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(SENTENCE + "\n")
    print(path)


if __name__ == "__main__":
    main()
