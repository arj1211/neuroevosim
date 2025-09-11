import pygame

from config import FPS, HEIGHT, WIDTH
from environment import Environment
from renderers import CreatureRenderer, FoodRenderer


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    env = Environment()

    running = True
    while running:
        screen.fill((20, 20, 30))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        env.update()

        # Draw
        for c in env.creatures:
            CreatureRenderer(c).draw(screen)
        for f in env.foods:
            FoodRenderer(f).draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
