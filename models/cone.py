class Cone ():
    def __init__(self, x, y, radius = 5): 
        self.x = x
        self.y = y
        self.radius = radius
        
    def draw(self, painter):
        painter.drawEllipse(
            (self.x-self.radius),
            (self.y-self.radius),
            10,
            10
        )