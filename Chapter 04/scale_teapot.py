from vectors import scale
from teapot import load_triangles
from draw_model import draw_model

def scale2(v):
    return scale(2.0, v)

original_triangles = load_triangles() #1
scaled_triangles = [
    [scale2(vertex) for vertex in triangle] #21
    for triangle in original_triangles #32
]

####################################################################
#### this code takes a snapshot to reproduce the exact figure 
#### shown in the book as an image saved in the "figs" directory
#### to run it, run this script with command line arg --snapshot
import sys
import camera
if '--snapshot' in sys.argv:
    camera.default_camera = camera.Camera('fig_4.5_scale_teapot',[0])
####################################################################

draw_model(scaled_triangles)