from math import *
import numpy as np
from utils import *
from Object import Object
from Plane import Plane


class Cone(Object):
    
    intersection_type = np.inf

    def __init__(self, center, raio, altura, direction, ka, kd, ke, s, has_base = True):
        self.center = center
        self.radius = raio
        self.h = altura
        self.direction = direction
        self.v = direction*altura + center
        self.has_base = has_base
        super().__init__(ka, kd, ke, s)
        if has_base:
            self.base = Plane(center, -direction, ka, kd, ke, s)
        else:
            self.base = None


    def intersection(self, origin, direction):
        intersection_point = np.inf
        t_corpo = np.inf
        t_base = np.inf

        w = self.v - origin

        costheta = self.h*self.h /(self.radius*self.radius + self.h*self.h)

        drdc = np.dot(direction, self.direction)
        DD = np.dot(direction, direction)
        wdr = np.dot(w, direction)
        wdc = np.dot(w, self.direction)
        ww = np.dot(w, w)

        a = drdc*drdc - DD*costheta
        b =  2*(np.dot(w, direction)*costheta - wdc*drdc)
        c = wdc*wdc - np.dot(w, w)*costheta

        delta = b*b - 4*a*c

        if(delta < 0):
            return np.inf, np.inf
        
        t1 = (-b + np.sqrt(delta)) / (2*a)
        t2 = (-b - np.sqrt(delta)) / (2*a)

        if(min(t1, t1)>0 and min(t1, t2) < t_corpo):
            t_corpo = min(t1,t2)
            p = origin + t_corpo*direction
            proj = self.projection(p)
            if(proj < 0 or proj > self.h):
                t_corpo = np.inf

        t_b = min(self.base.intersection(origin, direction))

        if (t_b > 0 and t_base < t_b):
            t_base = t_b
            p_base = origin + t_base*direction
            cb = np.linalg.norm(p_base - self.center)
            if(cb > self.radius):
                t_base = np.inf

        intersection_point = max(0, min(t_corpo, t_base))
        if(intersection_point == t_corpo): self.intersection_type = 0
        if(intersection_point == t_base): self.intersection_type = 1

        return intersection_point, intersection_point



    def getNormal(self, p):
        pv = self.v - p
        if self.intersection_type == 0:
            n = cross(pv, self.direction)
            return normalize(cross(n, pv))
        else:
            return normalize(-self.direction)

    def projection(self, p):
        projection = np.dot(self.v - p, self.direction)
        return projection