class Track():
    def __init__(self):
        self.cones = []
    
    def add_cone(self, cone):
        self.cones.append(cone)

    def get_cone_at(self, x, y):
        for cone in self.cones:
            if cone.contains(x, y):
                return cone

        return None
