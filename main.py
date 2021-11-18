import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from astropy import constants as const
from astropy import units as u


class Star:
    def __init__(self, radius, T):
        self.radius = radius
        self.T = T

    @property
    def luminosity(self): # temp in K, radius in Solar Radii
        luminosity = 4 * np.pi * self.radius ** 2 * const.k_B * self.T ** 4
        return luminosity

    @property
    def spectral_class(self):
        """Spectral classification based on https://lweb.cfa.harvard.edu/~pberlind/atlas/htmls/note.html

        Returns:
            string: spectral class of the star based on temp
        """
        if self.T < 3500:
            return "M"
        elif self.T < 5000:
            return "K"
        elif self.T < 6000:
            return "G"
        elif self.T < 7500:
            return "F"
        elif self.T < 10000:
            return "A"
        elif self.T < 25000:
            return "B"
        else:
            return "O"

    @property
    def absolute_magnitude(self):
        # M - 0 = -2.5 log_10 (L / L_0)
        abs_magnitude = -2.5 * np.log10(self.luminosity / const.L_bol0)
        return abs_magnitude

class HRDiagram:
    def __init__(self, num_stars):
        self.num_stars = num_stars

        # This is a list of Star objects in our simulated galaxy/cluster
        self.stars = []

        self.initialize()

    def initialize(self):
        pass # TODO

    def plot(self):
        fig = plt.figure(figsize=(10, 10))
        plt.title("HR Diagram ({} stars)".format(self.num_stars))
        plt.xlabel("Effective Temperature")
        plt.ylabel("Luminosity")
        plt.show()

if __name__ == "__main__":
    num_stars = 100
    hr_diagram = HRDiagram(num_stars)
    hr_diagram.plot()
    # Then save this plot as an image
