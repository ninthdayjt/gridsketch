import proj as P
import draw as DRAW
import os
import re
from netCDF4 import Dataset as NetCDFFile

pattern = re.compile(r'^test.nc$')


def adapter(fullname, filename, outdir, colormap):

    if pattern.search(filename):

        nc = NetCDFFile(fullname)

        lats = nc.variables['lat'][:]
        lons = nc.variables['lon'][:]

        pX, pY = P.transform2D(lats, lons)

        pre = nc.variables['PRE_1h'][0, :]
        pre[pre < -9000] = float('nan')
        rhu = nc.variables['RHU'][0, :]
        rhu[rhu < -9000] = float('nan')
        tem = nc.variables['TEM'][0, :]
        tem[tem < -9000] = float('nan')
        ws = nc.variables['WS'][0, :]
        ws[ws < -9000] = float('nan')
        wd = nc.variables['WD'][0, :]
        wd[wd < -9000] = float('nan')

        fname = filename.replace('.nc', '').replace('.NC', '')

        DRAW.contourf(x=pX, y=pY, data=pre, color=colormap['pre_1h'], output=os.path.join(
            outdir,  fname + '_PRE_1h.png'), format='svg')

        DRAW.contourf(x=pX, y=pY, data=rhu, color=colormap['rhu'], output=os.path.join(
            outdir,  fname + '_RHU.png'), format='svg')

        DRAW.contourf(x=pX, y=pY, data=tem, color=colormap['tem'], output=os.path.join(
            outdir,  fname + '_TEM.png'), format='svg')

        DRAW.contourfQuiver(x=pX, y=pY, ws=ws, wd=wd, color=colormap['wind'], step=20, output=os.path.join(
            outdir,  fname + '_WIND.png'), format='svg')

        nc.close()
