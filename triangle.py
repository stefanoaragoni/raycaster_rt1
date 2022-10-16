from lib import *
from intersect import *

class Triangle(object):
    def __init__(self, vertices, material):
        self.vertices = vertices
        self.material = material


    def ray_intersect(self, origin, direction):
        v0, v1, v2 = self.vertices

        normal = cross(sub(v1, v0), sub(v2, v0))
        normal = mul(normal, -1)

        if abs(dot(normal, direction)) < 0.0001:
            return None

        distance = dot(normal, v0)
        t = (dot(normal, origin) + distance) / (dot(normal, direction))
        if t < 0:
            return None

        point = sum(origin, mul(direction, t))
        w, v, u = barycentric(v0.x, v0.y, v1.x, v1.y, v2.x, v2.y, point.x, point.y)

        if w < 0 or v < 0 or u < 0:
            return None
        
        return Intersect(distance, point, norm(normal))



