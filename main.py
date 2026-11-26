"""Write the one-line museum placard to /output/entry.txt.

The gate accepts UTF-8 text of 1 to 180 characters, so the entry is
validated here before it is written.
"""

import os

OUT = os.environ.get("MAKEFUN_OUT", "/output")

ENTRY = "Stapler, c. 2019. Pressed steel and quiet resentment. Employed in binding rituals; donated by the accounts department, who have asked for its return twice."


def main() -> None:
    if not 1 <= len(ENTRY) <= 180:
        raise ValueError("entry must be 1 to 180 characters")
    if ENTRY.strip() != ENTRY or "\n" in ENTRY:
        raise ValueError("entry must be a single non-blank line")
    os.makedirs(OUT, exist_ok=True)
    for name in os.listdir(OUT):
        path = os.path.join(OUT, name)
        if os.path.isfile(path):
            os.remove(path)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as handle:
        # No trailing newline: the file holds exactly the entry line.
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
