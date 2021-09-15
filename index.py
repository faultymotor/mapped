import pygame
from noise import pnoise2
import numpy as np
import sys
import random

dim = (1024, 768)

rgbs = [
    [65, 105, 225], # 0 Water
    [238, 213, 180], # 1 Beach
    [168, 211, 171], # 2 Land
    [159, 146, 134], # 3 Hill
    [224, 224, 224], # 4 Snow
]

def get_rgb(height):
    idx = 0
    if height > 20: idx = 1
    if height > 25: idx = 2
    if height > 70: idx = 3
    if height > 75: idx = 4
    return rgbs[idx]

def create_heightmap(dim, noise):
    width, height = dim

    def to_filtered_tuple(x, y, z):
        val = noise(x / width, y / height)
        val = int(255 * abs(val))
        return get_rgb(val)[int(z)]

    hmap = np.fromfunction(np.vectorize(to_filtered_tuple), (width, height, 3))

    return hmap.astype('uint8')

base = np.random.randint(0, 100)

hmap = create_heightmap(dim, lambda x, y: pnoise2(x, y, octaves=8, base=base))
clock = pygame.time.Clock()
surf = pygame.surfarray.make_surface(hmap)
display = pygame.display.set_mode(dim)
display.blit(surf, (0, 0))

pygame.display.update()

while True:
    pygame.display.update()
    clock.tick(60)
