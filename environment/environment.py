import math
import random

import config
from brain.brain import SensoryInfo
from brain.rule_brain import RuleBasedBrain
from entity.creature import Creature
from entity.food import Food


class Environment:
    WIDTH, HEIGHT = config.WIDTH, config.HEIGHT
    PERCEPTION_RADIUS = min(HEIGHT, WIDTH) // 3  # pixels
    NUM_CREATURES = config.NUM_CREATURES
    NUM_FOOD = config.NUM_FOOD
    TICKS = 0.0  # I'm not sure what to do with this

    def __init__(self):
        self.creatures: list[Creature] = [
            Creature(
                x=random.randint(50, self.WIDTH - 50),
                y=random.randint(50, self.HEIGHT - 50),
                brain=RuleBasedBrain(),
            )
            for _ in range(self.NUM_CREATURES)
        ]
        self.foods: list[Food] = [
            Food(
                x=random.randint(20, self.WIDTH - 20),
                y=random.randint(20, self.HEIGHT - 20),
            )
            for _ in range(self.NUM_FOOD)
        ]

    def compute_sensory_for(self, creature):
        # find nearest food (if any within perception radius)
        nearest = None
        nearest_d = float("inf")
        for food in self.foods:
            d = math.dist((creature.x, creature.y), (food.x, food.y))
            if d < nearest_d:
                nearest = food
                nearest_d = d

        if nearest is None or nearest_d > self.PERCEPTION_RADIUS:
            nearest_pos = None
            nearest_norm_dist = 1.0
            nearest_angle = 0.0
        else:
            nearest_pos = (nearest.x, nearest.y)
            nearest_norm_dist = nearest_d / max(self.WIDTH, self.HEIGHT)
            # angle from creature heading to food (-pi..pi)
            world_angle = math.atan2(nearest.y - creature.y, nearest.x - creature.x)
            rel = (world_angle - creature.angle + math.pi) % (2 * math.pi) - math.pi
            nearest_angle = rel

        # similarly compute nearest creature
        # (for brevity, return defaults)
        return SensoryInfo(
            nearest_food_pos=nearest_pos,
            nearest_food_dist=nearest_norm_dist,
            nearest_food_angle=nearest_angle,
            nearby_foods=[],
            nearest_creature_dist=1.0,
            nearest_creature_angle=0.0,
            energy=creature.energy,
            time=self.TICKS,  # ?????
        )

    def update(self):
        for creature in self.creatures[:]:
            sensory = self.compute_sensory_for(creature)
            creature.update_from_sensory(sensory, dt=1.0)

            # After movement, check food collisions
            for food in self.foods[:]:
                if creature.collides_with(food):
                    creature.energy = min(1.0, creature.energy + 0.3)
                    # let brain adapt
                    if hasattr(creature.brain, "inform_reward"):
                        creature.brain.inform_reward(1.0)
                    self.foods.remove(food)
                    self.foods.append(
                        Food(
                            x=random.randint(20, self.WIDTH - 20),
                            y=random.randint(20, self.HEIGHT - 20),
                        )
                    )

            if creature.energy <= 0:
                self.creatures.remove(creature)
                self.creatures.append(
                    Creature(
                        x=random.randint(50, self.WIDTH - 50),
                        y=random.randint(50, self.HEIGHT - 50),
                        brain=RuleBasedBrain(),
                    )
                )
