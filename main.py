"""Alien field notes, beamed home as one line."""
import os

NOTE = ("Beautiful planet, four stars. The dominant species taught its "
        "rocks to speak, then mostly uses them for pictures of lunch. "
        "Would recommend to neighbors.")
LOG = "aln2"
PLANET = "earth"
RATING = "four-stars"
NEXT = "jupiter"


def beam(base):
    base = base or "output"
    os.makedirs(base, exist_ok=True)
    p = os.path.join(base, "entry.txt")
    draft = p + ".draft"
    with open(draft, "w", encoding="utf-8", newline="\n") as f:
        f.write(NOTE + "\n")
    os.replace(draft, p)
    with open(p, encoding="utf-8") as f:
        got = f.read()
    assert got == NOTE + "\n", "signal degraded"
    return got.strip()


logged = beam(os.environ.get("MAKEFUN_OUTPUT_DIR"))
print(LOG, PLANET, RATING, len(logged), "chars beamed")
print("next stop:", NEXT, "packing light")
