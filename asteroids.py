from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"purple",self.position,self.radius,2)
    
    def update(self,dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        elif ASTEROID_MIN_RADIUS < self.radius < ASTEROID_MAX_RADIUS:
            angle = random.uniform(20,50)
            v1 = self.velocity.rotate(angle)
            v2 = self.velocity.rotate(-angle)
            old_radius = self.radius
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, radius =new_radius)
            new_asteroid1.velocity = v1 *1.2
            new_asteroid2 = Asteroid(self.position.x, self.position.y, radius = new_radius)
            new_asteroid2.velocity = v2 *1.2
        elif self.radius == ASTEROID_MAX_RADIUS:
            angle = random.uniform(20,50)
            v1 = self.velocity.rotate(angle)
            v2 = self.velocity.rotate(-angle)
            old_radius = self.radius
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, radius =new_radius)
            new_asteroid1.velocity = v1 * 1.2
            new_asteroid2 = Asteroid(self.position.x, self.position.y, radius = new_radius)
            new_asteroid2.velocity = v2 *1.2

