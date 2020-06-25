from teapot import load_triangles
from draw_model import draw_model
from camera import Camera
from transforms import *
from math import pi
draw_model(polygon_map(rotate_y_by(pi/2), load_triangles()), camera=Camera('rotate-teapot-y', [0]))
