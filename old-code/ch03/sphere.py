from vectors import *
from vector_drawing import *
import matplotlib
import matplotlib.cm

blues = matplotlib.cm.get_cmap('Blues')

octahedron = [
    [(1,0,0), (0,1,0), (0,0,1)],
    [(1,0,0), (0,0,-1), (0,1,0)],
    [(1,0,0), (0,0,1), (0,-1,0)],
    [(1,0,0), (0,-1,0), (0,0,-1)],
    [(-1,0,0), (0,0,1), (0,1,0)],
    [(-1,0,0), (0,1,0), (0,0,-1)],
    [(-1,0,0), (0,-1,0), (0,0,1)],
    [(-1,0,0), (0,0,-1), (0,-1,0)],
]

def vertices(faces):
    return [vertex for face in faces for vertex in face]

s = Space((-2,-2,-2), (2,2,2), "octahedron")

s.draw_vectors(*[vertex for face in octahedron for vertex in face])

s.draw_origin()
s.draw_axes()
s.show()



def vector_to_2d(v):
    return (component(v,(1,0,0)), component(v,(0,1,0)))

def face_to_2d(face):
    return [vector_to_2d(vertex) for vertex in face]

def normal(face):
    return(cross(subtract(face[1], face[0]), subtract(face[2], face[0])))


def render(plane, faces, light=(1,2,3), color_map=blues, lines=None):
    for face in faces:
        unit_normal = unit(normal(face))
        if unit_normal[2] > 0:
            color = color_map(1 - dot(unit(normal(face)), unit(light)))
            plane.fill_polygon(face_to_2d(face), facecolors=[color], antialiaseds=[False])
            if lines:
                plane.draw_polygon(face_to_2d(face), color='k')



screen = Plane((-2,-2),(2,2),"screen")
render(screen, octahedron, lines='k')
screen.show()

def split(face):
    midpoints = [unit(add(face[i], face[(i+1)%len(face)])) for i in range(0,len(face))]
    triangles = [(face[i], midpoints[i], midpoints[(i-1)%len(face)]) for i in range(0,len(face))]
    return [midpoints] + triangles

def rec_split(faces, depth=0):
    if depth == 0:
        return faces
    else:
        return rec_split([new_face for face in faces for new_face in split(face)], depth-1)


# NICE SPHERE!
def sphere_approx(n):
    screen = Plane((-2,-2),(2,2),"sphere-approx-%d" % n)
    render(screen, rec_split(octahedron,n))
    screen.show()

# sphere_approx(0)
# sphere_approx(1)
# sphere_approx(2)
# sphere_approx(3)
sphere_approx(4)
# sphere_approx(5)

# (Plane((-2,-2),(2,2),"stupid-cube")
#     .fill_polygon([(1,1),(1,-1),(-1,-1),(-1,1)])
# ).show()
