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
        # if event.type == 768: # pygame.K_TAB doesn't work for some reason?
        #     nmap = create_new_map()
        #     draw_map_to_screen(nmap, display)
        if event.type == 768:
            map_obj.cycle_mode()

    draw_map_to_screen(map_obj.dmap, display)
    pygame.display.update()
    clock.tick(120)

