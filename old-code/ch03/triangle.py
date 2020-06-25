from vectors import *
from vector_drawing import *

triangle = [(2.3,1.1,0.9), (4.5,3.3,2.0), (1.0,3.5,3.9)]

(Space((0,0,0), (5,5,5), "triangle-space")
    .draw_vectors(*triangle, color='k')
    .draw_polygon(*triangle)
    .show())