from vectors import *
from vector_drawing import *

def S(v):
    x,y = v
    return x*x, y*y

p = Plane((0,0), (6,6), "grid-before-squaring-transform")
p.draw_axes()
p.draw_grid()
vs = [(x,y) for x in range(0,6) for y in range(0,6)]
p.draw_vectors(*vs)
p.show()


p = Plane((0,0), (26,26), "grid-under-squaring-transform")
p.draw_axes()
p.draw_grid()
vs = [S((x,y)) for x in range(0,6) for y in range(0,6)]
p.draw_vectors(*vs)
p.show()
