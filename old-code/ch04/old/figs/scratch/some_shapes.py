
a = (1,1,1)
b = (-1,1,1)
c = (-1,-1,1)
d = (1,-1,1)

e = (1,1,-1)
f = (-1,1,-1)
g = (-1,-1,-1)
h = (1,-1,-1)

cube = [
    [a,b,c,d],
    [e,f,g,h],
    [a,e,f,b],
    [b,f,g,c],
    [c,g,h,d],
    [d,h,e,a],
]

def prism(n):
    xys = [(cos(2.*pi *t/n), sin(2*pi*t/n)) for t in range(0,n)]
    tops = [(x,y,1) for x,y in xys]
    bottoms = [(x,y,-1) for x,y in xys]
    # print(tops)
    # print(bottoms)
    pairs = list(zip(tops,bottoms))
    sides = [pairs[i] + pairs[(i+1)%n] for i in range(0,n)]
    return tops + bottoms + sides

def triangulate(poly):
    if len(poly) < 3:
        raise ArgumentException("polygons must have at least 3 vertices")
    elif len(poly) == 3:
        yield poly
    else:
        for i in range(1,len(poly) - 1):
            yield (poly[0], poly[i], poly[i+1])

print(prism(5))
draw([t for face in cube for t in triangulate(face)], blues)
