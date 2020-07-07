from vectors import scale
from teapot import load_triangles
from draw_model import draw_model

def polygon_map(transformation, polygons):
    return [
        [transformation(vertex) for vertex in triangle]
        for triangle in polygons
    ]

def scale_by(scalar):
    def new_function(v):
        return scale(scalar, v)
    return new_function

####################################################################
#### this code takes a snapshot to reproduce the exact figure 
#### shown in the book as an image saved in the "figs" directory
#### to run it, run this script with command line arg --snapshot
import sys
import camera
if '--snapshot' in sys.argv:
    camera.default_camera = camera.Camera('MINIPROJ_4.3b',[0])
####################################################################

draw_model(polygon_map(scale_by(0.5), load_triangles()))