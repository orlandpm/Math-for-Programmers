from teapot import load_triangles
from draw_model import draw_model
from camera import Camera
from transforms import *

from vectors import scale
def scale2(v):
    return scale(2.0, v)

original_triangles = load_triangles()
scaled_triangles = [
    [scale2(vertex) for vertex in triangle]
    for triangle in original_triangles
]

# draw_model(transformed_triangles, camera=Camera('teapot_scale2',[0]))


from vectors import add
def translate1left(v):
    return add((-1,0,0), v)

scaled_translated_triangles = [
    [translate1left(scale2(vertex)) for vertex in triangle]
    for triangle in original_triangles
]

def scale2_then_translate1left(v):
    return translate1left(scale2(v))

scaled_translated_triangles = [
    [scale2_then_translate1left(vertex) for vertex in triangle]
    for triangle in original_triangles
]

from math import *


# draw_model(scaled_translated_triangles, camera=Camera('teapot_scale_translate',[0]))
#
# # draw_model(polygon_map(scale2, load_triangles()))
# draw_model(polygon_map(scale_by(1), load_triangles()), camera=Camera('teapot-no-scale',[0]))
# draw_model(polygon_map(scale_by(0.5), load_triangles()), camera=Camera('teapot-half-scale',[0]))
# draw_model(polygon_map(scale_by(-1), load_triangles()), camera=Camera('teapot-minusone-scale',[0]))
# draw_model(polygon_map(scale_by(-1), load_triangles()), camera=Camera('teapot-minusone-scale-onerotate',[0]), transform=lambda t:rotate_x_by(3*pi/2))
# draw_model(polygon_map(compose(translate_by((0.5,0,0.5)), scale_by(-1)), load_triangles()), camera=Camera('teapot-minusone-scale-rotate',10,comic_strip=5),
#             transform=lambda t:compose(translate_by((0,0,2)), rotate_x_by(-(t/10)*pi/180)))
# draw_model(polygon_map(translate_by((0,0,2)), load_triangles()), camera=Camera('teapot-translate-2up',[0]))
draw_model(polygon_map(compose(scale2, translate1left), load_triangles()), camera=Camera('translate-then-scale', [0]))
