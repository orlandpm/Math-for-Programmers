import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import matplotlib.cm
from camera import Camera
from vectors import *
from math import *
from transforms import *

def normal(face):
    return(cross(subtract(face[1], face[0]), subtract(face[2], face[0])))

blues = matplotlib.cm.get_cmap('Blues')

def shade(face,color_map=blues,light=(1,2,3)):
    return color_map(1 - dot(unit(normal(face)), unit(light)))


# def Axes():
#     axes =  [
#         [(-1000,0,0),(1000,0,0)],
#         [(0,-1000,0),(0,1000,0)],
#         [(0,0,-1000),(0,0,1000)]
#     ]
#     glBegin(GL_LINES)
#     for axis in axes:
#         for vertex in axis:
#             glColor3fv((1,1,1))
#             glVertex3fv(vertex)
#     glEnd()


def draw_model(faces, color_map=blues, light=(1,2,3),
                camera=Camera("default_camera",[]),
                glRotatefArgs=None,
                transform=None):
    print("camera", camera.name)
    pygame.init()
    display = (400,400)
    window = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    camera.set_window(window)
    gluPerspective(45, 1, 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)
    if glRotatefArgs:
        glRotatef(*glRotatefArgs)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    glCullFace(GL_BACK)

    while camera.is_shooting():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        # Axes()
        glBegin(GL_TRIANGLES)
        transformed_faces = polygon_map(transform(camera.total_ticks), faces) if transform else faces
        for face in transformed_faces:
            color = shade(face,color_map,light)
            for vertex in face:
                glColor3fv((color[0], color[1], color[2]))
                glVertex3fv(vertex)
        glEnd()
        camera.tick()
        pygame.display.flip()
        print(camera.get_fps())
