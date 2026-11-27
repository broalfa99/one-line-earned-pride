#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes a single line (1–240 characters) to /output/entry.txt: a quiet,
earned moment of pride for someone in a scene.

The line: a grandmother who learned to read at seventy-one writes her
first letter by herself — to the granddaughter she had only ever signed
for with a thumbprint. The effort (learning to read at 71) is felt
inside the line, the thumbprint is the concrete, fresh detail, and the
pride lands on the last word. No trophy, no podium, no graduation, no
congratulation — just the letter.
"""

LINE = (
    "My grandmother learned to read at seventy-one; the first letter she "
    "wrote by herself was to the granddaughter she had only ever signed "
    "for with a thumbprint."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 240, f"entry is {len(text)} chars, must be 1-240"
    assert text == text.strip(), "entry must not start or end with whitespace"
    # The brief needs all of these in one read: a real person, a concrete
    # scene, effort the reader can feel, and pride that arrives by the
    # last word — the thumbprint.
    assert "grandmother" in text.lower(), "must name a real person"
    assert "thumbprint" in text.lower(), "must carry the concrete detail"
    assert "seventy-one" in text, "must carry the long effort"
    import os

    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} chars to {out}")


if __name__ == "__main__":
    main()
