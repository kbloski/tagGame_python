import pygame # type: ignore

def isMasksColision( firstMask, firstPos, secondMask, secondPos):
    offset = [secondPos[0]-firstPos[0], secondPos[1]-firstPos[1]]
    return firstMask.overlap( secondMask, offset)

def getMaskFromSurface( surface ):
    return pygame.mask.from_surface( surface )

def getCenterPosSurface(surface, posX, posY):
    width = surface.get_width()
    height = surface.get_height()
    return [ 
        posX - (width/2),
        posY - (height/2)
    ]
    