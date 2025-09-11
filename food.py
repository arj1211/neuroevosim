import random

from config import HEIGHT, WIDTH
from entity import Entity


class Food(Entity):
    def __init__(self):
        self.x = random.randint(20, WIDTH - 20)
        self.y = random.randint(20, HEIGHT - 20)
        self.color = (0, 255, 0)
        self.radius = 5
