from math import *
import numpy as np
from Object import Object

class Plane(Object):
    def __init__(self, center, normal,ka, kd, ke, s):
        self.center=center
        self.normal = normal
        super().__init__(ka, kd, ke, s)
    
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