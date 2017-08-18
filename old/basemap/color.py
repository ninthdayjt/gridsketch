from matplotlib.colors import ListedColormap, BoundaryNorm


class COLOR:

    def getColor(self, type):
        if type == 'TEM':
            self.__tem()
        elif type == 'PRE':
            self.__pre()
        elif type == 'WIND':
            self.__wind()
        elif type == 'RHU':
            self.__rhu()

        return (self.cmap, self.norm)

    def __init__(self):
        self.cmap = None
        self.norm = None

    def __tem(self):
        self.cmap = ListedColormap(['#221C8D', '#0705EC', '#4059F1', '#3E87EB', '#76b7e7', '#89dfef', '#aaeffc', '#afe68f',
                                    '#d6e66e', '#f7dc3b', '#fbb92e', '#fb9b35', '#ff7a18', '#fd5e00', '#e71208', '#d20f06', '#9f043a', '#81032f'])

        self.norm = BoundaryNorm([-999, -30, -25, -20, -15, -10, -5,
                                  0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 999], self.cmap.N)

    def __pre(self):

        self.cmap = ListedColormap(
            ['#b4d7a5', '#79cf61', '#35bb34', '#5bb9f9', '#0000fb', '#007249', '#ff00f2', '#eb4900', '#740402'])

        self.norm = BoundaryNorm(
            [0, 1, 2, 4, 6, 8, 10, 20, 50, 999], self.cmap.N)

    def __wind(self):

        self.cmap = ListedColormap(
            ['#e6a96e', '#f7dc3b', '#baf894', '#89dfef', '#3e87eb', '#0541ec'])

        self.norm = BoundaryNorm([0, 3, 5, 7, 9, 12, 999], self.cmap.N)

    def __rhu(self):

        self.cmap = ListedColormap(
            ['#973100', '#ea7116', '#ff992a', '#fec34f', '#fee48f', '#bddef0', '#7fbad9', '#4394c3', '#1f63ac', '#053160'])

        self.norm = BoundaryNorm(
            [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], self.cmap.N)
