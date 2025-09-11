import pygame


class CreatureRenderer:
    def __init__(self, creature):
        self.creature = creature

    def draw(self, screen):
        c = self.creature
        # Trail
        for i, pos in enumerate(c.trail):
            alpha = int(255 * (i / len(c.trail)))
            glow = pygame.Surface((c.radius * 4, c.radius * 4), pygame.SRCALPHA)
            pygame.draw.circle(
                glow,
                (c.color[0], c.color[1], c.color[2], alpha),
                (c.radius * 2, c.radius * 2),
                c.radius,
            )
            screen.blit(glow, (pos[0] - c.radius * 2, pos[1] - c.radius * 2))

        # Glow + body
        glow = pygame.Surface((c.radius * 6, c.radius * 6), pygame.SRCALPHA)
        pygame.draw.circle(
            glow,
            (c.color[0], c.color[1], c.color[2], 100),
            (c.radius * 3, c.radius * 3),
            c.radius * 2,
        )
        screen.blit(glow, (c.x - c.radius * 3, c.y - c.radius * 3))
        pygame.draw.circle(screen, c.color, (int(c.x), int(c.y)), c.radius)


class FoodRenderer:
    def __init__(self, food):
        self.food = food

    def draw(self, screen):
        f = self.food
        glow = pygame.Surface((f.radius * 6, f.radius * 6), pygame.SRCALPHA)
        pygame.draw.circle(
            glow, (0, 255, 0, 120), (f.radius * 3, f.radius * 3), f.radius * 2
        )
        screen.blit(glow, (f.x - f.radius * 3, f.y - f.radius * 3))
        pygame.draw.circle(screen, (0, 255, 0), (f.x, f.y), f.radius)
