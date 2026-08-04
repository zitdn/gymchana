class Cone ():
    def __init__(self, x, y, radius = 5): 
        self.x = x
        self.y = y
        self.radius = radius
        self.selected = False
        
    def draw(self, painter):
        radius = self.radius
        if self.selected:
            radius*=1.5
            
        painter.drawEllipse(
            (self.x-radius),
            (self.y-radius),
            radius*2,
            radius*2
        )
        

    def contains(self, x, y ):
        distance = ((x- self.x)**2+ (y- self.y)**2)**0.5
        return distance <= self.radius
    
      