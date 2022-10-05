from importlib.util import spec_from_file_location
from lib import *
from sphere import *
from material import *
from light import *

MAX_RECURSION_DEPTH = 3


class Raytracer(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.background_color = color(0,0,0)
        self.current_color = color(255,255,255)
        self.scene = []
        self.light = Light(V3(0,0,0), 1, color(255,255,255))
        self.clear()

    def clear(self):
        self.framebuffer = [
            [ self.background_color for y in range(self.height)]
            for x in range(self.width) 
        ]

    def point(self, x, y, c = None):
        if y >= 0 and y < self.height and x >= 0 and x < self.width:
            self.framebuffer[x][y] = c or self.current_color

    def write(self, name='out.bmp'):
        self.writebmp(name)

    def writebmp(self, name):
        f = open(name, 'bw')

        # File header (14 bytes)
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(14 + 40))

        # Image header (40 bytes)
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        for y in range(self.height-1, -1, -1):
            for x in range(self.width):
                try:
                    f.write(self.framebuffer[x][y])
                except:
                    f.write(color(0,0,0))

        f.close()

    def render(self):
        fov = int(pi/2)
        ar = self.width/self.height
        tana = tan(fov/2)
        
        for x in range(self.width):
            for y in range(self.height):

                i = (2 * (x + 0.5) / self.width - 1) * ar * tana
                j = (1 - (2 * (y + 0.5) / self.height)) * tana

                origin = V3(0,0,0)
                direction = norm(V3(i, j, -1))

                c = self.cast_ray(origin, direction)
                self.point(x,y,c)

    def cast_ray(self, origin, direction):
        material, intersect = self.scene_intersect(origin, direction)

        if material is None:
            return self.background_color

        light_dir = norm(sub(self.light.position, intersect.point))

        #shadow
        shadow_bias = 1.1
        shadow_origin = sum(intersect.point, mul(intersect.normal, shadow_bias))
        shadow_material, shadow_intersect = self.scene_intersect(shadow_origin, light_dir)


        shadow_intensity = 1
        if shadow_material:
            shadow_intensity = 0.3

        #diffuse
        diffuse_intensity = dot(light_dir, intersect.normal)

        if diffuse_intensity < 0:
            return self.background_color

        #specular
        light_reflection = reflect(light_dir, intersect.normal)
        reflection_intensity = max(0, dot(light_reflection, direction))
        specular_intensity = reflection_intensity ** material.spec
        specular = color(
            self.light.c[0] * specular_intensity * material.albedo[1],
            self.light.c[1] * specular_intensity * material.albedo[1],
            self.light.c[2] * specular_intensity * material.albedo[1])


        diffuse = color(
            int(((material.diffuse[2] * diffuse_intensity * material.albedo[0] * shadow_intensity) + specular[2])),
            int(((material.diffuse[1] * diffuse_intensity * material.albedo[0] * shadow_intensity) + specular[1])),
            int(((material.diffuse[0] * diffuse_intensity * material.albedo[0] * shadow_intensity) + specular[0]))
        )
        
        return diffuse


    def scene_intersect(self, origin, direction):
        zbuffer = 9999
        material = None
        intersect = None

        for o in self.scene:
            object_intersect = o.ray_intersect(origin, direction)

            if object_intersect:
                if object_intersect.distance < zbuffer:
                    zbuffer = object_intersect.distance
                    material = o.material
                    intersect = object_intersect
            
        return material, intersect