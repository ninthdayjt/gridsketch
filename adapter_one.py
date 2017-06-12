from proj import transform1D, transform2D
import draw as DRAW
import os
from netCDF4 import Dataset as NetCDFFile
from cut import cut

def adapter(fullname, filename, outdir):

    if 'BJDW_SK_1KM_ANA' in filename:

        nc = NetCDFFile(fullname)

        lats = nc.variables['lat'][:]
        lons = nc.variables['lon'][:]

        pX, pY = transform2D(lats, lons)

        pre = nc.variables['PRE_1h'][0, :]
        pre[pre < 0.0001] = float('nan')
        rhu = nc.variables['RHU'][0, :]
        rhu[rhu < -9000] = float('nan')
        tem = nc.variables['TEM'][0, :]
        tem[tem < -9000] = float('nan')
        # u = nc.variables['usfc'][0,:]
        # u[u < -9000] = float('nan')
        # v = nc.variables['vsfc'][0,:]
        # v[v < -9000] = float('nan')

        ws = nc.variables['WS'][0, :]
        ws[ws < -9000] = float('nan')


        fname = filename.replace('.nc', '').replace('.NC', '')

        DRAW.contourf(x=pX, y=pY, data=pre, type='PRE1H', dpi=800, output=os.path.join(
            outdir,  fname + '_PRE_1h.png'))

        DRAW.contourf(x=pX, y=pY, data=rhu, type='RHU', dpi=800, output=os.path.join(
            outdir,  fname + '_RHU.png'))

        DRAW.contourf(x=pX, y=pY, data=tem, type='TEM', dpi=800, output=os.path.join(
            outdir,  fname + '_TEM.png'))

        DRAW.contourf(x=pX, y=pY, data=ws, type='WIND', dpi=800, output=os.path.join(
            outdir,  fname + '_WIND.png'))

        #DRAW.quiver(x=pX, y=pY, u=u, v=v, type='WIND', dpi=800, step=10,output=os.path.join(outdir,  fname + '_WIND.png'))

        #creat(minLat=min(lats.flatten()), maxLat=max(lats.flatten()),minLon=min(lons.flatten()), maxLon=max(lons.flatten()), dpi=800)

        cut(path='adapter_one_path.png',
            targetpath=os.path.join(outdir, fname + '_TEM.png'))

        cut(path='adapter_one_path.png',
            targetpath=os.path.join(outdir,  fname + '_PRE_1h.png'))

        cut(path='adapter_one_path.png',
            targetpath=os.path.join(outdir,  fname + '_RHU.png'))

        cut(path='adapter_one_path.png',
            targetpath=os.path.join(outdir,  fname + '_WIND.png'))

        nc.close()
