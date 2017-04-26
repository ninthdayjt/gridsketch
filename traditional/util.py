# anerkiz 20160907
import math
import numpy as np


def interp(inputMatrix, tXArr, tYArr):

    c = len(tXArr)
    r = len(tYArr)

    dataset = np.zeros([r, c])

    for i in range(r):
        for j in range(c):

            x0 = np.floor(tYArr[i])
            x1 = x0 + 1
            y0 = np.floor(tXArr[j])
            y1 = y0 + 1

            q1 = inputMatrix[x0, y0]
            q2 = inputMatrix[x1, y0]
            q3 = inputMatrix[x1, y1]
            q4 = inputMatrix[x0, y1]

            ret = bilinear_interpolation(tYArr[i], tXArr[j], [(x0, y0, q1), (x1, y0, q2), (x1, y1, q3), (x0, y1, q4)])

            dataset[i][j] = ret

    return dataset


def bilinear_interpolation(x, y, points):

    (x1, y1, q11), (_x1, y2, q12), (x2, _y1, q21), (_x2, _y2, q22) = sorted(points)

    return (q11 * (x2 - x) * (y2 - y) +
            q21 * (x - x1) * (y2 - y) +
            q12 * (x2 - x) * (y - y1) +
            q22 * (x - x1) * (y - y1)
            ) / ((x2 - x1) * (y2 - y1))


G = 4891.9698
PI180 = math.pi / 180
GDPI4 = G / (4 * math.pi)
GD360 = G / 360
G180D360 = G * 180 / 360
GD2 = G * 0.5


def mercator(lon, lat):

    sinLatitude = math.sin(lat * PI180)

    px = lon * GD360 + G180D360

    py = GD2 - math.log((1 + sinLatitude) / (1 - sinLatitude)) * GDPI4

    return np.array([px, py], dtype=np.int)
