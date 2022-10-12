from lib import *
from intersect import *
from plane import Plane

class Square(object):
    def __init__(self, center, size, material):
        self.center = center
        self.size = size
        self.material = material

        self.planes = []

        w, h = size[0] / max(1, abs(center.z)), size[1] / max(1, abs(center.z))

        self.planes.append( Plane(V3(center.x+(w/2), center.y, center.z), w, h, material, V3(1,0,0)))
        self.planes.append( Plane(V3(center.x-(w/2), center.y, center.z), w, h, material, V3(1,0,0)))


        self.planes.append( Plane(V3(center.x, center.y+(h/2), center.z), w, h, material, V3(0,1,0)))
        self.planes.append( Plane(V3(center.x, center.y-(h/2), center.z), w, h, material, V3(0,1,0)))

        self.planes.append( Plane(V3(center.x, center.y, center.z+(w/2)), w, h, material, V3(0,0,1)))
        self.planes.append( Plane(V3(center.x, center.y, center.z-(w/2)), w, h, material, V3(0,0,1)))

    def ray_intersect(self, origin, direction):
        for plane in self.planes:
            plane_intersect = plane.ray_intersect(origin, direction)

            if plane_intersect is not None:        
                    return plane_intersect

        return None