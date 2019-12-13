g = 0.5  # gravity acceleration per frame


def gravity(vy, on_platform):
    """Add a gravity effect if the object is not on the platform"""
    global g
    if not on_platform:
        vy += g
    else:
        vy = 0
    return vy
