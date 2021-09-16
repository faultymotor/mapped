import pygame
from noise import pnoise2
import numpy as np
import sys
import random

from mapped import biomes

def create_normalized_map(dim, noise):
    width, height = dim
    nmap = create_noisemap(dim, lambda x, y: noise(x / width, y / height))
    min_val, max_val = np.min(nmap), np.max(nmap)
    normalize = lambda val: (val - min_val) / (max_val - min_val)
    normalize = np.vectorize(normalize)

    return normalize(nmap)

# def create_heightmap(dim, noise, bmap):
#     width, height = dim

#     def mapper(x, y, z):
#         x, y, z = int(x), int(y), int(z)
#         elevation = noise(x / width, y / height)
#         elevation = pow(elevation * 1.3, 4)
#         moisture = bmap[x][y]
#         biome = biomes.biome(elevation, moisture)
#         return biome[z]

#     return create_noisemap((width, height, 3), mapper)

def create_noisemap(dim, mapper):
    filtered_mapper = np.vectorize(mapper)
    nmap = np.fromfunction(filtered_mapper, dim)
    return nmap

def create_colormap(hmap, bmap):
    width, height = hmap.shape
    colormap = np.zeros((width, height, 3))

    for x in range(width):
        for y in range(height):
            colormap[x][y] = biomes.biome(hmap[x][y], bmap[x][y])

    return colormap.astype('uint8')

def update_screen():
    print('=== GENERATING NEW MAP ===')
    print('[1/4] seed generated...')
    base = np.random.randint(0, 100)
    bmap = create_normalized_map(dim, lambda x, y: pnoise2(x, y, octaves=6, base=base))
    print('[2/4] biome map generated...')
    base = np.random.randint(0, 100)
    hmap = create_normalized_map(dim, lambda x, y: pnoise2(x, y, octaves=8, base=base))
    print('[3/4] height map generated...')
    cmap = create_colormap(hmap, bmap)
    surf = pygame.surfarray.make_surface(cmap)
    display.blit(surf, (0, 0))
    print('[4/4] done!')
    return bmap

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