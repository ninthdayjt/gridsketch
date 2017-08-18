from matplotlib.colors import ListedColormap, BoundaryNorm
import json
import numpy as np
import os
import re


class COLOR:

    # 根据项目名称列表
    # 初始化色标字典。key:projname，value:不同要素的colormap，包含(cmap,norm,levels)
    def __init__(self, projList):

        self.colormap = {}

        for proj in projList:

            filePath = self.__loadColorFile(proj)

            if filePath == "":
                raise ValueError('找不到色标文件:' + proj)

            with open(filePath, 'r', encoding='utf-8')as f:
                json_data = json.load(f)["legend"]
                p = {}

                for each in json_data:
                    if json_data[each]['levels']!=[]:
                        p[each] = {}
                        cmap = np.array(json_data[each]['colors']) / 255
                        p[each]["cmap"] = ListedColormap(list(map(tuple, cmap)))
                        p[each]["norm"] = BoundaryNorm(
                            json_data[each]['levels'], p[each]["cmap"].N)
                        p[each]["levels"] = json_data[each]['levels']

            self.colormap[proj] = p

        if len(self.colormap) == 0:
            raise ValueError('色标文件为空')

    def get(self, projName):
        return self.colormap[projName]

    # 加载本地色标
    def __loadColorFile(self, projName):

        regstr = re.compile(r'^' + projName + '_colormap.json$')

        colorFile = ''
        for parent, dirnames, filenames in os.walk('./asserts'):
            for filename in filenames:
                if regstr.search(filename):
                    colorFile = os.path.join(parent, filename)
                    break

        return colorFile
