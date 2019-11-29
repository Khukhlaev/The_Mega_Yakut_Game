g = 0.1667  # gravity acceleration


def gravity(vy, on_platform):
    global g
    if not on_platform:
        if vy >= 0:
            vy += g
        else:
            vy -= g
    else:
        vy = 0
    return vy