from noise import pnoise2 as pnoise
import numpy as np

def create_normalized_map(dim, octaves=6, base=None):
    width, height = dim

    if not base: base = np.random.randint(0, 100)
    mapper = lambda x, y: pnoise(x / width, y / height, octaves=octaves, base=base)
    mapper = np.vectorize(mapper)
    nmap = np.fromfunction(mapper, dim)

    min_val, max_val = np.min(nmap), np.max(nmap)
    normalize = lambda val: (val - min_val) / (max_val - min_val)
    normalize = np.vectorize(normalize)

    return normalize(nmap)    

def color_map(nmap, colorer):
    width, height = nmap.shape
    cmap = np.zeros((width, height, 3))

    for x in range(width):
        for y in range(height):
            cmap[x][y] = colorer(x, y)
    
    return cmap.astype('uint8')