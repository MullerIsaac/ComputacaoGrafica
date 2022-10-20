from math import *
import numpy as np
from utils import *
from Object import Object

class Sphere(Object):
    def __init__(self, center, radius, ka, kd, ke, s):
        self.center=center
        self.radius=radius
        super().__init__(ka, kd, ke, s)
    
    '''ray_direction é um vetor normalizado com a direção do raio'''
    def intersection(self, origin, ray_direction):
        OS = origin - self.center
        a = np.dot(ray_direction, ray_direction)
        b = 2*np.dot(ray_direction, OS)
        c = np.dot(OS, OS) - self.radius * self.radius

        delta = b*b - 4*a*c

        if delta >= 0:
            t1 = (-b+sqrt(delta))/2*a
            t2 = (-b-sqrt(delta))/2*a

            return (t1, t2)

        return (np.inf, np.inf)
    
    def getNormal(self, p):
        return (p - self.center)/self.radius