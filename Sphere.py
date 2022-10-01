from math import *
import numpy as np
from utils import *

class Sphere():
    def __init__(self, center, radius, color, kd, ka, ke, specular):
        self.center=center
        self.radius=radius
        self.colour=color
        self.kd = kd
        self.ke = ke
        self.ka = ka
        self.specular = specular
    
    '''ray_direction é um vetor normalizado com a direção do raio'''
    def intersection(self, origin, ray_direction):
        OS = origin - self.center
        a = np.dot(ray_direction, ray_direction)
        b = 2*np.dot(ray_direction, OS)
        c = np.dot(OS, OS) - self.radius * self.radius

        delta = b*b - 4*a*c

        if delta > 0:
            t1 = (-b+sqrt(delta))/2*a
            t2 = (-b-sqrt(delta))/2*a

            return (t1, t2)

        return (np.inf, np.inf)
    
    def getNormal(self, p):
        return (p - self.center)/self.radius