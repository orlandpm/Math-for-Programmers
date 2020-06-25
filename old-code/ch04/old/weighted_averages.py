from vectors import *
from vector_drawing import *

def weighted_average(s,v1,v2):
    return add(scale(s,v1), scale((1-s),v2))

def segment_with_averages(plane, v1,v2, points=10,color='red',transform=lambda x:x):
    plane.draw_vectors(*[transform(weighted_average(1.0 * s / points,v1,v2)) for s in range(0,points+1)], color=color)
    return plane

# (Plane((-2,0), (4,5),"line-segment-10-points")
#     .draw_vectors(*[weighted_average(0.1 * s,(-1,1),(3,4)) for s in range(0,10)])
#     ).show()
#
#
# (Plane((-2,0), (4,5),"line-segment-100-points")
#     .draw_vectors(*[weighted_average(0.01 * s,(-1,1),(3,4)) for s in range(0,100)])
#     ).show()

def triangle(p,v1,v2,v3,points=20, transform=lambda x:x):
    segment_with_averages(p,v1,v2, points,color='red',transform=transform)
    segment_with_averages(p,v2,v3, points,color='green',transform=transform)
    segment_with_averages(p,v3,v1, points,color='blue',transform=transform)

p = Plane((-5,0), (5,5), "triangle-under-rotation")
p.draw_axes()
p.draw_grid()
v1,v2,v3 = (1,1), (4,2), (2,3)
triangle(p,v1,v2,v3)
triangle(p,v1,v2,v3, transform=lambda v: (rotate2d(pi/2, v)))
p.show()


p = Plane((0,0), (17,10), "triangle-under-squaring")
p.draw_axes()
p.draw_grid()
v1,v2,v3 = (2,2), (4,1.5), (1.5,3)
triangle(p,v1,v2,v3)
triangle(p,v1,v2,v3,transform=lambda v: (v[0]*v[0],v[1]*v[1]))
p.show()
