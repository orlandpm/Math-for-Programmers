from vectors import scale, add
from teapot import load_triangles
from draw_model import draw_model

def scale2(v):
    return scale(2.0, v)

def translate1left(v):
    return add((-1,0,0), v)

original_triangles = load_triangles()

scaled_translated_triangles = [
    [translate1left(scale2(vertex)) for vertex in triangle]
    for triangle in original_triangles
]

####################################################################
#### this code takes a snapshot to reproduce the exact figure 
#### shown in the book as an image saved in the "figs" directory
#### to run it, run this script with command line arg --snapshot
import sys
import camera
if '--snapshot' in sys.argv:
    camera.default_camera = camera.Camera('fig4.6_scale_translate',[0])
####################################################################

draw_model(scaled_translated_triangles)