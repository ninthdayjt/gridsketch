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

#读取二进制格式经纬度数据
with open(latlonPath, 'rb') as f:

    for i in range(ROW):
        for j in range(COL):
            val = list(struct.unpack(">1f", f.read(4)))[0]
            latArr[i][j] = float(val)

    for i in range(ROW):
        for j in range(COL):
            val = list(struct.unpack(">1f", f.read(4)))[0]
            lonArr[i][j] = float(val)

#线性插值
tX = np.linspace(0, COL - 1, COL * _P, False)
tY = np.linspace(0, ROW - 1, ROW * _P, False)

#双线性插值
interpLat = U.interp(latArr, tX, tY)
interpLon = U.interp(lonArr, tX, tY)

#数组展平
latTable = interpLat.flatten()
lonTable = interpLon.flatten()

#投影计算（经纬度->像素）
upLeft = U.mercator(min(lonTable),  max(latTable))
downRight = U.mercator(max(lonTable), min(latTable))
resolution = downRight - upLeft

length = len(latTable)

mercatorMap = np.zeros([length, 2], dtype=np.int)

for i in range(length):
    mercatorMap[i] = U.mercator(lonTable[i], latTable[i]) - upLeft

#主函数
def start(input, output):

    valArr = np.zeros([ROW, COL])

    #读取数值数据
    with open(input, 'rb') as f:
        for i in range(ROW):
            for j in range(COL):
                val = list(struct.unpack(">1f", f.read(4)))[0]
                valArr[i][j] = float(val)

    #双线性插值
    interpVal = U.interp(valArr, tX, tY)

    valTable = interpVal.flatten()

    #初始化图片
    img = Image.new("RGBA", resolution + 1, (0, 0, 0, 0))

    length = len(latTable)

    #根据色标绘图
    for i in range(length):

        val = valTable[i]

        img.putpixel(mercatorMap[i], COLOR.color1(val))

    #用中国地图切图
    img = CUT.cut(img)

    #图例
    img = LEGEND.draw(img, 'l1')

    img.save(output + ".png", 'PNG')


start('testinputdata.dat', 'output')