from Sphere import Sphere
from Scene import Scene
from Canva import Canva
from Viewport import Viewport
from math import *
import numpy as np
import matplotlib.pyplot as plt


eye = np.array([0, 0, 0])
light = np.array([0, 60, -30])

viewport = Viewport(60, 60, -30)
canva = Canva(500, 500, np.array([0.5, 0.5, 0.5]))

scene = Scene(eye, viewport, canva)

scene.add_object(Sphere(np.array([0, 0, -50]), 10, np.array([1, 0, 0]), np.array([0.7, 0.2, 0.2]), np.array([0.7, 0.2, 0.2]), np.array([0.7, 0.2, 0.2]), 10))
scene.add_light(light)

scene.draw()

scene.save("image.jpg")