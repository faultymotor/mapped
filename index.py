import pygame
import numpy as np
import sys
import random

from mapped import biomes, maps

def update_screen():
    print('=== GENERATING NEW MAP ===')
    bmap = maps.create_normalized_map(dim, octaves=6)
    hmap = maps.create_normalized_map(dim, octaves=8)
    cmap = maps.color_map(hmap, lambda x, y: biomes.biome(hmap[x][y], bmap[x][y]))

    surf = pygame.surfarray.make_surface(cmap)
    display.blit(surf, (0, 0))

dim = (700, 700)
clock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption('mapped')
display = pygame.display.set_mode(dim)

update_screen()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == 768: # pygame.K_TAB doesn't work for some reason?
            bmap = update_screen()

    pygame.display.update()
    clock.tick(60)