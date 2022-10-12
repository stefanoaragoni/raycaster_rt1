from lib import *
from intersect import *

class Plane(object):
    def __init__(self, center, w=1, h=1, material=None, normal = V3(0, 1, 0)):
        self.center = center
        self.w = w
        self.h = h
        self.material = material
        self.normal = normal

    def ray_intersect(self, origin, direction):

        distance = -(((self.center.y + origin.y)) / direction.y)
        hit_point = sum(mul(direction, distance), origin)

        if ((distance <= 0) or (hit_point.x > (self.center.x + (self.w / 2))) or (hit_point.x < (self.center.x - (self.w / 2))) or (hit_point.z > (self.center.z + (self.h / 2))) or (hit_point.z < (self.center.z - (self.h / 2)))):
            return None

        # Retorno de la función.
        return Intersect(distance, hit_point, self.normal)

