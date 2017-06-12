import numpy as np
import math


def transform1D(lats, lons):

    LATS, LONS = np.meshgrid(lats, lons)

    x = np.zeros(LATS.shape)
    y = np.zeros(LATS.shape)

    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i][j], y[i][j] = __merc3857(LONS[i][j], LATS[i][j])

    y = y.min() - y

    return (x, y)


def transform2D(lats, lons):

    x = np.zeros(lats.shape)
    y = np.zeros(lats.shape)

    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i][j], y[i][j] = __merc3857(lons[i][j], lats[i][j])

    y = y.min() - y

    return (x, y)


def transformPoint(lats, lons):
    length = len(lats)

    x = np.zeros(length)
    y = np.zeros(length)
    for i in range(length):
        x[i], y[i] = __merc3857(lons[i], lats[i])

    #y = y.min() - y

    return (x, y)


def __merc3857(lon, lat):
    sinlat = math.sin(lat * 0.0174532925)
    px = lon * 46603.3777778 + 8388608
    py = 8388608 - math.log((1 + sinlat) / (1 - sinlat)) * 1335088.43038578
    return (px, py)
