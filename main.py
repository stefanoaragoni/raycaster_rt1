from ray import *
from lib import *
from material import *
from light import *

red = Material(diffuse=color(200,0,0), albedo = [0.6, 0.3, 0], spec = 50)
mirror = Material(diffuse=color(200,0,0), albedo = [0.6, 0.3,0.8], spec = 50)

r = Raytracer(800,600)

r.light = Light(V3(-20, 20, 20), 2, color(255, 255, 255))
r.scene = [
    Sphere(V3(0, -1.5, -8), 1.5, red),
    Sphere(V3(-2, -1, -12), 2, mirror),
    # Sphere(V3(1, 1, -8), 1.7, rubber),
    # Sphere(V3(-2, 2, -10), 2, mirror),
]

r.render()
r.write()
