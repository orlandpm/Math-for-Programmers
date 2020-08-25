# Import a library of functions called 'pygame'
import pygame
import vectors
from math import pi, sqrt, cos, sin, atan2
from random import randint, uniform
from linear_solver import do_segments_intersect
import sys

# DEFINE OBJECTS OF THE GAME

class PolygonModel():
    def __init__(self,points):
        self.points = points
        self.rotation_angle = 0
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.angular_velocity = 0

    def transformed(self):
        rotated = [vectors.rotate2d(self.rotation_angle, v) for v in self.points]
        return [vectors.add((self.x,self.y),v) for v in rotated]

    def move(self, milliseconds):
        dx, dy = self.vx * milliseconds / 1000.0, self.vy * milliseconds / 1000.0
        self.x, self.y = vectors.add((self.x,self.y), (dx,dy))
        self.rotation_angle += self.angular_velocity * milliseconds / 1000.0

    def segments(self):
        point_count = len(self.points)
        points = self.transformed()
        return [(points[i], points[(i+1)%point_count])
                for i in range(0,point_count)]

    def does_collide(self, other_poly):
        for other_segment in other_poly.segments():
            if self.does_intersect(other_segment):
                return True
        return False

    def does_intersect(self, other_segment):
        for segment in self.segments():
            if do_segments_intersect(other_segment,segment):
                return True
        return False

class Ship(PolygonModel):
    def __init__(self):
        super().__init__([(0.5,0), (-0.25,0.25), (-0.25,-0.25)])

    def laser_segment(self):
        dist = 20. * sqrt(2)
        x,y = self.transformed()[0]
        return (x,y), (x + dist * cos(self.rotation_angle), y + dist*sin(self.rotation_angle))


class Asteroid(PolygonModel):
    def __init__(self):
        sides = randint(5,9)
        vs = [vectors.to_cartesian((uniform(0.5,1.0), 2 * pi * i / sides))
                for i in range(0,sides)]
        super().__init__(vs)
        self.vx = 0 # uniform(-1,1)
        self.vy = 0 # uniform(-1,1)
        self.angular_velocity = uniform(-pi/2,pi/2)

# INITIALIZE GAME STATE

ship = Ship()

asteroid_count = 10
asteroids = [Asteroid() for _ in range(0,asteroid_count)]

for ast in asteroids:
    ast.x = randint(-9,9)
    ast.y = randint(-9,9)


# HELPERS / SETTINGS

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

width, height = 400, 400

def to_pixels(x,y):
    return (width/2 + width * x / 20, height/2 - height * y / 20)

def draw_poly(screen, polygon_model, color=GREEN):
    pixel_points = [to_pixels(x,y) for x,y in polygon_model.transformed()]
    pygame.draw.aalines(screen, color, True, pixel_points, 10)

def draw_segment(screen, v1,v2,color=RED):
    pygame.draw.aaline(screen, color, to_pixels(*v1), to_pixels(*v2), 10)

screenshot_mode = False

# INITIALIZE GAME ENGINE

def main():


    pygame.init()


    screen = pygame.display.set_mode([width,height])

    pygame.display.set_caption("Asteroids!")

    done = False
    clock = pygame.time.Clock()

    # p key prints screenshot (you can ignore this variable)
    p_pressed = False

    while not done:

        clock.tick()

        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop

        # UPDATE THE GAME STATE

        milliseconds = clock.get_time()
        keys = pygame.key.get_pressed()

        for ast in asteroids:
            ast.move(milliseconds)

        if keys[pygame.K_LEFT]:
            ship.rotation_angle += milliseconds * (2*pi / 1000)

        if keys[pygame.K_RIGHT]:
            ship.rotation_angle -= milliseconds * (2*pi / 1000)

        laser = ship.laser_segment()

        # p key saves screenshot (you can ignore this)
        if keys[pygame.K_p] and screenshot_mode:
            p_pressed = True
        elif p_pressed:
            pygame.image.save(screen, 'figures/asteroid_screenshot_%d.png' % milliseconds)
            p_pressed = False

        # DRAW THE SCENE

        screen.fill(WHITE)

        if keys[pygame.K_SPACE]:
            draw_segment(screen, *laser)

        draw_poly(screen,ship)

        for asteroid in asteroids:
            if keys[pygame.K_SPACE] and asteroid.does_intersect(laser):
                asteroids.remove(asteroid)
            else:
                draw_poly(screen, asteroid, color=GREEN)


        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    if '--screenshot' in sys.argv:
        screenshot_mode = True
    main()
