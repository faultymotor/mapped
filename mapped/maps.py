from noise import pnoise2 as pnoise
import numpy as np
from mapped import biomes

class Map():
    def __init__(self, dim=(700, 700), repeatx=1024, repeaty=1024):        
        width, height = dim
        self.mode = 'color'
        self.dim = dim
        self.dim3 = (width, height, 3)

        self.create_mapper = lambda base, octaves: np.vectorize(lambda x, y: pnoise(x / width, y / height, base=base, octaves=octaves, repeatx=repeatx, repeaty=repeaty))

        self.dmap = np.zeros(self.dim3)
        self.bmap, self.hmap = Map.create_normalized_map(self.dim, self.create_mapper, 8), Map.create_normalized_map(self.dim, self.create_mapper, 8)
        self.construct_display_map()

    def sample(self, x, y):
        return {
            'x': x,
            'y': y,
            'elevation': str(round(self.hmap[x][y] * 15 - 5, 2)) + 'km',
            'moisture': str(int(self.bmap[x][y] * 100)) + '%',
        }

    def cycle_mode(self):
        if self.mode == 'color': self.mode = 'height'
        elif self.mode == 'height': self.mode = 'moisture'
        else: self.mode = 'color'

        self.construct_display_map()

    def construct_display_map(self):
        colorer = None
        if self.mode == 'color': colorer = lambda x, y: biomes.biome(self.hmap[x][y], self.bmap[x][y])
        if self.mode == 'height': colorer = Map.create_map_terracer(self.hmap, 16)
        if self.mode == 'moisture': colorer = Map.create_map_terracer(self.bmap, 12, color=[65, 105, 225])

        print("Creating new display map with mode", self.mode)

        self.dmap = Map.color_map(self.dim3, colorer)

    @staticmethod
    def create_normalized_map(dim, create_mapper, octaves=6):
        print("Creating new map with octaves =", octaves)
        width, height = dim

        base = np.random.randint(0, 100)
        mapper = create_mapper(base, octaves)
        nmap = np.fromfunction(mapper, dim)

        min_val, max_val = np.min(nmap), np.max(nmap)
        normalize = lambda val: (val - min_val) / (max_val - min_val)
        normalize = np.vectorize(normalize)

        return normalize(nmap)   

    @staticmethod
    def create_map_terracer(nmap, step, color=[255, 255, 255]):
        return lambda x, y: [hue * (int(nmap[x][y] * 12) / 12) for hue in color]

    @staticmethod
    def color_map(dim, colorer):
        width, height, depth = dim
        cmap = np.zeros(dim)

        for x in range(width):
            for y in range(height):
                cmap[x][y] = colorer(x, y)
    
        return cmap.astype('uint8')
