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
   => Se implementó triángulos. 

- [5 puntos] por implementar un envmap

- [50 puntos] por cargar un modelo obj
    => Estrella (star.obj), rombo (circle.obj)

TOTAL: 125 puntos + 50 puntos subjetivos
TOTAL MAXIMO: 175 puntos
"""

r = Raytracer(500,500)

#----------------MATERIALES-----------------#
apple = Material(diffuse = color(130, 0, 0), albedo = [0.9,  0.1, 0, 0], spec = 100)
peach = Material(diffuse = color(134,83,71), albedo = [0.6,  0.3, 0.1, 0], spec = 50)

estrella = Material(diffuse = color(0, 0, 100), albedo = [0, 0.5, 0.1, 0.8], spec = 125, refractive_index = 1.5)
estrella2 = Material(diffuse = color(255,199,0), albedo = [0.9,  0.1, 0, 0], spec = 100)
water_reflective = Material(diffuse = color(150, 180, 200), albedo = [0, 0.5, 0.1, 0.8], spec = 125, refractive_index = 1.5)

wood = Material(diffuse = color(100, 50, 0), albedo = [0.9,  0.1, 0, 0], spec = 10)
leaf = Material(diffuse = color(0,79,0), albedo = [0.9,  0.1, 0, 0], spec = 10)
leaf2 = Material(diffuse = color(1,63,0), albedo = [0.8,  0.1, 0.1, 0], spec = 10)
leaf3 = Material(diffuse = color(0, 70, 1), albedo = [0.8,  0.2, 0, 0], spec = 10)

grass = Material(diffuse = color(94,157,52), albedo = [0.9,  0.1, 0, 0], spec = 10)

nether = Material(diffuse = color(63,17,135), albedo = [0.9,  0.1, 0, 0], spec = 10)
netherBlack = Material(diffuse = color(153,107,225), albedo = [0.9,  0.1, 0, 0], spec = 10)

#reflexion
nether2 = Material(diffuse = color(149, 53, 83), albedo = [0.0, 1.0, 0.8, 0], spec = 1425)
#refraccion
nether3 = Material(diffuse = color(149, 53, 83), albedo = [0.0, 0.5, 0.1, 0.8], spec = 125, refractive_index = 1.5)


#----------------LUZ, COLOR-----------------#
r.light = Light(V3(-20, 40, 20), 3, color(255, 255, 255))
r.density = 1
r.background_color = color(255, 255, 255)


#----------------OBJS-----------------#
obj = Obj('./circle.obj',1,1,nether3)
obj.glLoad((2,1.1,-10), (0.5,0.5,0.5))

star = Obj('./star.obj',1,1,estrella2)
star.glLoad((-2,-2,-5), (0.2,0.2,0.2))

star2 = Obj('./star.obj',1.2,1.2,estrella2)
star2.glLoad((-1.7,-1.7,-4), (0.1,0.1,0.1))


#----------------ENVMAP / FONDO-----------------#
r.envmap = Envmap('./envmap.bmp')

#----------------ESCENA-----------------#
r.scene = [
    Plane(V3(0, -5, -15), 25, 15, "y", grass),

    Triangle((V3(-2.1, 3.9, -10), V3(-2.3, 3.7, -10), V3(-2.5, 3.9, -10)), leaf),
    Triangle((V3(-2.8, 3.9, -10), V3(-3, 3.7, -10), V3(-3.2, 3.9, -10)), leaf),

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

    *(Square(V3(1, -3, -12), (10,10), nether)).planes,
    *(Square(V3(1, -2.2, -12), (10,10), nether)).planes,
    *(Square(V3(1, -1.4, -12), (10,10), nether)).planes,
    *(Square(V3(1, -0.6, -12), (10,10), nether)).planes,
    *(Square(V3(1, 0.2, -12), (10,10), netherBlack)).planes,

    *(Square(V3(4, -3, -12), (10,10), nether)).planes,
    *(Square(V3(4, -2.2, -12), (10,10), nether)).planes,
    *(Square(V3(4, -1.4, -12), (10,10), nether)).planes,
    *(Square(V3(4, -0.6, -12), (10,10), nether)).planes,
    *(Square(V3(4, 0.2, -12), (10,10), nether)).planes,

    *(Square(V3(1.75, -3, -12), (10,10), netherBlack)).planes,
    *(Square(V3(2.5, -3, -12), (10,10), netherBlack)).planes,
    *(Square(V3(3.25, -3, -12), (10,10), netherBlack)).planes,

    *(Square(V3(1.75, 0.2, -12), (10,10), nether)).planes,
    *(Square(V3(2.5, 0.2, -12), (10,10), nether)).planes,
    *(Square(V3(3.25, 0.2, -12), (10,10), nether)).planes,

    Plane(V3(3, 1.5, 15), 4, 4, "z", nether2),


    *obj.draw(),
    *star.draw(),
    *star2.draw(),
]

r.render()
r.write()