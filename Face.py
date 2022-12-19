import numpy as np
from utils import *
from Plane import Plane

class Face():
    def __init__(self, vertices, ka, kd, ke, s):
        self.vertices = vertices
        normal = normalize(cross(vertices[1] - vertices[0], vertices[2] - vertices[0]))
        self.normal = normal
        self.faceplane = Plane(vertices[0], normal, ka, kd, ke, s)