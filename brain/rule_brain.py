import math
import random

from brain.brain import Brain, Decision, SensoryInfo


def clamp(x, lo=-1.0, hi=1.0):
    return max(lo, min(hi, x))


class RuleBasedBrain(Brain):
    def __init__(self, boldness=0.5, curiosity=0.5, greed=0.5):
        """
        personality traits 0..1:
        - boldness: how aggressively the agent turns to targets
        - curiosity: how often it will explore even if not hungry
        - greed: how strongly hunger influences behavior
        """
        self.boldness = boldness
        self.curiosity = curiosity
        self.greed = greed

        # adaptive internals
        self.hunger_threshold = 0.5  # energy < threshold => strongly seek food
        self.recent_reward = 0.0

    def decide(self, sensory: SensoryInfo) -> Decision:
        # If no food visible, explore with prob=curiosity
        if sensory.nearest_food_pos is None:
            if random.random() < self.curiosity:
                # small biased exploration
                return Decision(turn=random.uniform(-0.4, 0.4), throttle=0.7)
            else:
                # relaxed wandering
                return Decision(turn=random.uniform(-0.2, 0.2), throttle=0.4)

        # if hungry, go straight for food
        if sensory.energy < self.hunger_threshold:
            # angle is -pi..pi; convert to -1..1
            raw_turn = sensory.nearest_food_angle / math.pi
            turn = clamp(raw_turn * (0.5 + self.boldness * 0.5))
            return Decision(turn=turn, throttle=1.0)

        # otherwise maybe approach but slower
        raw_turn = sensory.nearest_food_angle / math.pi
        if abs(raw_turn) < 0.2 and sensory.nearest_food_dist < 0.3:
            # close and nearly aligned -> nudge forward
            return Decision(turn=clamp(raw_turn * 0.2), throttle=0.9)
        # mild bias towards food or wander
        if random.random() < 0.6:
            return Decision(turn=clamp(raw_turn * 0.4), throttle=0.6)
        return Decision(turn=random.uniform(-0.3, 0.3), throttle=0.5)

    def inform_reward(self, reward: float) -> None:
        # very simple adaptation: if reward was large (ate food), slightly lower hunger threshold
        # so agent becomes less panic-hungry; if negative reward, become more cautious/hungry
        lr = 0.02
        self.hunger_threshold = max(
            0.05, min(0.95, self.hunger_threshold - lr * reward)
        )
        self.recent_reward = 0.9 * self.recent_reward + 0.1 * reward

    def on_tick(self, dt: float) -> None:
        # hunger slowly drifts upward if no rewards (makes agents eventually seek food)
        self.hunger_threshold = min(0.95, self.hunger_threshold + 0.0005 * dt)
