# ===============================================================
# Gráficas Por Computadora
# Stefano Aragoni - 20261
# ===============================================================

from logging import raiseExceptions
from collections import namedtuple
import struct
from math import *
from matrixmath import *

# ========== Tamaños =========

def char(c):
  return struct.pack('=c', c.encode('ascii'))

def word(w):
  return struct.pack('=h', w)

def dword(d):
  return struct.pack('=l', d)

def color(r, g, b):
  r = int(max(0, min(r, 255)))
  g = int(max(0, min(g, 255)))
  b = int(max(0, min(b, 255)))

  return bytes([b, g, r])

# ========== VECTOR =========
V3 = namedtuple('P3', ['x', 'y', 'z'])

def sum(v0, v1):
  return V3(v0.x + v1.x, v0.y + v1.y, v0.z + v1.z)

def sub(v0, v1):
  return V3(v0.x - v1.x, v0.y - v1.y, v0.z - v1.z)

def mul(v0, k):
  return V3(v0.x * k, v0.y * k, v0.z *k)

def dot(v0, v1):
  return v0.x * v1.x + v0.y * v1.y + v0.z * v1.z

def cross(v0, v1):
  return V3(
    v0.y * v1.z - v0.z * v1.y,
    v0.z * v1.x - v0.x * v1.z,
    v0.x * v1.y - v0.y * v1.x,
  )

def length(v0):
  return (v0.x**2 + v0.y**2 + v0.z**2)**0.5

def norm(v0):
  v0length = length(v0)

  if not v0length:
    return V3(0, 0, 0)

  return V3(v0.x/v0length, v0.y/v0length, v0.z/v0length)

  # ========== Utils =========

def bounding_box(x, y):
  x.sort()
  y.sort()

  return V3(x[0], y[0], 0), V3(x[-1], y[-1], 0)

def barycentric(x1, y1, x2, y2, x3, y3, x4, y4):

  c = cross(
    V3(x2 - x1, x3 - x1, x1 - x4), 
    V3(y2 - y1, y3 - y1, y1 - y4)
  )

  if c.z == 0:
    return -1, -1, -1

  return (c.x / c.z, c.y / c.z, 1 - ((c.x + c.y) / c.z))

def reflect(I, N):
  return norm(sub(I, mul(N, 2 * dot(I, N))))

def refract(I, N, roi):
  eta_i = 1
  eta_t = roi

  # Coseno i para calcular la refracción.
  cos_i = (dot(I, N) * -1)

  # Recálculo de valores si el coseno i es negativo.
  if (cos_i < 0):
    cos_i *= -1
    eta_i *= -1
    eta_t *= -1
    N = mul(N, -1)

  # Valor eta, resultante de la división de las dos componentes.
  eta = (eta_i / eta_t)

  # Simplificación de la expresión a un valor k para luego obtener su raíz cuadrada.
  k = (1 - ((eta ** 2) * (1 - (cos_i ** 2))))

  # Retorno de un vector nulo si el valor k es negativo.
  if (k < 0):
    return V3(0, 0, 0)

  # Cálculo del coseno t con la raíz cuadrada del valor k.
  cos_t = (k ** 0.5)

  # Retorno del nuevo vector refractado.
  return norm(sum(mul(I, eta), mul(N, ((eta * cos_i) - cos_t))))