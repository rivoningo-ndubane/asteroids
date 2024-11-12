import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import Shot


def main():
    # initialize pygame
    pygame.init()

    # Create a screen for the game
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create a clock to control FPS
    clock = pygame.time.Clock()
    dt = 0

    # Groups
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Object Instance
    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    asteroid_obj = AsteroidField()

    print("Starting asteroids!")

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

        for asteroid in asteroids:

            if asteroid.collision(player):
                print("Game Over!")
                sys.exit()

            for shot in shots:
                if shot.collision(asteroid):
                    asteroid.split()
                    shot.kill()
            
        # Limit the frames to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
