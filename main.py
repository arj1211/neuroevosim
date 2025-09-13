import pygame

from config import FPS, HEIGHT, WIDTH
from environment.environment import Environment


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    env = Environment()

    running = True
    while running:
        env.TICKS = clock.get_time()

        screen.fill((20, 20, 30))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        env.update()

        # Draw
        for entity in env.creatures + env.foods:
            entity.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
