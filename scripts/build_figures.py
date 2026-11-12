"""Generate theme-adaptive .euclid-graphic SVG plates for D'Arcy Thompson's On Growth and Form (1917).

All 11 figures follow the GEOMETOR Digital Scriptorium .euclid-graphic contract:
- Standalone static SVGs in docsrc/_static/figures/ (zero py_file directives in treatise RST)
- Embedded light/dark CSS (@media (prefers-color-scheme: dark))
- Standard <defs> tick marks (#geom-tick-1..3) and arrow markers
- 3-vertex midpoint straight-segment paths (M x1 y1 L mx my L x2 y2) with data-ref attributes
"""

from __future__ import annotations

import html
import math
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent.parent / "docsrc" / "_static" / "figures"

PHI = (1.0 + math.sqrt(5.0)) / 2.0
GOLDEN_ANGLE = 2.0 * math.pi / (PHI * PHI)

STYLE_AND_DEFS = """  <style>
    .euclid-graphic {
      font-family: Georgia, 'Times New Roman', serif;
      --fg: #18181b;
      --fg-muted: #52525b;
      --grid: #a1a1aa;
      --panel-bg: #fafaf9;
      --accent-blue: #1d4ed8;
      --accent-amber: #b45309;
      --accent-green: #15803d;
      --accent-crimson: #b91c1c;
      --fill-soft: rgba(29, 78, 216, 0.08);
      --fill-gold: rgba(180, 83, 9, 0.11);
      --fill-green: rgba(21, 128, 61, 0.09);
    }
    @media (prefers-color-scheme: dark) {
      .euclid-graphic {
        --fg: #f4f4f5;
        --fg-muted: #a1a1aa;
        --grid: #52525b;
        --panel-bg: #18181b;
        --accent-blue: #60a5fa;
        --accent-amber: #fbbf24;
        --accent-green: #4ade80;
        --accent-crimson: #f87171;
        --fill-soft: rgba(96, 165, 250, 0.13);
        --fill-gold: rgba(251, 191, 36, 0.15);
        --fill-green: rgba(74, 222, 128, 0.13);
      }
    }
    .geom-line {
      stroke: var(--fg);
      stroke-width: 1.7;
      fill: none;
      stroke-linecap: round;
      stroke-linejoin: round;
      vector-effect: non-scaling-stroke;
    }
    .geom-aux {
      stroke: var(--fg-muted);
      stroke-width: 1.1;
      stroke-dasharray: 4 3;
      fill: none;
      vector-effect: non-scaling-stroke;
    }
    .geom-grid {
      stroke: var(--grid);
      stroke-width: 0.9;
      fill: none;
      vector-effect: non-scaling-stroke;
    }
    .geom-blue {
      stroke: var(--accent-blue);
      stroke-width: 2.0;
      fill: none;
      stroke-linecap: round;
      vector-effect: non-scaling-stroke;
    }
    .geom-amber {
      stroke: var(--accent-amber);
      stroke-width: 2.1;
      fill: none;
      stroke-linecap: round;
      vector-effect: non-scaling-stroke;
    }
    .geom-green {
      stroke: var(--accent-green);
      stroke-width: 1.9;
      fill: none;
      stroke-linecap: round;
      vector-effect: non-scaling-stroke;
    }
    .geom-crimson {
      stroke: var(--accent-crimson);
      stroke-width: 1.9;
      stroke-dasharray: 5 3;
      fill: none;
      stroke-linecap: round;
      vector-effect: non-scaling-stroke;
    }
    .geom-fill-soft { fill: var(--fill-soft); stroke: none; }
    .geom-fill-gold { fill: var(--fill-gold); stroke: none; }
    .geom-fill-green { fill: var(--fill-green); stroke: none; }
    .geom-pt { fill: var(--fg); stroke: none; }
    .geom-pt-amber { fill: var(--accent-amber); stroke: none; }
    .geom-pt-blue { fill: var(--accent-blue); stroke: none; }
    .geom-label {
      fill: var(--fg);
      font-size: 13px;
      font-style: italic;
    }
    .geom-note {
      fill: var(--fg-muted);
      font-size: 11.5px;
      font-style: normal;
    }
    .geom-title {
      fill: var(--fg);
      font-size: 13.5px;
      font-weight: bold;
      font-style: normal;
    }
  </style>
  <defs>
    <marker id="geom-tick-1" viewBox="-2 -6 4 12" markerWidth="4" markerHeight="12" orient="auto">
      <line x1="0" y1="-4.5" x2="0" y2="4.5" stroke="context-stroke" stroke-width="1.3"/>
    </marker>
    <marker id="geom-tick-2" viewBox="-4 -6 8 12" markerWidth="8" markerHeight="12" orient="auto">
      <line x1="-2" y1="-4.5" x2="-2" y2="4.5" stroke="context-stroke" stroke-width="1.3"/>
      <line x1="2" y1="-4.5" x2="2" y2="4.5" stroke="context-stroke" stroke-width="1.3"/>
    </marker>
    <marker id="geom-tick-3" viewBox="-6 -6 12 12" markerWidth="12" markerHeight="12" orient="auto">
      <line x1="-3.5" y1="-4.5" x2="-3.5" y2="4.5" stroke="context-stroke" stroke-width="1.3"/>
      <line x1="0" y1="-4.5" x2="0" y2="4.5" stroke="context-stroke" stroke-width="1.3"/>
      <line x1="3.5" y1="-4.5" x2="3.5" y2="4.5" stroke="context-stroke" stroke-width="1.3"/>
    </marker>
  </defs>"""


def fmt(val: float) -> str:
    """Format coordinate to 2 decimal places."""
    return f"{val:.2f}"


def seg(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    cls: str = "geom-line",
    ref: str = "",
    tick: int = 0,
) -> str:
    """Create a 3-vertex midpoint SVG path for straight segments."""
    mx, my = 0.5 * (x1 + x2), 0.5 * (y1 + y2)
    ref_attr = f' data-ref="{ref}"' if ref else ""
    tick_attr = f' marker-mid="url(#geom-tick-{tick})"' if tick else ""
    return (
        f'  <path class="{cls}"{ref_attr}{tick_attr} '
        f'd="M {fmt(x1)} {fmt(y1)} L {fmt(mx)} {fmt(my)} L {fmt(x2)} {fmt(y2)}"/>'
    )


def pt(x: float, y: float, r: float = 3.0, cls: str = "geom-pt", ref: str = "") -> str:
    """Render a geometric point dot."""
    ref_attr = f' data-ref="{ref}"' if ref else ""
    return f'  <circle class="{cls}"{ref_attr} cx="{fmt(x)}" cy="{fmt(y)}" r="{fmt(r)}"/>'


def label(
    x: float,
    y: float,
    text: str,
    cls: str = "geom-label",
    anchor: str = "middle",
    ref: str = "",
) -> str:
    """Render a crisp SVG text element."""
    ref_attr = f' data-ref="{html.escape(ref, quote=True)}"' if ref else ""
    return (
        f'  <text class="{cls}"{ref_attr} x="{fmt(x)}" y="{fmt(y)}" '
        f'text-anchor="{anchor}">{html.escape(text)}</text>'
    )


def poly(points: list[tuple[float, float]], cls: str = "geom-fill-soft", closed: bool = True) -> str:
    """Render a polygon or polyline path."""
    coords = " L ".join(f"{fmt(x)} {fmt(y)}" for x, y in points)
    suffix = " Z" if closed else ""
    return f'  <path class="{cls}" d="M {coords}{suffix}"/>'


def wrap_svg(width: int, height: int, body: list[str], aria_label: str) -> str:
    """Wrap body elements in a complete .euclid-graphic SVG document."""
    safe_aria = html.escape(aria_label, quote=True)
    lines = [
        (
            f'<svg class="euclid-graphic" viewBox="0 0 {width} {height}" '
            f'role="img" aria-label="{safe_aria}" xmlns="http://www.w3.org/2000/svg">'
        ),
        STYLE_AND_DEFS,
        *body,
        "</svg>",
        "",
    ]
    return "\n".join(lines)


def build_galileo_scaling() -> str:
    """Plate 1: Similitude and Galileo's Square-Cube Scaling Law (Ch. II)."""
    body: list[str] = [
        label(190, 26, "A. Geometrically Similar Cubes (L = 1, 2, 3)", "geom-title"),
        label(555, 26, "B. Surface S ~ L² vs. Mass V ~ L³", "geom-title"),
    ]
    # Three isometric cubes at L = 1, 2, 3
    unit = 24.0
    centers = [(62.0, 205.0, 1), (155.0, 205.0, 2), (295.0, 205.0, 3)]
    cos30 = math.cos(math.radians(30))
    sin30 = 0.5
    for cx, by, scale in centers:
        s = unit * scale
        p0 = (cx, by)
        p_r = (cx + s * cos30, by - s * sin30)
        p_l = (cx - s * cos30, by - s * sin30)
        p_t = (cx, by - s)
        p_tr = (cx + s * cos30, by - s - s * sin30)
        p_tl = (cx - s * cos30, by - s - s * sin30)
        p_top = (cx, by - 2.0 * s)
        body.append(poly([p_t, p_tr, p_top, p_tl], "geom-fill-gold"))
        body.append(poly([p0, p_r, p_tr, p_t], "geom-fill-soft"))
        # Subdivision grid lines on faces
        for k in range(1, scale):
            frac = k / scale
            # Vertical lines on right & left face
            rx1 = p0[0] + frac * (p_r[0] - p0[0])
            ry1 = p0[1] + frac * (p_r[1] - p0[1])
            body.append(seg(rx1, ry1, rx1, ry1 - s, "geom-grid"))
            lx1 = p0[0] + frac * (p_l[0] - p0[0])
            ly1 = p0[1] + frac * (p_l[1] - p0[1])
            body.append(seg(lx1, ly1, lx1, ly1 - s, "geom-grid"))
            # Horizontal lines
            body.append(seg(p0[0], p0[1] - frac * s, p_r[0], p_r[1] - frac * s, "geom-grid"))
            body.append(seg(p0[0], p0[1] - frac * s, p_l[0], p_l[1] - frac * s, "geom-grid"))
        for a, b in [
            (p0, p_r),
            (p0, p_l),
            (p0, p_t),
            (p_r, p_tr),
            (p_l, p_tl),
            (p_t, p_tr),
            (p_t, p_tl),
            (p_tr, p_top),
            (p_tl, p_top),
        ]:
            body.append(seg(a[0], a[1], b[0], b[1], "geom-line", f"cube_{scale}"))
        body.append(label(cx, 230, f"L = {scale}", "geom-label"))
        body.append(label(cx, 248, f"S = {6 * scale**2}, V = {scale**3}", "geom-note"))

    # Right panel: Coordinate plot x in [0, 3.2], y in [0, 28]
    ox, oy = 425.0, 222.0
    pw, ph = 265.0, 170.0
    body.append(seg(ox, oy, ox + pw, oy, "geom-line", "axis_L"))
    body.append(seg(ox, oy, ox, oy - ph, "geom-line", "axis_mag"))
    for k in range(1, 4):
        xk = ox + (k / 3.2) * pw
        body.append(seg(xk, oy, xk, oy - ph, "geom-grid"))
        body.append(label(xk, oy + 18, str(k), "geom-note"))
    body.append(label(ox + pw - 8, oy + 32, "Linear Scale L", "geom-note", "end"))

    # Curves: L^3 (amber), L^2 (blue), 9/L specific surface scaled (green)
    pts_v: list[tuple[float, float]] = []
    pts_s: list[tuple[float, float]] = []
    pts_r: list[tuple[float, float]] = []
    for i in range(65):
        lv = 3.1 * i / 64.0
        px = ox + (lv / 3.2) * pw
        pts_v.append((px, oy - (lv**3 / 30.0) * ph))
        pts_s.append((px, oy - (lv**2 / 30.0) * ph))
        if i >= 8:
            pts_r.append((px, oy - ((9.0 / lv) / 30.0) * ph))
    body.append(poly(pts_v, "geom-amber", closed=False))
    body.append(poly(pts_s, "geom-blue", closed=False))
    body.append(poly(pts_r, "geom-green", closed=False))
    for k in (1, 2, 3):
        xk = ox + (k / 3.2) * pw
        body.append(pt(xk, oy - (k**3 / 30.0) * ph, 3.2, "geom-pt-amber", f"V_{k}"))
        body.append(pt(xk, oy - (k**2 / 30.0) * ph, 3.2, "geom-pt-blue", f"S_{k}"))
    body.append(label(ox + 205, oy - 148, "V ~ L³ (Weight)", "geom-label", "start"))
    body.append(label(ox + 200, oy - 64, "S ~ L² (Strength)", "geom-label", "start"))
    body.append(label(ox + 56, oy - 142, "S / V ~ 1/L", "geom-note", "start"))
    return wrap_svg(730, 270, body, "Galileo square-cube law and geometric similitude")


def build_plateau_fermat_hex() -> str:
    """Plate 2: Plateau 120-degree Soap-Film Junction & Fermat Point X(13) (Ch. VII)."""
    body: list[str] = [
        label(185, 26, "A. Steiner–Fermat 120° Junction X(13)", "geom-title"),
        label(540, 26, "B. Hexagonal Cellular Equilibrium (s = 3/4)", "geom-title"),
    ]
    # Left panel: Equilateral triangle ABC + Fermat center F = X(13)
    cx, cy, rad = 185.0, 152.0, 96.0
    angles = [-90.0, 30.0, 150.0]
    verts = [
        (cx + rad * math.cos(math.radians(a)), cy + rad * math.sin(math.radians(a)))
        for a in angles
    ]
    pa, pb, pc = verts
    body.append(poly([pa, pb, pc], "geom-fill-soft"))
    body.append(seg(pa[0], pa[1], pb[0], pb[1], "geom-aux", "AB", tick=1))
    body.append(seg(pb[0], pb[1], pc[0], pc[1], "geom-aux", "BC", tick=1))
    body.append(seg(pc[0], pc[1], pa[0], pa[1], "geom-aux", "CA", tick=1))
    for vx, vy, ref in [(pa[0], pa[1], "FA"), (pb[0], pb[1], "FB"), (pc[0], pc[1], "FC")]:
        body.append(seg(cx, cy, vx, vy, "geom-amber", ref))
    # 120 degree angle arcs around F
    ar = 22.0
    for a1, a2 in [(-90, 30), (30, 150), (150, 270)]:
        x1 = cx + ar * math.cos(math.radians(a1))
        y1 = cy + ar * math.sin(math.radians(a1))
        x2 = cx + ar * math.cos(math.radians(a2))
        y2 = cy + ar * math.sin(math.radians(a2))
        body.append(
            f'  <path class="geom-blue" d="M {fmt(x1)} {fmt(y1)} '
            f'A {fmt(ar)} {fmt(ar)} 0 0 1 {fmt(x2)} {fmt(y2)}"/>'
        )
    body.append(pt(pa[0], pa[1], 3.2, "geom-pt", "A"))
    body.append(pt(pb[0], pb[1], 3.2, "geom-pt", "B"))
    body.append(pt(pc[0], pc[1], 3.2, "geom-pt", "C"))
    body.append(pt(cx, cy, 4.0, "geom-pt-amber", "X13"))
    body.append(label(pa[0], pa[1] - 10, "A", "geom-label", ref="A"))
    body.append(label(pb[0] + 14, pb[1] + 12, "B", "geom-label", ref="B"))
    body.append(label(pc[0] - 14, pc[1] + 12, "C", "geom-label", ref="C"))
    body.append(label(cx + 28, cy - 16, "120°", "geom-note"))
    body.append(label(cx, cy + 38, "P = X(13)", "geom-label", ref="X13"))
    body.append(label(185, 250, "Plateau's First Law: three films meet at 120°", "geom-note"))

    # Right panel: 7-cell hexagonal honeycomb cluster
    hcx, hcy, hr = 540.0, 142.0, 36.0
    offsets = [(0, 0)]
    for k in range(6):
        ang = math.radians(60 * k + 30)
        offsets.append((math.sqrt(3) * hr * math.cos(ang), math.sqrt(3) * hr * math.sin(ang)))
    drawn_edges: set[tuple[int, int, int, int]] = set()
    for idx, (dx, dy) in enumerate(offsets):
        mx, my = hcx + dx, hcy + dy
        hverts = [
            (mx + hr * math.cos(math.radians(60 * j)), my + hr * math.sin(math.radians(60 * j)))
            for j in range(6)
        ]
        body.append(poly(hverts, "geom-fill-gold" if idx == 0 else "geom-fill-soft"))
        for j in range(6):
            p1 = hverts[j]
            p2 = hverts[(j + 1) % 6]
            key = tuple(
                sorted([( round(p1[0]), round(p1[1]) ), ( round(p2[0]), round(p2[1]) )])
            )  # type: ignore[assignment]
            ekey = (key[0][0], key[0][1], key[1][0], key[1][1])  # type: ignore[index]
            if ekey not in drawn_edges:
                drawn_edges.add(ekey)
                body.append(seg(p1[0], p1[1], p2[0], p2[1], "geom-line"))
    # Highlight one triple vertex on central hexagon
    vx, vy = hcx + hr, hcy
    body.append(pt(vx, vy, 4.0, "geom-pt-amber", "V_hex"))
    body.append(label(540, 250, "Minimal perimeter partition (spread s = 3/4)", "geom-note"))
    return wrap_svg(730, 270, body, "Plateau 120-degree soap-film triple junction and honeycomb")


def build_maraldi_honeycomb() -> str:
    """Plate 3: Bee's Rhombic Dodecahedral Apex & Maraldi Angle (Ch. VII, Fig. 132)."""
    body: list[str] = [
        label(200, 26, "A. Hexagonal Cell & Trihedral Rhombic Cap", "geom-title"),
        label(555, 26, "B. Rhombus Face: cos θ = -1/3, s = 8/9", "geom-title"),
    ]
    # Isometric/oblique projection of hexagonal prism + 3-rhombus pyramidal cap (Thompson Fig. 132)
    def proj(x: float, y: float, z: float) -> tuple[float, float]:
        px = 195.0 + 68.0 * (x - 0.38 * y)
        py = 178.0 - 68.0 * (z - 0.30 * y)
        return (px, py)

    # Regular hexagon of radius 1 in xy-plane; prism base z = -0.95, rim alternates z = +/- h
    # Exact Maraldi geometry: h = 1 / (2 * sqrt(2)) relative to hexagon circumradius R = 1, apex z_v = 3*h?
    # Wait: for unit hex circumradius R=1: alternating rim vertices at z = +h and z = -h, apex at (0,0, +3h? No, +h_apex)
    # Let's check exact rhombic dodecahedron cap:
    # Base hexagon vertices at angle k*60 deg, r=1:
    # Alternating vertices: k=0,2,4 at z = h_low = 0; k=1,3,5 at z = d = 1/sqrt(2); apex V at (0,0, 3/(2*sqrt(2)))?
    # Let's verify vector edges from V(0,0, 1/sqrt(2)) to k=1 (cos60, sin60, 0)?
    # Even simpler: V = (0, 0, 1/sqrt(2)), B_even (k=0,2,4) at z = 0: |B_even - V|^2 = 1 + 1/2 = 3/2!
    # Then 4th vertex of rhombus between k=0 and k=2 is D_1 = B_0 + B_2 - V = (1 - 1/2, sqrt(3)/2, -1/sqrt(2)) = (sqrt(3)*cos30... wait: |(1/2, sqrt(3)/2)| = 1, z = -1/sqrt(2))!
    # Check edge lengths of rhombus (V, B_0, D_1, B_2):
    # V - B_0 = (-1, 0, 1/sqrt(2)) -> Q = 1 + 1/2 = 3/2.
    # V - B_2 = (1/2, -sqrt(3)/2, 1/sqrt(2)) -> Q = 1/4 + 3/4 + 1/2 = 3/2!
    # Dot product (V - B_0).(V - B_2) = -1/2 + 0 + 1/2? Wait: B_0=(1,0,0), B_2=(-1/2, sqrt(3)/2, 0):
    # V - B_0 = (-1, 0, 1/sqrt(2)), V - B_2 = (1/2, -sqrt(3)/2, 1/sqrt(2)):
    # dot = -1/2 + 0 + 1/2 = 0?! Wait: if z_V = 1/(2*sqrt(2)):
    # Q(V - B_0) = 1 + 1/8 = 9/8!
    # dot(B_0 - V, B_2 - V) = (1)(-1/2) + 0 + (1/8) = -3/8!
    # cos(angle B_0 V B_2) = (-3/8) / (9/8) = -1/3!! EXACT!! 109 deg 28' 16''!
    s2 = math.sqrt(2.0)
    zv = 1.0 / (2.0 * s2)
    z_base = -1.15
    rim: list[tuple[float, float, float]] = []
    base: list[tuple[float, float, float]] = []
    for k in range(6):
        ang = math.radians(60 * k - 15)
        xk, yk = math.cos(ang), math.sin(ang)
        zk = 0.0 if k % 2 == 0 else -2.0 * zv
        rim.append((xk, yk, zk + 0.55))
        base.append((xk, yk, z_base))
    apex3 = (0.0, 0.0, zv + 0.55)

    v2 = proj(*apex3)
    rim2 = [proj(*p) for p in rim]
    base2 = [proj(*p) for p in base]

    # Shade the three top rhombi: (V, R0, R1, R2), (V, R2, R3, R4), (V, R4, R5, R0)
    body.append(poly([v2, rim2[0], rim2[1], rim2[2]], "geom-fill-gold"))
    body.append(poly([v2, rim2[2], rim2[3], rim2[4]], "geom-fill-soft"))
    body.append(poly([v2, rim2[4], rim2[5], rim2[0]], "geom-fill-green"))

    # Back prism edges dashed, front solid
    for k in range(6):
        cls = "geom-aux" if k in (2, 3) else "geom-line"
        body.append(seg(rim2[k][0], rim2[k][1], base2[k][0], base2[k][1], cls))
        bcls = "geom-aux" if k in (1, 2, 3) else "geom-line"
        nk = (k + 1) % 6
        body.append(seg(base2[k][0], base2[k][1], base2[nk][0], base2[nk][1], bcls))

    # Rim edges and apex ridges
    for k in range(6):
        nk = (k + 1) % 6
        body.append(seg(rim2[k][0], rim2[k][1], rim2[nk][0], rim2[nk][1], "geom-line"))
    for k in (0, 2, 4):
        body.append(seg(v2[0], v2[1], rim2[k][0], rim2[k][1], "geom-amber", f"ridge_{k}"))
    body.append(pt(v2[0], v2[1], 3.8, "geom-pt-amber", "V"))
    body.append(label(v2[0], v2[1] - 11, "V", "geom-label", ref="V"))
    body.append(label(195, 260, "Three rhombi replace flat hexagonal roof", "geom-note"))

    # Right panel: True-shape Maraldi rhombus (diagonals in ratio 1 : sqrt(2))
    rcx, rcy = 555.0, 138.0
    dx = 64.0
    dy = dx * math.sqrt(2.0)  # half-diagonals: tan(theta/2) = sqrt(2) -> obtuse angle 109.47 deg!
    p_top = (rcx, rcy - dy)
    p_bot = (rcx, rcy + dy)
    p_left = (rcx - dx, rcy)
    p_right = (rcx + dx, rcy)
    body.append(poly([p_top, p_right, p_bot, p_left], "geom-fill-gold"))
    body.append(seg(p_top[0], p_top[1], p_right[0], p_right[1], "geom-line", "rh1", tick=1))
    body.append(seg(p_right[0], p_right[1], p_bot[0], p_bot[1], "geom-line", "rh2", tick=1))
    body.append(seg(p_bot[0], p_bot[1], p_left[0], p_left[1], "geom-line", "rh3", tick=1))
    body.append(seg(p_left[0], p_left[1], p_top[0], p_top[1], "geom-line", "rh4", tick=1))
    body.append(seg(p_left[0], p_left[1], p_right[0], p_right[1], "geom-blue", "diag_short"))
    body.append(seg(p_top[0], p_top[1], p_bot[0], p_bot[1], "geom-aux", "diag_long"))
    for px, py in [p_top, p_right, p_bot, p_left]:
        body.append(pt(px, py, 3.2, "geom-pt"))
    body.append(label(p_left[0] - 14, p_left[1] + 4, "V", "geom-label"))
    body.append(label(p_left[0] + 34, p_left[1] - 10, "109°28′", "geom-note"))
    body.append(label(p_top[0] + 28, p_top[1] + 26, "70°32′", "geom-note"))
    body.append(label(555, 246, "Diagonal ratio 1 : √2  |  Rational spread s = 8/9", "geom-note"))
    return wrap_svg(730, 275, body, "Maraldi honeycomb rhombic cap and 109 degree 28 minute rhombus")


def build_kelvin_tetrakaidecahedron() -> str:
    """Plate 4: Plateau Central Cube Film & Kelvin Tetrakaidecahedron (Ch. VII, Fig. 134)."""
    body: list[str] = [
        label(180, 26, "A. Plateau's Wire Cube Film (Fig. 134)", "geom-title"),
        label(545, 26, "B. Kelvin's Tetrakaidecahedron (8 Hex + 6 Sq)", "geom-title"),
    ]

    def proj_cube(x: float, y: float, z: float) -> tuple[float, float]:
        return (180.0 + 66.0 * (x + 0.34 * y), 144.0 - 66.0 * (z + 0.26 * y))

    cverts = [
        proj_cube(sx, sy, sz)
        for sz in (-1, 1)
        for sy in (-1, 1)
        for sx in (-1, 1)
    ]
    cube_edges = [
        (0, 1), (2, 3), (4, 5), (6, 7),
        (0, 2), (1, 3), (4, 6), (5, 7),
        (0, 4), (1, 5), (2, 6), (3, 7),
    ]
    for i, j in cube_edges:
        body.append(seg(cverts[i][0], cverts[i][1], cverts[j][0], cverts[j][1], "geom-line"))
    # Central square soap lamina in xy-plane (s = 0.28)
    s_lam = 0.30
    lam = [
        proj_cube(-s_lam, -s_lam, 0),
        proj_cube(s_lam, -s_lam, 0),
        proj_cube(s_lam, s_lam, 0),
        proj_cube(-s_lam, s_lam, 0),
    ]
    body.append(poly(lam, "geom-fill-gold"))
    for k in range(4):
        nk = (k + 1) % 4
        body.append(seg(lam[k][0], lam[k][1], lam[nk][0], lam[nk][1], "geom-amber", ref=f"lamina_{k}"))
        body.append(pt(lam[k][0], lam[k][1], 3.0, "geom-pt-amber", ref=f"L_{k}"))
    # Connect lamina corners to cube corners (12 trapezoidal/triangular films)
    corner_map = [(0, 0), (0, 4), (1, 1), (1, 5), (2, 3), (2, 7), (3, 2), (3, 6)]
    for lk, ck in corner_map:
        body.append(seg(lam[lk][0], lam[lk][1], cverts[ck][0], cverts[ck][1], "geom-blue", ref=f"film_{lk}_{ck}"))
    body.append(label(180, 254, "Unstable 8-ray vertex splits into central lamina", "geom-note"))

    # Right panel: Truncated octahedron = permutations of (0, +/-1, +/-2)
    raw_verts: list[tuple[float, float, float]] = []
    for a in (-1.0, 1.0):
        for b in (-2.0, 2.0):
            raw_verts.extend([(0.0, a, b), (a, 0.0, b), (a, b, 0.0)])
            raw_verts.extend([(0.0, b, a), (b, 0.0, a), (b, a, 0.0)])
    # Deduplicate
    verts3 = sorted(set(raw_verts))

    # Rotate nicely so both square and hexagonal faces show clearly
    ry, rx = math.radians(26.0), math.radians(20.0)
    rot_verts: list[tuple[float, float, float]] = []
    for x, y, z in verts3:
        x1 = x * math.cos(ry) + z * math.sin(ry)
        z1 = -x * math.sin(ry) + z * math.cos(ry)
        y2 = y * math.cos(rx) - z1 * math.sin(rx)
        z2 = y * math.sin(rx) + z1 * math.cos(rx)
        rot_verts.append((x1, y2, z2))

    scale_k = 40.0
    p2d = [(545.0 + scale_k * x, 142.0 - scale_k * y) for x, y, _ in rot_verts]

    # Highlight front z=+2 square face and front (+,+,+) hexagon face
    sq_idx = [i for i, v in enumerate(verts3) if v[2] == 2.0]
    # Order around centroid
    cx_s = sum(p2d[i][0] for i in sq_idx) / 4.0
    cy_s = sum(p2d[i][1] for i in sq_idx) / 4.0
    sq_idx.sort(key=lambda i: math.atan2(p2d[i][1] - cy_s, p2d[i][0] - cx_s))
    body.append(poly([p2d[i] for i in sq_idx], "geom-fill-gold"))

    hex_idx = [i for i, v in enumerate(verts3) if v[0] >= 0 and v[1] >= 0 and v[2] >= 0]
    cx_h = sum(p2d[i][0] for i in hex_idx) / 6.0
    cy_h = sum(p2d[i][1] for i in hex_idx) / 6.0
    hex_idx.sort(key=lambda i: math.atan2(p2d[i][1] - cy_h, p2d[i][0] - cx_h))
    body.append(poly([p2d[i] for i in hex_idx], "geom-fill-soft"))

    # Edges have squared Euclidean length = 2
    n_v = len(verts3)
    for i in range(n_v):
        for j in range(i + 1, n_v):
            d2 = sum((verts3[i][m] - verts3[j][m]) ** 2 for m in range(3))
            if abs(d2 - 2.0) < 1e-6:
                front = (rot_verts[i][2] + rot_verts[j][2]) >= -0.35
                cls = "geom-line" if front else "geom-aux"
                body.append(seg(p2d[i][0], p2d[i][1], p2d[j][0], p2d[j][1], cls))
    body.append(label(545, 254, "Space-filling minimal foam: 24 vertices, 36 edges", "geom-note"))
    return wrap_svg(730, 275, body, "Plateau wire cube soap film and Kelvin tetrakaidecahedron")


def build_hambidge_root_rectangles() -> str:
    """Plate 5: Hambidge Dynamic Symmetry Root Rectangles & Reciprocal (Unit 7)."""
    body: list[str] = [
        label(220, 26, "A. Root-Rectangle Unfolding (Q = 1, 2, 3, 4, 5)", "geom-title"),
        label(580, 26, "B. Orthogonal Diagonal of the Reciprocal", "geom-title"),
    ]
    ox, oy = 48.0, 218.0
    u = 148.0  # unit height = 1
    body.append(poly([(ox, oy - u), (ox + u * math.sqrt(5), oy - u), (ox + u * math.sqrt(5), oy), (ox, oy)], "geom-fill-soft"))
    body.append(poly([(ox, oy - u), (ox + u, oy - u), (ox + u, oy), (ox, oy)], "geom-fill-gold"))

    # Outer baseline & top line
    max_x = ox + u * math.sqrt(5.0)
    body.append(seg(ox, oy, max_x, oy, "geom-line", "base"))
    body.append(seg(ox, oy - u, max_x, oy - u, "geom-line", "top"))
    body.append(seg(ox, oy, ox, oy - u, "geom-line", "left_unit"))

    for n in range(1, 6):
        rn = math.sqrt(float(n))
        xn = ox + u * rn
        body.append(seg(xn, oy, xn, oy - u, "geom-line", f"end_root_{n}"))
        # Diagonal of root-n rectangle (from bottom-left to top-right of root-n)
        if n <= 4:
            diag_r = u * math.sqrt(float(n + 1))
            tx, ty = xn, oy - u
            bx = ox + diag_r
            body.append(seg(ox, oy, tx, ty, "geom-blue", f"diag_{n}"))
            # Compass arc dropping diagonal length onto baseline
            body.append(
                f'  <path class="geom-amber" d="M {fmt(tx)} {fmt(ty)} '
                f'A {fmt(diag_r)} {fmt(diag_r)} 0 0 1 {fmt(bx)} {fmt(oy)}"/>'
            )
        lbl = "1" if n == 1 else ("2 (√4)" if n == 4 else f"√{n}")
        body.append(label(xn, oy + 18, lbl, "geom-label"))
        body.append(pt(xn, oy, 2.8, "geom-pt"))
    body.append(label(ox - 12, oy - u / 2.0, "1", "geom-label"))
    body.append(label(220, 256, "Incommensurable in length, commensurable in square (Euclid X)", "geom-note"))

    # Right panel: Root-2 or Golden rectangle with reciprocal rectangle & perpendicular diagonals
    rx, ry = 468.0, 214.0
    rh = 140.0
    rw = rh * PHI
    rec_w = rh / PHI  # reciprocal width = 1/phi of height -> diagonal perpendicular!
    body.append(poly([(rx, ry - rh), (rx + rw, ry - rh), (rx + rw, ry), (rx, ry)], "geom-fill-soft"))
    body.append(poly([(rx, ry - rh), (rx + rec_w, ry - rh), (rx + rec_w, ry), (rx, ry)], "geom-fill-gold"))
    body.append(seg(rx, ry, rx + rw, ry, "geom-line"))
    body.append(seg(rx, ry - rh, rx + rw, ry - rh, "geom-line"))
    body.append(seg(rx, ry, rx, ry - rh, "geom-line"))
    body.append(seg(rx + rw, ry, rx + rw, ry - rh, "geom-line"))
    body.append(seg(rx + rec_w, ry, rx + rec_w, ry - rh, "geom-green", "recip_cut"))
    # Main diagonal A(rx, ry) -> B(rx+rw, ry-rh); Reciprocal diagonal C(rx, ry-rh) -> D(rx+rec_w, ry)
    body.append(seg(rx, ry, rx + rw, ry - rh, "geom-blue", "diag_whole"))
    body.append(seg(rx, ry - rh, rx + rec_w, ry, "geom-amber", "diag_recip"))
    # Exact intersection E:
    # Line 1: (rx + t*rw, ry - t*rh); Line 2: (rx + s*rec_w, ry - rh + s*rh)
    # t + s = 1 and t*rw = s*rec_w -> t * phi^2 = 1 - t -> t = 1/(1 + phi^2) = 1/(2 + phi)
    t_int = 1.0 / (1.0 + PHI * PHI)
    ex, ey = rx + t_int * rw, ry - t_int * rh
    # Right-angle square marker at E
    ux, uy = rw / math.hypot(rw, rh), -rh / math.hypot(rw, rh)
    vx, vy = rec_w / math.hypot(rec_w, rh), rh / math.hypot(rec_w, rh)
    ms = 9.0
    p_ra1 = (ex + ms * ux, ey + ms * uy)
    p_ra2 = (ex + ms * (ux + vx), ey + ms * (uy + vy))
    p_ra3 = (ex + ms * vx, ey + ms * vy)
    body.append(poly([p_ra1, p_ra2, p_ra3], "geom-line", closed=False))
    body.append(pt(ex, ey, 3.5, "geom-pt-amber", "E"))
    body.append(label(rx - 10, ry + 4, "A", "geom-label"))
    body.append(label(rx + rw + 10, ry - rh + 4, "B", "geom-label"))
    body.append(label(rx - 10, ry - rh + 4, "C", "geom-label"))
    body.append(label(rx + rec_w, ry + 16, "D", "geom-label"))
    body.append(label(ex + 15, ey + 5, "E (90°)", "geom-note", "start"))
    body.append(label(580, 256, "Reciprocal diagonal CD cuts whole diagonal AB at 90°", "geom-note"))
    return wrap_svg(740, 275, body, "Hambidge root rectangles and orthogonal reciprocal diagonal")


def build_golden_gnomon_spiral() -> str:
    """Plate 6: Whirling-Square Golden Gnomon & Euclid IV.10 Golden Triangle (Ch. XI, Figs. 252, 254)."""
    body: list[str] = [
        label(215, 26, "A. Whirling-Square Golden Gnomons (Fig. 252)", "geom-title"),
        label(575, 26, "B. Euclid IV.10 Golden Triangle 36°–72°–72° (Fig. 254)", "geom-title"),
    ]
    # Left panel: Golden rectangle subdivided into 6 whirling squares + quarter-circle / exact log spiral
    rx, ry = 55.0, 48.0
    rh = 178.0
    rw = rh * PHI
    body.append(poly([(rx, ry), (rx + rw, ry), (rx + rw, ry + rh), (rx, ry + rh)], "geom-fill-soft"))

    # Iteratively slice squares clockwise: left, top, right, bottom...
    x0, y0, w0, h0 = rx, ry, rw, rh
    arc_cmds: list[str] = []
    for step in range(7):
        direction = step % 4
        if direction == 0:  # square on left of width h0
            s = h0
            if step == 0:
                body.append(poly([(x0, y0), (x0 + s, y0), (x0 + s, y0 + s), (x0, y0 + s)], "geom-fill-gold"))
            body.append(seg(x0 + s, y0, x0 + s, y0 + s, "geom-grid"))
            arc_cmds.append(
                f"M {fmt(x0)} {fmt(y0 + s)} A {fmt(s)} {fmt(s)} 0 0 1 {fmt(x0 + s)} {fmt(y0)}"
            )
            x0 += s
            w0 -= s
        elif direction == 1:  # square on top of height w0
            s = w0
            body.append(seg(x0, y0 + s, x0 + s, y0 + s, "geom-grid"))
            arc_cmds.append(
                f"M {fmt(x0)} {fmt(y0)} A {fmt(s)} {fmt(s)} 0 0 1 {fmt(x0 + s)} {fmt(y0 + s)}"
            )
            y0 += s
            h0 -= s
        elif direction == 2:  # square on right of width h0
            s = h0
            body.append(seg(x0 + w0 - s, y0, x0 + w0 - s, y0 + s, "geom-grid"))
            arc_cmds.append(
                f"M {fmt(x0 + w0)} {fmt(y0)} A {fmt(s)} {fmt(s)} 0 0 1 {fmt(x0 + w0 - s)} {fmt(y0 + s)}"
            )
            w0 -= s
        else:  # square on bottom of height w0
            s = w0
            body.append(seg(x0, y0 + h0 - s, x0 + s, y0 + h0 - s, "geom-grid"))
            arc_cmds.append(
                f"M {fmt(x0 + s)} {fmt(y0 + h0)} A {fmt(s)} {fmt(s)} 0 0 1 {fmt(x0)} {fmt(y0 + h0 - s)}"
            )
            h0 -= s

    body.append(seg(rx, ry, rx + rw, ry, "geom-line"))
    body.append(seg(rx + rw, ry, rx + rw, ry + rh, "geom-line"))
    body.append(seg(rx + rw, ry + rh, rx, ry + rh, "geom-line"))
    body.append(seg(rx, ry + rh, rx, ry, "geom-line"))
    # Perpendicular diagonals locating the pole O
    body.append(seg(rx, ry + rh, rx + rw, ry, "geom-aux", "diag1"))
    body.append(seg(rx + rh, ry, rx + rw, ry + rh, "geom-aux", "diag2"))
    for ac in arc_cmds:
        body.append(f'  <path class="geom-amber" d="{ac}"/>')
    # Pole intersection of (rx, ry+rh)->(rx+rw, ry) and (rx+rh, ry)->(rx+rw, ry+rh)
    # Parametric: t = phi / (phi + 1/phi) = phi^2 / (phi^2 + 1)
    tp = (PHI * PHI) / (PHI * PHI + 1.0)
    px_pole = rx + tp * rw
    py_pole = ry + rh - tp * rh
    body.append(pt(px_pole, py_pole, 3.6, "geom-pt-blue", "O"))
    body.append(label(px_pole + 14, py_pole - 8, "O", "geom-label", ref="O"))
    body.append(label(200, 252, "Square gnomons leave self-similar φ rectangles", "geom-note"))

    # Right panel: Golden isosceles triangle ABC (36-72-72) recursively subdivided
    base_w = 128.0
    leg = base_w * PHI
    tri_h = math.sqrt(leg * leg - (0.5 * base_w) ** 2)
    pb_t = (510.0, 224.0)
    pc_t = (510.0 + base_w, 224.0)
    pa_t = (510.0 + 0.5 * base_w, 224.0 - tri_h)
    body.append(poly([pa_t, pb_t, pc_t], "geom-fill-soft"))

    # Recursive bisectors: D divides AC in golden ratio from C: AD : DC = phi : 1 -> D = A + (phi/(1+phi))*(C-A) = A + (1/phi)*(C-A)
    cur_a, cur_b, cur_c = pa_t, pb_t, pc_t
    tri_verts = [pa_t, pb_t, pc_t]
    for step in range(5):
        nx = cur_a[0] + (cur_c[0] - cur_a[0]) / PHI
        ny = cur_a[1] + (cur_c[1] - cur_a[1]) / PHI
        nd = (nx, ny)
        if step == 0:
            body.append(poly([cur_a, cur_b, nd], "geom-fill-gold"))
        body.append(seg(cur_b[0], cur_b[1], nd[0], nd[1], "geom-blue", f"bisect_{step}"))
        body.append(pt(nd[0], nd[1], 2.8, "geom-pt"))
        tri_verts.append(nd)
        cur_a, cur_b, cur_c = cur_b, nd, cur_a

    body.append(seg(pa_t[0], pa_t[1], pb_t[0], pb_t[1], "geom-line", "AB"))
    body.append(seg(pb_t[0], pb_t[1], pc_t[0], pc_t[1], "geom-line", "BC"))
    body.append(seg(pc_t[0], pc_t[1], pa_t[0], pa_t[1], "geom-line", "CA"))
    body.append(label(pa_t[0], pa_t[1] - 8, "A (36°)", "geom-label"))
    body.append(label(pb_t[0] - 16, pb_t[1] + 4, "B (72°)", "geom-label"))
    body.append(label(pc_t[0] + 18, pc_t[1] + 4, "C (72°)", "geom-label"))
    body.append(label(575, 252, "Obtuse 108° gnomon + similar 36°–72°–72° triangle", "geom-note"))
    return wrap_svg(740, 272, body, "Whirling-square golden gnomon and Euclid IV.10 golden triangle")


def build_nautilus_chambered_spiral() -> str:
    """Plate 7: Chambered Nautilus Equiangular Spiral r = a e^(theta cot alpha) (Ch. XI)."""
    body: list[str] = [
        label(365, 26, "The Equiangular Spiral of Nautilus: r = a e^(θ cot α), Constant Tangent Angle α", "geom-title"),
    ]
    cx, cy = 355.0, 156.0
    cot_alpha = 0.185  # alpha ~ 79.5 deg (realistic Nautilus pompilius whorl expansion ~3.2 per turn)
    a0 = 3.2

    # Polar grid rays every 30 deg
    max_theta = 5.65 * math.pi
    for deg in range(0, 360, 30):
        rad = math.radians(deg)
        body.append(seg(cx, cy, cx + 118.0 * math.cos(rad), cy + 118.0 * math.sin(rad), "geom-grid"))

    # Spiral curve
    spiral_pts: list[tuple[float, float]] = []
    steps = 340
    for i in range(steps + 1):
        th = max_theta * i / steps
        r = a0 * math.exp(cot_alpha * th)
        spiral_pts.append((cx + r * math.cos(th), cy - r * math.sin(th)))

    # Concave chamber septa between theta and theta - 2*pi
    d_septa = math.pi / 8.0
    th = 2.2 * math.pi
    while th <= max_theta - 0.05:
        r_out = a0 * math.exp(cot_alpha * th)
        r_in = a0 * math.exp(cot_alpha * (th - 2.0 * math.pi))
        p_out = (cx + r_out * math.cos(th), cy - r_out * math.sin(th))
        p_in = (cx + r_in * math.cos(th), cy - r_in * math.sin(th))
        # Curved septum concave toward aperture
        rmid = 0.52 * (r_out + r_in)
        th_back = th - 0.16
        ctrl = (cx + rmid * math.cos(th_back), cy - rmid * math.sin(th_back))
        body.append(
            f'  <path class="geom-blue" d="M {fmt(p_in[0])} {fmt(p_in[1])} '
            f'Q {fmt(ctrl[0])} {fmt(ctrl[1])} {fmt(p_out[0])} {fmt(p_out[1])}"/>'
        )
        th += d_septa

    body.append(poly(spiral_pts, "geom-amber", closed=False))
    body.append(pt(cx, cy, 3.5, "geom-pt", "O"))

    # Show constant tangent angle alpha at theta_mark = 5.22 * pi (upper-left / right)
    th_m = 4.22 * math.pi  # around +39.6 deg (upper-right!)
    rm = a0 * math.exp(cot_alpha * th_m)
    px = cx + rm * math.cos(th_m)
    py = cy - rm * math.sin(th_m)
    body.append(seg(cx, cy, px, py, "geom-green", "radius_vector"))
    # Tangent vector d/dth (cx + r cos th, cy - r sin th):
    tx_v = cot_alpha * math.cos(th_m) - math.sin(th_m)
    ty_v = -cot_alpha * math.sin(th_m) - math.cos(th_m)
    tnorm = math.hypot(tx_v, ty_v)
    tx_v, ty_v = tx_v / tnorm, ty_v / tnorm
    body.append(
        seg(px - 36 * tx_v, py - 36 * ty_v, px + 48 * tx_v, py + 48 * ty_v, "geom-crimson", "tangent")
    )
    body.append(pt(px, py, 3.8, "geom-pt-amber", "P"))
    body.append(label(px + 16, py - 8, "P (∠OPT = α ≈ 80°)", "geom-label", "start"))
    body.append(label(cx - 12, cy + 14, "O", "geom-label"))
    body.append(
        label(
            365,
            274,
            "Bernoulli's Spira mirabilis: growth at aperture preserves unchanging form (Eadem mutata resurgo)",
            "geom-note",
        )
    )
    return wrap_svg(730, 290, body, "Chambered Nautilus logarithmic spiral and constant tangent angle")


def build_phyllotaxis_parastichy() -> str:
    """Plate 8: Cylindrical & Planar (5, 8) / (8, 13) Fibonacci Parastichy Lattice (Ch. XIV)."""
    body: list[str] = [
        label(185, 26, "A. Cylindrical Bravais–Tait Lattice (Fig. 325)", "geom-title"),
        label(548, 26, "B. Apical Capitulum: (8, 13) Parastichies", "geom-title"),
    ]
    # Left panel: Unwrapped cylinder x in [0, 1] -> [55, 315], y = plastochrone rise n
    lx, ly, lw, lh = 55.0, 228.0, 260.0, 172.0
    body.append(poly([(lx, ly - lh), (lx + lw, ly - lh), (lx + lw, ly), (lx, ly)], "geom-fill-soft"))
    body.append(seg(lx, ly, lx + lw, ly, "geom-line"))
    body.append(seg(lx, ly - lh, lx + lw, ly - lh, "geom-grid"))
    body.append(seg(lx, ly, lx, ly - lh, "geom-aux"))
    body.append(seg(lx + lw, ly, lx + lw, ly - lh, "geom-aux"))

    n_cyl = 22
    div_frac = 1.0 / (PHI * PHI)  # 0.381966...
    cyl_pts: dict[int, tuple[float, float]] = {}
    for n in range(n_cyl):
        u_pos = (n * div_frac) % 1.0
        px = lx + u_pos * lw
        py = ly - (n + 0.8) * (lh / (n_cyl + 0.8))
        cyl_pts[n] = (px, py)

    # Connect parastichies +5 (blue) and +8 (amber) when they don't wrap across seam
    for n in range(n_cyl):
        if n + 5 < n_cyl and abs(cyl_pts[n + 5][0] - cyl_pts[n][0]) < 0.5 * lw:
            body.append(
                seg(cyl_pts[n][0], cyl_pts[n][1], cyl_pts[n + 5][0], cyl_pts[n + 5][1], "geom-blue")
            )
        if n + 8 < n_cyl and abs(cyl_pts[n + 8][0] - cyl_pts[n][0]) < 0.5 * lw:
            body.append(
                seg(cyl_pts[n][0], cyl_pts[n][1], cyl_pts[n + 8][0], cyl_pts[n + 8][1], "geom-amber")
            )
    for n, (px, py) in cyl_pts.items():
        body.append(pt(px, py, 3.0, "geom-pt", f"leaf_{n}"))
        if n in (0, 1, 2, 3, 5, 8, 13):
            body.append(label(px + 9, py + 3, str(n), "geom-note", "start"))
    body.append(label(185, 254, "Divergence Δθ = 360°/φ² ≈ 137°30′28″", "geom-note"))

    # Right panel: Planar Vogel/Church sunflower disc with 8-arm and 13-arm parastichies
    dcx, dcy = 548.0, 142.0
    n_seeds = 98
    c_scale = 9.4
    seeds: list[tuple[float, float]] = []
    for n in range(1, n_seeds + 1):
        r = c_scale * math.sqrt(float(n))
        th = n * GOLDEN_ANGLE
        seeds.append((dcx + r * math.cos(th), dcy - r * math.sin(th)))

    # Draw all 8-parastichies (blue) and 13-parastichies (amber)
    for arm in range(8):
        pts8 = [seeds[idx] for idx in range(arm, n_seeds, 8)]
        if len(pts8) >= 2:
            body.append(poly(pts8, "geom-blue", closed=False))
    for arm in range(13):
        pts13 = [seeds[idx] for idx in range(arm, n_seeds, 13)]
        if len(pts13) >= 2:
            body.append(poly(pts13, "geom-amber", closed=False))
    for px, py in seeds:
        body.append(pt(px, py, 2.3, "geom-pt"))
    body.append(label(548, 254, "Intersecting Fibonacci parastichy families (8, 13)", "geom-note"))
    return wrap_svg(730, 272, body, "Cylindrical and apical Fibonacci phyllotaxis parastichy lattices")


def build_culmann_femur_trajectories() -> str:
    """Plate 9: Culmann's Crane & Meyer's Orthogonal Femur Trajectories (Ch. XVI, Fig. 335)."""
    body: list[str] = [
        label(185, 26, "A. Culmann's Fairbairn Crane", "geom-title"),
        label(535, 26, "B. Meyer's Trabecular Arch in Human Femur", "geom-title"),
    ]

    # Helper mapping (u, s) in [0,1]x[-1,1] along a curved cantilever spine
    def crane_pt(u: float, s: float, ox: float, neck_bend: float) -> tuple[float, float]:
        # u=0 at base shaft, u=1 at overhanging head
        if u < 0.45:
            t = u / 0.45
            cx = ox
            cy = 232.0 - 105.0 * t
            hw = 22.0 - 3.0 * t
            nx, ny = 1.0, 0.0
        else:
            t = (u - 0.45) / 0.55
            ang = math.radians(neck_bend * t)
            rad = 78.0
            cx = ox + rad * (1.0 - math.cos(ang))
            cy = 127.0 - rad * math.sin(ang)
            hw = 19.0 - 4.0 * t + (6.0 * math.sin(math.pi * t) if neck_bend > 95 else 0.0)
            nx, ny = math.cos(ang), -math.sin(ang)
        return (cx + s * hw * nx, cy + s * hw * ny)

    for panel_idx, (ox, bend, is_femur) in enumerate([(152.0, 92.0, False), (502.0, 108.0, True)]):
        outer = [crane_pt(i / 40.0, -1.0, ox, bend) for i in range(41)]
        inner = [crane_pt(i / 40.0, 1.0, ox, bend) for i in range(40, -1, -1)]
        body.append(poly(outer + inner, "geom-fill-soft"))
        body.append(poly(outer, "geom-line", closed=False))
        body.append(poly(inner, "geom-line", closed=False))
        # Base & tip cap
        body.append(seg(outer[0][0], outer[0][1], inner[-1][0], inner[-1][1], "geom-line"))
        if is_femur:
            # Greater trochanter prominence & rounded femoral head cap
            htip1 = outer[-1]
            htip2 = inner[0]
            hmid = (0.5 * (htip1[0] + htip2[0]) + 15.0, 0.5 * (htip1[1] + htip2[1]) + 10.0)
            body.append(
                f'  <path class="geom-line" d="M {fmt(htip1[0])} {fmt(htip1[1])} '
                f'Q {fmt(hmid[0])} {fmt(hmid[1])} {fmt(htip2[0])} {fmt(htip2[1])}"/>'
            )
        else:
            body.append(seg(outer[-1][0], outer[-1][1], inner[0][0], inner[0][1], "geom-line"))

        # Compression trajectories (solid amber): rise from inner medial cortex (s=+1) up to load head (s=-1..+1)
        for k in range(5):
            u_start = 0.06 + 0.14 * k
            pts_c: list[tuple[float, float]] = []
            for j in range(25):
                tau = j / 24.0
                uu = u_start + (1.0 - u_start) * tau
                ss = 1.0 - 1.75 * (tau**1.35) + 0.25 * k * tau
                ss = max(-0.95, min(0.95, ss))
                pts_c.append(crane_pt(uu, ss, ox, bend))
            body.append(poly(pts_c, "geom-amber", closed=False))

        # Orthogonal tension trajectories (dashed blue): arch from outer lateral cortex (s=-1) over neck to inner head
        for k in range(5):
            u_start = 0.08 + 0.14 * k
            pts_t: list[tuple[float, float]] = []
            for j in range(25):
                tau = j / 24.0
                uu = u_start + (0.96 - u_start) * tau
                ss = -1.0 + 1.80 * (tau**1.25) - 0.20 * k * tau
                ss = max(-0.95, min(0.95, ss))
                pts_t.append(crane_pt(uu, ss, ox, bend))
            body.append(poly(pts_t, "geom-crimson", closed=False))

        # Downward load arrow at overhanging head
        tip = crane_pt(0.98, 0.0, ox, bend)
        body.append(seg(tip[0] + 10, tip[1] - 32, tip[0] + 10, tip[1] - 6, "geom-blue", f"load_{panel_idx}"))
        body.append(label(tip[0] + 22, tip[1] - 20, "W", "geom-label", "start"))

    body.append(
        label(
            365,
            262,
            "Solid amber: principal compression arches  |  Dashed red: orthogonal principal tension trajectories",
            "geom-note",
        )
    )
    return wrap_svg(730, 280, body, "Culmann crane and Meyer human femur orthogonal stress trajectories")


def build_transform_affine_shear() -> str:
    """Plate 10: Coordinate Transformation I — Affine Shear (Argyropelecus -> Sternoptyx, Figs. 373-374)."""
    body: list[str] = [
        label(175, 26, "A. Argyropelecus Olfersi (90° Cartesian)", "geom-title"),
        label(540, 26, "B. Sternoptyx diaphana (70° Oblique Shear)", "geom-title"),
    ]
    # Stylized anatomical contour of hatchetfish in normalized [0, 6] x [0, 5] grid
    fish_outline = [
        (0.45, 2.55), (0.85, 1.55), (1.75, 1.05), (2.95, 0.95), (4.15, 1.45),
        (5.10, 2.05), (5.65, 1.75), (5.45, 2.35), (5.68, 2.88), (5.05, 2.55),
        (4.10, 2.95), (3.45, 4.15), (2.25, 4.45), (1.25, 3.85), (0.62, 3.15),
    ]
    eye_c = (1.35, 1.85)
    dorsal_fin = [(2.55, 0.98), (2.95, 0.42), (3.45, 1.12)]

    cell = 30.0
    # Left panel: Orthogonal grid
    ox1, oy1 = 82.0, 52.0
    for ix in range(7):
        body.append(seg(ox1 + ix * cell, oy1, ox1 + ix * cell, oy1 + 5 * cell, "geom-grid"))
        body.append(label(ox1 + ix * cell, oy1 - 6, str(ix), "geom-note"))
    for iy in range(6):
        body.append(seg(ox1, oy1 + iy * cell, ox1 + 6 * cell, oy1 + iy * cell, "geom-grid"))
        body.append(label(ox1 - 12, oy1 + iy * cell + 4, chr(97 + iy), "geom-note"))

    pts1 = [(ox1 + x * cell, oy1 + y * cell) for x, y in fish_outline]
    df1 = [(ox1 + x * cell, oy1 + y * cell) for x, y in dorsal_fin]
    body.append(poly(pts1, "geom-fill-soft"))
    body.append(poly(pts1, "geom-blue", closed=True))
    body.append(poly(df1, "geom-amber", closed=False))
    body.append(pt(ox1 + eye_c[0] * cell, oy1 + eye_c[1] * cell, 4.2, "geom-pt-amber", "eye1"))
    body.append(label(175, 236, "x' = x,  y' = y  (ω = 90°)", "geom-note"))

    # Right panel: 70-degree oblique shear (cot 70 deg = 0.3640, sin 70 deg = 0.9397)
    ox2, oy2 = 415.0, 56.0
    cot70 = math.cos(math.radians(70.0))
    sin70 = math.sin(math.radians(70.0))

    def shear_map(u: float, v: float) -> tuple[float, float]:
        return (ox2 + (u + v * cot70) * cell, oy2 + (v * sin70) * cell)

    for ix in range(7):
        p_a = shear_map(float(ix), 0.0)
        p_b = shear_map(float(ix), 5.0)
        body.append(seg(p_a[0], p_a[1], p_b[0], p_b[1], "geom-grid"))
        body.append(label(p_a[0], p_a[1] - 6, str(ix), "geom-note"))
    for iy in range(6):
        p_a = shear_map(0.0, float(iy))
        p_b = shear_map(6.0, float(iy))
        body.append(seg(p_a[0], p_a[1], p_b[0], p_b[1], "geom-grid"))
        body.append(label(p_a[0] - 12, p_a[1] + 4, chr(97 + iy), "geom-note"))

    pts2 = [shear_map(x, y) for x, y in fish_outline]
    df2 = [shear_map(x, y) for x, y in dorsal_fin]
    ec2 = shear_map(*eye_c)
    body.append(poly(pts2, "geom-fill-gold"))
    body.append(poly(pts2, "geom-amber", closed=True))
    body.append(poly(df2, "geom-blue", closed=False))
    body.append(pt(ec2[0], ec2[1], 4.2, "geom-pt-blue", "eye2"))
    body.append(label(540, 236, "x' = x + y cos 70°,  y' = y sin 70°  (ω = 70°)", "geom-note"))
    return wrap_svg(730, 258, body, "Thompson coordinate transformation affine shear Argyropelecus to Sternoptyx")


def build_transform_coaxial_mesh() -> str:
    """Plate 11: Coordinate Transformation II — Coaxial-Hyperbolic Mesh (Diodon -> Orthagoriscus, Figs. 381-382)."""
    body: list[str] = [
        label(175, 26, "A. Diodon (Rectangular Coordinates)", "geom-title"),
        label(535, 26, "B. Orthagoriscus mola (Coaxial-Hyperbolic Mesh)", "geom-title"),
    ]
    # Normalized contour of Diodon in [0, 5] x [-2.5, 2.5]
    diodon_pts = [
        (0.35, 0.0), (0.65, -0.95), (1.55, -1.55), (2.75, -1.65), (3.65, -1.35),
        (4.05, -2.25), (4.35, -1.15), (4.78, -0.65), (4.88, 0.0), (4.78, 0.65),
        (4.35, 1.15), (4.05, 2.25), (3.65, 1.35), (2.75, 1.65), (1.55, 1.55),
        (0.65, 0.95),
    ]
    eye_d = (1.10, -0.58)

    cell = 30.0
    ox1, cy1 = 88.0, 142.0
    for ix in range(6):
        body.append(seg(ox1 + ix * cell, cy1 - 2.5 * cell, ox1 + ix * cell, cy1 + 2.5 * cell, "geom-grid"))
        body.append(label(ox1 + ix * cell, cy1 - 2.5 * cell - 6, str(ix), "geom-note"))
    for iy in range(-2, 3):
        body.append(seg(ox1, cy1 + iy * cell, ox1 + 5 * cell, cy1 + iy * cell, "geom-grid"))

    d1 = [(ox1 + x * cell, cy1 + y * cell) for x, y in diodon_pts]
    body.append(poly(d1, "geom-fill-soft"))
    body.append(poly(d1, "geom-blue", closed=True))
    body.append(pt(ox1 + eye_d[0] * cell, cy1 + eye_d[1] * cell, 4.0, "geom-pt-amber", "eye_diodon"))
    body.append(label(175, 250, "Orthogonal Cartesian net (x, y)", "geom-note"))

    # Right panel: Conformal exponential-polar / coaxial expansion caudally
    # Map (u, v) -> R(u) = R0 * exp(0.30 * u), angle phi(u, v) = 0.24 * v * (0.65 + 0.18 * u)
    # so caudal verticals curve strongly into nested coaxial arcs and horizontals diverge hyperbolically!
    ox2, cy2 = 398.0, 142.0

    def coax_map(u: float, v: float) -> tuple[float, float]:
        r = 38.0 * math.exp(0.33 * u)
        ang = 0.22 * v * (0.72 + 0.14 * u)
        px = ox2 + r * math.cos(ang) - 24.0
        py = cy2 + r * math.sin(ang) * (0.85 + 0.12 * u)
        return (px, py)

    for ix in range(6):
        curve_v = [coax_map(float(ix), -2.5 + 5.0 * k / 32.0) for k in range(33)]
        body.append(poly(curve_v, "geom-grid", closed=False))
        top_p = curve_v[0]
        body.append(label(top_p[0], top_p[1] - 5, str(ix), "geom-note"))
    for iy in [-2.0, -1.0, 0.0, 1.0, 2.0]:
        curve_h = [coax_map(5.0 * k / 32.0, iy) for k in range(33)]
        body.append(poly(curve_h, "geom-grid", closed=False))

    # Interpolate diodon contour densely so curved transformation is smooth
    dense_diodon: list[tuple[float, float]] = []
    n_dp = len(diodon_pts)
    for i in range(n_dp):
        p_a = diodon_pts[i]
        p_b = diodon_pts[(i + 1) % n_dp]
        for s in range(6):
            t = s / 6.0
            dense_diodon.append((p_a[0] + t * (p_b[0] - p_a[0]), p_a[1] + t * (p_b[1] - p_a[1])))
    d2 = [coax_map(x, y) for x, y in dense_diodon]
    ed2 = coax_map(*eye_d)
    body.append(poly(d2, "geom-fill-gold"))
    body.append(poly(d2, "geom-amber", closed=True))
    body.append(pt(ed2[0], ed2[1], 4.0, "geom-pt-blue", "eye_mola"))
    body.append(label(535, 250, "Nested coaxial circles & orthogonal hyperbolae", "geom-note"))
    return wrap_svg(730, 270, body, "Thompson coaxial-hyperbolic coordinate transformation Diodon to Orthagoriscus")


FIGURES: dict[str, callable] = {
    "fig_galileo_scaling.svg": build_galileo_scaling,
    "fig_plateau_fermat_hex.svg": build_plateau_fermat_hex,
    "fig_maraldi_honeycomb.svg": build_maraldi_honeycomb,
    "fig_kelvin_tetrakaidecahedron.svg": build_kelvin_tetrakaidecahedron,
    "fig_hambidge_root_rectangles.svg": build_hambidge_root_rectangles,
    "fig_golden_gnomon_spiral.svg": build_golden_gnomon_spiral,
    "fig_nautilus_chambered_spiral.svg": build_nautilus_chambered_spiral,
    "fig_phyllotaxis_parastichy.svg": build_phyllotaxis_parastichy,
    "fig_culmann_femur_trajectories.svg": build_culmann_femur_trajectories,
    "fig_transform_affine_shear.svg": build_transform_affine_shear,
    "fig_transform_coaxial_mesh.svg": build_transform_coaxial_mesh,
}


def main() -> None:
    """Build all 11 SVG figures into docsrc/_static/figures/."""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for filename, builder in FIGURES.items():
        svg_text = builder()
        target = OUT_DIR / filename
        target.write_text(svg_text, encoding="utf-8")
        print(f"Wrote {target.relative_to(OUT_DIR.parent.parent.parent)} ({len(svg_text)} bytes)")


if __name__ == "__main__":
    main()
