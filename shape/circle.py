class Circle:
    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius

    def __contains__(self, item):
        px, py = item
        cx, cy = self.centre
        return ((px - cx)**2 + (py - cy)**2)**0.5 <= self.radius