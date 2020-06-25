from teapot import load_triangles
from draw_model import draw_model
from camera import Camera

draw_model(load_triangles(), glRotatefArgs=(-90,1,0,0), camera=Camera('teapot_glRotatef_second',[0]))
