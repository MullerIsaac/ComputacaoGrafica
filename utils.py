import numpy as np


def normalize(x):
    x /= np.linalg.norm(x)
    return x

def vec_product(x, y):
    return np.array([x[0]*y[0], x[1]*y[1], x[2]*y[2]])
