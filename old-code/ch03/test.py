from vectors import *
from vector_drawing import *

# (Space((-2,-3,-1), (1,1,3),"ex-draw-vector")
#     .draw_origin()
#     .draw_axes()
#     .draw_vectors((-1,-2,2))
#     .draw_arrow((0,0,0),(-1,-2,2),color='purple')
#     .draw_box((-1,-2,2))
# ).show()

def draw_cube():
    pm1 = [1,-1]
    vertices = [(x,y,z) for x in pm1 for y in pm1 for z in pm1]
    edges = [((-1,y,z),(1,y,z)) for y in pm1 for z in pm1] +\
                [((x,-1,z),(x,1,z)) for x in pm1 for z in pm1] +\
                [((x,y,-1),(x,y,1)) for x in pm1 for y in pm1]
    s = (Space((-2,-2,-2), (2,2,2),"ex-cube").draw_axes())
    s.draw_vectors(*vertices)
    for edge in edges:
        s.draw_segment(*edge, color='blue')
    s.show()



def vector_sum():
    (Space((-2,-2,-2), (5,1,4),"ex-vector-sum")
        .draw_axes()
        .draw_arrow((0,0,0), (4,0,3), color='red')
        .draw_arrow((0,0,0), (-1,0,1), color='blue')
        .draw_arrow((4,0,3), (3,0,4), color='blue')
        .draw_arrow((-1,0,1), (3,0,4), color='red')
        .draw_arrow((0,0,0),(3,0,4))
    ).show()

def octahedron_skeleton():
    top = (0,0,1)
    bottom = (0,0,-1)
    xy_plane = [(1,0,0),(0,1,0),(-1,0,0),(0,-1,0)]
    edges = [(top,p) for p in xy_plane] +\
                [(bottom, p) for p in xy_plane] +\
                [(xy_plane[i],xy_plane[(i+1)%4]) for i in range(0,4)]
    s = (Space((-2,-2,-2), (2,2,2),"ex-octahedron-skeleton")
        .draw_axes())

    for edge in edges:
        s.draw_segment(*edge, color='blue')

    s.show()

octahedron_skeleton()
