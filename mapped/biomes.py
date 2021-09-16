DEEP_OCEAN = [2, 70, 135]
COASTAL_OCEAN = [1, 168, 229]
BEACH = [255, 209, 2]

SCORCHED = [188, 188, 188]
BARE = [116, 116, 116]
SNOW = [255, 254, 254]

TEMPERATE_DESERT = [225, 184, 14]
SHRUBLAND = [131, 151, 0]
TAIGA = [2, 129, 53]

GRASSLAND = [99, 136, 5]
TEMPERATE_DECIDUOUS_FOREST = [1, 109, 0]
TEMPERATE_RAIN_FOREST = [2, 129, 3]

SUBTROPICAL_DESERT = [225, 239, 3]
TROPICAL_SEASONAL_FOREST = [132, 200, 3]
TROPICAL_RAIN_FOREST = [41, 109, 0]

def biome(elevation, moisture):
    """
    Find biome corresponding to given elevation and moisture.
    Based on https://www.redblobgames.com/maps/terrain-from-noise/
    """
    if elevation < 0.05: return DEEP_OCEAN
    if elevation < 0.1: return COASTAL_OCEAN
    if elevation < 0.12: return BEACH
    
    if elevation > 0.8:
        if moisture < 0.4: return SCORCHED
        if moisture < 0.6: return BARE
        return SNOW

    if elevation > 0.6:
        #if moisture < 0.33: return TEMPERATE_DESERT
        #if moisture < 0.66: return SHRUBLAND
        return TAIGA

    if elevation > 0.3:
        #if moisture < 0.16: return TEMPERATE_DESERT
        #if moisture < 0.50: return GRASSLAND
        #if moisture < 0.83: return TEMPERATE_DECIDUOUS_FOREST
        return TEMPERATE_RAIN_FOREST

    #if moisture < 0.16: return SUBTROPICAL_DESERT
    #if moisture < 0.33: return GRASSLAND
    #if moisture < 0.66: return TROPICAL_SEASONAL_FOREST
    return TROPICAL_RAIN_FOREST
