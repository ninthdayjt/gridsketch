from PIL import Image, ImageFilter
import numpy as np
#import pandas as pd
import os

# def Merge(wsPath, uvPath, outputPath):
#     base_img = Image.open(wsPath)
#     tmp_img = Image.open(uvPath)
#     r, g, b, a = tmp_img.split()
#     base_img.paste(tmp_img, mask=a)
#     base_img.save(outputPath, "PNG")
#     os.remove(uvPath)
#     os.remove(wsPath)


def cut(path, targetpath):
    pathdata = np.array(Image.open(path).filter(ImageFilter.SHARPEN))
    targetdata = np.array(Image.open(targetpath))

    pathdata[pathdata == 255] = 1
    newdata = pathdata * targetdata

    img = Image.fromarray(newdata)
    img.save(targetpath, "PNG")


# def interp(data, lats, lons, res):

#     df = pd.DataFrame(data, index=lats, columns=lons)

#     interpLons = np.linspace(lons[0], lons[-1], num=res)
#     interplats = np.linspace(lats[0], lats[-1], num=res)

#     df_interpRow = pd.DataFrame(np.zeros([len(interplats), data.shape[1]]) + np.nan,
#                                 columns=lons, index=interplats)
#     df_interpCol = pd.DataFrame(np.zeros([data.shape[0], len(interpLons)]) + np.nan,
#                                 index=lats, columns=interpLons)

#     new = pd.concat([df, df_interpRow], axis=0).sort_index(
#         axis=0, ascending=True)
#     new = pd.concat([new, df_interpCol], axis=1).sort_index(
#         axis=1, ascending=True)

#     new = new.interpolate(method='cubic', axis=0).interpolate(
#         method='cubic', axis=1)

#     return(new.values, new.index, new.columns)
