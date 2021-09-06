import pygame

pygame.init()
W_H = (800, 600)
fps = pygame.time.Clock()
screen = pygame.display.set_mode(W_H)
icon = pygame.image.load("image_name.png")
pygame.display.set_icon(icon)

bg = pygame.image.load("bg_name.png")


running = True
while running:
	for event.type in event.get():
		if event.type == pygame.QUIT:
			running = False
	screen.blit(bg, (0, 0))
	fps.tick(15)
	pygame.display.update()
