from abc import ABC, abstractmethod

class Object(ABC):
    def __init__(self, ka, kd, ke, shininess):
        self.ka = ka
        self.kd = kd
        self.ke = ke
        self.shininess = shininess

    @abstractmethod
    def intersection(self, origin, direction):
        pass