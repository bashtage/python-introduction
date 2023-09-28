import glob
import hashlib
import os

import matplotlib.pyplot as plt
import nbformat
import numpy as np
from PIL import Image

width = 16 * 2
height = int(9 * 2 * np.sqrt(4 / 3))
color = ("#eeeeee", "#6D6E73", "#FED201", "#19354C", "#BDBCCC")

lesson_name = "Data"
subtitle = "Dataset Construction"
filepath = "test.png"


def generate_cover(title, subtitle, file_name):
    sha = hashlib.sha3_512()
    sha.update((title + subtitle).encode("utf8"))
    rem = int.from_bytes(sha.digest(), "little")
    rg = np.random.default_rng(rem)
    r = np.sqrt(1 - 0.5**2)
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
            plt.fill(x_data, y_data, color=color[rg.integers(0, len(color))])
            x_data += 2 * r
        y_data -= 1 + 0.5

    fig.savefig(f"{file_name}-back.png", pad_inches=0, bbox_inches="tight", dpi=108)
    ax = fig.axes[0]
    ylim = ax.get_ylim()
    h = ylim[1] - ylim[0]
    img = Image.open(f"{file_name}-back.png")
    vadj = int(img.size[1] / h // 1)
    px = img.size[0] // (width + 1)
    box = [px // 2, vadj, img.size[0] - px // 2, img.size[1] - vadj]
    crop = img.crop(box)
    sz = crop.size
    if sz[0] / sz[1] > 16 / 9:
        new_width = int(np.ceil(sz[0] * (16 / 9) / (sz[0] / sz[1])))
        loss = sz[0] - new_width
        box = [loss // 2, 0, sz[0] - loss // 2, crop.size[1]]
        crop = crop.crop(box)
    crop.save(f"{file_name}-back.png")

    plt.fill(
        [0, (width + r / 2) * 2 * r, (width + r / 2) * 2 * r, 0],
        [-3 + 0.5 - 1.5, -3 + 0.5 - 1.5, -8 - 2 - 1.5, -8 - 2 - 1.5],
        color="#ffffff",
    )

    plt.subplots_adjust(0, 0, 1, 1, 0, 0)
    for ax in fig.axes:
        ax.set_axis_off()
        ax.axis("off")
        ax.margins(0, 0)
        ax.xaxis.set_major_locator(plt.NullLocator())
        ax.yaxis.set_major_locator(plt.NullLocator())
    ax.text(
        5 * r,
        -6 - 1.5,
        title.replace("`", ""),
        fontsize=3 * 60,
        color=color[1],
        fontweight="normal",
        fontname="Roboto Condensed",
    )
    if subtitle:
        ax.text(
            5 * r,
            -8.5 - 1.5,
            subtitle.replace("`", ""),
            fontsize=3 * 40,
            color=color[3],
            fontname="Roboto Condensed",
            fontweight="light",
        )

    fig.savefig(f"{file_name}-cover.png", pad_inches=0, bbox_inches="tight", dpi=108)

    ylim = ax.get_ylim()
    h = ylim[1] - ylim[0]
    img = Image.open(f"{file_name}-cover.png")
    vadj = int(img.size[1] / h // 1)
    px = img.size[0] // (width + 1)
    box = [px // 2, vadj, img.size[0] - px // 2, img.size[1] - vadj]
    crop = img.crop(box)
    sz = crop.size
    if sz[0] / sz[1] > 16 / 9:
        new_width = int(np.ceil(sz[0] * (16 / 9) / (sz[0] / sz[1])))
        loss = sz[0] - new_width
        box = [loss // 2, 0, sz[0] - loss // 2, crop.size[1]]
        crop = crop.crop(box)
    crop.save(f"{file_name}-cover.png")


content = []
files = glob.glob("../solutions/autumn/*.ipynb")
for file_name in files:
    with open(file_name) as nb_file:
        nb = nbformat.reader.read(nb_file)
    lines = nb["cells"][0]["source"].split("\n")
    title = None
    for line in lines:
        line = line.strip()
        if line.startswith("## "):
            title = line[2:]
    if title is None:
        raise ValueError("Title not found")
    if ":" in title:
        title, subtitle = map(str.strip, title.split(":"))
    else:
        title = title.strip()
        subtitle = ""
    file_name = os.path.splitext(os.path.split(file_name)[-1])[0]

    content.append((title, subtitle, file_name))

for title, subtitle, file_name in content:
    generate_cover(title, subtitle, file_name)
    print(file_name)

for png in ("cover", "back"):
    if os.path.exists(f"{png}.png"):
        os.unlink(f"{png}.png")
