def isAppropiateForWeather(style, temperatureF):
    warmthLevels = {'casual': (50, 95), 'business-casual': (55, 90), 'semi-formal': (60, 85), 'business-formal': (60, 80)}

    if style not in warmthLevels:
        return True # will not judge unknown styles
    
    minTemp, maxTemp = warmthLevels[style]
    return minTemp <= temperatureF <= maxTemp