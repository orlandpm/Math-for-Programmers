import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import matplotlib.cm
from vectors import *
from random import random
from teapot import tris
from math import *

def compose(f,g):
    return (lambda x: f(g(x)))

def normal(face):
    try:
        return(cross(subtract(face[1], face[0]), subtract(face[2], face[0])))

    except IndexError:

        print(len(face))
        raise IndexError('bad face')

blues = matplotlib.cm.get_cmap('Blues')

def random_colors(n,cmap_name='magma'):
    cmap=matplotlib.cm.get_cmap(cmap_name)
    return [cmap(i*1.0/n) for i in range(0,n)]

def vertices(faces):
    return [vertex for face in faces for vertex in face]

def identity_transform(v): return v

def rot_y(theta):
    def r(v):
        return (v[0] * cos(theta) - v[2] * sin(theta),
        v[1],
        v[0] * sin(theta) + v[2] * cos(theta))
    return r

def rot_x(theta):
    def r(v):
        return (v[0],
        v[1] * cos(theta) - v[2] * sin(theta),
        v[1] * sin(theta) + v[2] * cos(theta))
    return r

def rot_z(theta):
    def r(v):
        return (
        v[0] * cos(theta) - v[1] * sin(theta),
        v[0] * sin(theta) + v[1] * cos(theta),
        v[2])
    return r

def Triangles(triangles, color_map, light, transform=identity_transform):
    faces = [map(transform,t) for t in triangles]
    glBegin(GL_TRIANGLES)
    for face in faces:
        color = color_map(1 - dot(unit(normal(face)), unit(light)))
        for vertex in face:
            glColor3fv((color[0], color[1], color[2]))
            glVertex3fv(vertex)
    glEnd()

oct_colors = random_colors(8,'gist_ncar')
def Octahedron(color_map, light, transform=identity_transform):

    top = transform((0.,0.,1.))
    north = transform((0.,1.,0.))
    south = transform((0.,-1.,0.))
    east = transform((1.,0.,0.))
    west = transform((-1.,0.,0.))
    bottom = transform((0.,0.,-1.))

    edges = [
        [top,north],
        [top,east],
        [top,south],
        [top,west],
        [east,north],
        [north,west],
        [west,south],
        [south,east],
        [bottom,north],
        [bottom,south],
        [bottom,east],
        [bottom,west]
    ]

    faces = [
        [top, east, north],
        [top, north, west],
        [top, west, south],
        [top, south, east],
        [bottom, east, south],
        [bottom, south, west],
        [bottom, west, north],
        [bottom, north, east]
    ]

    glBegin(GL_TRIANGLES)
    for color,face in zip(oct_colors,faces):
        # color = color_map(1 - dot(unit(normal(face)), unit(light)))
        for vertex in face:
            glColor3fv((color[0], color[1], color[2]))
            glVertex3fv(vertex)
    glEnd()

    # glBegin(GL_LINES)
    # for edge in edges:
    #     for vertex in edge:
    #         glVertex3fv(vertex)
    # glEnd()

def main(light=(1,2,3)):
    pygame.init()
    display = (400,400)
    window = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)


    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    glCullFace(GL_BACK)

    theta = 0
    clock = pygame.time.Clock()


    def once():
        yield True
        while True:
            yield False

    def forever():
        while True:
            yield True
    cond = forever()

    while cond.next():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        theta += 0.001 * clock.tick()
        # glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Triangles(tris, blues, light, compose(rot_z(sin(5 * theta)/10), rot_x(-pi/2)))
        pygame.display.flip()
        print(clock.get_fps())

main()
