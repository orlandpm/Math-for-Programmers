from teapot import load_triangles
from draw_model import draw_model
from transforms import polygon_map, multiply_matrix_vector

def transform(v):
    m = ((2,1,1),(1,2,1),(1,1,2))
    return multiply_matrix_vector(m,v)

####################################################################
#### this code takes a snapshot to reproduce the exact figure 
#### shown in the book as an image saved in the "figs" directory
#### to run it, run this script with command line arg --snapshot
import sys
import camera
if '--snapshot' in sys.argv:
    camera.default_camera = camera.Camera('ex_matrix_transform_teapot',[0])
####################################################################

draw_model(polygon_map(transform,load_triangles()))