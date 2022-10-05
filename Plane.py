from math import *
import numpy as np




class Plane():
    def __init__(self, center, normal, colour, ka, ke, kd, s):
        self.center=center
        self.normal = normal
        self.colour=colour
        self.ka = ka
        self.kd = kd
        self.ke=ke
        self.shininess = s
    
    
    '''ray_direction é um vetor normalizado com a direção do raio'''
    def intersection(self, origin, ray_direction):
        w = origin - self.center
        num = np.dot(w, self.normal)
        denom = np.dot(ray_direction, self.normal)

        if(denom == 0):
            return np.inf, np.inf
        t = -num/denom

        if (t < 0):
            return np.inf, np.inf
        
        return t, np.inf
    
    def getNormal(self, s):
        return self.normal