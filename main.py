import json
import os

BEACON = "aln3-orbit"
SPAN = 200


def scout(repo_root):
    probe = os.path.join(repo_root, "entry.txt")
    with open(probe, "rb") as feed:
        return feed.read()


def radio(blob):
    if not blob:
        return "", "silent transmission"
    rows = blob.decode("utf-8", "strict").replace("\r", "").split("\n")
    picked = ""
    idx = 0
    while idx < len(rows):
        if rows[idx].strip():
            picked = rows[idx]
            break
        idx += 1
    if not picked.strip():
        return "", "nothing picked up"
    if len(picked) > SPAN:
        return "", "signal over span %d" % SPAN
    return picked, ""


def transmit(note, repo_root):
    target = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(target, exist_ok=True)
    slot = os.path.join(target, "entry.txt")
    with open(slot, "wb") as drop:
        drop.write(note.encode("utf-8"))
    with open(slot, "rb") as mirror:
        assert mirror.read() == note.encode("utf-8"), "mirror drift"
    return slot


root = os.path.dirname(os.path.abspath(__file__))
note, static = radio(scout(root))
if static:
    print(json.dumps({"code": 4, "static": static, "beacon": BEACON}))
    raise SystemExit(1)
lane = transmit(note, root)
print(json.dumps({"code": 0, "span": len(note), "beacon": BEACON, "lane": lane}))
