from teapot import load_triangles
from draw_model import draw_model
from camera import Camera
from transforms import *
from math import *
from vectors import add

# def stretch_x(vector):
#     x,y,z = vector
#     return (4.*x, y, z)
#
# draw_model(polygon_map(stretch_x, load_triangles()), camera=Camera("stretch_x", [0]))
# t2 = compose(rotate_x_by(3*pi/2), stretch_x)
# draw_model(polygon_map(t2, load_triangles()), camera=Camera("stretch_x_rot", [0]))
# t3 = compose(translate_by((-2,0,-3)), t2)
# draw_model(polygon_map(t3, load_triangles()), camera=Camera("stretch_x_rot_trans", [0]))

def stretch_z(vector):
    x,y,z = vector
    return (x, y, 4*z)

def stretch_x(scalar,vector):
    x,y,z = vector
    return (scalar*x, y, z)

def stretch_x_by(scalar):
    def new_function(vector):
        return stretch_x(scalar,vector)
    return new_function
    


t4 = compose(translate_by((-1,-3,-2)), compose(rotate_x_by(3*pi/2), stretch_z))
draw_model(polygon_map(t4, load_triangles()), camera=Camera("stretch_z_rot_trans", [0]))


def cube_stretch_z(vector):
    x,y,z = vector
    return (x, y, 2*z*z*z)


t5 = compose(translate_by((-1,-2,-2)), compose(rotate_x_by(3*pi/2), cube_stretch_z))
draw_model(polygon_map(t5, load_triangles()), camera=Camera("cube_stretch_z_rot_trans", [0]))

def slant_xz(vector):
    x,y,z = vector
    return (x+z, y, z)

t6 = compose(translate_by((-1,-1,0)), compose(rotate_x_by(3*pi/2), slant_xz))
draw_model(polygon_map(t6, load_triangles()), camera=Camera("slant_xz", [0]))
