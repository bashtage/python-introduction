import glob
import os
import hashlib

import matplotlib.pyplot as plt
import nbformat
import numpy as np

from PIL import Image

width = 16 * 2
height = int(9 * 2 * np.sqrt(4 / 3))
#color = ("#eeeeee", "#83c6ff", "#6D6E73", "#FED201", "#19354C", "#BDBCCC")
# "#83c6ff"
color = ("#eeeeee", "#6D6E73", "#FED201", "#19354C", "#BDBCCC")


def triangle(left, size, invert, color):
    x, y = left
    h = np.sqrt(3 / 4) * size
    if invert:
        x_data = [x - size / 2, x + size / 2, x, x - size / 2]
        y_data = [y + h, y + h, y, y + h]
    else:
        x_data = [x, x + size, x + size / 2, x]
        y_data = [y, y, y + h, y]
    plt.fill(x_data, y_data, color=color)


def save(filepath, fig=None):
    """
    Save the current image with no whitespace
    Example filepath: "output.png" or r"/home/user/output.pdf"
    """
    if not fig:
        fig = plt.gcf()

    plt.subplots_adjust(0, 0, 1, 1, 0, 0)
    for ax in fig.axes:
        ax.axis("off")
        ax.margins(0, 0)
        ax.xaxis.set_major_locator(plt.NullLocator())
        ax.yaxis.set_major_locator(plt.NullLocator())
    fig.savefig(filepath, pad_inches=0, bbox_inches="tight", dpi=108)


def generate_cover(lesson_name, subtitle):
    name = " ".join([lesson_name, subtitle]).lower().replace(" ", "-")
    name = name.replace(",", "-").replace(":", "-")
    while "--" in name:
        name = name.replace("--", "-")
    print(name)
    sha = hashlib.sha3_512()
    sha.update((lesson_name + subtitle).encode('utf8'))
    rem = int.from_bytes(sha.digest(), "little")
    seed = []
    while rem:
        seed.append(rem % 2**32)
        rem >>= 32
    seed = np.array(seed, dtype=np.uint32)
    rs = np.random.RandomState(seed)

    fig = plt.figure(figsize=(66, 36))
    triangle_width = 0.2
    trangle_height = triangle_width * np.sqrt(3 / 4)
    for i in range(height):
        left = 0.0
        bot = trangle_height * i
        for j in range(width + 1):
            c = color[rs.randint(0, len(color))]
            triangle((left, bot), triangle_width, False, c)
            left += triangle_width
            c = color[rs.randint(0, len(color))]
            triangle((left, bot), triangle_width, True, c)
        c = color[rs.randint(0, len(color))]
        triangle((left, bot), triangle_width, False, c)

    ax = plt.gca()
    ax.set_axis_off()
    ax.margins(0, 0)
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())
    save("back.png", fig)

    plt.fill(
        [0, triangle_width * (width + 2), triangle_width * (width + 2), 0],
        [
            13 * trangle_height,
            13 * trangle_height,
            17 * trangle_height,
            17 * trangle_height,
        ],
        color="#ffffff",
    )
    ax.text(
        1.5 * triangle_width,
        15 * trangle_height,
        lesson_name,
        fontsize=3 * 72,
        color=color[1],
        fontweight="normal",
        fontname="Roboto Condensed",
    )
    ax.text(
        1.5 * triangle_width,
        13.7 * trangle_height,
        subtitle,
        fontsize=3 * 48,
        color=color[3],
        fontname="Roboto Condensed",
        fontweight="light",
    )
    save("cover.png", fig)

    img = Image.open("cover.png")
    px = img.size[0] // (width + 1)
    box = [px // 2, 0, img.size[0] - px // 2, img.size[1]]
    crop = img.crop(box)
    crop.save(f"{name}-cover.png")

    img = Image.open("back.png")
    crop = img.crop(box)
    crop.save(f"{name}-back.png")
    plt.close(fig)


content = [("Installation", "Anaconda, VS Code, and PyCharm")]

files = glob.glob("../solutions/introduction/lesson*.ipynb")
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
