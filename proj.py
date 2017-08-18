import numpy as np


def transform1D(lats, lons):
    LATS, LONS = np.meshgrid(lats, lons)
    x, y = __merc3857(LONS, LATS)
    y = y.min() - y
    return (x.T, y.T)


def transform2D(lats, lons):
    x, y = __merc3857(lons, lats)
    y = y.min() - y
    return (x, y)


def transformPoint(lats, lons):
    x, y = __merc3857(lons, lats)
    return (x, y)


def __merc3857(lon, lat):
    sinlat = np.sin(lat * 0.0174532925)
    px = lon * 46603.3777778 + 8388608
    py = 8388608 - np.log((1 + sinlat) / (1 - sinlat)) * 1335088.43038578
    return (px, py)
