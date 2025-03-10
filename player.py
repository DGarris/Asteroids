import pygame
import constants 
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, shots_group):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)  # Create a surface for the player
        self.rect = self.image.get_rect(center=self.position)  # Set rect based on position
        self.position = pygame.Vector2(x,y)
        self.shots_group = shots_group
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)


    def rotate(self, dt):
        self.rotation = (constants.PLAYER_TURN_SPEED * dt) + self.rotation 
        
    def update(self, dt):
            keys = pygame.key.get_pressed()

            if keys[pygame.K_a]:
                self.rotate(-dt)
            if keys[pygame.K_d]:
                self.rotate(dt)
            if keys[pygame.K_w]:
                self.move(dt)
            if keys[pygame.K_s]:
                self.move(-dt)
            if keys[pygame.K_SPACE]:
                self.shoot()     

        
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    def shoot(self):
        shot_velocity = pygame.Vector2(0, 1)
        shot_velocity.rotate_ip(self.rotation)
        shot_velocity *= constants.PLAYER_SHOOT_SPEED
        new_shot = Shot(self.position.copy(), shot_velocity)
        self.shots_group.add(new_shot)


          