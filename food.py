import random

import pygame

from config import HEIGHT, WIDTH


class Food:
    def __init__(self):
        self.x = random.randint(20, WIDTH - 20)
        self.y = random.randint(20, HEIGHT - 20)
        self.color = (0, 255, 0)
        self.radius = 5

    def draw(self, screen):
        glow_surface = pygame.Surface(
            (self.radius * 6, self.radius * 6), pygame.SRCALPHA
        )
        pygame.draw.circle(
            glow_surface,
            (self.color[0], self.color[1], self.color[2], 120),
            (self.radius * 3, self.radius * 3),
            self.radius * 2,
        )
        screen.blit(glow_surface, (self.x - self.radius * 3, self.y - self.radius * 3))
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
