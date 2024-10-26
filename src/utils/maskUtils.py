import pygame

def isMasksColision( firstMask, firstPos, secondMask, secondPos):
    offset = [secondPos[0]-firstPos[0], secondPos[1]-firstPos[1]]
    return firstMask.overlap( secondMask, offset)

def getMaskFromSurface( surface ):
    return pygame.mask.from_surface( surface )