import pygame
from mapped import biomes, maps
import numpy as np

def draw_map_to_screen(nmap, display):
    surface = pygame.surfarray.make_surface(nmap)
    display.blit(surface, (0, 0))

dim = (700, 700)

mode = 'color'

clock = pygame.time.Clock()
 
pygame.init()
pygame.display.set_caption('mapped')
display = pygame.display.set_mode(dim)

running = True

map_obj = maps.Map(dim)
draw_map_to_screen(map_obj.dmap, display)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                map_obj = maps.Map(dim)
                draw_map_to_screen(map_obj.dmap, display)
            elif event.key == pygame.K_SPACE:
                map_obj.cycle_mode()

    draw_map_to_screen(map_obj.dmap, display)
    pygame.display.update()
    clock.tick(120)

