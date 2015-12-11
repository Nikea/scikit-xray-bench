if __name__ == "__main__":
    from skxray.core.accumulators.histogram import Histogram
    import numpy as np
    from time import time

    axis_x = [1000, 0, 10.01]
    axis_y = [900, 0, 9.01]

    nelems = 50000000

    xdata = np.linspace(0, 10, nelems)
    ydata = np.linspace(0, 10, nelems)

    h = Histogram(axis_x, axis_y)
    t0 = time()
    h.fill(xdata, ydata)
    t1 = time()

    print('elements binned per second = %s' % (nelems / (t1-t0)))
