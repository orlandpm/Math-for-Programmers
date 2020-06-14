from math import sqrt, pi
import matplotlib
import os
from matplotlib.patches import Polygon, FancyArrowPatch
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, proj3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from colors import *

## https://stackoverflow.com/a/22867877/1704140
class FancyArrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)


class Polygon3D():
    def __init__(self, *vertices, color=blue):
        self.vertices = vertices
        self.color = color

class Points3D():
    def __init__(self, *vectors, color=black):
        self.vectors = list(vectors)
        self.color = color

class Arrow3D():
    def __init__(self, tip, tail=(0,0,0), color=red):
        self.tip = tip
        self.tail = tail
        self.color = color

class Segment3D():
    def __init__(self, start_point, end_point, color=blue):
        self.start_point = start_point
        self.end_point = end_point
        self.color = color

class Box3D():
    def __init__(self, *vector):
        self.vector = vector

# helper function to extract all the vectors from a list of objects
def extract_vectors_3D(objects):
    for object in objects:
        if type(object) == Polygon3D:
            for v in object.vertices:
                yield v
        elif type(object) == Points3D:
            for v in object.vectors:
                yield v
        elif type(object) == Arrow3D:
            yield object.tip
            yield object.tail
        elif type(object) == Segment3D:
            yield object.start_point
            yield object.end_point
        elif type(object) == Box3D:
            yield object.vector
        else:
            raise TypeError("Unrecognized object: {}".format(object))

def draw3d(*objects, origin=True, axes=True, width=6, save_as=None):

    fig = plt.gcf()
    ax = fig.add_subplot(111, projection='3d')

    all_vectors = list(extract_vectors_3D(objects))
    if origin:
        all_vectors.append((0,0,0))
    xs, ys, zs = zip(*all_vectors)

    max_x, min_x = max(0,*xs), min(0,*xs)
    max_y, min_y = max(0,*ys), min(0,*ys)
    max_z, min_z = max(0,*zs), min(0,*zs)

    x_size = max_x-min_x
    y_size = max_y-min_y
    z_size = max_z-min_z

    padding_x = 0.05 * x_size if x_size else 1
    padding_y = 0.05 * y_size if y_size else 1
    padding_z = 0.05 * z_size if z_size else 1

    plot_x_range = (min(min_x - padding_x,-2), max(max_x + padding_x,2))
    plot_y_range = (min(min_y - padding_y,-2), max(max_y + padding_y,2))
    plot_z_range = (min(min_z - padding_z,-2), max(max_z + padding_z,2))
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    def draw_segment(start, end, color=black, linestyle='solid'):
        xs, ys, zs = [[start[i],end[i]] for i in range(0,3)]
        ax.plot(xs, ys, zs, color=color, linestyle=linestyle)

    if axes:
        draw_segment((plot_x_range[0],0,0), (plot_x_range[1],0,0))
        draw_segment((0,plot_y_range[0],0), (0,plot_y_range[1],0))
        draw_segment((0,0,plot_z_range[0]), (0,0,plot_z_range[1]))

    if origin:
        ax.scatter([0],[0],[0], color='k', marker='x')

    for object in objects:
        if type(object) == Points3D:
            xs, ys, zs = zip(*object.vectors)
            ax.scatter(xs,ys,zs,color=object.color)

        elif type(object) == Polygon3D:
            for i in range(0,len(object.vertices)):
                draw_segment(
                    object.vertices[i],
                    object.vertices[(i+1)%len(object.vertices)],
                    color=object.color)

        elif type(object) == Arrow3D:
            xs, ys, zs = zip(object.tail, object.tip)
            a = FancyArrow3D(xs,ys,zs, mutation_scale=20,arrowstyle='-|>', color=object.color)
            ax.add_artist(a)

        elif type(object) == Segment3D:
            draw_segment(object.start_point, object.end_point, color=object.color)

        elif type(object) == Box3D:
            x,y,z = object.vector
            kwargs = {'linestyle':'dashed', 'color':'gray'}
            draw_segment((0,y,0),(x,y,0),**kwargs)
            draw_segment((0,0,z),(0,y,z),**kwargs)
            draw_segment((0,0,z),(x,0,z),**kwargs)
            draw_segment((0,y,0),(0,y,z),**kwargs)
            draw_segment((x,0,0),(x,y,0),**kwargs)
            draw_segment((x,0,0),(x,0,z),**kwargs)
            draw_segment((0,y,z),(x,y,z),**kwargs)
            draw_segment((x,0,z),(x,y,z),**kwargs)
            draw_segment((x,y,0),(x,y,z),**kwargs)
        else:
            raise TypeError("Unrecognized object: {}".format(object))

    if save_as:
        plt.savefig("images/"+save_as)

    plt.show()
