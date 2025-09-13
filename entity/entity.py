from abc import ABC
from typing import Optional

import pygame


class Entity(ABC):
    """
    An Entity is merely something that can be drawn

    For now, the most basic representation of an Entity is a circle
    """

    x: int | float
    y: int | float
    radius: int | float
    color: tuple[int, int, int]
    trail: Optional[list[tuple[int | float, int | float]]]

    def draw(self, screen: pygame.Surface):
        trail = getattr(self, "trail", None)
        if trail is not None:
            # Trail
            for i, pos in enumerate(trail):
                alpha = int(255 * (i / len(trail)))
                glow = pygame.Surface(
                    (self.radius * 4, self.radius * 4), pygame.SRCALPHA
                )
                pygame.draw.circle(
                    glow,
                    (self.color[0], self.color[1], self.color[2], alpha),
                    (self.radius * 2, self.radius * 2),
                    self.radius,
                )
                screen.blit(glow, (pos[0] - self.radius * 2, pos[1] - self.radius * 2))

        # Glow + body
        glow = pygame.Surface((self.radius * 6, self.radius * 6), pygame.SRCALPHA)
        pygame.draw.circle(
            glow,
            (self.color[0], self.color[1], self.color[2], 100),
            (self.radius * 3, self.radius * 3),
            self.radius * 2,
        )
        screen.blit(glow, (self.x - self.radius * 3, self.y - self.radius * 3))
        pygame.draw.circle(
            screen, self.color, (round(self.x), round(self.y)), self.radius
        )


# class CreatureEntity(Entity):
#     def draw(self, screen):
#         trail = getattr(self, "trail", None)
#         if trail is not None:
#             # Trail
#             for i, pos in enumerate(trail):
#                 alpha = int(255 * (i / len(trail)))
#                 glow = pygame.Surface(
#                     (self.radius * 4, self.radius * 4), pygame.SRCALPHA
#                 )
#                 pygame.draw.circle(
#                     glow,
#                     (self.color[0], self.color[1], self.color[2], alpha),
#                     (self.radius * 2, self.radius * 2),
#                     self.radius,
#                 )
#                 screen.blit(glow, (pos[0] - self.radius * 2, pos[1] - self.radius * 2))

#         # Glow + body
#         glow = pygame.Surface((self.radius * 6, self.radius * 6), pygame.SRCALPHA)
#         pygame.draw.circle(
#             glow,
#             (self.color[0], self.color[1], self.color[2], 100),
#             (self.radius * 3, self.radius * 3),
#             self.radius * 2,
#         )
#         screen.blit(glow, (self.x - self.radius * 3, self.y - self.radius * 3))
#         pygame.draw.circle(
#             screen, self.color, (round(self.x), round(self.y)), self.radius
#         )


# class FoodRenderer(Entity):
#     def draw(self, screen):
#         glow = pygame.Surface((self.radius * 6, self.radius * 6), pygame.SRCALPHA)

#         pygame.draw.circle(
#             glow,
#             (self.color[0], self.color[1], self.color[2], 120),
#             (self.radius * 3, self.radius * 3),
#             self.radius * 2,
#         )
#         screen.blit(glow, (self.x - self.radius * 3, self.y - self.radius * 3))
#         pygame.draw.circle(
#             screen, self.color, (round(self.x), round(self.y)), self.radius
#         )
