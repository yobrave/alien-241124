"""Alien review line: audit checks stream, then write output copy."""
import json
import os

OUT_ENV = "MAKEFUN_OUTPUT_DIR"
BOUND = 200


def audit(text):
    yield ("length_ok", 1 <= len(text) <= BOUND)
    yield ("not_blank", bool(text.strip()))


def run():
    with open("entry.txt", encoding="utf-8") as fh:
        src = fh.read().strip()
    flags = dict(audit(src))
    if not all(flags.values()):
        raise SystemExit(json.dumps({"flags": flags, "text": src}))
    root = os.environ.get(OUT_ENV) or "/output"
    os.makedirs(root, exist_ok=True)
    path = os.path.join(root, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(src)
    return json.dumps({"verdict": "pass", "chars": len(src), "path": path})


if __name__ == "__main__":
    print(run())
