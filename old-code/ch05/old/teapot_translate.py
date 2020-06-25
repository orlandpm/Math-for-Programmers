from teapot import load_triangles
from matrices import *
from draw_model import *
from camera import Camera
from transforms import polygon_map

def translate_3d(translation):
    def new_function(target):
        a,b,c = translation
        x,y,z = target
        matrix = ((1,0,0,a),(0,1,0,b),(0,0,1,c),(0,0,0,1))
        vector = (x,y,z,1)
        x_out, y_out, z_out, _ = multiply_matrix_vector(matrix,vector)
        return (x_out,y_out,z_out)
    return new_function

draw_model(load_triangles(), camera=Camera("translate-teapot-pre",[0]))
draw_model(polygon_map(translate_3d((2,2,-3)), load_triangles()), camera=Camera("translate-teapot-post",[0]))
