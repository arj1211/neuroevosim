import math
import random

from brain.brain import Brain, Decision, SensoryInfo
from entity.entity import Entity


class Creature(Entity):
    def __init__(
        self,
        x: int | float,
        y: int | float,
        brain: Brain,
        color: tuple[int, int, int] = (-1, -1, -1),
    ):
        # entity-level
        self.x, self.y = x, y
        self.color = (
            random.choice([(0, 200, 255), (200, 0, 255), (255, 200, 0)])
            if color == (-1, -1, -1)
            else color
        )
        self.trail = []

        # creature brain instance
        self.brain = brain

        # creature behaviour params
        self.energy = 1.0
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = 2.0
        self.radius = 10

    def update_from_sensory(self, sensory: SensoryInfo, dt: float = 1.0):
        # call brain to decide
        decision: Decision = self.brain.decide(sensory)
        # apply decision -> update angle & speed
        self.angle += decision.turn * random.uniform(0.1, 0.5)  # scale turning rate
        forward_speed = max(0.0, decision.throttle) * self.speed
        self.x += math.cos(self.angle) * forward_speed
        self.y += math.sin(self.angle) * forward_speed

        # energy bookkeeping (example)
        self.energy -= 0.001 * (abs(decision.throttle) + abs(decision.turn)) * dt
        self.energy = max(0.0, min(1.0, self.energy))

        # trail + bounds
        self.trail = self.trail or []
        self.trail.append((self.x, self.y))
        if len(self.trail) > 50:
            self.trail.pop(0)

        # let brain see a tick
        if hasattr(self.brain, "on_tick"):
            self.brain.on_tick(dt)

    def collides_with(self, other: Entity) -> bool:
        return (
            math.dist((self.x, self.y), (other.x, other.y)) < self.radius + other.radius
        )
