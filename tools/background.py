width = 16 * 2
height = 9 * 2

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

rs = np.random.RandomState(1)

#color = ("#f1d45a",
#          "#93a6b3",
#          "#214564",
#          "#1a2829",
#          "#afafaf")

color = ("#eeeeee", "#6D6E73", "#FED201", "#214564", "#BDBCCC")

X = np.array([[1, 1], [2, 2.5], [3, 1], [8, 7.5], [7, 9], [9, 9]])
Y = ['red', 'red', 'red', 'blue', 'blue', 'blue']

fig = plt.figure(figsize=(16, 9))


def triangle(left, size, invert, color):
    x, y = left
    if invert:
        plt.fill([x - size / 2, x + size / 2, x, x - size / 2],
                 [y + size, y + size, y, y + size], color=color)
    else:
        plt.fill([x, x + size, x + size / 2, x],
                 [y, y, y + size, y], color=color)


triangle_width = .2
for i in range(height):
    left = 0.0
    bot = triangle_width * i
    for j in range(width):
        c = color[rs.randint(0, 5)]
        triangle((left, bot), triangle_width, False, c)
        left += triangle_width
        c = color[rs.randint(0, 5)]
        triangle((left, bot), triangle_width, True, c)
    c = color[rs.randint(0, 5)]
    triangle((left, bot), triangle_width, False, c)

ax = plt.gca()
ax.set_xticks([])
ax.set_yticks([])
sns.despine(left=True, right=True, bottom=True)
plt.show()

fig.savefig('background.png', dpi=300,transparent=True)
