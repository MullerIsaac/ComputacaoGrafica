import numpy as np
from Mesh import Mesh
from utils import *
from Face import Face

class Cube(Mesh):
    
    normal = np.array([0, 0, 0])

    def __init__(self, center, edge_len, ka, kd, ke, shininess):
        vertices = [
            np.array([center[0] - edge_len/2, center[1] - edge_len/2, center[2] + edge_len/2]),
            np.array([center[0] + edge_len/2, center[1] - edge_len/2, center[2] + edge_len/2]),
            np.array([center[0] + edge_len/2, center[1] + edge_len/2, center[2] + edge_len/2]),
            np.array([center[0] - edge_len/2, center[1] + edge_len/2, center[2] + edge_len/2]),
            np.array([center[0] - edge_len/2, center[1] + edge_len/2, center[2] - edge_len/2]),
            np.array([center[0] - edge_len/2, center[1] - edge_len/2, center[2] - edge_len/2]),
            np.array([center[0] + edge_len/2, center[1] - edge_len/2, center[2] - edge_len/2]),
            np.array([center[0] + edge_len/2, center[1] + edge_len/2, center[2] - edge_len/2])
        ]

        cube_faces = [
            Face(np.array([vertices[0], vertices[1], vertices[3]]), ka, kd, ke, shininess),
            Face(np.array([vertices[1], vertices[2], vertices[3]]), ka, kd, ke, shininess),
            Face(np.array([vertices[1], vertices[6], vertices[2]]), ka, kd, ke, shininess),
            Face(np.array([vertices[2], vertices[6], vertices[7]]), ka, kd, ke, shininess),
            Face(np.array([vertices[5], vertices[7], vertices[6]]), ka, kd, ke, shininess),
            Face(np.array([vertices[5], vertices[4], vertices[7]]), ka, kd, ke, shininess),
            Face(np.array([vertices[0], vertices[4], vertices[5]]), ka, kd, ke, shininess),
            Face(np.array([vertices[3], vertices[4], vertices[0]]), ka, kd, ke, shininess),
            Face(np.array([vertices[4], vertices[2], vertices[7]]), ka, kd, ke, shininess),
            Face(np.array([vertices[4], vertices[3], vertices[2]]), ka, kd, ke, shininess),
            Face(np.array([vertices[0], vertices[5], vertices[1]]), ka, kd, ke, shininess),
            Face(np.array([vertices[1], vertices[5], vertices[6]]), ka, kd, ke, shininess),
        ]

        super().__init__(cube_faces, ka, kd, ke, shininess)


    def getNormal(self, p):
        return self.normal
        
    def intersection(self, origin, direction):
        intersection_point, normal = super().AllFaceIntersection(origin, direction)
        self.normal = normal
        return intersection_point, intersection_point
        