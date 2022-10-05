from Sphere import Sphere
from Plane import Plane
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

scene.add_object(Sphere(np.array([0, 0, -100]), 40, np.array([1, 0, 0]), np.array([0.7, 0.2, 0.2]), np.array([0.7, 0.2, 0.2]), np.array([0.7, 0.2, 0.2]), 10))
scene.add_object(Plane(np.array([0, -40, 0]), np.array([0, 1, 0]), np.array([1, 0, 0]), np.array([0.2, 0.7, 0.2]), np.array([0.2, 0.7, 0.2]), np.array([0.0, 0.0, 0.0]), 1))
scene.add_object(Plane(np.array([0, 0, -200]), np.array([0, 0, 1]), np.array([1, 0, 0]), np.array([0.3, 0.3, 0.7]), np.array([0.3, 0.3, 0.7]), np.array([0.0, 0.0, 0.0]), 1))
scene.add_light(light)

scene.draw()

scene.save("image.jpg")