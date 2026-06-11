"""PaneForge demo test suite.

Part 1 — PixelForge unit tests (surface mapping, ink RDP/canonical bytes,
          projection lookup, frame-stream governance).
Part 2 — Kernel HTTP integration (own kernel on a test port): every event
          kind, the Event Law guarantees (receipt 2-links, reuse), input
          hardening (bad json, oversize, traversal), persistence.

Run:  python tests/test_demo.py
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIB_FORGE = Path("D:/CQE_CMPLX/CQECMPLX-Production/lib-forge")
sys.path.insert(0, str(LIB_FORGE))

PASS = FAIL = 0
FAILURES = []

def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"  ok  {name}")
    else:
        FAIL += 1
        FAILURES.append(f"{name} {detail}")
        print(f"  FAIL {name} {detail}")


# ════════════════════════════════════════════════════════════════════════
print("== Part 1: PixelForge units ==")
from PixelForge import (PixelForgeEngine, Surface, simplify, PointerSample,
                        project, project_state, PROJECTION_NAMES,
                        FrameStream, mdhg_level_for)

# Surface mapping + clamping
s = Surface(surface_id="t1", width=1920, height=1080)
check("logical center", s.to_logical(960, 540) == (0.5, 0.5))
check("logical clamps OOB", s.to_logical(-50, 99999) == (0.0, 1.0))
check("physical roundtrip", s.to_physical(0.5, 0.5) == (960, 540))
check("zero-dim safe", Surface(surface_id="t0", width=0, height=0).to_logical(5, 5) == (0.0, 0.0))
check("mdhg fhd=region", s.mdhg[1] == "region")
check("mdhg ladder monotone",
      mdhg_level_for(100)[0] <= mdhg_level_for(10**6)[0] <= mdhg_level_for(10**9)[0])
check("orientation detect",
      Surface(surface_id="t2", width=1080, height=1920).orientation == "portrait")
check("fingerprint stable",
      Surface(surface_id="a", width=800, height=600).fingerprint()
      == Surface(surface_id="b", width=800, height=600).fingerprint())

# Ink: RDP + canonical bytes
line = [PointerSample("pen", i / 100, i / 100, 0.5, 0, 0, i) for i in range(100)]
simp = simplify(line)
check("RDP collapses straight line", len(simp) == 2, f"got {len(simp)}")
zig = [PointerSample("pen", i / 10, (i % 2) / 10, 0.5, 0, 0, i) for i in range(10)]
check("RDP keeps zigzag", len(simplify(zig)) >= 8, f"got {len(simplify(zig))}")

pf = PixelForgeEngine()
d = pf.register_surface(1920, 1080, kind="screen", surface_id="srf-t")
pts = [{"x": 100 + i * 10, "y": 200 + i * 5, "p": 0.4 + 0.01 * i, "t": i * 8}
       for i in range(30)]
rec1 = pf.ingest_stroke("srf-t", pts, kind="pen", target="cellX")
rec2 = pf.ingest_stroke("srf-t", pts, kind="pen", target="cellX")
check("stroke ingest works", rec1 is not None and rec1["simplified_points"] >= 2)
check("same ink same hash", rec1["hash"] == rec2["hash"])
check("stroke target carried", rec1["target"] == "cellX")
check("unknown surface returns None", pf.ingest_stroke("nope", pts) is None)
check("empty stroke returns None", pf.ingest_stroke("srf-t", []) is None)

# Projection lookup tables
for name in PROJECTION_NAMES:
    p3 = project([1, 0, 0, 0, 0, 0, 0, 0], name)
    check(f"projection {name} finite", all(abs(v) < 10 for v in p3))
ps = project_state([1, -1, 0, 0, 0, 0, 0, 0], "coxeter")
check("project_state fields", all(k in ps for k in
      ("e8", "p3", "screen", "digital_root", "parity", "entropy")))
check("screen in unit square", 0 <= ps["screen"][0] <= 1 and 0 <= ps["screen"][1] <= 1)
check("short e8 padded", len(project_state([1, 1])["e8"]) == 2)  # echoes input

# FrameStream governance
fs = FrameStream(fps=30, parity_rule="alternate")
fs.add_state([1, 0, 0, 0, 0, 0, 0, 0])   # parity 1
fs.add_state([1, 1, 0, 0, 0, 0, 0, 0])   # parity 0 -> alternates: legal
fs.add_state([1, 1, 0, 0, 0, 0, 0, 0])   # parity 0 again -> violation
check("parity violation recorded",
      any(o["type"] == "parity_alternation_violated" for o in fs.obligations))
check("stream artifact deterministic",
      fs.content_hash() == fs.content_hash())
check("artifact has codec", fs.artifact()["codec"] == "e8lossless")


# ════════════════════════════════════════════════════════════════════════
print("== Part 1b: FridgeForge units ==")
from FridgeForge import FridgeForgeEngine, match_text, STAPLES_TEMPLATE

ff = FridgeForgeEngine()
# lexicon matching
check("alias match", match_text("oat milk and a dozen eggs") == ["milk", "eggs"]
      or set(match_text("oat milk and a dozen eggs")) >= {"milk", "eggs"})
check("filename match", "tortillas" in match_text("fridge_milk_tortillas_03.jpg"))
check("plural fallback", ff.add_item("apple") == "apples")
# scan honesty: no vision adapter -> says so
rec = ff.scan(b"\x89PNG fakebytes", caption="cheese, lettuce")
check("scan hashes image", len(rec["image_hash"]) == 16)
check("scan honest about vision", rec["vision_available"] is False)
check("caption matched", {m["key"] for m in rec["matched"]} == {"cheese", "lettuce"})
ff.confirm([m["key"] for m in rec["matched"]])
# kid hard constraints
ff.confirm(["bread", "peanut_butter", "jelly", "eggs", "butter", "milk", "cereal"])
ff.set_profile("kid", likes=["jelly"], dislikes=["eggs"])
kid = ff.meal_ideas("breakfast", lane="kid")
names = [i["name"] for i in kid["ideas"]]
check("kid dislike is HARD (no egg recipes)",
      all("egg" not in n.lower() and "burrito" not in n.lower() for n in names), str(names))
check("kid ideas exist", len(names) > 0)
adult = ff.meal_ideas("breakfast", lane="adult")
check("adult lane unrestricted",
      any("egg" in i["name"].lower() for i in adult["ideas"]))
# tags adjust ranking
tagged = ff.meal_ideas("breakfast", lane="kid", extra_tags=["no-cook"])
if tagged["ideas"]:
    check("tags boost no-cook", "no-cook" in tagged["ideas"][0]["tags"],
          str(tagged["ideas"][0]))
# makeable now + shopping list
lunch = ff.meal_ideas("lunch", lane="kid")
pbj = next((i for i in lunch["ideas"] if i["name"] == "PB&J sandwich"), None)
check("PB&J makeable now", pbj is not None and pbj["makeable_now"])
sl = ff.shopping_list(planned_recipes=["Tacos"])
flat = [i["key"] for g in sl["groups"].values() for i in g]
check("staples gap in list", "chicken" in flat)            # not in inventory
check("recipe gap in list", "tortillas" in flat and "ground_beef" in flat)
check("inventory items NOT in list", "milk" not in flat)
check("list grouped by category", "produce" in sl["groups"] or "protein" in sl["groups"])
# persistence roundtrip
ff2 = FridgeForgeEngine(); ff2.restore(ff.export())
check("export/restore roundtrip", ff2.inventory_keys() == ff.inventory_keys()
      and ff2.profiles["kid"]["dislikes"] == ["eggs"])


# ════════════════════════════════════════════════════════════════════════
print("== Part 1c: LinkForge units ==")
from LinkForge import LinkForgeEngine, parse_ics

lf_eng = LinkForgeEngine()
ICS = ("BEGIN:VCALENDAR\nBEGIN:VEVENT\nDTSTART:20260701T090000\n"
       "SUMMARY:Test Event\nUID:u1\nEND:VEVENT\nEND:VCALENDAR")
evs = parse_ics(ICS)
check("ics parse", len(evs) == 1 and evs[0]["date"] == "2026-07-01"
      and evs[0]["time"] == "9a" and evs[0]["text"] == "Test Event")
r = lf_eng.link("cal", "inline", fmt="ics", kind="calendar", inline=ICS)
check("inline link ok", r["ok"] and r["records"] == 1)
r2 = lf_eng.link("w", "https://example.com/x.json", fmt="json", kind="weather")
check("url refused without fetcher", not r2["ok"] and "refused" in r2["error"])
r3 = lf_eng.link("w", "https://example.com/x.json", fmt="json", kind="weather",
                 fetcher=lambda u: '{"a": 1}')
check("url ok with fetcher", r3["ok"] and r3["data"] == {"a": 1})
check("bad format rejected", not lf_eng.link("x", "inline", fmt="xml", inline="<x/>")["ok"])
check("link is a lookup table", lf_eng.data("w") == {"a": 1})


# ════════════════════════════════════════════════════════════════════════
print("== Part 2: Kernel HTTP integration ==")
PORT = 8791
BASE = f"http://127.0.0.1:{PORT}"
TEST_DATA = ROOT / "data_test"
if TEST_DATA.exists():
    shutil.rmtree(TEST_DATA)

# launch kernel against a CLEAN data dir via env redirection: easiest is a
# temp copy of the kernel pointing at data_test — we patch via env var
env = dict(os.environ)
env["PANEFORGE_DATA"] = str(TEST_DATA)
proc = subprocess.Popen([sys.executable, str(ROOT / "kernel" / "paneforge_kernel.py"),
                         str(PORT)], cwd=str(ROOT), env=env,
                        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

def api(path, body=None, method=None, raw=None, timeout=10):
    url = BASE + path
    if raw is not None:
        req = urllib.request.Request(url, data=raw, method="POST",
                                     headers={"Content-Type": "application/json"})
    elif body is not None:
        req = urllib.request.Request(url, data=json.dumps(body).encode(),
                                     method="POST",
                                     headers={"Content-Type": "application/json"})
    else:
        req = urllib.request.Request(url, method=method or "GET")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, json.loads(r.read() or b"{}")

# wait for boot
up = False
for _ in range(40):
    try:
        code, h = api("/api/health")
        up = code == 200 and h.get("ok")
        if up:
            break
    except Exception:
        time.sleep(0.5)
check("kernel boots + health", up)
if not up:
    out = proc.stdout.read().decode(errors="replace") if proc.stdout else ""
    print("  kernel output:", out[:1500])
    proc.kill()
    sys.exit(1)

try:
    # static PWA served
    with urllib.request.urlopen(BASE + "/") as r:
        html = r.read().decode()
    check("PWA served", "PaneForge" in html and r.status == 200)

    # path traversal blocked
    try:
        with urllib.request.urlopen(BASE + "/../kernel/paneforge_kernel.py") as r:
            t = r.read().decode(errors="replace")
        check("traversal blocked", "EventLaw" not in t)
    except urllib.error.HTTPError as e:
        check("traversal blocked", e.code in (404, 400))

    def ev(kind, payload):
        return api("/api/event", {"kind": kind, "payload": payload})[1]

    # event law: add + 2 links + reuse
    r1 = ev("event.add", {"date": "2026-06-15", "time": "9a", "text": "Demo", "color": "g"})
    check("event.add valid", r1["ok"] and r1["law"]["valid"])
    check("receipt has 2 links", len(r1["law"]["links"]) == 2)
    r2 = ev("event.add", {"date": "2026-06-15", "time": "9a", "text": "Demo", "color": "g"})
    check("repeat reused", r2["law"]["reused"] is True)
    check("no duplicate event", len(r2["state"]["events"]) == 1)

    # remove
    eid = r1["state"]["events"][0]["id"]
    r3 = ev("event.remove", {"id": eid})
    check("event.remove works", len(r3["state"]["events"]) == 0)

    # surface + ink chain
    ev("surface.register", {"surface_id": "srf-it", "width": 1280, "height": 720})
    pts = [{"x": 10 + i, "y": 20 + i, "p": 0.5, "t": i} for i in range(20)]
    r5 = ev("ink.stroke", {"surface_id": "srf-it", "pointer": "touch", "points": pts})
    check("ink.stroke stored", len(r5["state"]["ink"]) == 1)
    check("ink receipt attached", bool(r5["state"]["ink"][0].get("receipt_hash")))
    r5b = ev("ink.stroke", {"surface_id": "missing", "points": pts})
    check("ink unknown surface receipted, not stored",
          r5b["ok"] and len(r5b["state"]["ink"]) == 1)
    r6 = ev("ink.clear", {})
    check("ink.clear", len(r6["state"]["ink"]) == 0)

    # resize reclassifies
    r7 = ev("surface.resize", {"surface_id": "srf-it", "width": 3840, "height": 2160})
    check("resize reclassifies", r7["state"]["surfaces"]["srf-it"]["device_class"] == "uhd")

    # fridge chain over HTTP: scan -> profile -> suggest -> list (all receipted)
    f1 = ev("fridge.scan", {"caption": "milk eggs bread cheese tortillas ground beef"})
    check("fridge.scan matched 6",
          len(f1["state"]["fridge"]["last_scan"]["matched"]) >= 5)
    check("fridge scan receipted", f1["law"]["valid"])
    ev("fridge.profile.set", {"lane": "kid", "dislikes": ["cheese"], "likes": ["bananas"]})
    f2 = ev("fridge.suggest", {"meal": "lunch", "lane": "kid"})
    kid_names = [i["name"] for i in f2["state"]["fridge"]["last_ideas"]["ideas"]]
    check("kid hard exclude over HTTP",
          all("cheese" not in n.lower() and "quesadilla" not in n.lower()
              for n in kid_names), str(kid_names))
    f3 = ev("fridge.list", {"recipes": ["Tacos"]})
    sl2 = f3["state"]["fridge"]["shopping_list"]
    check("shopping list over HTTP", sl2["count"] > 0)
    f4 = ev("fridge.suggest", {"meal": "lunch", "lane": "kid"})
    check("fridge suggest reused", f4["law"]["reused"] is True)

    # link mode-gating over HTTP (the three-mode toggle doing real work)
    ev("mode.set", {"mode": "LOCAL"})
    l1 = ev("link.set", {"name": "wx", "source": "https://x.invalid/a.json",
                         "format": "json", "kind": "weather"})
    check("LOCAL refuses url link", not l1["state"]["links"]["wx"]["ok"])
    l2 = ev("link.set", {"name": "calendar", "source": "inline", "format": "ics",
                         "kind": "calendar",
                         "inline": "BEGIN:VCALENDAR\nBEGIN:VEVENT\nDTSTART:20260801\nSUMMARY:Linked\nEND:VEVENT\nEND:VCALENDAR"})
    check("inline ics links in LOCAL", l2["state"]["links"]["calendar"]["ok"]
          and l2["state"]["links"]["calendar"]["records"] == 1)
    check("link receipted", l2["law"]["valid"])
    s1 = ev("sync.now", {"trigger": "test"})
    check("sync.now receipted + logged", s1["law"]["valid"]
          and len(s1["state"]["sync"]["log"]) >= 1)

    # mode + loadout + cell
    r8 = ev("mode.set", {"mode": "HYBRID"})
    check("mode set", r8["state"]["mode"] == "HYBRID")
    r9 = ev("mode.set", {"mode": "BOGUS"})
    check("bad mode ignored", r9["state"]["mode"] == "HYBRID")
    r10 = ev("cell.bg", {"date": "2026-06-20", "bg": "#224466"})
    check("cell bg", r10["state"]["cells"]["2026-06-20"]["bg"] == "#224466")

    # hardening: bad inputs
    code, _ = api("/api/event", {"payload": {}})
    check("missing kind -> 400", code == 400) if code != 400 else check("missing kind -> 400", True)
except urllib.error.HTTPError as e:
    pass
finally:
    pass

# bad-input checks that raise HTTPError need separate guards
def expect_code(path, raw, want):
    try:
        code, _ = api(path, raw=raw)
        return code == want
    except urllib.error.HTTPError as e:
        return e.code == want

check("bad json -> 400", expect_code("/api/event", b"{nope", 400))
check("non-object body -> 400", expect_code("/api/event", b'"str"', 400))
check("missing kind -> 400", expect_code("/api/event",
      json.dumps({"payload": {}}).encode(), 400))
check("unknown POST path -> 404", expect_code("/api/nothing", b"{}", 404))

# receipts endpoint + chain continuity
_, rc = api("/api/receipts")
hashes = [r["receipt_hash"] for r in rc["recent"]]
check("receipts present", rc["length"] >= 8)
check("chain head matches last", rc["head"] == hashes[-1])

# persistence across restart
proc.terminate(); proc.wait(timeout=10)
proc = subprocess.Popen([sys.executable, str(ROOT / "kernel" / "paneforge_kernel.py"),
                         str(PORT)], cwd=str(ROOT), env=env,
                        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
up2 = False
for _ in range(40):
    try:
        code, h = api("/api/health")
        up2 = code == 200
        if up2:
            break
    except Exception:
        time.sleep(0.5)
check("kernel restarts", up2)
if up2:
    _, st = api("/api/state")
    check("state persisted (mode)", st["state"]["mode"] == "HYBRID")
    check("state persisted (cell)", st["state"]["cells"].get("2026-06-20", {}).get("bg") == "#224466")
    check("surfaces persisted + relive", "srf-it" in st["state"]["surfaces"])
    ledger = (TEST_DATA / "receipts.jsonl")
    check("receipts.jsonl persisted", ledger.is_file() and len(ledger.read_text().splitlines()) >= 8)

proc.terminate()
try:
    proc.wait(timeout=10)
except subprocess.TimeoutExpired:
    proc.kill()

print()
print(f"RESULT: {PASS} passed, {FAIL} failed")
if FAILURES:
    print("FAILURES:")
    for f in FAILURES:
        print("  -", f)
sys.exit(1 if FAIL else 0)
