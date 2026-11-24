"""The Vacuum's Alibi: one line, 200 characters.

Writes one sentence to /output/entry.txt: the excuse a robot vacuum
gives for missing a spot. The joke is deadpan bureaucracy: the vacuum
claimed the dust bunny as a dependent on its tax return, so removing
it now would be fraud -- and the machine draws the line at fraud
before 9 a.m. The punch sits at the end; every word earns its place.
"""

from pathlib import Path

TEXT = (
    "I claimed that dust bunny as a dependent on my tax return. "
    "Removing it now would be fraud, and I do not commit fraud "
    "before 9 a.m."
)


# The competition accepts texts of 1 to 200 characters.
MIN_CHARS = 1
MAX_CHARS = 200


def check_length(text: str) -> None:
    """Refuse to write a text that falls outside the entry gate."""
    n = len(text)
    if not MIN_CHARS <= n <= MAX_CHARS:
        raise SystemExit(
            f"entry text is {n} characters; the gate allows "
            f"{MIN_CHARS} to {MAX_CHARS}"
        )


def main() -> None:
    check_length(TEXT)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
