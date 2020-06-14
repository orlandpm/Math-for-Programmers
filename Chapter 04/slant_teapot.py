from teapot import load_triangles
from draw_model import draw_model
from math import pi

def polygon_map(transformation, polygons):
    return [
        [transformation(vertex) for vertex in triangle]
        for triangle in polygons
    ]

def slant_xy(vector):
    x,y,z = vector
    return (x+y, y, z)

####################################################################
#### this code takes a snapshot to reproduce the exact figure 
#### shown in the book as an image saved in the "figs" directory
#### to run it, run this script with command line arg --snapshot
import sys
import camera
if '--snapshot' in sys.argv:
    camera.default_camera = camera.Camera('fig_4.16_slant_teapot',[0])
####################################################################

draw_model(polygon_map(slant_xy, load_triangles()))
