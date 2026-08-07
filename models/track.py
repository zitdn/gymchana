class Track():
    def __init__(self):
        self.objects = []
    
    def add_object(self, obj):
        self.objects.append(obj)

    def get_object_at(self, x, y):
        for obj in self.objects:
            if obj.contains(x, y):
                return obj

        return None
