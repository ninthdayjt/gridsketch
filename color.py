from matplotlib.colors import ListedColormap, BoundaryNorm, Normalize


class COLOR:

    def getColor(self, type):
        if type == 'TEM':
            self.__tem()
        elif type == 'PRE1H':
            self.__pre1h()
        elif type == 'PRE45D':
            self.__pre45d()
        elif type == 'PRE5D':
            self.__pre5d()
        elif type == 'PRE1D':
            self.__pre1d()
        elif type == 'WIND':
            self.__wind()
        elif type == 'RHU':
            self.__rhu()
        elif type == 'PROB':
            self.__probability()
        elif type == 'PRERANDOM':
            self.__prerandom()

        return (self.cmap, self.norm)

    def __init__(self):
        self.cmap = None
        self.norm = None

    def __tem(self):
        self.cmap = ListedColormap(['#0033cc', '#0066ff', '#3399ff', '#00ccff', '#00ffff', '#66ffcc', '#00ff00',
                                    '#99ff66', '#ccff33', '#ffff00', '#ffcc00', '#ff9900', '#ff6600', '#ff0000', '#cc0000', '#990000'])
        self.cmap.set_under('#000099')
        self.cmap.set_over('#660000')
        self.cmap.set_bad((0, 0, 0, 0))

        self.norm = BoundaryNorm(
            [-30, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50], self.cmap.N)

    def __pre1h(self):
        self.cmap = ListedColormap(
            ['#ccffcc', '#33cc99', '#00cc00', '#66ccff', '#0033ff', '#006600',  '#ff00ff', '#ff6600'])
        self.cmap.set_under((0, 0, 0, 0))
        self.cmap.set_over('#990000')
        self.cmap.set_bad((0, 0, 0, 0))

        self.norm = BoundaryNorm(
            [0.001, 1, 2, 4, 6, 8, 10, 20, 50], self.cmap.N)

    def __pre1d(self):

        self.cmap = ListedColormap(
            ['#ccffcc',  '#00cc00', '#66ccff', '#0033ff',  '#ff00ff'])
        self.cmap.set_under((0, 0, 0, 0))
        self.cmap.set_over('#990000')
        self.cmap.set_bad((0, 0, 0, 0))
        self.norm = BoundaryNorm(
            [0.1, 10, 25, 50, 100, 250], self.cmap.N)

        # self.cmap = 'GnBu'
        # self.norm = Normalize(vmin=0.1)

    def __pre5d(self):
        self.cmap = 'gist_ncar'
        self.norm = Normalize(vmin=0, vmax=600)

    def __pre45d(self):
        self.cmap = 'gist_ncar'
        self.norm = Normalize(vmin=0, vmax=1200)

    def __wind(self):
        self.cmap = ListedColormap(
            ['#00cc00', '#ccffcc', '#ffff00', '#ffcc00', '#ff9900', '#ff6600', '#ff0000', '#cc0000', '#990000', '#660000'])
        self.cmap.set_under((0, 0, 0, 0))
        self.cmap.set_over('#660000')
        self.cmap.set_bad((0, 0, 0, 0))
        self.norm = BoundaryNorm(
            [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], self.cmap.N)

    def __rhu(self):
        self.cmap = ListedColormap(
            ['#990000', '#ff6600', '#ff9900', '#ffcc00', '#ffff00', '#ccff33', '#66ffcc', '#00ccff', '#0066ff', '#000099'])

        self.norm = BoundaryNorm(
            [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], self.cmap.N)
        #self.cmap = 'RdYlBu'
        #self.norm = Normalize(vmin=0, vmax=100)

    def __probability(self):
        self.cmap = 'plasma'
        self.norm = Normalize(vmin=0, vmax=100)

    def __prerandom(self):
        self.cmap = 'gist_ncar'
        self.norm = None
