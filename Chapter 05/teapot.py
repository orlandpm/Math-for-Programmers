from transforms import *
from math import pi

with open("teapot.off") as f:
    lines = f.readlines()

vertex_count, face_count, edge_count = map(int,lines[1].split())

def triple(xs):
    xs = list(xs)
    return (xs[0],xs[1],xs[2])

def load_vertices():
    vertices = []
    for i in range(2,2+vertex_count):
        v = triple(map(float,lines[i].split()))
        vertices.append(scale_by(2)(rotate_x_by(-pi/2)(translate_by((-0.5,0,-0.6))(v))))
    return vertices

def load_polygons():
    polys = []
    vertices = load_vertices()
    for i in range(2+vertex_count,2+vertex_count+face_count):
        poly = list(map(vertices.__getitem__, map(int,lines[i].split()[1:])))
        polys.append(poly)
    return polys

def triangulate(poly):
    if len(poly) < 3:
        raise ArgumentException("polygons must have at least 3 vertices")
    # elif len(poly) == 3:
    #     return [poly]
    else:
        for i in range(1,len(poly) - 1):
            yield (poly[0], poly[i+1], poly[i])

def load_triangles():
    tris = []
    polys = load_polygons()
    for poly in polys:
        for tri in triangulate(poly):
            assert(len(tri)==3)
            for v in tri:
                assert(len(v)==3)
            tris.append(tri)
    return tris

#
# print(len(polys), len(tris))
# for i in range(2,481):
#     r = content[i].split()
#     print (float(r[0]), float(r[1]), float(r[2]))

# vertex_lines = [(float(r[0]), float(r[1]), float(r[2])) for i in range(2,481) for r in content[i].split(" ")]
