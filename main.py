from Cylinder import Cylinder
from Sphere import Sphere
from Plane import Plane
from Cone import Cone
from Cube import Cube
from Scene import Scene
from Canva import Canva
from Viewport import Viewport
from math import *
import numpy as np
import matplotlib.pyplot as plt


eye = np.array([0, 0, 0])
light = np.array([0, 50, -30])

viewport = Viewport(60, 60, -30)
canva = Canva(500, 500, np.array([0.5, 0.5, 0.5]))

scene = Scene(eye, viewport, canva)


scene.add_object(Sphere(np.array([70, 0, -120]), 15, np.array([0.2, 0.7, 0.2]), np.array([0.2, 0.7, 0.2]), np.array([0.2, 0.7, 0.2]), 10))
scene.add_object(Sphere(np.array([60, -5, -120]), 15, np.array([0.2, 0.7, 0.2]), np.array([0.2, 0.7, 0.2]), np.array([0.2, 0.7, 0.2]), 10))
scene.add_object(Sphere(np.array([80, -5, -120]), 15, np.array([0.2, 0.7, 0.2]), np.array([0.2, 0.7, 0.2]), np.array([0.2, 0.7, 0.2]), 10))

scene.add_object(Cone(np.array([-80, -15, -100]), 15, 25, np.array([0, 1, 0]), np.array([0.2, 0.7, 0.2]), np.array([0.2, 0.7, 0.2]), np.array([0.2, 0.7, 0.2]), 3))
scene.add_object(Cylinder(np.array([-80, -65, -100]), 5, 50, np.array([0, 1, 0]), np.array([0.3, 0.2, 0.1]), np.array([0.3, 0.2, 0.1]), np.array([0.3, 0.2, 0.1]), 1))

scene.add_object(Plane(np.array([0, -40, 0]), np.array([0, 1, 0]), np.array([0.2, 0.5, 0.2]), np.array([0.2, 0.5, 0.2]), np.array([0.0, 0.0, 0.0]), 1))
scene.add_object(Plane(np.array([0, 0, -200]), np.array([0, 0, 1]), np.array([0.52, 0.8, 0.98]), np.array([0.5, 0.8, 0.98]), np.array([0.0, 0.0, 0.0]), 1))
scene.add_object(Cylinder(np.array([70, -45, -120]), 5, 40, np.array([0, 1, 0]), np.array([0.3, 0.2, 0.1]), np.array([0.3, 0.2, 0.1]), np.array([0.3, 0.2, 0.1]), 1))
scene.add_object(Cone(np.array([0, 5, -150]), 32, 20, np.array([0, 1, 0]), np.array([0.3, 0.2, 0.2]), np.array([0.3, 0.2, 0.2]), np.array([0.3, 0.2, 0.2]), 50))
scene.add_object(Cube(np.array([0, -20, -150]), 50, np.array([0.7, 0.2, 0.0]), np.array([0.7, 0.2, 0.0]), np.array([0.7, 0.2, 0.0]), 2))

scene.add_light(light)

scene.draw()

scene.save("image.jpg")