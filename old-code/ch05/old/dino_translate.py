from vector_drawing import *
from matrices import *
dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4),
    (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3),
    (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)
]

count = len(dino_vectors)

# p = Plane((-7,-7),(7,7),"dino-plane")
# p.draw_vectors(*dino_vectors)

# for i in range(0,count):
#     p.draw_segment(dino_vectors[i],dino_vectors[(i+1)%count], color='blue')
# p.show()

dino_vectors_3d = [(x,y,1) for x,y in dino_vectors]

# s = Space((-7,-7,-1), (7,7,3), "dino-space")
# s.draw_vectors(*dino_vectors_3d)
# s.draw_axes()
# for i in range(0,count):
#     s.draw_segment(
#         dino_vectors_3d[i],
#         dino_vectors_3d[(i+1)%count], color='blue')
# s.show()
#
# magic_matrix = (
#     (1,0,3),
#     (0,1,1),
#     (0,0,1))
#
# translated = [multiply_matrix_vector(magic_matrix, v) for v in dino_vectors_3d]


# exercise ###################
# dino_vectors_3d_z2 = [(x,y,2) for x,y in dino_vectors]
#
# magic_matrix = (
#     (1,0,3),
#     (0,1,1),
#     (0,0,1))
#
# translated = [multiply_matrix_vector(magic_matrix, v) for v in dino_vectors_3d_z2]
# projected = [(x,y) for (x,y,z) in translated]
#
# translated_2d = [(x,y) for x,y,z in translated]
# p = Plane((-7,-7),(7,7),"dino-2z-plane-translated")
# p.draw_grid()
# p.draw_vectors(*dino_vectors, color='blue')
# p.draw_vectors(*translated_2d, color='red')
# for i in range(0,count):
#     p.draw_segment(dino_vectors[i],dino_vectors[(i+1)%count], color='blue')
#     p.draw_segment(translated_2d[i],projected[(i+1)%count], color='red')
# p.show()

##################

# exercise ###################
# dino_vectors_3d = [(x,y,1) for x,y in dino_vectors]
#
# magic_matrix = (
#     (1,0,-2),
#     (0,1,-2),
#     (0,0,1))
#
# translated = [multiply_matrix_vector(magic_matrix, v) for v in dino_vectors_3d]
# projected = [(x,y) for (x,y,z) in translated]
#
# translated_2d = [(x,y) for x,y,z in translated]
# p = Plane((-7,-7),(7,7),"dino-translated-neg2-neg2")
# p.draw_grid()
# p.draw_vectors(*dino_vectors, color='blue')
# p.draw_vectors(*translated_2d, color='red')
# for i in range(0,count):
#     p.draw_segment(dino_vectors[i],dino_vectors[(i+1)%count], color='blue')
#     p.draw_segment(translated_2d[i],projected[(i+1)%count], color='red')
# p.show()

##################


#EXERCISE
dino_vectors_3d = [(x,y,1) for x,y in dino_vectors]

magic_matrix = ((0.3535533905932738, -0.35355339059327373, 2), (0.35355339059327373, 0.3535533905932738, 2), (0, 0, 1))

translated = [multiply_matrix_vector(magic_matrix, v) for v in dino_vectors_3d]
projected = [(x,y) for (x,y,z) in translated]

translated_2d = [(x,y) for x,y,z in translated]
p = Plane((-7,-7),(7,7),"dino-rot-scale-trans")
p.draw_grid()
p.draw_vectors(*dino_vectors, color='blue')
p.draw_vectors(*translated_2d, color='red')
for i in range(0,count):
    p.draw_segment(dino_vectors[i],dino_vectors[(i+1)%count], color='blue')
    p.draw_segment(translated_2d[i],projected[(i+1)%count], color='red')
p.show()

#################################################




# s = Space((-7,-7,-1), (7,7,3), "dino-translated-space")
# s.draw_vectors(*dino_vectors_3d, color='blue')
# s.draw_vectors(*translated, color='red')
# s.draw_axes()
# for i in range(0,count):
#     s.draw_segment(
#         dino_vectors_3d[i],
#         dino_vectors_3d[(i+1)%count], color='blue')
#     s.draw_segment(
#         translated[i],
#         translated[(i+1)%count], color='red')
# s.show()
#
# translated_2d = [(x,y) for x,y,z in translated]
# p = Plane((-7,-7),(7,7),"dino-plane-translated")
# p.draw_vectors(*dino_vectors, color='blue')
# p.draw_vectors(*translated_2d, color='red')
# for i in range(0,count):
#     p.draw_segment(dino_vectors[i],dino_vectors[(i+1)%count], color='blue')
#     p.draw_segment(translated_2d[i],translated_2d[(i+1)%count], color='red')
# p.show()

# s = Space((-1,-1,-1),(4,4,4),"translation-move-standard-basis")
# s.draw_axes()
# s.draw_arrow((0,0,0),(1,0,0))
# s.draw_arrow((0,0,0),(0,1,0))
# s.draw_arrow((0,0,0),(0,0,1),color='blue')
# s.draw_arrow((0,0,0),(3,1,1),color='blue')
# s.draw_box((3,1,1))
# # s.draw_segment((0,0,1),(3,1,1),color='gray')
# s.show()

# rotate_and_translate = ((0,-1,3),(1,0,1),(0,0,1))
# rotated_translated_dino = [
#     multiply_matrix_vector(rotate_and_translate, v)
#     for v in dino_vectors_3d]
#
# s = Space((-7,-7,-1), (7,7,3), "dino-rotated-translated")
# # s.draw_vectors(*dino_vectors_3d, color='blue')
# s.draw_vectors(*rotated_translated_dino, color='red')
# s.draw_axes()
# for i in range(0,count):
#     # s.draw_segment(
#     #     dino_vectors_3d[i],
#     #     dino_vectors_3d[(i+1)%count], color='blue')
#     s.draw_segment(
#         rotated_translated_dino[i],
#         rotated_translated_dino[(i+1)%count], color='red')
# s.show()
