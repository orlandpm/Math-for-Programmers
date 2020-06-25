from vector_drawing import *
s = (Space((-1,-1,-1), (5,5,6), "x-y-z-components")
    .draw_origin()
    .draw_axes()
    .draw_arrow((0,0,0),(4,3,5),color='purple')
    .draw_box((4,3,5))
    .draw_vectors((4,3,5))

)

for x in range(0,4):
    s.draw_arrow((x,0,0),(x+1,0,0), color='red')

for y in range(0,3):
    s.draw_arrow((4,y,0),(4,y+1,0), color='green')

for z in range(0,5):
    s.draw_arrow((4,3,z),(4,3,z+1), color='blue')

s.show()
