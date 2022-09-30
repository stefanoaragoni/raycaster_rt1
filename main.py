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
r.light = Light(position=V3(-10,0,10), intensity=5, c=color(255,255,255))

r.scene = [
    #cuerpo
    Sphere(V3(4,-2.5,-16), 2.5, red),

    #arms
    Sphere(V3(6.5,-1.1,-16), 1.15, brown),
    Sphere(V3(1.5,-1.1,-16), 1.15, brown),

    #feet
    Sphere(V3(6.2,-3.7,-16), 1.15, brown),
    Sphere(V3(1.8,-3.7,-16), 1.15, brown),

    #cabeza
    Sphere(V3(2.32,0.5,-9), 1.2, brown),

    #nose
    Sphere(V3(2.10,0.1,-8), 0.5, brown2),
    Sphere(V3(1.85,0.1,-7), 0.07, black),

    #eyes
    Sphere(V3(1.77,0.5,-6), 0.07, black),
    Sphere(V3(1.37,0.5,-6), 0.07, black),

    #ears
    Sphere(V3(1.3,1.4,-9), 0.4, brown2),
    Sphere(V3(3.3,1.4,-9), 0.4, brown2),

    #////////////////RED/////////////////////
    #cuerpo
    Sphere(V3(-4,-2.5,-16), 2.5, ivory),

    #arms
    Sphere(V3(-6.5,-1.1,-16), 1.15, white),
    Sphere(V3(-1.5,-1.1,-16), 1.15, white),

    #feet
    Sphere(V3(-6.2,-3.7,-16), 1.15, white),
    Sphere(V3(-1.8,-3.7,-16), 1.15, white),

    #cabeza
    Sphere(V3(-2.32,0.5,-9), 1.2, white),

    #nose
    Sphere(V3(-2.10,0.1,-8), 0.5, white2),
    Sphere(V3(-1.85,0.1,-7), 0.07, black),

    #eyes
    Sphere(V3(-1.77,0.5,-6), 0.07, black),
    Sphere(V3(-1.37,0.5,-6), 0.07, black),

    #ears
    Sphere(V3(-1.3,1.4,-9), 0.4, white2),
    Sphere(V3(-3.3,1.4,-9), 0.4, white2)
]
r.render()
r.write()
