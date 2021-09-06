import pygame

pygame.init()
W_H = (800, 600)
fps = pygame.time.Clock()
screen = pygame.display.set_mode(W_H)
icon = pygame.image.load("image_name.png")
pygame.display.set_icon(icon)

bg = pygame.image.load("bg_name.png")

player = pygame.image.load("player.png")
player_rect = player.get_rect(topleft=(0,0))

running = True
while running:
	for events in pygame.event.get():
		if events.type == pygame.QUIT:
			running = False
	screen.blit(bg, (0, 0))
	screen.blit(player, player_rect)
	fps.tick(15)
	pygame.display.update()
