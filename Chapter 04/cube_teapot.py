from teapot import load_triangles
from draw_model import draw_model
from math import pi

def polygon_map(transformation, polygons):
    return [
        [transformation(vertex) for vertex in triangle]
        for triangle in polygons
    ]

def cube_stretch_y(vector):
    x,y,z = vector
    return (x, y*y*y, z)

####################################################################
#### this code takes a snapshot to reproduce the exact figure 
#### shown in the book as an image saved in the "figs" directory
#### to run it, run this script with command line arg --snapshot
import sys
import camera
if '--snapshot' in sys.argv:
    camera.default_camera = camera.Camera('fig_4.15_cube_teapot_y',[0])
####################################################################

draw_model(polygon_map(cube_stretch_y, load_triangles()))
