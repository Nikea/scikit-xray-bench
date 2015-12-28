import numpy as np
from skxray.core.accumulators.histogram import Histogram


class TimeSuite:
    params = [10**n for n in range(5, 9)]
    param_names = ['data length']

    def setup(self, n):
        self.axis_x = [1000, 0, 10.01]
        self.axis_y = [900, 0, 9.01]
        self.axis_z = [800, 0, 8.01]
        self.xdata = np.linspace(0, 10, n)
        self.ydata = np.linspace(0, 9, n)
        self.zdata = np.linspace(0, 8, n)

    def time_1d_histogram(self, n):
        h = Histogram(self.axis_x)
        h.fill(self.xdata)

    def time_2d_histogram(self, n):
        h = Histogram(self.axis_x, self.axis_y)
        h.fill(self.xdata, self.ydata)

    def time_3d_histogram(self, n):
        h = Histogram(self.axis_x, self.axis_y, self.axis_z)
        h.fill(self.xdata, self.ydata, self.zdata)
