import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField

def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers= (updatable)
	asteroid_field = AsteroidField()

	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	dt = 0
	
	

	while True:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		for thing in updatable:
			thing.update(dt)

		

		screen.fill("black")
		
		for thing in drawable:
			thing.draw(screen)
		
		pygame.display.flip()
		dt = clock.tick(60) /1000

		
		
if __name__=="__main__":
	main()
