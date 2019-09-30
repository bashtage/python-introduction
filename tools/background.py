from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

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
    name = name.replace(',', '-')
    while '--' in name:
        name = name.replace('--', '-')
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
        [13 * trangle_height, 13 * trangle_height, 17 * trangle_height,
         17 * trangle_height],
        color='#ffffff')
    ax.text(1.5 * triangle_width, 15 * trangle_height, lesson_name,
            fontsize=3 * 72, color=color[1], fontweight='bold',
            fontname='Roboto Condensed')
    ax.text(1.5 * triangle_width, 13.7 * trangle_height, subtitle,
            fontsize=3 * 48, color=color[3], fontname='Roboto Condensed',
            fontweight='light')
    save('cover.png', fig)

    img = Image.open('cover.png')
    px = img.size[0] // (width + 1)
    box = [px // 2, 0, img.size[0] - px // 2, img.size[1]]
    crop = img.crop(box)
    crop.save(f'{name}-cover.png')

    img = Image.open('back.png')
    crop = img.crop(box)
    crop.save(f'{name}-back.png')


content = (('Installation', 'Anaconda, VS Code, and PyCharm'),
           ('Lesson 1', 'Pycharm'),
           ('Lesson 1', 'Spyder'),
           ('Lesson 1', 'VS Code'),
           ('Lesson 2', 'Basic Python Types'),
           ('Lesson 8', 'Importing and Exporting Data'),
           ('Lesson 3', 'Modules and Functions'),
           ('Lesson 14', 'Importing Data'),
           ('Lesson 15', 'Saving and Exporting Data')
           )

for name, sub in content[-2:]:
    generate_cover(name, sub)
