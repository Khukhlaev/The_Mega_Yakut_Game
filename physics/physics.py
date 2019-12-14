g = 0.5  # gravity acceleration per frame
k = 0.2  # x_resistance acceleration per frame


def gravity(vy, on_platform):
    """Add a gravity effect if the object is not on the platform"""
    global g
    if not on_platform:
        vy += g
    else:
        vy = 0
    return vy


def x_resistance(vx):
    """Stopping player while flying on x. Needed for death animation."""
    global k
    if vx >= 0:
        vx -= k
    else:
        vx += k
    return vx
