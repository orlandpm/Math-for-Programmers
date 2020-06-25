def positions(dt):
    t = 0
    (x, y) = (0, 0)
    while y >= 0:
        yield (t, x, y)
        (vx, vy) = (15.0, 26.0 - 9.8 * t)
        (x, y) = (x + vx*dt, y + vy*dt)
        t = t + dt

for x in positions(1):
    print x
