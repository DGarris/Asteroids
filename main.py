
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot


updateables_group = pygame.sprite.Group()
drawables_group = pygame.sprite.Group()
asteroids_group = pygame.sprite.Group()
asteroid_field_group = pygame.sprite.Group()
Player.containers = (updateables_group, drawables_group)
Asteroid.containers = (asteroids_group, updateables_group, drawables_group)


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    shots_group = pygame.sprite.Group()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, shots_group)
    AsteroidField.containers = (updateables_group,)
    asteroid_field = AsteroidField()
    Shot.containers = (updateables_group,)
    updateables_group.add(player)
    
    clock = pygame.time.Clock()
    dt = 0
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0 , 0, 0))
        for drawable in drawables_group:
            drawable.draw(screen)
        updateables_group.update(dt)
        
        for asteriod in asteroids_group:
            if player.collision(asteriod) == True:
                print("Game over!")
                sys.exit()

        for shot in shots_group:
            shot.draw(screen)
        shots_group.update(dt)


        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()