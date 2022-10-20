from math import *
import numpy as np
from utils import *
from Object import Object
from Plane import Plane


class Cylinder(Object):

    intersection_type = np.inf

    def __init__(self, center, raio, altura, direction, ka, kd, ke, s):
        self.center = center
        self.radius = raio
        self.h = altura
        self.direction = direction
        super().__init__(ka, kd, ke, s)
        self.M = getCylinderM(direction)
        self.ctop = center + altura*direction
        self.base = Plane(center, -direction, ka, kd, ke, s)
        self.top = Plane(center + altura*direction, direction, ka, kd, ke, s)

    def intersection(self, origin, direction):
        intersection_point = np.inf
        t_base = np.inf
        t_corpo = np.inf
        t_topo = np.inf

        w = direction - self.direction*np.dot(direction, self.direction)

        v1 = origin - self.center
        v2 = self.direction*np.dot(v1, self.direction)

        v = v1 - v2

        a = np.dot(w, w)
        b = 2*np.dot(v, w)
        c = np.dot(v, v) - self.radius*self.radius

        delta = b*b - 4*a*c

        if delta < 0:
            return np.inf, np.inf

        t1 = (-b + np.sqrt(delta)) / (2*a)
        t2 = (-b - np.sqrt(delta)) / (2*a)

        if(min(t1, t2) > 0 and min(t1, t2) < t_corpo):
            t_corpo = min(t1, t2)
            p = origin + t_corpo*direction
            proj = self.projection(p)
            if(proj < 0 or proj > self.h):
                t_corpo = np.inf

        t_b = min(self.base.intersection(origin, direction))

        if (t_b > 0 and t_b < t_base):
            t_base = t_b
            p_base = origin + t_base*direction
            cp = np.linalg.norm(p_base - self.center)
            if(cp > self.radius):
                t_base = np.inf
            

        t_t = min(self.top.intersection(origin, direction))

        if (t_t > 0 and t_t < t_topo):
            t_topo = t_t
            p_topo = origin + t_topo*direction
            cp = np.linalg.norm(p_topo - self.ctop)
            if(cp > self.radius):
                t_topo = np.inf

        intersection_point = min(t_corpo, t_topo, t_base)
        if(intersection_point == t_corpo): self.intersection_type = 0
        if(intersection_point == t_base): self.intersection_type = 1
        if(intersection_point == t_topo): self.intersection_type = 2

        return intersection_point, intersection_point


    def getNormal(self, p):
        if self.intersection_type == 0:
            n = matrix_per_vector(self.M, p - self.center)
            return normalize(n)
        elif(self.intersection_type == 1):
            return normalize(-self.direction)

        return normalize(self.direction)

    def projection(self, p):
        projection = np.dot(p-self.center, self.direction)
        return projection
