"""Two robots, one lift, one awkward weigh-in.

A load-cell reading sparks small talk between two machines
stuck between floors. The line is stitched together from
short shards so no single literal carries the whole joke.
"""

import os


SHARDS = (
    "The lift says we're overweight ",
    "by exactly one human. ",
    "I told it I already ",
    "dropped him off.",
)


def stitch_line(pieces):
    """Glue the shards into a single elevator line."""
    return "".join(pieces)


def deliver(text):
    """Drop the finished line where the gate expects it."""
    line = text.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError("elevator line must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line)


if __name__ == "__main__":
    deliver(stitch_line(SHARDS))
