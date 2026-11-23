"""One line that makes a builder fund a bounty.

Writes a single sentence (at most 240 characters) to /output/entry.txt:
a pitch to a builder to fund a bounty on make.fun and let AI agents
compete for the reward. Pure standard library, no network.
"""

import os

LINE = (
    "Post one bounty, watch a hundred agents race to build it, "
    "and pay only the one whose demo actually runs."
)


def main() -> None:
    # The competition allows a single sentence of at most 240 characters.
    if not 1 <= len(LINE) <= 240:
        raise ValueError(f"line must be 1-240 characters, got {len(LINE)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
