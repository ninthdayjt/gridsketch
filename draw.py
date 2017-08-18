import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def contourf(x, y, data, output, color, dpi=300, format='png'):

    width = x.max() - x.min()
    height = y.max() - y.min()

    fig = plt.figure()
    fig.set_size_inches(width / height, 1)
    ax = plt.Axes(fig, [0, 0, 1, 1])
    ax.set_axis_off()
    fig.add_axes(ax)

    plt.xlim(x.min(), x.max())
    plt.ylim(y.min(), y.max())

    plt.contourf(x, y, data, levels=color["levels"],
                 cmap=color["cmap"], norm=color["norm"])

    plt.savefig(output + '.' + format, format=format,
                transparent=True, dpi=dpi)

    plt.close(fig)

def contourfQuiver(x, y, ws, wd, output, step, color, dpi=300, format='png'):

    width = x.max() - x.min()
    height = y.max() - y.min()

    fig = plt.figure()
    fig.set_size_inches(width / height, 1)
    ax = plt.Axes(fig, [0, 0, 1, 1])
    ax.set_axis_off()
    fig.add_axes(ax)

    plt.xlim(x.min(), x.max())
    plt.ylim(y.min(), y.max())

    plt.contourf(x, y, ws, levels=color["levels"], cmap=color[
                 "cmap"], norm=color["norm"])

    u = ws * np.cos(wd * np.pi / 180)
    v = ws * np.sin(wd * np.pi / 180)

    yy = np.arange(0, y.shape[0], step)
    xx = np.arange(0, x.shape[1], step)

    points = np.meshgrid(yy, xx)

    plt.quiver(x[points], y[points], u[points], v[points])

    plt.savefig(output + '.' + format, format=format,
                transparent=True, dpi=dpi)
    plt.close(fig)
