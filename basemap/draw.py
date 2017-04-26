from color import COLOR
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings("ignore")


# 等值面色斑

def pcolormesh(x, y, data, map, type, output, dpi):
    fig = plt.figure()
    fig.set_size_inches(1, 1)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)

    colorMap = COLOR().getColor(type=type)
    map.pcolormesh(x, y, data, cmap=colorMap[0], norm=colorMap[1])

    plt.savefig(output, format='png',  transparent=True, dpi=dpi)
    plt.close(fig)

# 箭头向量

def quiver(x, y, u, v, map, type, output,dpi):

    speed = np.sqrt(u * u + v * v)

    # 抽稀
    yy = np.arange(0, y.shape[0], 15)
    xx = np.arange(0, x.shape[1], 15)

    points = np.meshgrid(yy, xx)

    fig = plt.figure()
    fig.set_size_inches(1, 1)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)

    colorMap = COLOR().getColor(type)
    map.quiver(x[points], y[points], u[points], v[points],
               speed[points], cmap=colorMap[0], norm=colorMap[1])

    plt.savefig(output, format='png', transparent=True, dpi=dpi)
    plt.close(fig)
