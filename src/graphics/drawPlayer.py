import pygame

def drawCharacter( bodyColor = '#AA0000' ):
    bodyRadius = 25
    sizeSurface = [ bodyRadius*2, bodyRadius*2]

    eyePos = [bodyRadius, bodyRadius-10]    
    eyeRadius = 10
    pupilRadius = 7
    

    playerSurface = pygame.Surface(sizeSurface, pygame.SRCALPHA)
    pygame.draw.rect( playerSurface, bodyColor, (0, bodyRadius, sizeSurface[0], bodyRadius))
    pygame.draw.circle(playerSurface, bodyColor, (bodyRadius,bodyRadius), bodyRadius)

    pygame.draw.circle(playerSurface, '#FFFFFF', eyePos, eyeRadius)
    pygame.draw.circle(playerSurface, '#000000', eyePos, pupilRadius)



    # playerSurface.blit(eye, (80,10))

    return playerSurface
