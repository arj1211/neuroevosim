from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass
class SensoryInfo:
    # positions are raw (x,y) in world coordinates if you need them;
    # also provide normalized values to make brains simpler.
    nearest_food_pos: Optional[Tuple[float, float]]
    nearest_food_dist: float  # normalized 0..1 (1 = far)
    nearest_food_angle: float  # -pi..pi (angle relative to creature heading)
    nearby_foods: List[Tuple[float, float]]  # optional: raw positions
    nearest_creature_dist: float  # normalized 0..1
    nearest_creature_angle: float  # -pi..pi
    energy: float  # 0..1
    time: float  # simulation time or timestep idx


@dataclass
class Decision:
    # basic locomotion decisions
    turn: float  # -1 .. 1  (negative = turn left, positive = right)
    throttle: float  # -1 .. 1  (negative = move backward, positive = forward)
    # optional higher-level decisions
    eat: bool = False
    reproduce: bool = False
    signal: Optional[float] = None


class Brain(ABC):
    """Abstract brain. Implementations must implement decide()."""

    @abstractmethod
    def decide(self, sensory: SensoryInfo) -> Decision:
        raise NotImplementedError

    def inform_reward(self, reward: float) -> None:
        """Optional: called by environment when agent gets a reward (food, success, etc)."""
        return

    def on_tick(self, dt: float) -> None:
        """Optional: called every tick (for time-decay, internal timers)."""
        return
