import numpy as np
import matplotlib.pyplot as plt

from astropy import constants as const
from astropy import units as u

class Star:
    def __init__(self, radius, temperature):
        self.radius = radius
        self.temperature = temperature

    @property
    def luminosity(self):
        luminosity = 0 # TODO
        return luminosity

    @property
    def spectral_class(self):
        spectral_class = "G0" # TODO
        return spectral_class

    @property
    def absolute_magnitude(self):
        abs_magnitude = 0 # TODO
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
