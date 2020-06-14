# Import a library of functions called 'pygame'
import pygame
import vectors
from math import pi, sqrt, cos, sin, atan2
from random import randint, uniform
from linear_solver import do_segments_intersect
import numpy as np

# DEFINE OBJECTS OF THE GAME

bounce = True

class PolygonModel():
    def __init__(self,points):
        self.points = points
        self.rotation_angle = 0
        self.gravity = 0 # G * m1 from Newton's law
        self.mass = 1
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.angular_velocity = 0
        self.draw_center = False

    def transformed(self):
        rotated = [vectors.rotate2d(self.rotation_angle, v) for v in self.points]
        return [vectors.add((self.x,self.y),v) for v in rotated]


# def move(self, milliseconds, thrust_vector=(0,0), gravity_source):
#     tx, ty = thrust_vector
#     gx, gy = gravitational_field(src, self.x, self.y)
#     ax = tx + gx
#     ay = ty + gy
#     self.vx += ax * milliseconds/1000
#     self.vy += ay * milliseconds/1000
#
#     dx, dy = self.vx * milliseconds / 1000.0, self.vy * milliseconds / 1000.0
#     self.x, self.y = vectors.add((self.x,self.y), (dx,dy))
#
#     if bounce:
#         if self.x < -10 or self.x > 10:
#             self.vx = - self.vx
#         if self.y < -10 or self.y > 10:
#             self.vy = - self.vy
#     else:
#         if self.x < -10:
#             self.x += 20
#         if self.y < -10:
#             self.y += 20
#         if self.x > 10:
#             self.x -= 20
#         if self.y > 10:
#             self.y -=20
#
#     self.rotation_angle += self.angular_velocity * milliseconds / 1000.0

    def move(self, milliseconds, thrust_vector=(0,0), gravity_sources=[]):
        ax, ay = thrust_vector
        gx, gy = gravitational_field(gravity_sources, self.x, self.y)
        ax += gx
        ay += gy
        self.vx += ax * milliseconds/1000
        self.vy += ay * milliseconds/1000

        dx, dy = self.vx * milliseconds / 1000.0, self.vy * milliseconds / 1000.0
        self.x, self.y = vectors.add((self.x,self.y), (dx,dy))

        if bounce:
            if self.x < -10 or self.x > 10:
                self.vx = - self.vx
            if self.y < -10 or self.y > 10:
                self.vy = - self.vy
        else:
            if self.x < -10:
                self.x += 20
            if self.y < -10:
                self.y += 20
            if self.x > 10:
                self.x -= 20
            if self.y > 10:
                self.y -=20

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
        self.vx = uniform(-1,1)
        self.vy = uniform(-1,1)
        self.angular_velocity = uniform(-pi/2,pi/2)

class BlackHole(PolygonModel):
    def __init__(self,gravity):
        vs = [vectors.to_cartesian((0.5, 2 * pi * i / 20))
                for i in range(0,20)]
        super().__init__(vs)
        self.gravity = gravity
# ASTEROID HELPERS

def trajectory(start,end,steps):
    xi,yi = start
    xf,yf = end
    xs = np.linspace(xi,xf,steps+1)
    ys = np.linspace(yi,yf,steps+1)
    model = Asteroid()
    asts = [Asteroid() for _ in range(0,steps+1)]
    for x,y,ast in zip(xs,ys,asts):
        ast.vx = ast.vy = ast.angular_velocity = 0
        ast.points = model.points
        ast.x = x
        ast.y = y
        ast.draw_center = True
    return asts

# INITIALIZE GAME STATE

ship = Ship()
ship.x = 7
ship.y = 3

asteroid_count = 10

default_asteroids = [Asteroid() for _ in range(0,asteroid_count)]

black_hole = BlackHole(0.1)
black_hole2 = BlackHole(0.1)

black_hole.x, black_hole.y = -3, 4
black_hole2.x, black_hole2.y = 2, -1

black_holes = [black_hole, black_hole2]

def gravitational_field(sources, x, y):
    fields = [vectors.scale(- source.gravity, (x - source.x, y - source.y))
                for source in sources]
    return vectors.add(*fields)

for ast in default_asteroids:
    ast.x = randint(-9,9) # 9 * uniform(ast.vy, 0)
    ast.y = randint(-9,9) # 9 * uniform(0, - ast.vx)

# HELPERS / SETTINGS

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE =  (0, 0, 255)
GREEN = (0, 255, 0)
RED =   (255, 0, 0)
LIGHT_GRAY =  (240, 240, 240)
DARK_GRAY = (128, 128, 128)
width, height = 400, 400

def to_pixels(x,y):
    return (width/2 + width * x / 20, height/2 - height * y / 20)

def draw_poly(screen, polygon_model, color=BLACK, fill=False):
    pixel_points = [to_pixels(x,y) for x,y in polygon_model.transformed()]
    if fill:
        pygame.draw.polygon(screen, color, pixel_points, 0)
    else:
        pygame.draw.lines(screen, color, True, pixel_points, 2)
    if polygon_model.draw_center:
        cx, cy = to_pixels(polygon_model.x, polygon_model.y)
        pygame.draw.circle(screen, BLACK, (int(cx), int(cy)), 4, 4)

def draw_segment(screen, v1,v2,color=RED):
    pygame.draw.line(screen, color, to_pixels(*v1), to_pixels(*v2), 2)

def draw_grid(screen):
    for x in range(-9,10):
        draw_segment(screen, (x,-10), (x,10), color=LIGHT_GRAY)
    for y in range(-9,10):
        draw_segment(screen, (-10, y), (10, y), color=LIGHT_GRAY)

    draw_segment(screen, (-10, 0), (10, 0), color=DARK_GRAY)
    draw_segment(screen, (0, -10), (0, 10), color=DARK_GRAY)



thrust = 3
trajectory_mode = False
trajectory_frame = 1000

# INITIALIZE GAME ENGINE

def main(asteroids=default_asteroids):

    pygame.init()

    screen = pygame.display.set_mode([width,height])

    pygame.display.set_caption("Asteroids!")

    done = False
    clock = pygame.time.Clock()

    if trajectory_mode:
        screen.fill(WHITE)
        draw_grid(screen)

    since_last_trajectory_frame = trajectory_frame

    while not done:

        clock.tick()

        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop

        # UPDATE THE GAME STATE

        milliseconds = clock.get_time()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            ship.rotation_angle += milliseconds * (2*pi / 1000)

        if keys[pygame.K_RIGHT]:
            ship.rotation_angle -= milliseconds * (2*pi / 1000)

        for ast in asteroids:
            ast.move(milliseconds,(0,0),gravity_sources=black_holes)

        for bh in black_holes:
            others = [other for other in black_holes if other != bh]
            bh.move(milliseconds, (0,0), others)

        ship_thrust_vector = (0,0)

        if keys[pygame.K_UP]:
            ship_thrust_vector = vectors.to_cartesian((thrust, ship.rotation_angle))

        elif keys[pygame.K_DOWN]:
            ship_thrust_vector = vectors.to_cartesian((- thrust, ship.rotation_angle))

        ship.move(milliseconds, ship_thrust_vector, black_holes)

        laser = ship.laser_segment()

        # DRAW THE SCENE


        if not trajectory_mode:
            screen.fill(WHITE)
            draw_grid(screen)

        if keys[pygame.K_SPACE]:
            draw_segment(screen, *laser)

        since_last_trajectory_frame += milliseconds
        if not trajectory_mode or since_last_trajectory_frame >= trajectory_frame:

            draw_poly(screen,ship)
            since_last_trajectory_frame = 0

            for bh in black_holes:
                draw_poly(screen, bh, fill=True)

            for asteroid in asteroids:
                if keys[pygame.K_SPACE] and asteroid.does_intersect(laser):
                    asteroids.remove(asteroid)
                else:
                    draw_poly(screen, asteroid, color=GREEN)


        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
