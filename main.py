import pygame
from player import Player
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # initialize the game
    pygame.init()

    # fps/clock
    clock = pygame.time.Clock()
    dt = 0

    # screen and game play loop
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_over = False

    # player instance
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        player.draw(screen)
        pygame.display.flip()

        clock.tick(60)
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
