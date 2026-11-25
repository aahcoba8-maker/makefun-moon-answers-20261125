"""The Moon Finally Answers Back — one line, in the Moon's voice."""

import os

ENTRY = "Four billion years of wishes, howls, and 2 a.m. promises. I am a rock. I do not take requests."


def main():
    text = ENTRY
    # Self-gate mirroring the sealed scorer: UTF-8, 1-240 chars, one line.
    assert 1 <= len(text) <= 240, "entry must be 1-240 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
