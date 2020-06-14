import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import matplotlib.cm
import camera
from vectors import *
from math import *
from transforms import *

def normal(face):
    return(cross(subtract(face[1], face[0]), subtract(face[2], face[0])))

blues = matplotlib.cm.get_cmap('Blues')

def shade(face,color_map=blues,light=(1,2,3)):
    return color_map(1 - dot(unit(normal(face)), unit(light)))

def Axes():
    axes =  [
        [(-1000,0,0),(1000,0,0)],
        [(0,-1000,0),(0,1000,0)],
        [(0,0,-1000),(0,0,1000)]
    ]
    glBegin(GL_LINES)
    for axis in axes:
        for vertex in axis:
            glColor3fv((1,1,1))
            glVertex3fv(vertex)
    glEnd()

def draw_model(faces, color_map=blues, light=(1,2,3),
                glRotatefArgs=None,
                get_matrix=None):
    pygame.init()
    display = (400,400)
    window = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    cam = camera.default_camera
    cam.set_window(window)
    gluPerspective(45, 1, 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)
    if glRotatefArgs:
        glRotatef(*glRotatefArgs)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    glCullFace(GL_BACK)

    while cam.is_shooting():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Axes()
        glBegin(GL_TRIANGLES)
        def do_matrix_transform(v):
            if get_matrix:
                m = get_matrix(pygame.time.get_ticks())
                return multiply_matrix_vector(m, v)
            else:
                return v
        transformed_faces = polygon_map(do_matrix_transform, faces)
        for face in transformed_faces:
            color = shade(face,color_map,light)
            for vertex in face:
                glColor3fv((color[0], color[1], color[2]))
                glVertex3fv(vertex)
        glEnd()
        cam.tick()
        pygame.display.flip()
