from teapot import load_triangles
from draw_model import draw_model
from camera import Camera
from transforms import *
from math import *
from vectors import add
import os

# draw_model(polygon_map(rotate_z_by(pi/4.), load_triangles()), camera=Camera("teapot_45deg_z", [0]))
# draw_model(polygon_map(rotate_x_by(3*pi/2.), load_triangles()), camera=Camera("teapot_270deg_x", [0]))
#

Ae1 = (1,1,1)
Ae2 = (1,0,-1)
Ae3 = (0,1,1)

def apply_A(v):
    return add(
        scale(v[0], Ae1),
        scale(v[1], Ae2),
        scale(v[2], Ae3)
    )

draw_model(polygon_map(apply_A, load_triangles()),
            camera=Camera('teapot-linear-transform',[0]))
