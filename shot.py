from circleshape import CircleShape
import pygame
import constants


class Shot(CircleShape):
    def __init__(self, position, velocity):
        super().__init__(position.x, position.y, constants.SHOT_RADIUS)
        self.velocity = velocity
        
        
        

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), constants.SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += self.velocity * dt  # Sync position
