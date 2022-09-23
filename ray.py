from lib import *
from sphere import *

class Raytracer(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.background_color = color(0,0,0)
        self.current_color = color(255,255,255)
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
        s = Sphere(V3(-3,0,-16), 2)
        intersection = s.ray_intersect(origin, direction)

        if intersection:
            return color(255,0,0)
        else:
            return color(0,0,0)