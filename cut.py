from proj import transformPoint
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image, ImageFilter
import math
import json


def cut(path, targetpath):

    pathdata = np.array(Image.open(path).filter(ImageFilter.SHARPEN))

    targetdata = np.array(Image.open(targetpath))

    pathdata[pathdata == 255] = 1

    newdata = pathdata * targetdata

    img = Image.fromarray(newdata)

    img.save(targetpath, "PNG")
