DEEP_OCEAN = [2, 70, 135]
COASTAL_OCEAN = [1, 168, 229]
BEACH = [255, 209, 2]

SCORCHED = [116, 116, 116]
BARE = [188, 188, 188]
SNOW = [255, 254, 254]

TEMPERATE_DESERT = [255, 209, 2]
SHRUBLAND = [132, 200, 3]
TAIGA = [132, 152, 1]

GRASSLAND = [131, 151, 0]
TEMPERATE_DECIDUOUS_FOREST = [96, 133, 1]
TEMPERATE_RAIN_FOREST = [96, 143, 1]

SUBTROPICAL_DESERT = [255, 180, 0]
TROPICAL_SEASONAL_FOREST = [1, 109, 0]
TROPICAL_RAIN_FOREST = [2, 109, 30]

def biome(elevation, moisture):
    """
    Find biome corresponding to given elevation and moisture.
    Based on https://www.redblobgames.com/maps/terrain-from-noise/
    """
    if elevation < 0.2: return DEEP_OCEAN
    if elevation < 0.25: return COASTAL_OCEAN
    if elevation < 0.27: return BEACH

    if elevation > 0.9: 
        if moisture < 0.6: return BARE
        return SNOW

    if elevation > 0.8:
        if moisture < 0.4: return SCORCHED
        return BARE

    if elevation > 0.6:
        if moisture < 0.33: return TEMPERATE_DESERT
        if moisture < 0.66: return SHRUBLAND
        return TAIGA

    if elevation > 0.4:
        if moisture < 0.16: return TEMPERATE_DESERT
        if moisture < 0.50: return GRASSLAND
        if moisture < 0.83: return TEMPERATE_DECIDUOUS_FOREST
        return TEMPERATE_RAIN_FOREST

    if moisture < 0.16: return SUBTROPICAL_DESERT
    if moisture < 0.33: return GRASSLAND
    if moisture < 0.66: return TROPICAL_SEASONAL_FOREST
    return TROPICAL_RAIN_FOREST
