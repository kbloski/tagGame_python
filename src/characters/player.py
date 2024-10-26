import pygame
import src.helpers.SurfaceHelper as SurfaceHelper
import src.utils.inputHandler as inputHandler
from src.utils.measurement_utils import roundNumber
import src.settings as settings
import src.utils.maskUtils as maskUtils

class Player:
    def __init__(self, characterSurface):
        self.controlKeys = {
            "UP" : pygame.K_UP,
            "DOWN" : pygame.K_DOWN,
            "LEFT" : pygame.K_LEFT,
            "RIGHT" : pygame.K_RIGHT
        }

        self.__characterSurfaceWithMask = [ characterSurface, maskUtils.getMaskFromSurface(characterSurface) ]
        self.characterSurface = self.__characterSurfaceWithMask[0]

        self.pos = [500,500]
        self.moveDirection = [0, 0]
        self.acceleration = 0.05
        self.jumpPower = 12
        self.speed = [0, 0]
        self.maxSpeed = [4, 5]

    def setDirection(self):
        keys = inputHandler.keyboard['keys']

        # Change direction
        if keys[self.controlKeys['UP']] and not self.moveDirection[1]:
            self.moveDirection[1] = -1
        elif keys[self.controlKeys['DOWN']] and not self.moveDirection[1]:
            self.moveDirection[1] = 1

        if keys[self.controlKeys['LEFT']]:
            self.moveDirection[0] = -1
        elif keys[self.controlKeys['RIGHT']]:
            self.moveDirection[0] = 1

        # Clear direction
        if self.speed[0] <= 0 and self.moveDirection[0]:
            self.moveDirection[0] = 0
        if self.speed[1] <= 0 and self.moveDirection[1]:
            self.moveDirection[1] = 0

    def move(self, mapMask, mapPos):
        self.setDirection()
        keys = inputHandler.keyboard['keys']

        # RESET SPEED
        if self.speed[0] < 0:
            self.speed[0] = 0
        if self.speed[1] < 0:
            self.speed[1] = 0

        # ACCELERATION HORIZONTAL
        if (keys[self.controlKeys['LEFT']] or keys[self.controlKeys['RIGHT']]):
            if self.speed[0] < self.maxSpeed[0]:
                self.speed[0] += self.acceleration
        elif (self.speed[0] > 0):
            self.speed[0] -= self.acceleration
        else:
            self.moveDirection[0] = 0
            self.speed[0] = 0

        # COLISION UP
        newMapPos = [mapPos[0], mapPos[1] + self.speed[1]]
        if (self.colisionWithMask(mapMask, newMapPos) and self.moveDirection[1] == -1):
            self.moveDirection[1] = 1


        # GRAVITY
        newMapPos = [mapPos[0], mapPos[1] - self.speed[1]]
        if (not self.colisionWithMask(mapMask, newMapPos)):
            if not self.moveDirection[1]:
                self.moveDirection[1] = 1
            if self.moveDirection[1] == 1:
                self.speed[1] += settings.GRAVITY
            elif self.moveDirection[1] == -1 and self.speed[1] > 0:
                self.speed[1] -= settings.GRAVITY
        else:
                self.speed[1] = 0

        # ACCELERATION VERTICALL
        if (keys[self.controlKeys['UP']]) and self.speed[1] == 0:
            self.speed[1] = self.jumpPower
            self.moveDirection[1] = -1

        # CHANGE POS
        colisionWithMap = self.__colisionWithMap(mapMask, mapPos)
        if not colisionWithMap[0]:
            self.pos[0] += self.speed[0] * self.moveDirection[0]
            self.pos[0] = roundNumber(self.pos[0])
        if not colisionWithMap[1]:
            self.pos[1] += self.speed[1] * self.moveDirection[1]
            self.pos[1] = roundNumber(self.pos[1])

    def __colisionWithMap(self, mapMask, mapPos):
        result = [False, False]
        nextMapPosX = [ mapPos[0] - self.speed[0] * self.moveDirection[0], mapPos[1] ]
        if (self.colisionWithMask(mapMask, nextMapPosX)):
            result[0] = True
        nextMapPosY = [mapPos[0] , mapPos[1] - self.speed[1] * self.moveDirection[1] ]
        if (self.colisionWithMask(mapMask, nextMapPosY)):
            result[1] = True
        return result

    def colisionWithMask( self, mask, pos):
        return maskUtils.isMasksColision(self.__characterSurfaceWithMask[1], self.pos, mask, pos)

    def run(self, mapMask, mapPos):
        self.move( mapMask, mapPos )