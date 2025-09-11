import random

from config import HEIGHT, NUM_CREATURES, NUM_FOOD, WIDTH
from creature import Creature
from food import Food


class Environment:
    def __init__(self):
        self.creatures = [
            Creature(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
            for _ in range(NUM_CREATURES)
        ]
        self.foods = [Food() for _ in range(NUM_FOOD)]

    def update(self):
        """Advance simulation by one tick"""
        for creature in self.creatures[:]:
            creature.move()

            # Food interactions
            for food in self.foods[:]:
                if creature.collides_with(food):
                    creature.energy += 30
                    self.foods.remove(food)
                    self.foods.append(Food())

            # Death & respawn
            if creature.energy <= 0:
                self.creatures.remove(creature)
                self.creatures.append(
                    Creature(
                        random.randint(50, WIDTH - 50),
                        random.randint(50, HEIGHT - 50),
                    )
                )
