# anerkiz 20160907
import struct
from PIL import Image
import numpy as np
import color as COLOR
import util as U
import cut as CUT
import legend as LEGEND
import datetime

latlonPath = 'latlong_grid.dat'

now = datetime.datetime.now()
timestr = now.strftime("%Y%m%d")

ROW, COL = 479, 520

_P = 2

############################################################

latArr = np.zeros([ROW, COL])
lonArr = np.zeros([ROW, COL])

with open(latlonPath, 'rb') as f:

    for i in range(ROW):
        for j in range(COL):
            val = list(struct.unpack(">1f", f.read(4)))[0]
            latArr[i][j] = float(val)

    for i in range(ROW):
        for j in range(COL):
            val = list(struct.unpack(">1f", f.read(4)))[0]
            lonArr[i][j] = float(val)

tX = np.linspace(0, COL - 1, COL * _P, False)
tY = np.linspace(0, ROW - 1, ROW * _P, False)

interpLat = U.interp(latArr, tX, tY)
interpLon = U.interp(lonArr, tX, tY)

latTable = interpLat.flatten()
lonTable = interpLon.flatten()

upLeft = U.mercator(min(lonTable),  max(latTable))
downRight = U.mercator(max(lonTable), min(latTable))
resolution = downRight - upLeft

length = len(latTable)

mercatorMap = np.zeros([length, 2], dtype=np.int)

for i in range(length):
    mercatorMap[i] = U.mercator(lonTable[i], latTable[i]) - upLeft


def start(input, output):

    valArr = np.zeros([ROW, COL])

    with open(input, 'rb') as f:
        for i in range(ROW):
            for j in range(COL):
                val = list(struct.unpack(">1f", f.read(4)))[0]
                valArr[i][j] = float(val)

    interpVal = U.interp(valArr, tX, tY)

    valTable = interpVal.flatten()

    img = Image.new("RGBA", resolution + 1, (0, 0, 0, 0))

    length = len(latTable)

    for i in range(length):

        val = valTable[i]

        img.putpixel(mercatorMap[i], COLOR.color1(val))

    img = CUT.cut(img)

    img = LEGEND.draw(img, 'l1')

    img.save(output + ".png", 'PNG')


start('testinputdata.dat', 'output')