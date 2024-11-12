import pygame
from constants import *
from player import *


def main():
    # initialize pygame
    pygame.init()

    # Create a screen for the game
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create a clock to control FPS
    clock = pygame.time.Clock()
    dt = 0

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    # Player Instance
    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for character in updatable:
            character.update(dt)

        screen.fill("black")
        
        for character in drawable:
            character.draw(screen)
        
        pygame.display.flip()

        # Limit the frames to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
