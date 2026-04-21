from uuid import uuid4

class Yarn:
    def __init__(self, name, colour, weight, meters, type, yarn_id=None):
        self.name = name
        self.colour = colour
        self.weight = weight
        self.meters = meters
        self.type = type
        self.id = yarn_id if yarn_id else str(uuid4())
