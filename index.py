import pygame

from noise import pnoise2
import numpy as np

import random

dim = (256, 256)

def create_heightmap(dim, noise):
    width, height = dim

    def to_filtered_tuple(x, y, z):
        val = noise(x / width, y / height)
        val = int(255 * val)
        return val

    hmap = np.fromfunction(np.vectorize(to_filtered_tuple), (width, height, 3))

    return hmap.astype('uint8')

base = np.random.randint(0, 100)

hmap = create_heightmap(dim, lambda x, y: pnoise2(x, y, base=base))

clock = pygame.time.Clock()
surf = pygame.surfarray.make_surface(hmap)
display = pygame.display.set_mode(dim)
display.blit(surf, (0, 0))

pygame.display.update()

while True:
    pygame.display.update()
    clock.tick(60)
