import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

width = 16 * 2
height = int(9 * 2 * np.sqrt(4 / 3))
color = ("#eeeeee", "#6D6E73", "#FED201", "#214564", "#BDBCCC")


def triangle(left, size, invert, color):
    x, y = left
    h = np.sqrt(3 / 4) * size
    if invert:
        plt.fill([x - size / 2, x + size / 2, x, x - size / 2],
                 [y + h, y + h, y, y + h], color=color)
    else:
        plt.fill([x, x + size, x + size / 2, x],
                 [y, y, y + h, y], color=color)


def save(filepath, fig=None):
    """
    Save the current image with no whitespace
    Example filepath: "output.png" or r"/home/user/output.pdf"
    """
    if not fig:
        fig = plt.gcf()

    plt.subplots_adjust(0, 0, 1, 1, 0, 0)
    for ax in fig.axes:
        ax.axis('off')
        ax.margins(0, 0)
        ax.xaxis.set_major_locator(plt.NullLocator())
        ax.yaxis.set_major_locator(plt.NullLocator())
    fig.savefig(filepath, pad_inches=0, bbox_inches='tight', dpi=108)


def generate_cover(lesson_name, subtitle):
    name = ' '.join([lesson_name, subtitle]).lower().replace(' ', '-')
    print(name)
    seed = np.array([hash(lesson_name + subtitle)]).view(np.uint32)
    rs = np.random.RandomState(seed)

    fig = plt.figure(figsize=(66, 36))
    triangle_width = .2
    trangle_height = triangle_width * np.sqrt(3 / 4)
    for i in range(height):
        left = 0.0
        bot = trangle_height * i
        for j in range(width + 1):
            c = color[rs.randint(0, 5)]
            triangle((left, bot), triangle_width, False, c)
            left += triangle_width
            c = color[rs.randint(0, 5)]
            triangle((left, bot), triangle_width, True, c)
        c = color[rs.randint(0, 5)]
        triangle((left, bot), triangle_width, False, c)

    ax = plt.gca()
    ax.set_axis_off()
    ax.margins(0, 0)
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())
    save('back.png', fig)

    plt.fill(
        [0, triangle_width * (width + 2), triangle_width * (width + 2), 0],
        [12 * trangle_height, 12 * trangle_height, 16 * trangle_height,
         16 * trangle_height],
        color='#ffffff')
    ax.text(1.5 * triangle_width, 14 * trangle_height, LESSON_NAME,
            fontsize=3 * 72, color=color[1], fontweight='bold',
            fontname='Roboto Condensed')
    ax.text(1.5 * triangle_width, 12.7 * trangle_height, SUBTITLE,
            fontsize=3 * 48, color=color[3], fontname='Roboto Condensed')
    save('cover.png', fig)

    img = Image.open('cover.png')
    px = img.size[0] // (width + 1)
    box = [px // 2, 0, img.size[0] - px // 2, img.size[1]]
    crop = img.crop(box)
    crop.save(f'{name}-cover.png')

    img = Image.open('back.png')
    crop = img.crop(box)
    crop.save(f'{name}-back.png')


LESSON_NAME = 'Lesson 8'
SUBTITLE = 'Importing Data'

generate_cover(LESSON_NAME, SUBTITLE)
