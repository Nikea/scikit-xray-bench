from skxray.core import correlation
import numpy as np

class FakeStack:
    """Fake up a big pile of images that are identical
    """
    def __init__(self, img_shape, maxlen):
        """

        Parameters
        ----------
        img_shape : tuple
            Tuple of the dimensions of the thing to fake up.
            For an image, pass in (rr, cc)
        maxlen : int
            The maximum number of images to fake up
        """
        self.img = np.ones(img_shape, dtype=int)
        self.maxlen = maxlen

    def __len__(self):
        return self.maxlen

    def __getitem__(self, item):
        if item > len(self):
            raise IndexError
        return self.img


class TimeSuite:
    params = [[100, 512], [100, 1000]]
    param_names = ['img_shape', 'num_imgs']

    def setup(self, x, z):
        self.stack = FakeStack(img_shape=(x, x), maxlen=z)

    def time_whole_image_correlation(self, x, z):
        num_levels = 100
        num_bufs = 8
        img_mesh = np.ones_like(self.stack[0])

        g2, lag_steps = correlation.multi_tau_auto_corr(num_levels, num_bufs,
                                                        img_mesh, self.stack)

        assert np.all(g2[:, 0], axis=0)
