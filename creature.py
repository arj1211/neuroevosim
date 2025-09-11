import math
import random

from config import HEIGHT, WIDTH


class Creature:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.energy = 100
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = 2
        self.color = random.choice([(0, 200, 255), (200, 0, 255), (255, 200, 0)])
        self.radius = 10
        self.trail = []

    def move(self):
        self.angle += random.uniform(-0.2, 0.2)
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed

        self.x = max(self.radius, min(WIDTH - self.radius, self.x))
        self.y = max(self.radius, min(HEIGHT - self.radius, self.y))

        self.energy -= 0.1

        self.trail.append((self.x, self.y))
        if len(self.trail) > 25:
            self.trail.pop(0)

    def collides_with(self, other):
        return (
            math.dist((self.x, self.y), (other.x, other.y)) < self.radius + other.radius
        )
