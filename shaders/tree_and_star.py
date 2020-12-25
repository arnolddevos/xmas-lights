def pattern(t, dt, x, y, prev_state):
    
    b = 150/214
    
    def head(x, t):
        row = math.floor(x*8)
        a = math.floor(x * 64 % 8)
        col = a if row % 2 else 7-a
    
        r = abs((row-3.5)/7) + abs((col-3.5)/7)

        v = plasma_sines_octave(r, 1 - r, t, 3, 0.5, 0.5)
        c = palette(v)

        return (c[0], c[1], c[2]*0.5), hsv

    def body(x):
        v = plasma_sines_octave(x, y, t, 7, 1.5, 0.5)
        c = palette(v)
        return c, hsv
    
    return body(x/b) if x < b else head((x-b)/(1-b), t)
