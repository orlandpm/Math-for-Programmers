import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import matplotlib.cm
from vectors import *
from math import *


def normal(face):
    return(cross(subtract(face[1], face[0]), subtract(face[2], face[0])))

blues = matplotlib.cm.get_cmap('Blues')

def shade(face,color_map=blues,light=(1,2,3)):
    return color_map(1 - dot(unit(normal(face)), unit(light)))

light = (1,2,3)
faces = [
    [(1,0,0), (0,1,0), (0,0,1)],
    [(1,0,0), (0,0,-1), (0,1,0)],
    [(1,0,0), (0,0,1), (0,-1,0)],
    [(1,0,0), (0,-1,0), (0,0,-1)],
    [(-1,0,0), (0,0,1), (0,1,0)],
    [(-1,0,0), (0,1,0), (0,0,-1)],
    [(-1,0,0), (0,-1,0), (0,0,1)],
    [(-1,0,0), (0,0,-1), (0,-1,0)],
]

pygame.init()
display = (400,400) #1
window = pygame.display.set_mode(display, DOUBLEBUF|OPENGL) #2

gluPerspective(45, 1, 0.1, 50.0) #1
glTranslatef(0.0,0.0, -5) #2
glEnable(GL_CULL_FACE) #3
glEnable(GL_DEPTH_TEST) #4
glCullFace(GL_BACK) #5


clock = pygame.time.Clock() #1
while True:
    for event in pygame.event.get(): #2
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    clock.tick() #3
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glBegin(GL_TRIANGLES) 
    for face in faces:
        color = shade(face,blues,light)
        for vertex in face:
            glColor3fv((color[0], color[1], color[2])) 
            glVertex3fv(vertex) 
    glEnd()
    pygame.display.flip() 
    print(clock.get_fps())
