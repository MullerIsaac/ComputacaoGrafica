import numpy as np
import matplotlib.pyplot as plt

from Canva import Canva
from Viewport import Viewport
from utils import *

class Scene():

    objects = []
    light = None

    def __init__(self, origin, viewport:Viewport, canva:Canva):
        self.origin = origin
        self.viewport = viewport
        self.canva = canva
        self.dx = viewport.width/canva.width
        self.dy = viewport.height/canva.height

    def canvaToviewport(self, i, j):
        return np.array([-self.viewport.width/2+self.dx/2+j*self.dx,
         self.viewport.height/2.0 - self.dy/2.0 - i*self.dy, self.viewport.d])

    def add_object(self, object):
        self.objects.append(object)

    def add_light(self, light):
        self.light = light


    def calc_light(self, light_position, p):
        L = normalize(light_position - p)
        return L

    def compute_lightning(self, N, L, R, V, object, isShadowed = False):
        s = object.specular

        fd = max(0, np.dot(L, N))
        fe = pow(max(0, np.dot(R, V)), s)

        fonte = np.array([0.7, 0.7, 0.7])
        ambient = np.array([0.3, 0.3, 0.3])

        diffuse = fd*vec_product(fonte, object.kd)
        e = fe*vec_product(fonte, object.ke) 
        ambient = vec_product(ambient, object.ka)

        if(isShadowed):
            return ambient
        
        return ambient+diffuse+e

    def trace_objects(self, origin, direction, t_min, t_max):
        closest_object = None
        closest_t = np.inf

        for obj in self.objects:
            t1, t2 = obj.intersection(origin, direction)
            if(t1 + 0.00001 >= t_min and t1 <= t_max and t1 < closest_t):
                closest_t = t1
                closest_object = obj
            if(t2 + 0.00001 >= t_min and t2 <= t_max and t2 < closest_t):
                closest_t = t2
                closest_object = obj
        
        if(closest_object == None): 
            return np.inf, closest_object 

        return closest_t, closest_object


    def trace(self, origin, direction, t_min, t_max):
        closest_t = np.inf
        closest_object = None
        intensidade = np.zeros([3, 3])

        closest_t, closest_object = self.trace_objects(origin, direction, t_min, t_max)

        if(closest_object == None):
            return self.canva.background
            
        closest_t = closest_t + 0.001
        P = origin + closest_t*direction
        N = closest_object.getNormal(P)
        L = self.calc_light(self.light, P)
        V = normalize(origin - P)
        R = N*(np.dot(L, N)*2)
        
        t, _= self.trace_objects(P, L, t_min, t_max)

        if(t > 0  and t < np.linalg.norm(self.light - P)):
            intensidade = self.compute_lightning(N, L, R, V, closest_object, True)
        else:
            intensidade = self.compute_lightning(N, L, R, V, closest_object)

        return intensidade

    def draw(self):
        for i in range(self.canva.width):
            for j in range(self.canva.height):
                ray_direction = self.canvaToviewport(i, j)
                ray_direction = normalize(ray_direction)
                color = self.trace(self.origin, ray_direction, 1, np.inf)
                self.canva.paint(i, j, color)

    def save(self, name):
        plt.imsave(name, self.canva.pixels)


