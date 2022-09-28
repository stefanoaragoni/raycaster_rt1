from ray import *
from lib import *
from material import *
from light import *

brown = Material(diffuse=color(101,67,33))
black = Material(diffuse=color(0,0,0))
orange = Material(diffuse=color(255,140,0))
white = Material(diffuse=color(243,246,251))

r = Raytracer(800,600)
r.light = Light(position=V3(0,0,0), intensity=1)

r.scene = [
    #brazos
    Sphere(V3(0,-0.5,-16), 2.5, white),
    Sphere(V3(0,2.5,-20), 1.5, orange)
]
r.render()
r.write()
