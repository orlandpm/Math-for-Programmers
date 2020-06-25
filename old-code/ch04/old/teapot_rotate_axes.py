from teapot import load_triangles
from draw_model import draw_model
from camera import Camera
from transforms import *
from math import *
from vectors import add
import os

# draw_model(polygon_map(rotate_z_by(pi/4.), load_triangles()), camera=Camera("teapot_45deg_z", [0]))
# draw_model(polygon_map(rotate_x_by(3*pi/2.), load_triangles()), camera=Camera("teapot_270deg_x", [0]))
#

camera=Camera('teapot-rotation-chapter-intro',
                range(0,45),
                comic_strip=9,
                dir=os.path.join('figs','chapter-intro-teapot'))


def t(ticks):
    rate = 1./100. # 1 degree per 100 ms
    return compose(
                    rotate_z_by(ticks * .5 * rate * pi / 180.),
                    compose(translate_by((-0.5,-0.5,3)),
                    rotate_x_by(3*pi/2)))

draw_model(load_triangles(),
            camera=camera,
            transform=t)
