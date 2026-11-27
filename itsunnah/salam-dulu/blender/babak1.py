# Babak 1 "Salam Dulu" — Amir & Hana berjalan ke pintu (Blender, gaya 3D ringkas)
# Jalankan:  python babak1.py <folder_output>
import bpy, math, sys, os

OUT = sys.argv[-1] if len(sys.argv) > 1 else "/tmp/babak1"
os.makedirs(OUT, exist_ok=True)
FPS, SECS = 24, 3
N = FPS * SECS

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.render.engine = "CYCLES"
sc.cycles.device = "CPU"
sc.cycles.samples = 24
sc.cycles.use_denoising = True
sc.render.resolution_x, sc.render.resolution_y = 720, 1280
sc.render.fps = FPS
sc.frame_start, sc.frame_end = 1, N
sc.render.image_settings.file_format = "PNG"
sc.render.filepath = os.path.join(OUT, "f_")
sc.view_settings.view_transform = "AgX"
sc.view_settings.look = "AgX - Medium High Contrast" if "AgX - Medium High Contrast" in [l.identifier for l in bpy.types.ColorManagedViewSettings.bl_rna.properties["look"].enum_items] else "None"

def mat(name, rgb, rough=0.6, emit=0.0):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*rgb, 1)
    b.inputs["Roughness"].default_value = rough
    if emit:
        b.inputs["Emission Color"].default_value = (*rgb, 1)
        b.inputs["Emission Strength"].default_value = emit
    return m

def srgb(h):
    h = h.lstrip("#"); c = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    return tuple(x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c)

M = {k: mat(k, srgb(v), r) for k, (v, r) in {
    "grass": ("#6f9a4a", .9), "path": ("#c9c2b4", .8), "wall": ("#efe6d6", .7), "roof": ("#4a4440", .7),
    "door": ("#4f7a5c", .5), "trim": ("#5a3e2b", .6), "step": ("#bdb5a8", .8), "leaf": ("#4f7f3a", .8),
    "leaf2": ("#6a9a45", .8), "pink": ("#e88aa6", .7), "pot": ("#d9d4ca", .6), "window": ("#3a4a50", .2),
    "skin": ("#e9b996", .5), "hair": ("#2a211c", .6), "kopiah": ("#f6f4ef", .7), "sage": ("#8fa77f", .7),
    "sage_d": ("#7d9670", .7), "apricot": ("#e7a27a", .75), "cream": ("#f1e7d3", .75), "shoe_d": ("#2c2a28", .5),
    "shoe_w": ("#f4f2ee", .5)}.items()}
M["lamp"] = mat("lamp", srgb("#ffd79a"), .3, emit=4)

def add(kind, loc, scale=(1, 1, 1), m=None, rot=(0, 0, 0), parent=None, **kw):
    getattr(bpy.ops.mesh, "primitive_" + kind + "_add")(location=loc, rotation=rot, **kw)
    o = bpy.context.active_object
    o.scale = scale
    if m: o.data.materials.append(M[m])
    if kind in ("uv_sphere", "cylinder", "cone"):
        bpy.ops.object.shade_smooth()
    if parent:
        o.parent = parent
    return o

def empty(loc, parent=None):
    bpy.ops.object.empty_add(location=loc)
    e = bpy.context.active_object
    if parent: e.parent = parent
    return e

# ---- set ----
add("plane", (0, 4, 0), (30, 30, 1), "grass")
add("cube", (0, 1.5, 0.01), (0.65, 5.2, 0.01), "path")
for i in range(-6, 12):  # garis jubin
    add("cube", (0, -3.6 + i * 0.6, 0.022), (0.66, 0.012, 0.005), "step")
# rumah
add("cube", (0, 9.2, 1.6), (4.6, 2.2, 1.6), "wall")
add("cube", (0, 8.05, 3.75), (5.3, 1.45, 0.08), "roof", rot=(math.radians(-24), 0, 0))
add("cube", (0, 10.35, 3.75), (5.3, 1.45, 0.08), "roof", rot=(math.radians(24), 0, 0))
add("cube", (0, 6.6, 3.15), (5.2, 0.6, 0.08), "roof")           # anjung
for x in (-2.2, 2.2):
    add("cube", (x, 6.2, 1.55), (0.14, 0.14, 1.55), "wall")       # tiang
add("cube", (0, 6.94, 1.12), (0.62, 0.05, 1.12), "door")
add("cube", (0, 6.98, 1.16), (0.7, 0.03, 1.2), "trim")
for zz in (0.55, 1.6):
    add("cube", (0, 6.885, zz), (0.5, 0.01, 0.34), "sage_d")
add("cube", (0.42, 6.86, 1.05), (0.03, 0.04, 0.18), "shoe_d")    # pemegang
add("cube", (0.95, 6.9, 1.25), (0.06, 0.03, 0.1), "shoe_d")      # loceng
for x in (-2.6, 2.6):
    add("cube", (x, 6.95, 1.6), (0.75, 0.04, 0.7), "window")
    add("cube", (x, 6.98, 1.6), (0.82, 0.03, 0.78), "trim")
    add("cube", (x, 6.9, 1.6), (0.02, 0.01, 0.7), "trim")
add("cube", (0, 6.3, 0.09), (1.4, 0.6, 0.09), "step")
add("cube", (0, 5.8, 0.045), (1.6, 0.5, 0.045), "step")
add("uv_sphere", (0, 6.7, 2.75), (0.12, 0.12, 0.16), "lamp")
# pokok & pasu
for x, y, s, m in [(-1.4, 5.6, .45, "leaf"), (1.5, 5.6, .5, "leaf2"), (-3.2, 2.5, .8, "leaf"), (-3.6, 0.5, .9, "leaf2"),
                   (3.3, 2.0, .7, "leaf"), (3.8, 4.2, .9, "leaf2"), (-2.6, 4.8, .6, "leaf2")]:
    add("uv_sphere", (x, y, s * 0.9), (s, s, s * 0.9), m)
for x, y in [(-1.4, 5.6), (1.5, 5.6)]:
    add("cylinder", (x, y, 0.22), (0.32, 0.32, 0.22), "pot")
for i, (x, y) in enumerate([(-3.0, 1.2), (-3.3, 2.0), (-2.8, 2.9), (-3.5, 3.2), (-2.9, 0.6)]):
    add("uv_sphere", (x + .55, y - .45, 0.55 + (i % 3) * .2), (.1, .1, .1), "pink")

# ---- watak ----
def kid(x, y0, hijab):
    root = empty((x, y0, 0))
    torso_m = "cream" if hijab else "sage"
    pants_m = "sage_d"
    body = add("uv_sphere", (0, 0, 0.74), (0.2, 0.15, 0.3 if hijab else 0.27), torso_m, parent=root)
    body.location = (0, 0, 0.72 if hijab else 0.74)
    legs, arms = [], []
    for s in (-1, 1):
        hip = empty((0, 0, 0), root); hip.location = (s * 0.08, 0, 0.5)
        add("cylinder", (0, 0, 0), (0.065, 0.065, 0.22), pants_m, parent=hip).location = (0, 0, -0.22)
        add("cube", (0, 0, 0), (0.07, 0.11, 0.04), "shoe_w" if hijab else "shoe_d", parent=hip).location = (0, 0.03, -0.46)
        legs.append(hip)
        sh = empty((0, 0, 0), root); sh.location = (s * 0.2, 0, 0.92)
        add("cylinder", (0, 0, 0), (0.055, 0.055, 0.19), torso_m, parent=sh).location = (s * 0.02, 0, -0.18)
        add("uv_sphere", (0, 0, 0), (0.05, 0.05, 0.05), "skin", parent=sh).location = (s * 0.02, 0, -0.39)
        arms.append(sh)
    head = empty((0, 0, 0), root); head.location = (0, 0, 1.2)
    add("uv_sphere", (0, 0, 0), (0.19, 0.18, 0.19), "skin", parent=head)
    if hijab:
        add("uv_sphere", (0, 0, 0), (0.225, 0.215, 0.235), "apricot", parent=head).location = (0, 0.02, 0.02)
        add("cone", (0, 0, 0), (1, 1, 1), "apricot", parent=head, radius1=0.3, radius2=0.17, depth=0.36, vertices=48).location = (0, 0.01, -0.27)
    else:
        add("uv_sphere", (0, 0, 0), (0.198, 0.19, 0.18), "hair", parent=head).location = (0, -0.03, 0.03)
        add("cylinder", (0, 0, 0), (0.185, 0.18, 0.06), "kopiah", parent=head).location = (0, 0.0, 0.14)
        add("cube", (0, 0, 0), (0.07, 0.03, 0.08), "sage", parent=root).location = (0, -0.0, 1.0)  # kolar
    return root, legs, arms, head

amir = kid(-0.28, -2.0, False)
hana = kid(0.3, -2.3, True)

def animate(k, y0, y1, phase):
    root, legs, arms, head = k
    for f in range(1, N + 1, 2):
        t = (f - 1) / (N - 1)
        cyc = (f / FPS) * 2 * math.pi * 1.6 + phase
        root.location = (root.location.x, y0 + (y1 - y0) * t, 0.03 * abs(math.sin(cyc)))
        root.keyframe_insert("location", frame=f)
        for i, hip in enumerate(legs):
            hip.rotation_euler = (0.42 * math.sin(cyc + i * math.pi), 0, 0); hip.keyframe_insert("rotation_euler", frame=f)
        for i, sh in enumerate(arms):
            sh.rotation_euler = (-0.32 * math.sin(cyc + i * math.pi), 0, 0); sh.keyframe_insert("rotation_euler", frame=f)
        head.rotation_euler = (0, 0.04 * math.sin(cyc / 2), 0.05 * math.sin(cyc / 2 + phase)); head.keyframe_insert("rotation_euler", frame=f)

animate(amir, -2.0, 1.6, 0.0)
animate(hana, -2.3, 1.3, 1.3)

# ---- cahaya & kamera ----
bpy.ops.object.light_add(type="SUN", rotation=(math.radians(52), math.radians(-18), math.radians(-35)))
sun = bpy.context.active_object; sun.data.energy = 4.2; sun.data.color = (1.0, 0.86, 0.7); sun.data.angle = math.radians(6)
w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True
w.node_tree.nodes["Background"].inputs["Color"].default_value = (*srgb("#cfe3f2"), 1)
w.node_tree.nodes["Background"].inputs["Strength"].default_value = 0.9

bpy.ops.object.camera_add(location=(0.1, -6.2, 1.45))
cam = bpy.context.active_object; sc.camera = cam; cam.data.lens = 30
tgt = empty((0, 4.0, 1.05))
c = cam.constraints.new("TRACK_TO"); c.target = tgt; c.track_axis = "TRACK_NEGATIVE_Z"; c.up_axis = "UP_Y"
cam.keyframe_insert("location", frame=1)
cam.location = (0.1, -5.3, 1.4); cam.keyframe_insert("location", frame=N)

if os.environ.get("TEST"):
    sc.frame_set(int(os.environ["TEST"])); sc.render.filepath = os.path.join(OUT, "test.png")
    bpy.ops.render.render(write_still=True)
else:
    bpy.ops.render.render(animation=True)
print("RENDER SIAP", OUT)
