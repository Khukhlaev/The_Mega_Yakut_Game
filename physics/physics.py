g = 0.1667  # gravity acceleration per frame


def gravity(vy, on_platform):
    global g
    if not on_platform:
        vy += g
    else:
        vy = 0
    return vy
