from ray import *
from lib import *

r = Raytracer(800,600)
r.scene = [
    #brazos
    Sphere(V3(0,2.5,-16), 2.5, color(101,67,33)),
    Sphere(V3(0,2.7,-16), 2.5, color(0,0,0)),

    #circulos principales
    Sphere(V3(0,-2.8,-16), 2.7, color(243, 246, 251)),
    
    Sphere(V3(0,1,-16), 1.90, color(0, 0, 0)),
    Sphere(V3(0,1,-16), 1.87, color(243, 246, 251)),

    Sphere(V3(0,3.7,-16), 1.155, color(0, 0, 0)),
    Sphere(V3(0,3.7,-16), 1.125, color(243, 246, 251)),

    #sonrisa
    Sphere(V3(0,3.5,-16), 0.5, color(0, 0, 0)),
    Sphere(V3(0,3.6,-16), 0.5, color(243, 246, 251)),

    #ojos
    Sphere(V3(-0.25,4.1,-16), 0.14, color(0, 0, 0)),
    Sphere(V3(0.25,4.1,-16), 0.14, color(0, 0, 0)),

    #nariz
    Sphere(V3(0,3.6,-16), 0.14, color(255, 140, 0)),
    Sphere(V3(-0.1,3.5,-16), 0.10, color(255, 140, 0)),

    #botones
    Sphere(V3(0,1,-16), 0.14, color(0, 0, 0)),
    Sphere(V3(0,2,-16), 0.14, color(0, 0, 0)),
    Sphere(V3(0,0,-16), 0.14, color(0, 0, 0)),
]
r.render()
r.write()
