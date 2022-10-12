from math import atan2, acos, pi
import struct

class Envmap(object):
    def __init__(self, path):
        self.path = path
        self.read()

    def read(self):
        with open(self.path, "rb") as image:
            image.seek(2 + 4 + 4) 
            header_size = struct.unpack("=l", image.read(4))[0] 
            image.seek(2 + 4 + 4 + 4 + 4)
            
            self.width = struct.unpack("=l", image.read(4))[0]
            self.height = struct.unpack("=l", image.read(4))[0]

            image.seek(header_size)

            self.pixels = [
                [ bytes([0, 0, 0]) for y in range(self.height)]
                for x in range(self.width) 
            ]

            for y in range(self.height):
                self.pixels.append([])
                for x in range(self.width):
                    b = ord(image.read(1))
                    g = ord(image.read(1))
                    r = ord(image.read(1))

                    color = bytes([b, g, r])

                    self.pixels[y][x] = color

    def get_color(self, direction, info):
        x = atan2(direction.z, direction.x) / (2 * pi) + 0.5
        y = acos(-direction.y) / pi

        x = int(x) * self.width
        y = int(y) * self.height

        try:
            return self.pixels[info[1]][info[0]]
        except:
            return bytes([0, 0, 0])




