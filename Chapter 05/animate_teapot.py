from teapot import load_triangles
from draw_model import draw_model
from math import sin,cos

def get_rotation_matrix(t): #1
    seconds = t/1000 #2
    return (
        (cos(seconds),0,-sin(seconds)),
        (0,1,0),
        (sin(seconds),0,cos(seconds))
    )

####################################################################
#### this code takes a snapshot to reproduce the exact figure 
#### shown in the book as an image saved in the "figs" directory
#### to run it, run this script with command line arg --snapshot
import sys
import camera
if '--snapshot' in sys.argv:
    camera.default_camera = camera.Camera('fig_5.4_draw_teapot',[0,1000,2000,3000,4000])
####################################################################

draw_model(load_triangles(), get_matrix=get_rotation_matrix)