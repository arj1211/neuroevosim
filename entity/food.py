from entity.entity import Entity


class Food(Entity):
    def __init__(
        self,
        x: int | float,
        y: int | float,
    ):
        self.x = x
        self.y = y
        self.radius = 5
        self.color = (0, 255, 0)
