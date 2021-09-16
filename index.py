import pygame
from noise import pnoise2
import numpy as np
import sys
import random

dim = (700, 700)

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

def update_screen():
    print("=== GENERATING NEW MAP ===")
    base = np.random.randint(0, 100)
    print("[1/4] seed generated...")
    hmap = create_heightmap(dim, lambda x, y: pnoise2(x, y, octaves=8, base=base))
    print("[2/4] heightmap generated...")
    surf = pygame.surfarray.make_surface(hmap)
    print("[3/4] surface generated...")
    display.blit(surf, (0, 0))
    print("[4/4] blit generated!")

clock = pygame.time.Clock()
display = pygame.display.set_mode(dim)

update_screen()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == 768: # pygame.K_TAB doesn't work for some reason?
            update_screen()

    pygame.display.update()
    clock.tick(60)