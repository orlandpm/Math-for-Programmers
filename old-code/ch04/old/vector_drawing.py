from math import sqrt, pi
import matplotlib
import os
from matplotlib.patches import Polygon, FancyArrowPatch
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, proj3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

class Plane():
    def __init__(self, bottom_left, top_right, name=None):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.name = name or ("fig-%d" % self.fig.number)
        self.bottom_left = bottom_left
        self.top_right = top_right
        self.set_bounds(bottom_left, top_right)
    def draw_vectors(self, *vectors, **kwargs):
        xs = map(lambda x:x[0], vectors)
        ys = map(lambda x:x[1], vectors)
        self.ax.scatter(xs,ys,**kwargs)
        return self
    def draw_origin(self):
        self.ax.scatter([0],[0], color='k', marker='x')
        return self
    def fill_polygon(self, vertices, **kwargs):
        patches = []
        polygon = Polygon(vertices, True)
        patches.append(polygon)
        p = PatchCollection(patches, **kwargs)
        # colors = 100*np.random.rand(len(patches))
        # p.set_array(np.array(colors))
        self.ax.add_collection(p)
        return self
    def draw_arrow(self, tail, head, color=None):
        head_length = 0.4
        length = sqrt((head[1]-tail[1])**2 + (head[0]-tail[0])**2)
        new_length = length - head_length
        new_y = (head[1] - tail[1]) * (new_length / length)
        new_x = (head[0] - tail[0]) * (new_length / length)
        self.ax.arrow(tail[0], tail[1], new_x, new_y,
            head_width=0.2, head_length=head_length,
            fc=color, ec=color)
        return self
    def draw_segment(self, p1,p2, color=None):
        x1, y1 = p1
        x2, y2 = p2
        self.ax.plot([x1,x2],[y1,y2], color=color)
        return self
    def draw_grid(self):
        xmin, xmax = self.ax.get_xbound()
        ymin, ymax = self.ax.get_ybound()
        print(xmin,xmax,ymin,ymax)
        self.ax.set_xticks(np.arange(xmin,xmax,1))
        self.ax.set_yticks(np.arange(ymin,ymax,1))
        self.ax.grid(True)
        self.ax.set_axisbelow(True)
        return self
    def set_bounds(self, bottom_left, top_right):
        xmin,ymin = bottom_left
        xmax,ymax = top_right
        self.ax.set_ylim(ymin,ymax)
        self.ax.set_xlim(xmin,xmax)
        return self
    def draw_polygon(self, vectors, color=None):
        for i in range(0,len(vectors)):
            self.draw_segment(vectors[i], vectors[(i+1)%len(vectors)], color=color)
        return self
    def draw_axes(self):
        self.ax.axhline(linewidth=1, color='k')
        self.ax.axvline(linewidth=2, color='k')
        return self
    def save(self):
        dir = os.getcwd()
        relative = os.path.join("figs","%s.png" % self.name)
        path = os.path.join(dir,relative)
        self._path = path
        self.fig.savefig(relative, bbox_inches='tight')
    def show(self):
        self.save()
        os.startfile(self._path)

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

class Space():


    def __init__(self, xyz_min, xyz_max, name=None):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.name = name or ("fig-%d" % self.fig.number)
        self.xmin, self.ymin, self.zmin = xyz_min
        self.xmax, self.ymax, self.zmax = xyz_max
        self.ax.set_xbound(self.xmin, self.xmax)
        self.ax.set_ybound(self.ymin, self.ymax)
        self.ax.set_zbound(self.zmin, self.zmax)
    def draw_axes(self):
        self.draw_segment((self.xmin,0,0), (self.xmax,0,0))
        self.draw_segment((0,self.ymin,0), (0,self.ymax,0))
        self.draw_segment((0,0,self.zmin), (0,0,self.zmax))
        return self
    def draw_vectors(self, *vectors, **kwargs):
        xs, ys, zs = zip(*vectors)
        self.ax.scatter(xs,ys,zs,**kwargs)
        return self
    def draw_box(self,vector):
        x,y,z = vector
        kwargs = {'linestyle':'dashed', 'color':'gray'}
        (self
            .draw_segment((0,y,0),(x,y,0),**kwargs)
            .draw_segment((0,0,z),(0,y,z),**kwargs)
            .draw_segment((0,0,z),(x,0,z),**kwargs)
            .draw_segment((0,y,0),(0,y,z),**kwargs)
            .draw_segment((x,0,0),(x,y,0),**kwargs)
            .draw_segment((x,0,0),(x,0,z),**kwargs)
            .draw_segment((0,y,z),(x,y,z),**kwargs)
            .draw_segment((x,0,z),(x,y,z),**kwargs)
            .draw_segment((x,y,0),(x,y,z),**kwargs))
        return self
    def draw_origin(self):
        self.draw_vectors((0,0,0), color='k', marker='x')
        return self
    def draw_segment(self, start, end, color='k', linestyle='solid'):
        xs, ys, zs = [[start[i],end[i]] for i in range(0,3)]
        self.ax.plot(xs, ys, zs, color=color, linestyle=linestyle)
        return self
    def draw_arrow(self, tail, head, color='k'):
        xs, ys, zs = [(tail[i],head[i]) for i in range(0,3)]
        a = Arrow3D(xs,ys,zs, mutation_scale=20,arrowstyle='-|>', color=color)
        self.ax.add_artist(a)
        return self
    def draw_polygon(self, *vs, **kwargs):
        self.ax.add_collection3d(Poly3DCollection([vs], **kwargs))
        return self
    def save(self):
        dir = os.getcwd()
        relative = os.path.join("figs","%s.png" % self.name)
        path = os.path.join(dir,relative)
        self._path = path
        self.fig.savefig(relative, bbox_inches='tight')
    def show(self):
        self.save()
        os.startfile(self._path)



#

#

#
