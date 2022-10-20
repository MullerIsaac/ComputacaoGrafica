import numpy as np


def normalize(x):
    x /= np.linalg.norm(x)
    return x

def vec_product(x, y):
    return np.array([x[0]*y[0], x[1]*y[1], x[2]*y[2]])

    
def getCylinderM(direction):
    M = np.zeros([3, 3])
    I = np.eye(3)

    for i in range(3):
        for j in range(3):
            M[i, j] = direction[i]*direction[j]

    M = I - M

    return M

def matrix_per_vector(M, v):
    v = np.array([
        M[0,0]*v[0]+M[0,1]*v[1]+ M[0,2]*v[2],
        M[1,0]*v[0]+M[1,1]*v[1]+ M[1,2]*v[2],
        M[2,0]*v[0]+M[2,1]*v[1]+ M[2,2]*v[2]
    ])
    return v

