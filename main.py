# Alien field notes: one-line Earth review exporter, round 4.
import io, json, pathlib

BOUND = 200
ENTRY_FILE = "entry.txt"
RELEASE = "ali4-alien-review-r4"


def gate_pass(text):
    trimmed = text.strip()
    ok = 1 <= len(trimmed) <= BOUND
    return ok, len(trimmed)


def main():
    raw = io.open(ENTRY_FILE, encoding="utf-8").read()
    ok, size = gate_pass(raw)
    if not ok:
        raise SystemExit("gate fail")
    dest = pathlib.Path("out") / ENTRY_FILE
    dest.parent.mkdir(exist_ok=True)
    dest.write_bytes(raw.encode("utf-8"))
    print(json.dumps({"build": RELEASE, "ok": ok, "size": size, "bound": BOUND}))


if __name__ == "__main__":
    main()
