"""Generate the animated Solar Ram Studios / Solar Forge GitHub banner.

Usage: python3 scripts/gen_banner.py > assets/solar-forge-banner.svg
"""
import math
import random
import sys

W, H = 1200, 400
SUN = (912, 204)
GOLD = "#efbd6d"
GOLD_HI = "#ffdda5"
GOLD_DIM = "#a36c2d"
INK = "#090908"
TEXT = "#f2ede3"
TEXT2 = "#b2ada3"
MUTED = "#8a8478"
SANS = "system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"
MONO = "ui-monospace, 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace"

# (rx, ry, seconds per orbit, apps)
ORBITS = [
    (108, 40, 26, ["Harness", "Diagrams", "Game Engine"]),
    (164, 66, 40, ["Life Helper", "Boards", "Arcade", "Signal Lab"]),
    (220, 96, 58, ["Dashboard", "Pets", "Themes", "Game Guides"]),
]
PLANET_COLORS = ["#efbd6d", "#e8a845", "#f6d49a", "#c89956"]

random.seed(7)
out = []
w = out.append


def ellipse_path(rx, ry):
    cx, cy = SUN
    # Start on the right, travel clockwise (down first) so motion reads left-to-right in front.
    return (f"M{cx + rx} {cy} A{rx} {ry} 0 1 1 {cx - rx} {cy} "
            f"A{rx} {ry} 0 1 1 {cx + rx} {cy}")


w(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
  'role="img" aria-labelledby="title desc">')
w('<title id="title">Chase Struse · Solar Ram Studios</title>')
w('<desc id="desc">Animated banner: Chase Struse, Senior Software Engineer at Solar Ram Studios, '
  'forging the Solar Forge suite of local-first apps. A glowing sun is orbited by Solar Forge apps '
  'while a terminal runs a local LLM with zero bytes sent to the cloud.</desc>')

w("""<style>
  .twinkle { animation: twinkle 4s ease-in-out infinite; }
  @keyframes twinkle { 0%, 100% { opacity: .15 } 50% { opacity: .9 } }
  .sun-glow { transform-origin: %(sx)spx %(sy)spx; animation: breathe 6s ease-in-out infinite; }
  @keyframes breathe { 0%, 100% { transform: scale(1); opacity: .85 } 50% { transform: scale(1.12); opacity: 1 } }
  .rays { transform-origin: %(sx)spx %(sy)spx; animation: spin 60s linear infinite; }
  .rays-2 { transform-origin: %(sx)spx %(sy)spx; animation: spin 90s linear infinite reverse; }
  @keyframes spin { to { transform: rotate(360deg) } }
  .cursor { animation: blink 1s steps(1) infinite; }
  @keyframes blink { 50% { opacity: 0 } }
  .bar { transform-box: fill-box; transform-origin: 50%% 100%%; animation: eq 1.1s ease-in-out infinite; }
  @keyframes eq { 0%, 100% { transform: scaleY(.25) } 50% { transform: scaleY(1) } }
  .dot-live { animation: live 2s ease-in-out infinite; }
  @keyframes live { 0%, 100% { opacity: 1 } 50% { opacity: .3 } }
  .comet { animation: comet 11s ease-in infinite; opacity: 0; }
  @keyframes comet {
    0%, 78% { opacity: 0; transform: translate(0, 0) }
    80% { opacity: 1 }
    92% { opacity: 0; transform: translate(-520px, 210px) }
    100% { opacity: 0; transform: translate(-520px, 210px) }
  }
  .shimmer { animation: shimmer 7s ease-in-out infinite; }
  @keyframes shimmer { 0%%, 100%% { opacity: .35 } 50%% { opacity: .75 } }
  @media (prefers-reduced-motion: reduce) {
    .twinkle, .sun-glow, .rays, .rays-2, .cursor, .bar, .dot-live, .comet, .shimmer { animation: none; }
  }
</style>""".replace("%(sx)s", str(SUN[0])).replace("%(sy)s", str(SUN[1])).replace("%%", "%"))

w(f"""<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop stop-color="#0d0c0a" /><stop offset=".55" stop-color="{INK}" /><stop offset="1" stop-color="#161109" />
  </linearGradient>
  <radialGradient id="halo" cx="{SUN[0]}" cy="{SUN[1]}" r="300" gradientUnits="userSpaceOnUse">
    <stop stop-color="#e8a845" stop-opacity=".30" /><stop offset=".45" stop-color="#e8a845" stop-opacity=".07" />
    <stop offset="1" stop-color="#e8a845" stop-opacity="0" />
  </radialGradient>
  <radialGradient id="core" cx=".42" cy=".38" r=".7">
    <stop stop-color="#fff4dc" /><stop offset=".35" stop-color="{GOLD_HI}" />
    <stop offset=".8" stop-color="#e8a845" /><stop offset="1" stop-color="#b9772c" />
  </radialGradient>
  <linearGradient id="cometTail" x1="0" y1="0" x2="1" y2="0">
    <stop stop-color="{GOLD_HI}" stop-opacity="0" /><stop offset="1" stop-color="{GOLD_HI}" />
  </linearGradient>
  <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M40 0H0V40" fill="none" stroke="#e3cfaa" stroke-opacity=".035" />
  </pattern>
  <clipPath id="frame"><rect width="{W}" height="{H}" rx="24" /></clipPath>
  <clipPath id="type1"><rect x="96" y="262" height="24" width="0">
    <animate attributeName="width" dur="12s" repeatCount="indefinite" calcMode="discrete"
      values="{';'.join(str(int(i * 9.1)) for i in range(0, 27))};{';'.join(['250'] * 26)};0"
      keyTimes="{';'.join(f'{i / 53 * 0.98:.4f}' for i in range(53))};1" />
  </rect></clipPath>
</defs>""")

w(f'<g clip-path="url(#frame)">')
w(f'<rect width="{W}" height="{H}" fill="url(#bg)" />')
w(f'<rect width="{W}" height="{H}" fill="url(#grid)" />')
w(f'<rect width="{W}" height="{H}" fill="url(#halo)" class="sun-glow" />')

# Starfield
for i in range(70):
    x = random.uniform(10, W - 10)
    y = random.uniform(10, H - 10)
    if x < 700 and 30 < y < 385:  # keep the text column calm
        continue
    r = random.choice([0.6, 0.8, 1, 1.2, 1.6])
    delay = random.uniform(0, 4)
    dur = random.uniform(2.5, 6)
    w(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="#fff1d6" class="twinkle" '
      f'style="animation-delay:-{delay:.2f}s;animation-duration:{dur:.2f}s" />')

# Comet
w(f'<g class="comet"><line x1="1150" y1="20" x2="1230" y2="-12" stroke="url(#cometTail)" '
  f'stroke-width="2" stroke-linecap="round" transform="rotate(180 1150 20)" />'
  f'<circle cx="1150" cy="20" r="2.4" fill="{GOLD_HI}" /></g>')

# Orbits (back halves first so the sun covers them)
for rx, ry, _, _ in ORBITS:
    w(f'<ellipse cx="{SUN[0]}" cy="{SUN[1]}" rx="{rx}" ry="{ry}" fill="none" stroke="{GOLD}" '
      f'stroke-opacity=".5" stroke-dasharray="2 5" class="shimmer" />')

# Sun: the Solar Ram Studios mark, scaled up
sx, sy = SUN
w(f'<g class="rays-2" stroke="{GOLD_DIM}" stroke-linecap="round" stroke-opacity=".55">')
for k in range(24):
    a = math.radians(k * 15 + 7.5)
    w(f'<line x1="{sx + 40 * math.cos(a):.1f}" y1="{sy + 40 * math.sin(a):.1f}" '
      f'x2="{sx + 50 * math.cos(a):.1f}" y2="{sy + 50 * math.sin(a):.1f}" stroke-width="1.2" />')
w('</g>')
w(f'<g class="rays" stroke="{GOLD}" stroke-linecap="round">')
for k in range(8):
    a = math.radians(k * 45)
    w(f'<line x1="{sx + 36 * math.cos(a):.1f}" y1="{sy + 36 * math.sin(a):.1f}" '
      f'x2="{sx + 60 * math.cos(a):.1f}" y2="{sy + 60 * math.sin(a):.1f}" stroke-width="2" />')
w('</g>')
w(f'<circle cx="{sx}" cy="{sy}" r="33" fill="none" stroke="{GOLD_DIM}" stroke-width="1.2" />')
w(f'<circle cx="{sx}" cy="{sy}" r="26" fill="url(#core)" />')

# Planets: animateMotion keeps the labels upright as they orbit
for oi, (rx, ry, dur, apps) in enumerate(ORBITS):
    path = ellipse_path(rx, ry)
    n = len(apps)
    for ai, app in enumerate(apps):
        begin = -dur * ai / n - oi * 3.3
        color = PLANET_COLORS[(oi + ai) % len(PLANET_COLORS)]
        pr = 5 if oi == 0 else 4.5
        w(f'<g>')
        w(f'<animateMotion dur="{dur}s" begin="{begin:.2f}s" repeatCount="indefinite" path="{path}" />')
        w(f'<circle r="{pr + 5}" fill="{color}" fill-opacity=".14" />')
        w(f'<circle r="{pr}" fill="{color}" />')
        w(f'<text y="{-pr - 7}" text-anchor="middle" fill="{TEXT}" font-family="{MONO}" font-size="12" '
          f'stroke="{INK}" stroke-width="4" stroke-linejoin="round" paint-order="stroke">{app}</text>')
        w('</g>')

# --- Left column -------------------------------------------------------------
# Kicker with the studio mark
w(f'<g transform="translate(62 46)">'
  f'<rect width="28" height="28" rx="7" fill="#141411" stroke="{GOLD_DIM}" stroke-opacity=".6" />'
  f'<g stroke="#f2bd69" stroke-linecap="round" stroke-width="1.2">'
  f'<path d="M14 5v18M5 14h18M7.6 7.6l12.8 12.8M20.4 7.6 7.6 20.4" /></g>'
  f'<circle cx="14" cy="14" r="2.6" fill="#e8a845" /></g>')
w(f'<text x="102" y="65" fill="#cab18c" font-family="{MONO}" font-size="13" letter-spacing="3.5">'
  f'SOLAR RAM STUDIOS <tspan fill="{MUTED}">· IDEAS BUILT TO SHINE</tspan></text>')

w(f'<text x="58" y="146" fill="{TEXT}" font-family="{SANS}" font-size="66" font-weight="750" '
  f'letter-spacing="-2.5">Chase Struse<tspan fill="{GOLD}">.</tspan></text>')
w(f'<text x="62" y="188" fill="{TEXT2}" font-family="{SANS}" font-size="21">'
  f'Forging <tspan fill="{GOLD_HI}" font-weight="600">Solar Forge</tspan>: '
  f'local-first apps for Linux.</text>')

# Terminal card running a local model
tx, ty, tw, th = 62, 214, 548, 116
w(f'<rect x="{tx}" y="{ty}" width="{tw}" height="{th}" rx="14" fill="#141411" fill-opacity=".92" '
  f'stroke="#e3cfaa" stroke-opacity=".16" />')
w(f'<path d="M{tx} {ty + 32}h{tw}" stroke="#e3cfaa" stroke-opacity=".1" />')
for i, c in enumerate(["#e0715a", "#efbd6d", "#8fbf7a"]):
    w(f'<circle cx="{tx + 20 + i * 16}" cy="{ty + 16}" r="4.5" fill="{c}" fill-opacity=".85" />')
w(f'<text x="{tx + 76}" y="{ty + 21}" fill="{MUTED}" font-family="{MONO}" font-size="12">forge@omarchy: ~/solar-forge</text>')
# Token meter
w(f'<circle cx="{tx + tw - 132}" cy="{ty + 16}" r="3.5" fill="#8fbf7a" class="dot-live" />')
w(f'<text x="{tx + tw - 122}" y="{ty + 21}" fill="{MUTED}" font-family="{MONO}" font-size="11" letter-spacing="1">LOCAL LLM</text>')
for i in range(6):
    w(f'<rect x="{tx + tw - 48 + i * 6}" y="{ty + 8}" width="3.5" height="16" rx="1.5" fill="{GOLD}" '
      f'class="bar" style="animation-delay:-{(i * 0.37) % 1.1:.2f}s;animation-duration:{0.8 + (i % 3) * 0.25:.2f}s" />')

# Line 1: typed command
w(f'<text x="{tx + 18}" y="{ty + 62}" fill="{GOLD}" font-family="{MONO}" font-size="15">❯</text>')
w(f'<g clip-path="url(#type1)"><text x="96" y="{ty + 62}" fill="{TEXT}" font-family="{MONO}" font-size="15">'
  f'ollama run forge-assistant</text></g>')
w(f'<rect x="96" y="{ty + 49}" width="8" height="17" fill="{GOLD}" class="cursor">'
  f'<animate attributeName="x" dur="12s" repeatCount="indefinite" calcMode="discrete" '
  f'values="{";".join(str(96 + int(i * 9.1)) for i in range(0, 27))};{";".join(["-100"] * 26)};96" '
  f'keyTimes="{";".join(f"{i / 53 * 0.98:.4f}" for i in range(53))};1" /></rect>')

# Lines 2 & 3: model output fades in after typing, holds, resets with the loop
def reveal(begin_frac, text_svg, y):
    b = begin_frac
    w(f'<g opacity="0"><animate attributeName="opacity" dur="12s" repeatCount="indefinite" '
      f'values="0;0;1;1;0" keyTimes="0;{b:.3f};{b + 0.04:.3f};0.95;1" />'
      f'<text x="{tx + 18}" y="{y}" font-family="{MONO}" font-size="14">{text_svg}</text></g>')


reveal(0.52, f'<tspan fill="{GOLD}">☀</tspan><tspan fill="{TEXT2}"> model loaded · 100% on-device · </tspan>'
       f'<tspan fill="#8fbf7a">0 bytes to the cloud</tspan>', ty + 86)
reveal(0.64, f'<tspan fill="{MUTED}">›</tspan><tspan fill="{TEXT2}"> forging 11 apps across work, play &amp; Linux…</tspan>', ty + 106)

# Chips
chips = ["LOCAL-FIRST", "LOCAL LLMs", "PYTHON · QT · TAURI", "OMARCHY LINUX"]
cx = 62
for c in chips:
    cw = len(c) * 8.2 + 36
    w(f'<rect x="{cx}" y="346" width="{cw:.0f}" height="28" rx="14" fill="{GOLD}" fill-opacity=".07" '
      f'stroke="{GOLD}" stroke-opacity=".28" />')
    w(f'<circle cx="{cx + 14}" cy="360" r="3" fill="{GOLD}" />')
    w(f'<text x="{cx + 24}" y="364.5" fill="#e6cfa6" font-family="{MONO}" font-size="11.5" letter-spacing="1">{c}</text>')
    cx += cw + 10

w('</g></svg>')
sys.stdout.write("\n".join(out) + "\n")
