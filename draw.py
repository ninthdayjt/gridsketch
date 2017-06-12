import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from color import COLOR
import numpy as np
import math


def pcolormesh(x, y, data, type, output, dpi):
    width = x.max() - x.min()
    height = y.max() - y.min()

    fig = plt.figure()
    fig.set_size_inches(width / height, 1)
    ax = plt.Axes(fig, [0, 0, 1, 1])
    ax.set_axis_off()
    fig.add_axes(ax)

    plt.xlim(x.min(), x.max())
    plt.ylim(y.min(), y.max())

    cn = COLOR().getColor(type=type)
    plt.pcolormesh(x, y, data, cmap=cn[0], norm=cn[1])

    plt.savefig(output, format='png',  transparent=True, dpi=dpi)
    plt.close(fig)


def contourf(x, y, data, type, output, dpi):

    width = x.max() - x.min()
    height = y.max() - y.min()
    aspect = width / height

    fig = plt.figure()
    fig.set_size_inches(aspect, 1)
    ax = plt.Axes(fig, [0, 0, 1, 1])
    ax.set_axis_off()
    fig.add_axes(ax)

    plt.xlim(x.min(), x.max())
    plt.ylim(y.min(), y.max())

    cn = COLOR().getColor(type=type)

    plt.contourf(x, y, data, cmap=cn[0], norm=cn[1])

    plt.savefig(output, format='png',  transparent=True, dpi=dpi)

    plt.close(fig)



def quiver(x, y, u, v, type, output, dpi, step):

    width = x.max() - x.min()
    height = y.max() - y.min()

    fig = plt.figure()
    fig.set_size_inches(width / height, 1)
    ax = plt.Axes(fig, [0, 0, 1, 1])
    ax.set_axis_off()
    fig.add_axes(ax)

    plt.xlim(x.min(), x.max())
    plt.ylim(y.min(), y.max())

    speed = np.sqrt(u * u + v * v)

    yy = np.arange(0, y.shape[0], step)
    xx = np.arange(0, x.shape[1], step)

    points = np.meshgrid(yy, xx)

    cn = COLOR().getColor(type=type)

    plt.quiver(x[points], y[points], u[points], v[points],
               speed[points], cmap=cn[0], norm=cn[1])

    plt.savefig(output, format='png',  transparent=True, dpi=dpi)
    plt.close(fig)
