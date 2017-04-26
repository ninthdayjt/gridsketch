from mpl_toolkits.basemap import Basemap, cm
import draw as DRAW
import numpy as np
import time
from netCDF4 import Dataset as NetCDFFile
import os
import os.path
import warnings
import math
warnings.filterwarnings("ignore")


def go(input):

    outdir = ''
    nc = NetCDFFile(input)
    lats = nc.variables['latitude'][:]
    lons = nc.variables['longitude'][:]

    # 初始化投影对象
    map = Basemap(projection='merc', llcrnrlat=lats[
                  0], urcrnrlat=lats[-1], llcrnrlon=lons[0], urcrnrlon=lons[-1])
    # 经纬度矩阵
    LATS, LONS = np.meshgrid(lats, lons)
    # 投影转换
    x, y = map(LONS, LATS)

    ##########################################################################
    DRAW.pcolormesh(x=x.T, y=y.T,
                    data=nc.variables['TEM'][:],
                    map=map, type='TEM', dpi=800,
                    output=os.path.join(outdir,  'TEM.png'))

    DRAW.pcolormesh(x=x.T, y=y.T,
                    data=nc.variables['RHU'][:],
                    map=map, type='RHU', dpi=800,
                    output=os.path.join(outdir, 'RHU.png'))

    DRAW.pcolormesh(x=x.T, y=y.T,
                    data=nc.variables['PRE'][:],
                    map=map, type='PRE', dpi=800,
                    output=os.path.join(outdir, 'PRE.png'))

    ws = nc.variables['WS'][:]
    wd = nc.variables['WD'][:]

    u = ws * np.cos(wd * math.pi / 180)
    v = ws * np.sin(wd * math.pi / 180)

    DRAW.quiver(x=x.T, y=y.T,
                u=u,
                v=v,
                map=map, type='WIND', dpi=800,
                output=os.path.join(outdir, 'WIND.png'))


start = time.clock()

go('input/test.nc')

end = time.clock()
print("time: %f s" % (end - start))
