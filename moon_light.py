def pattern(t, dt, x, y, prev_state):
    row = math.floor(x * 150 / 9)
    col = math.floor(x * 150 % 9)

    v = plasma_sines_octave(row * 9 / 150, col/8, t, 3, 0.7, 0.7)
    c = palette(v)

    return c, hsv
