import numpy as np
from utils import *
from Face import Face
from abc import ABC, abstractmethod

class Mesh(ABC):
    def __init__(self, faces:list[Face], ka, kd, ke, shininess):
        self.faces = faces
        self.ka = ka
        self.kd = kd
        self.ke = ke
        self.shininess = shininess

    def facecheck(self, p, face:Face):
        area = np.dot(cross(face.vertices[1] - face.vertices[0], face.vertices[2] - face.vertices[0]), face.normal)
        c1 = np.dot(cross(face.vertices[0] - p, face.vertices[1] - p), face.normal)/area   
        c2 = np.dot(cross(face.vertices[2] - p, face.vertices[0] - p), face.normal)/area
        c3 = 1 - c1 - c2

        return c1 > 0.0 and c2 > 0.0 and c3 > 0.0


    def FaceIntersection(self, face:Face, origin, direction):
        t = min(face.faceplane.intersection(origin, direction))
        p = origin + direction*t

        if(self.facecheck(p, face)):
            return t
        return np.inf


    def AllFaceIntersection(self, origin, direction):
        intersection_point = np.inf
        t = 0
        normal = 0

        for face in self.faces:
            if(np.dot(face.normal, direction) < 0):
                t = self.FaceIntersection(face, origin, direction)
                if(t < intersection_point):
                    intersection_point = t
                    normal = face.normal
        return intersection_point, normal