from teapot import load_triangles
from matrices import *
from draw_model import *
from camera import Camera
from transforms import polygon_map
from vector_drawing import *

def transform(v):
    m = ((2,1,1),(1,2,1),(1,1,2))
    return multiply_matrix_vector(m,v)

draw_model(polygon_map(transform, load_triangles()), camera=Camera("teapot-matrix-exercise",[0]))

s = Space((-1,-1,-1),(3,3,3),"stretched-squeezed-standard-basis")
s.draw_axes()
s.draw_arrow((0,0,0),(1,0,0),color='black')
s.draw_arrow((0,0,0),(0,1,0),color='black')
s.draw_arrow((0,0,0),(0,0,1),color='black')
s.draw_arrow((0,0,0),(2,1,1),color='blue')
s.draw_arrow((0,0,0),(1,2,1),color='blue')
s.draw_arrow((0,0,0),(1,1,2),color='blue')
s.show()
