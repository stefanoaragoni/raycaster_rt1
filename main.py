from ray import *
from lib import *
from material import *
from light import *

red = Material(diffuse=color(200,0,0), albedo = [0.6, 0.3], spec = 50)
brown = Material(diffuse=color(253,198,168), albedo=[1, 0], spec=0)
brown2 = Material(diffuse=color(232,139,72), albedo=[1, 0], spec=0)

ivory = Material(diffuse=color(250,250,250), albedo = [0.9, 0.1], spec = 50)
white = Material(diffuse=color(255,255,255), albedo=[0.5, 0.5], spec=0)
white2 = Material(diffuse=color(255,255,255), albedo=[0.3, 0.7], spec=0)

black = Material(diffuse=color(0,0,0), albedo=[0.4, 0.6], spec=4)

r = Raytracer(800,600)

r.light = Light(V3(-20, 20, 20), 2, color(255, 255, 255))
r.scene = [
    Sphere(V3(0, -1.5, -10), 1.5, ivory),
    Sphere(V3(-2, -1, -12), 2, brown),
    Sphere(V3(1, 1, -8), 1.7, brown),
    Sphere(V3(-2, 2, -10), 2, ivory),
]

r.render()
r.write()
