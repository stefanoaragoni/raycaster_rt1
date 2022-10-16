from lib import *
from intersect import *
from triangle import Triangle

class Obj(object):
  def __init__(self, filename, width, height, material):
    self.width = width
    self.height = height
    self.material = material

    self.Model = None
    self.vertex_buffer_object = []
    self.active_vertex_array = []
    self.active_texture = None
    
    with open(filename) as f:
      self.lines = f.read().splitlines()

    self.vertex = []  #v
    self.faces = [] #f
    self.tvertex = [] #tv
    self.nvertex = [] #vn

    for line in self.lines:
      line = line.strip()
      if line:
        prefix, value = line.split(' ', 1)

        if prefix == 'v':
          temp = value.split(' ')
          tempArray = []

          for tempValue in temp:
            tempArray.append((float(tempValue)))

          self.vertex.append(tempArray)

        elif prefix == 'vt':
          temp = value.split(' ')
          tempArray = []

          for tempValue in temp:
            tempArray.append((float(tempValue)))

          if(len(tempArray)==2):
            tempArray.append(0)
            
          self.tvertex.append(tempArray)

        elif prefix == 'vn':
          temp = value.split(' ')
          tempArray = []

          for tempValue in temp:
            tempArray.append((float(tempValue)))

          if(len(tempArray)==2):
            tempArray.append(0)
            
          self.nvertex.append(tempArray)

          
        elif prefix == 'f':
          temp = value.split(' ')
          tempArray = []
          
          for tempValue in temp:
            temp2 = tempValue.split('/')
            tempArray2 = []

            for tempValue2 in temp2:
              tempArray2.append((int(tempValue2)))

            tempArray.append(tempArray2)
          
          self.faces.append(tempArray)

  def transform_vertex(self, vertex, scale, translate):
    return V3(
      (vertex[0] * scale[0] + translate[0]),
      (vertex[1] * scale[1] + translate[1]),
      (vertex[2] * scale[2] + translate[2]),
    )

  def glLoad(self, translate=(0,0,0), scale=(1,1,1)):     
    ############################# FOR #############################

    for face in self.faces:
      vcount = len(face)

      ############################# VCOUNT 3 #############################

      if vcount == 3:
        f1 = face[0][0] - 1
        f2 = face[1][0] - 1
        f3 = face[2][0] - 1

        v1 = self.transform_vertex(self.vertex[f1], scale, translate)
        v2 = self.transform_vertex(self.vertex[f2], scale, translate)
        v3 = self.transform_vertex(self.vertex[f3], scale, translate)

        self.vertex_buffer_object.append(v1)
        self.vertex_buffer_object.append(v2)
        self.vertex_buffer_object.append(v3)

        if self.active_texture:
          ft1 = face[0][1] - 1
          ft2 = face[1][1] - 1
          ft3 = face[2][1] - 1

          vt1 = V3(*self.tvertex[ft1])
          vt2 = V3(*self.tvertex[ft2])
          vt3 = V3(*self.tvertex[ft3])

          self.vertex_buffer_object.append(vt1)
          self.vertex_buffer_object.append(vt2)
          self.vertex_buffer_object.append(vt3)

        try:
          fn1 = face[0][2] - 1
          fn2 = face[1][2] - 1
          fn3 = face[2][2] - 1

          vn1 = V3(*self.nvertex[fn1])
          vn2 = V3(*self.nvertex[fn2])
          vn3 = V3(*self.nvertex[fn3])
      
          self.vertex_buffer_object.append(vn1)
          self.vertex_buffer_object.append(vn2)
          self.vertex_buffer_object.append(vn3)
        except:
          pass
          
      ############################# VCOUNT 4 #############################

      if vcount == 4:
        f1 = face[0][0] - 1
        f2 = face[1][0] - 1
        f3 = face[2][0] - 1
        f4 = face[3][0] - 1

        v1 = self.transform_vertex(self.vertex[f1], scale, translate)
        v2 = self.transform_vertex(self.vertex[f2], scale, translate)
        v3 = self.transform_vertex(self.vertex[f3], scale, translate)
        v4 = self.transform_vertex(self.vertex[f4], scale, translate)
        
        self.vertex_buffer_object.append(v1)
        self.vertex_buffer_object.append(v2)
        self.vertex_buffer_object.append(v3)
        
        if self.active_texture:

            ft1 = face[0][1] - 1
            ft2 = face[1][1] - 1
            ft3 = face[2][1] - 1

            vt1 = V3(*self.tvertex[ft1])
            vt2 = V3(*self.tvertex[ft2])
            vt3 = V3(*self.tvertex[ft3])

            self.vertex_buffer_object.append(vt1)
            self.vertex_buffer_object.append(vt2)
            self.vertex_buffer_object.append(vt3)

        try:
            fn1 = face[0][2] - 1
            fn2 = face[1][2] - 1
            fn3 = face[2][2] - 1

            vn1 = V3(*self.nvertex[fn1])
            vn2 = V3(*self.nvertex[fn2])
            vn3 = V3(*self.nvertex[fn3])
        
            self.vertex_buffer_object.append(vn1)
            self.vertex_buffer_object.append(vn2)
            self.vertex_buffer_object.append(vn3)
        except:
            pass

        self.vertex_buffer_object.append(v1)
        self.vertex_buffer_object.append(v3)
        self.vertex_buffer_object.append(v4)

        if self.active_texture:

            ft1 = face[0][1] - 1
            ft3 = face[2][1] - 1
            ft4 = face[3][1] - 1

            vt1 = V3(*self.tvertex[ft1])
            vt3 = V3(*self.tvertex[ft3])
            vt4 = V3(*self.tvertex[ft4])

            self.vertex_buffer_object.append(vt1)
            self.vertex_buffer_object.append(vt3)
            self.vertex_buffer_object.append(vt4)
        try:
            fn1 = face[0][2] - 1
            fn3 = face[2][2] - 1
            fn4 = face[3][2] - 1

            vn1 = V3(*self.nvertex[fn1])
            vn3 = V3(*self.nvertex[fn3])
            vn4 = V3(*self.nvertex[fn4])
        
            self.vertex_buffer_object.append(vn1)
            self.vertex_buffer_object.append(vn3)
            self.vertex_buffer_object.append(vn4)
        except:
            pass

    self.active_vertex_array = iter(self.vertex_buffer_object)

  def draw(self):
    triangles = []
    try:
        while True:
            A = next(self.active_vertex_array)
            B = next(self.active_vertex_array)
            C = next(self.active_vertex_array)

            if (A.x == B.x == C.x) and (A.y == B.y == C.y) and (A.z == B.z == C.z):
                continue
            else:
              triangles.append(Triangle((A, B, C), self.material))

    except StopIteration:
        print("terminado")
    self.vertex_buffer_object = []
    self.active_vertex_array = []

    return triangles