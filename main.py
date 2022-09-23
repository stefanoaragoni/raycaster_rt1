from ray import *

r = Raytracer(800,600)
r.scene = [
    Sphere(V3(0,3,-16), 1),
    Sphere(V3(0,0,-16), 2),
    Sphere(V3(0,-3,-16), 3)
]
r.render()
r.write()
