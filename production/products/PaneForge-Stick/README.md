# PaneForge

Turn any screen into a smart wall calendar. **One engine, any device, from a thumb drive.**

A bring-your-own-screen alternative to the locked, subscription-gated smart-calendar
appliances (Skylight / Cozyla / DAKboard category). The software is the product: it ships
on a USB stick and runs on whatever screen+compute is in front of it, controlled from your
phone. No proprietary hardware, no mandatory subscription.

## The thesis: one engine, an adapter ring

The calendar engine is written once. A thin per-target **adapter** makes the same payload
run on any runtime. The PWA is simultaneously the demo, the on-wall display, and the mobile
control surface — because a browser is the one runtime every target already has.

```
THE STICK  (one USB, "as much as fits")
├─ engine/     one calendar engine (event model, layout, weather, photo rail, grid)
├─ app/        the PWA bundle — display + control, same codebase   [BUILT: display demo]
├─ adapters/   same engine, per target:
│   ├─ browser    pure PWA (instant demo + mobile control; any browser)   [v1]
│   ├─ firestick  Fire TV / Android TV: fullscreen webview + autostart
│   ├─ x86-boot   bootable Linux kiosk -> any old laptop / ~$35 mini-PC + any monitor
│   ├─ pi         same kiosk on ARM
│   └─ android    tablet webview wrapper (carries the stylus tier later)
├─ data/       local store: events, photos, settings
└─ modes/      connectivity toggle
    ├─ LOCAL     everything on-device, phone controls over Wi-Fi (mDNS), no internet
    ├─ HYBRID    ONLY Google-type calendar services online; everything else local
    └─ CLOUD     optional account for remote control + multi-device
```

## Status

- **app/** — v1 display PWA demo. Self-contained, offline-first, installable. Replicates the
  reference layout (left rail: clock / date / weather / 4-day forecast; right: M-S two-week
  grid with today highlighted and colored event chips). Demo data is inline; the product
  feeds it from the engine + sync layer.

## View the demo

- Quickest: double-click `app/index.html`.
- Full PWA (installable, service worker): serve the folder over http and open the URL —
  e.g. `python -m http.server 8000` from `app/`, then open `http://localhost:8000/`.
- It scales to any aspect ratio (landscape wall display and portrait/phone both handled).

## Roadmap

1. **Control PWA** — same codebase, "control" mode: add/edit events, photos, layout, weather
   location, connectivity mode. Discovers the display on the LAN (mDNS).
2. **Sync layer** — three modes (LOCAL / HYBRID-Google / CLOUD) behind one toggle.
3. **Adapter ring** — firestick + x86-boot first (widest cheap reach), then pi, then android.
4. **Stick image** — pack engine + app + adapters + data onto one bootable/auto-loading USB.
5. **Stylus tier** — framed touchscreen; engine stays input-agnostic, ink -> text into the
   event model.
