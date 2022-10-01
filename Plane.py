from math import *
import numpy as np




class Plane():
    def __init__(self, center, normal, colour, ka, ke, kd):
        self.center=center
        self.normal = normal
        self.colour=colour
        self.ka = ka
        self.kd = kd
        self.ke=ke
    
    
    '''ray_direction é um vetor normalizado com a direção do raio'''
    def intersection(self, origin, ray_direction):
        pass
    
    def getNormal(self, s):
        return self.normal