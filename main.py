from plane import Plane
from sphere import Sphere
from square import Square
from ray import *
from lib import *
from material import *
from light import *
from envmap import *
from triangle import Triangle
from obj import *


"""
- [20 puntos] Criterio subjetivo. Por qué tan compleja sea su escena
- [30 puntos] Criterio subjetivo. por qué tan visualmente atractiva sea su escena

- [25 puntos | 5 puntos c/u] por cada material diferente que implementen, para un máximo de 5
- [10 puntos] por implementar refracción en al menos uno de sus materiales
- [5 puntos] por implementar reflexión en al menos uno de sus materiales

- [30 puntos] por implementar figuras geométricas distintas a esferas, cubos, rectangulos y planos
   => Se implementó triángulos. También estrellas y piramides/rombos a través de OBJs

- [5 puntos] por implementar un envmap

- [50 puntos] por cargar un modelo obj
    => star.obj, circle.obj

TOTAL: 125 puntos + 50 puntos subjetivos
TOTAL MAXIMO: 175 puntos
"""
r = Raytracer(500,500)

#----------------MATERIALES-----------------#
apple = Material(diffuse = color(130, 0, 0), albedo = [0.9,  0.1, 0, 0], spec = 100)
ivory = Material(diffuse = color(100, 100, 80), albedo = [0.6,  0.3, 0.1, 0], spec = 50)
mirror = Material(diffuse = color(255, 255, 255), albedo = [0, 1, 0.8, 0], spec = 1425)
glass = Material(diffuse = color(150, 180, 200), albedo = [0, 0.5, 0.1, 0.8], spec = 125, refractive_index = 1.5)

wood = Material(diffuse = color(100, 50, 0), albedo = [0.9,  0.1, 0, 0], spec = 10)

leaf = Material(diffuse = color(0,79,0), albedo = [0.9,  0.1, 0, 0], spec = 10)
leaf2 = Material(diffuse = color(1,63,0), albedo = [0.8,  0.1, 0.1, 0], spec = 10)
leaf3 = Material(diffuse = color(0, 70, 1), albedo = [0.8,  0.2, 0, 0], spec = 10)

grass = Material(diffuse = color(94,157,52), albedo = [0.9,  0.1, 0, 0], spec = 10)

#----------------LUZ, COLOR-----------------#
r.light = Light(V3(-20, 40, 20), 5, color(255, 255, 255))
r.density = 0.4
r.background_color = color(255, 255, 255)


#----------------OBJS-----------------#
obj = Obj('./circle.obj',5,5,apple)
obj.glLoad((0,0,-5), (0.3,0.3,0.3))

star = Obj('./star.obj',5,5,apple)
star.glLoad((0,0,-5), (1,1,1))


#----------------ENVMAP / FONDO-----------------#
r.envmap = Envmap('./envmap.bmp')

#----------------ESCENA-----------------#
r.scene = [
    Plane(V3(0, -5, -15), 25, 15, "y", grass),

    *(Square(V3(-3, -4, -12), (10,10), wood)).planes,
    *(Square(V3(-3, -3.2, -12), (10,10), wood)).planes,
    *(Square(V3(-3, -2.4, -12), (10,10), wood)).planes,
    *(Square(V3(-3, -1.6, -12), (10,10), wood)).planes,

    *(Square(V3(-4, -1, -12), (11,11), leaf2)).planes,
    *(Square(V3(-2, -1, -12), (11,11), leaf)).planes,
    *(Square(V3(-4, -1, -13), (11,11), leaf3)).planes,
    *(Square(V3(-2, -1, -13), (11,11), leaf)).planes,
    *(Square(V3(-3, -1, -11), (11,11), leaf2)).planes,
    *(Square(V3(-4, -1, -11), (11,11), leaf2)).planes,
    *(Square(V3(-2, -1, -11), (11,11), leaf3)).planes,

    *(Square(V3(-3, -0.1, -13), (11,11), leaf)).planes,
    *(Square(V3(-3, -0.1, -11), (11,11), leaf2)).planes,
    *(Square(V3(-4, -0.1, -12), (11,11), leaf3)).planes,
    *(Square(V3(-2.1, -0.1, -12), (11,11), leaf3)).planes,

    Sphere(V3(-3, 1.3, -10), 0.3, apple),
]

r.render()
r.write()

"""
    *(Square(V3(-3, -4, -12), (10,10), wood)).planes,
    *(Square(V3(-3, -3.2, -12), (10,10), wood)).planes,
    *(Square(V3(-3, -2.4, -12), (10,10), wood)).planes,
    *(Square(V3(-3, -1.6, -12), (10,10), wood)).planes,

    *(Square(V3(-4, -1, -12), (11,11), leaf2)).planes,
    *(Square(V3(-2, -1, -12), (11,11), leaf)).planes,
    *(Square(V3(-4, -1, -13), (11,11), leaf3)).planes,
    *(Square(V3(-2, -1, -13), (11,11), leaf)).planes,
    *(Square(V3(-3, -1, -11), (11,11), leaf2)).planes,
    *(Square(V3(-4, -1, -11), (11,11), leaf2)).planes,
    *(Square(V3(-2, -1, -11), (11,11), leaf3)).planes,

    *(Square(V3(-3, -0.1, -13), (11,11), leaf)).planes,
    *(Square(V3(-3, -0.1, -11), (11,11), leaf2)).planes,
    *(Square(V3(-4, -0.1, -12), (11,11), leaf3)).planes,
    *(Square(V3(-2.1, -0.1, -12), (11,11), leaf3)).planes,

    *(Square(V3(-3, 0.8, -12), (12,12), leaf)).planes,
"""