from teapot import load_triangles
from draw_model import draw_model
from camera import Camera
from transforms import *
from math import *
from vectors import add


def get_rotation_matrix(t):
    return (
        (cos(t),0,-sin(t)),
        (0,1,0),
        (sin(t),0,cos(t))
    )

def get_rotation_matrix(t):
    theta = t/1000
    return (
        (cos(theta),0,-sin(theta)),
        (0,1,0),
        (sin(theta),0,cos(theta))
    )

cam = Camera('parametrize_rotation',[1000,2000,3000,4000,5000],comic_strip=5)
draw_model(load_triangles(), get_matrix=get_rotation_matrix, camera=cam)
