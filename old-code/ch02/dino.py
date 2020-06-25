from vector_drawing import *
from vectors import *

dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4),
    (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3),
    (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)
]

fig, ax = plt.subplots()
plane = plt, ax

# def drawing_one():
#     draw_origin(plt)
#     set_bounds(plt, (-8,-8), (8,8))
#     draw_vectors(plt, dino_vectors)
#     plt.show()
#
#
# def drawing_two():
#     connect_the_dots(plt, dino_vectors)
#     draw_vectors(plt, dino_vectors)
#     draw_origin(plt)
#     set_bounds(plt, (-8,-8), (8,8))
#     plt.show()

# def drawing_three():
#     fig, ax = plt.subplots()
#     draw_axes(plt, ax)
#     draw_grid(plt, ax)
#     draw_origin(plt)
#     set_bounds(plt, (-8,-8), (8,8))
#     connect_the_dots(plt, dino_vectors)
#     draw_vectors(plt, dino_vectors)
#     plt.show()

# def drawing_four():
#     fig, ax = plt.subplots()
#     draw_axes(plt, ax)
#     draw_grid(plt, ax)
#     draw_origin(plt)
#     set_bounds(plt, (-2,-2), (8,8))
#     draw_vectors(plt, [(6,4)])
#     plt.show()

# def exercise2():
#     fig, ax = plt.subplots()
#     draw_axes(plt, ax)
#     draw_grid(plt, ax)
#     draw_origin(plt)
#     set_bounds(plt, (-2,-4), (4,2))
#     draw_vectors(plt, [(2,-2)])
#     plt.show()ing_three():
#     fig, ax = plt.subplots()
#     draw_axes(plt, ax)
#     draw_grid(plt, ax)
#     draw_origin(plt)
#     set_bounds(plt, (-8,-8), (8,8))
#     connect_the_dots(plt, dino_points)
#     draw_points(plt, dino_points)
#     plt.show()
#
# drawing_three()


# def drawing_five():
#     draw_axes(plane)
#     draw_grid(plane)
#     draw_origin(plane)
#     set_bounds(plane, (-8,-8), (8,8))
#     draw_segment(plane, (6,4), (3,1), color='blue')
#     # connect_the_dots(plane, dino_vectors, color='blue')
#     draw_vectors(plane, dino_vectors)
#     display(plane)
#
# drawing_five()

# def drawing_six():
#     draw_axes(plane)
#     draw_grid(plane)
#     draw_origin(plane)
#     set_bounds(plane, (-1,-1), (5,5))
#     draw_arrow(plane, (1,1), (4,3), color='blue')
#     # connect_the_dots(plane, dino_vectors, color='blue')
#     draw_vectors(plane, dino_vectors)
#     display(plane)
#
# drawing_six()


# def drawing_seven():
#     draw_axes(plane)
#     draw_grid(plane)
#     draw_origin(plane)
#     set_bounds(plane, (-2,-1), (5,5))
#     v1 = (4,3)
#     v2 = (-1, 1)
#     draw_arrow(plane, (0,0), v1, 'purple')
#     draw_arrow(plane, (0,0), v2, 'red')
#     draw_arrow(plane, v1, add(v1,v2), 'red')
#     draw_arrow(plane, (0,0), add(v1,v2), 'k')
#     draw_vectors(plane, [v1, v2, add(v1,v2)])
#
#     display(plane)
#
# drawing_seven()


# def drawing_eight():
#     draw_axes(plane)
#     draw_grid(plane)
#     draw_origin(plane)
#     set_bounds(plane, (-1,-1), (5,4))
#     v1 = (4,0)
#     v2 = (0,3)
#     draw_arrow(plane, (0,0), v1, 'blue')
#     draw_arrow(plane, v1, add(v1,v2), 'red')
#     draw_arrow(plane, (0,0), add(v1,v2), 'purple')
#     draw_vectors(plane, [v1, add(v1,v2)])
#
#     display(plane)
#
# drawing_eight()
#
# dino_vectors2 = [add((-1.5,-2.5), v) for v in dino_vectors]
#
# def translated_dino():
#         draw_axes(plane)
#         draw_grid(plane)
#         draw_origin(plane)
#         set_bounds(plane, (-8,-8), (8,8))
#         # connect_the_dots(plane, dino_vectors, color='blue')
#         draw_vectors(plane, dino_vectors, color='blue')
#         draw_vectors(plane, dino_vectors2, color='red')
#         connect_the_dots(plane, dino_vectors, color='blue')
#         connect_the_dots(plane, dino_vectors2, color='red')
#         for v1, v2 in zip(dino_vectors, dino_vectors2):
#             draw_arrow(plane, v1, v2, color='black')
#         display(plane)
#
# translated_dino()

# def hundred_dinos():
#     translations = [(12*x,10*y) for x in range(-5,5) for y in range(-5,5)]
#     draw_origin(plane)
#     set_bounds(plane, (-70,-60), (60,50))
#     for t in translations:
#         dino_copy =  [add(t, v) for v in dino_vectors]
#         connect_the_dots(plane, dino_copy, color='blue')
#     display(plane)
#
# hundred_dinos()

# def draw

# draw_segment(plt, (0,0), (1,1))
# draw_vectors(plt, dino_vectors)
# connect_the_dots(plt,dino_vectors)

# from math import sqrt, atan2
# def to_polar(v):
#     x,y = v[0], v[1]
#     length = sqrt(x**2 + y**2)
#     angle = atan2(y,x)
#     return (length, angle)

#
# def neg2_3():
#     fig, ax = plt.subplots()
#     draw_axes(plt, ax)
#     draw_grid(plt, ax)
#     draw_origin(plt)
#     set_bounds(plt, (-4,-4), (4,4))
#     draw_points(plt, [(-2,3)])
#     draw_segment(plt, (0,0),(6,9), 'k')
#     plt.show()
#
# neg2_3()
#





# max([length(v) for v in dino_vectors])


# def five_fold_sum():
#     draw_axes(plane)
#     draw_grid(plane)
#     draw_origin(plane)
#     set_bounds(plane, (-1,-1), (11,6))
#     draw_vectors(plane, [(10,5)])
#     for i in range(0,5):
#         draw_arrow(plane,(2*i,i),(2*i+2,i+1))
#     display(plane)
#
# five_fold_sum()

# def scalar_mult_example():
#     set_bounds(plane, (-3,-1), (1,7))
#     draw_arrow(plane, (0,0), (-1, 2), 'k')
#     draw_arrow(plane, (0,1), (-2.5, 6), 'k')
#     display(plane)
#
# scalar_mult_example()

# def aspect_ratio():
#     draw_axes(plane)
#     draw_grid(plane)
#     draw_origin(plane)
#     set_bounds(plane, (-1,-1), (10,7))
#     draw_vectors(plane, [(6,0), (6,4), (9,0), (9,6)])
#     draw_arrow(plane, (0,0), (6,0), color='red')
#     draw_arrow(plane, (0,0), (9,0), color='red')
#     draw_arrow(plane, (6,0), (6,4), color='blue')
#     draw_arrow(plane, (9,0), (9,6), color='blue')
#     draw_arrow(plane, (0,0), (6,4), color='purple')
#     draw_arrow(plane, (0,0), (9,6), color='purple')
#     display(plane)
#
# aspect_ratio()


# def negative_scalar_multiple():
#     draw_axes(plane)
#     draw_grid(plane)
#     draw_origin(plane)
#     set_bounds(plane, (-4,-3), (7,5))
#     draw_vectors(plane, [(6,4),(-3,-2)])
#     draw_arrow(plane, (0,0), (6,4))
#     draw_arrow(plane, (0,0), (-3,-2))
#     display(plane)
#
# negative_scalar_multiple()

# from random import uniform
# def vector_region():
#     draw_axes(plane)
#     draw_grid(plane)
#     draw_origin(plane)
#     set_bounds(plane, (-5,-5), (5,5))
#     u = (-1,1)
#     v = (1,1)
#     r = lambda: uniform(-3,3)
#     s = lambda: uniform(-1,1)
#     possibilities = [add(scale(r(), u), scale(s(), v)) for i in range(0,500)]
#     draw_vectors(plane, possibilities)
#     display(plane)
#
# vector_region()
#
# def negative_vector():
#     draw_axes(plane)
#     draw_grid(plane)
#     draw_origin(plane)
#     set_bounds(plane, (-5,-5), (5,5))
#     draw_vectors(plane, [(-4,3),(4,-3)])
#     draw_arrow(plane, (0,0), (-4,3))
#     draw_arrow(plane, (0,0), (4,-3))
#     display(plane)
# negative_vector()

# def subtract_vector():
#     draw_axes(plane)
#     draw_grid(plane)
#     draw_origin(plane)
#     set_bounds(plane, (-4,0), (3,4))
#     draw_vectors(plane, [(2,2),(-1,3),(-3,1)])
#     draw_arrow(plane, (0,0), (-1,3))
#     draw_arrow(plane, (0,0), (2,2))
#     draw_arrow(plane, (2,2), (-1,3), 'red')
#     draw_arrow(plane, (0,0), (-3,1), 'red')
#     display(plane)
# subtract_vector()

#
# def distance_segment():
#     draw_axes(plane)
#     draw_grid(plane)
#     draw_origin(plane)
#     set_bounds(plane, (-2,0), (3,4))
#     draw_vectors(plane, [(2,2),(-1,3)])
#     draw_segment(plane, (2,2), (-1,3), 'red')
#     display(plane)
# distance_segment()


# def distance_dups():
#     draw_axes(plane)
#     draw_grid(plane)
#     draw_origin(plane)
#     set_bounds(plane, (-2,-2), (4,6))
#     draw_vectors(plane, [(2,2),(-1,3), (-1,1), (3,5), (3,-1)])
#     draw_segment(plane, (2,2), (-1,3), 'red')
#     for x in [(-1,1), (3,5), (3,-1)]:
#         draw_segment(plane, (2,2), x, 'purple')
#     display(plane)
# distance_dups()
#
# from math import sin, cos, pi
# def protractor():
#     draw_grid(plane)
#     set_bounds(plane, (-1,0), (1,1))
#
#     for x in range(0,181):
#         theta = (pi * x / 180)
#         endpoint = (cos(theta),sin(theta))
#         sc = 0.8 if x % 10 == 0 else 0.9 if x % 5 == 0 else 0.95
#         startpoint = scale(sc, endpoint)
#         draw_segment(plane,startpoint,endpoint,'k')
#     display(plane)
# protractor()

# def four_three_vector():
#     draw_axes(plane)
#     draw_grid(plane)
#     draw_origin(plane)
#     set_bounds(plane, (-1,-1), (5,4))
#     draw_vectors(plane, [(4,3)])
#     draw_segment(plane, (0,0), (4,3), 'red')
#     display(plane)
# four_three_vector()
#
# from math import sin, cos, pi
# def polar_to_cart():
#     draw_axes(plane)
#     draw_grid(plane)
#     set_bounds(plane, (-5,-1), (3,4))
#
#     for x in range(0,181):
#         theta = (pi * x / 180)
#         endpoint = (cos(theta),sin(theta))
#         sc = 0.8 if x % 10 == 0 else 0.9 if x % 5 == 0 else 1
#         startpoint = scale(sc, endpoint)
#         draw_segment(plane,startpoint,endpoint,'k')
#     draw_segment(plane, (0,0), (-3,6), 'red')
#     draw_vectors(plane, [(-1.34,2.68)])
#     draw_arrow(plane, (0,0), (-1.34,0), 'blue')
#     draw_arrow(plane, (-1.34,0), (-1.34,2.68), 'blue')
#     display(plane)
#
#
# polar_to_cart()




# from math import sin, cos, pi
# def tan_neg_2():
#     draw_axes(plane)
#     draw_grid(plane)
#     set_bounds(plane, (-4,-1), (2,7))
#
#     for x in range(0,181):
#         theta = (pi * x / 180)
#         endpoint = (cos(theta),sin(theta))
#         sc = 0.8 if x % 10 == 0 else 0.9 if x % 5 == 0 else 1
#         startpoint = scale(sc, endpoint)
#         draw_segment(plane,startpoint,endpoint,'k')
#     draw_segment(plane, (0,0), (-10,20), 'red')
#     for x,y in [(-1.34, 2.68), (-1,2), (-3,6)]:
#         draw_vectors(plane, [(x,y)])
#         draw_arrow(plane, (0,0), (x,0), 'blue')
#         draw_arrow(plane, (x,0), (x,y), 'blue')
#     display(plane)
#
#
# tan_neg_2()

# from math import sin, cos, tan, pi
# def tan_examples():
#     draw_axes(plane)
#     draw_grid(plane)
#     set_bounds(plane, (-2,-2), (2,2))
#
#     for x in range(0,360):
#         theta = (pi * x / 180)
#         endpoint = (cos(theta),sin(theta))
#         sc = 0.8 if x % 10 == 0 else 0.9 if x % 5 == 0 else 1
#         startpoint = scale(sc, endpoint)
#         draw_segment(plane,startpoint,endpoint,'k')
#     draw_segment(plane, (0,0), (10,10), 'red')
#     draw_segment(plane, (0,0), (-10, -10 * tan(pi * 200/180)), 'red')
#     for x,y in [(1,1), (-1,-0.36)]:
#         draw_vectors(plane, [(x,y)])
#     #     draw_arrow(plane, (0,0), (x,0), 'blue')
#     #     draw_arrow(plane, (x,0), (x,y), 'blue')
#     display(plane)
#
#
# tan_examples()

#
# from math import sin, cos, tan, pi
# def tan_22():
#     draw_axes(plane)
#     draw_grid(plane)
#     set_bounds(plane, (-1,-1), (11,5))
#
#     # for x in range(0,181):
#     #     theta = (pi * x / 180)
#     #     endpoint = (cos(theta),sin(theta))
#     #     sc = 0.8 if x % 10 == 0 else 0.9 if x % 5 == 0 else 1
#     #     startpoint = scale(sc, endpoint)
#     #     draw_segment(plane,startpoint,endpoint,'k')
#     draw_segment(plane, (0,0), (20, 20 * tan(22*pi/180)), 'red')
#     # for x,y in [(1,1), (-1,-0.36)]:
#     #     draw_vectors(plane, [(x,y)])
#     display(plane)
#
# tan_22()
#
# from math import pi
# def polar_rose():
#     draw_axes(plane)
#     draw_grid(plane)
#     set_bounds(plane, (-1.5,-1.5), (1.5,1.5))
#     polars = [(cos(x*pi/100.0), 2*pi*x/1000.0) for x in range(0,1000)]
#     vectors = [to_cartesian(p) for p in polars]
#     connect_the_dots(plane, vectors, 'green')
#     display(plane)
# polar_rose()
#

#

#
# fig, ax = plt.subplots()
# plt.scatter([0],[0], color='k', marker='x')
#
# xs = map(lambda x:x[0], dino_vectors)
# ys = map(lambda x:x[1], dino_vectors)
# plt.scatter(xs,ys)
#
#
#
# ax.set_xticks(np.arange(-8,8,1))
# ax.set_yticks(np.arange(-8,8,1))
# plt.grid(True)
# ax.set_axisbelow(True)
#
# xmin,ymin = (-8,-8)
# xmax,ymax = (8,8)
# plt.ylim(ymin,ymax)
# plt.xlim(xmin,xmax)
#
# plt.show()

# def dino_again():
#     connect_the_dots(plane, dino_vectors, color='black')
#     draw_vectors(plane, dino_vectors)
#     draw_origin(plane)
#     set_bounds(plane, (-8,-8), (8,8))
#     display(plane)
#
# dino_again()

# def rotate():
#     draw_axes(plane)
#     draw_grid(plane)
#     set_bounds(plane, (-1.5,-0.5), (1.5,1))
#     vs = [to_cartesian((1,2)),to_cartesian((1,1)),to_cartesian((1,3))]
#     draw_vectors(plane, vs)
#     # for v in vs:
#     #     draw_arrow(plane, (0,0), v, color='blue')
#     display(plane)
#
# rotate()


# from math import pi
# def rotate_dino(rotation_angle):
#     connect_the_dots(plane, dino_vectors, color='gray')
#     dino_polar = [to_polar(v) for v in dino_vectors]
#     dino_rotated_polar = [(l,angle + rotation_angle) for l,angle in dino_polar]
#     dino_rotated = [to_cartesian(p) for p in dino_rotated_polar]
#     connect_the_dots(plane, dino_rotated, color='red')
#     draw_grid(plane)
#     draw_origin(plane)
#     set_bounds(plane, (-8,-8), (8,8))
#     plt.show()
#
# rotate_dino(pi/4)


# from math import pi
# def polygon(n):
#     return [to_cartesian((1, 2*pi*k/n)) for k in range(0,n)]
#
# def draw_polygon():
#     draw_grid(plane)
#     draw_axes(plane)
#     draw_origin(plane)
#     draw_vectors(plane, polygon(7))
#     connect_the_dots(plane, polygon(7), color='black')
#     set_bounds(plane, (-1.5,-1.5), (1.5,1.5))
#     display(plane)
#
# draw_polygon()


#
# from math import pi
# def rotate_dino(rotation_angle):
#     connect_the_dots(plane, dino_vectors, color='gray')
#     dino_polar = [to_polar(v) for v in dino_vectors]
#     dino_rotated_polar = [(l,angle + rotation_angle) for l,angle in dino_polar]
#     dino_rotated = [to_cartesian(p) for p in dino_rotated_polar]
#     connect_the_dots(plane, dino_rotated, color='red')
#     draw_grid(plane)
#     draw_origin(plane)
#     set_bounds(plane, (-8,-8), (8,8))
#     plt.show()

# from math import pi
# def translate_rotate_dino():
#     connect_the_dots(plane, dino_vectors, color='gray')
#     # new_dino = translate((8,8), rotate(5 * pi/3, dino_vectors))
#
#     # exercise
#     step_1 = translate((8,8), dino_vectors)
#     connect_the_dots(plane, step_1, color='black')
#     draw_arrow(plane, (0,0), (8,8), color='black')
#     draw_vectors(plane,[(8,8)] + rotate(5*pi/3,[(8,8)]))
#     new_dino = rotate(5 * pi/3, step_1)
#
#     connect_the_dots(plane, new_dino, color='red')
#     draw_axes(plane)
#     draw_grid(plane)
#     draw_origin(plane)
#     set_bounds(plane, (-8,-8), (20,16))
#     display(plane)
#
# translate_rotate_dino()



### ex5
# parabola = [(x,x**2) for x in range(-10,11)]
# draw_axes(plane)
# draw_origin(plane)
# set_bounds(plane, (-11,-1), (10,101))
# draw_vectors(plane,parabola)
# display(plane)

### ex16
# from math import sqrt, pi
# draw_axes(plane)
# draw_origin(plane)
# set_bounds(plane, (-1,-1), (6,8))
# w = (sqrt(2),sqrt(3))
# print(w)
# print(scale(pi,w))
#
# draw_arrow(plane,(0,0),scale(pi,w),color='red')
# draw_arrow(plane,(0,0),w,color='black')
# draw_vectors(plane,[w, scale(pi, w)])
# display(plane)

# #### ex 26
# for n in range(-12,15):
#     for m in range(-14, 13):
#         if distance((n,m), (1,-1)) == 13 and n > m > 0:
#             print((n,m))

## ex 29
# v = (-4.879, 6.962)
# draw_axes(plane)
# draw_origin(plane)
# draw_grid(plane)
# set_bounds(plane, (-6,-1), (3,8))
# draw_vectors(plane, [v])
# draw_arrow(plane,(0,0),v,color='red')
# display(plane)
