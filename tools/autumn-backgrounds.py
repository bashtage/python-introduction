import glob
import hashlib
import nbformat

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

width = 16 * 2
height = int(9 * 2 * np.sqrt(4 / 3))
color = ("#eeeeee", "#6D6E73", "#FED201", "#19354C", "#BDBCCC")

lesson_name = "Data"
subtitle = "Dataset Construction"
filepath = "test.png"
sha = hashlib.sha3_512()
sha.update((lesson_name + subtitle).encode("utf8"))
rem = int.from_bytes(sha.digest(), "little")
seed = []
while rem:
    seed.append(rem % 2 ** 32)
    rem >>= 32
seed = np.array(seed, dtype=np.uint32)
rs = np.random.RandomState(seed)
r = np.sqrt(1 - 0.5 ** 2)
x = [0, 0, r, 2 * r, 2 * r, r, 0]
y = [1, 0, -0.5, 0, 1, 1.5, 1]
x_data = np.array(x)
y_data = np.array(y)
fig = plt.figure(figsize=(66, 36))
x_orig = x_data.copy()

width = 37
height = 25
for j in range(height):
    x_data = x_orig.copy()
    shift = (j % 2) == 0
    x_data += shift * r
    for i in range(width):
        plt.fill(x_data, y_data, color=color[rs.randint(0, len(color))])
        x_data += 2 * r
    y_data -= 1 + 0.5

plt.fill(
    [0, (width + r / 2) * 2 * r, (width + r / 2) * 2 * r, 0],
    [-3+0.5, -3+0.5, -8 - 2, -8 - 2],
    color="#ffffff",
)

plt.subplots_adjust(0, 0, 1, 1, 0, 0)
for ax in fig.axes:
    ax.set_axis_off()
    ax.axis("off")
    ax.margins(0, 0)
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())

lesson_name = "Data"
subtitle = "Dataset Creation"

ax.text(
 5*r,
 -6,
 lesson_name.replace("`", ""),
 fontsize=3 * 72,
 color=color[1],
 fontweight="normal",
 fontname="Roboto Condensed",
)
ax.text(
 5*r,
 -8.75,
 subtitle.replace("`", ""),
 fontsize=3 * 48,
 color=color[3],
 fontname="Roboto Condensed",
 fontweight="light",
)


fig.savefig(filepath, pad_inches=0, bbox_inches="tight", dpi=108)

ylim = ax.get_ylim()
h = ylim[1] - ylim[0]
shave = 2/ h

img = Image.open(filepath)
vadj = int(img.size[1]/h//1)
px = img.size[0] // (width + 1)
box = [px // 2, vadj, img.size[0] - px // 2, img.size[1]-vadj]
crop = img.crop(box)
name = "blah"
sz = crop.size
if sz[0] / sz[1] > 16/ 9:
    new_width = int(np.ceil(sz[0] * (16/9)/(sz[0] / sz[1])))
    loss = sz[0] - new_width
    box = [loss // 2,0, sz[0] - loss//2,crop.size[1]]
    crop = crop.crop(box)
crop.save(f"{name.replace('`','')}-cover.png")


content = []
files = glob.glob("../solutions/autumn/lesson*.ipynb")
for file_name in files:
    with open(file_name) as nb_file:
        nb = nbformat.reader.read(nb_file)
    lines = nb["cells"][0]["source"].split("\n")
    title = None
    for line in lines:
        line = line.strip()
        if line.startswith("# "):
            title = line[2:]
    if title is None:
        raise ValueError("Title not found")

    key = os.path.splitext(file_name)[0].split("-")[-1]
    content.append((f"Lesson {key}", title))

content.extend(
    [
        ("Lesson 1", "Spyder"),
        ("Lesson 1", "VS Code"),
        ("Lesson 1", "PyCharm Professional"),
    ]
)

for name, sub in content:
    generate_cover(name, sub)

for png in ("cover", "back"):
    if os.path.exists(f"{png}.png"):
        os.unlink(f"{png}.png")
