def getCenterPosSurface(surface, posX, posY):
    width = surface.get_width()
    height = surface.get_height()
    return [ 
        posX - (width/2),
        posY - (height/2)
    ]
    