import pygame
import pygame.freetype

from mapped import biomes, maps
import numpy as np

def draw_map_to_screen(nmap, display):
    surface = pygame.surfarray.make_surface(nmap)
    display.blit(surface, (0, 0))

def draw_text_to_screen(text_obj, display):
    string = ''
    for key in text_obj:
        string += key + ': ' + str(text_obj[key]) + ', '

    FONT.render_to(display, (0, 0), string, (0, 0, 0))

dim = (700, 700)

mode = 'color'

clock = pygame.time.Clock()
 
pygame.init()
pygame.font.init() 

pygame.display.set_caption('mapped')
display = pygame.display.set_mode(dim)

FONT = pygame.freetype.SysFont("Sans Serif", 24)
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

    mouse_x, mouse_y = pygame.mouse.get_pos()

    draw_map_to_screen(map_obj.dmap, display)
    draw_text_to_screen(map_obj.sample(mouse_x, mouse_y), display)

    pygame.display.update()
    clock.tick(120)

