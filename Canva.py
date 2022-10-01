import numpy as np

class Canva():
    
    def __init__(self, height, width, background_color):
        self.height = height
        self.width = width
        self.background = background_color
        self.pixels = np.zeros([height, width, 3])

    def paint(self, i, j, color):
        self.pixels[i, j] = np.clip(color, 0, 1)

