import pygame # type: ignore
import src.utils.handlerUtils as inputHandler
from src.utils.measurementUtils import roundNumber
from src.config import settings
import src.utils.surfaceUtils as surfaceUtils



class Player:
    PLAYERID = 1
    ACCELERATION = 0.05
    JUMP_POWER = 12
    MAX_SPEED = [4, 0]
    BOOSTED_ACCELERATION = 0.06
    BOOSTED_JUMP_POWER = 13
    BOOSTED_MAX_SPEED = [4.2, 0]

    def __init__(self, characterSurface):
        self.id = self.__getNewPlayerId()

        self.controlKeys = {
            "UP" : pygame.K_ESCAPE,
            "DOWN" : pygame.K_ESCAPE,
            "LEFT" : pygame.K_ESCAPE,
            "RIGHT" : pygame.K_ESCAPE
        }

        self.__characterSurfaceWithMask = [ characterSurface, surfaceUtils.getMaskFromSurface(characterSurface) ]
        self.characterSurface = self.__characterSurfaceWithMask[0]

        self.pos = [500,500]
        self.moveDirection = [0, 0]
        self.acceleration = self.ACCELERATION
        self.jumpPower = self.JUMP_POWER
        self.speed = [0, 0]
        self.maxSpeed = self.MAX_SPEED
    
    def __getNewPlayerId(self):
        newId = self.PLAYERID
        Player.PLAYERID += 1
        return newId

    def __setDirection(self):
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

    def __move(self, mapMask, mapPos):
        self.__setDirection()
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
        if (self.colisionWithOtherMask(mapMask, newMapPos) and self.moveDirection[1] == -1):
            self.moveDirection[1] = 1


        # GRAVITY
        newMapPos = [mapPos[0], mapPos[1] - self.speed[1]]
        if (not self.colisionWithOtherMask(mapMask, newMapPos)):
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
        if (self.colisionWithOtherMask(mapMask, nextMapPosX)):
            result[0] = True
        nextMapPosY = [mapPos[0] , mapPos[1] - self.speed[1] * self.moveDirection[1] ]
        if (self.colisionWithOtherMask(mapMask, nextMapPosY)):
            result[1] = True
        return result

    def colisionWithOtherMask( self, mask, pos):
        return surfaceUtils.isMasksColision(self.__characterSurfaceWithMask[1], self.pos, mask, pos)
    
    def setControlKeys(
            self, 
            controls = {
                "UP" : None,
                "DOWN" : None,
                "LEFT" : None,
                "RIGHT" : None,
            },
        ):
        if controls["UP"]:
            self.controlKeys['UP'] = controls["UP"]
        if controls["DOWN"]:
            self.controlKeys['DOWN'] = controls["DOWN"]
        if controls["LEFT"]:
            self.controlKeys['LEFT'] = controls["LEFT"]
        if controls["RIGHT"]:
            self.controlKeys['RIGHT'] = controls["RIGHT"]

    def addBoost(self):
        self.maxSpeed = self.BOOSTED_MAX_SPEED
        self.jumpPower = self.BOOSTED_JUMP_POWER
        self.acceleration = self.BOOSTED_ACCELERATION

    def removeBost(self):
        self.maxSpeed = self.MAX_SPEED
        self.jumpPower = self.JUMP_POWER
        self.acceleration = self.ACCELERATION

    def getCurrentMask(self):
        return self.__characterSurfaceWithMask[1]

    def getCurrentPos(self):
        return  self.pos.copy()
    
    def getId(self):
        return self.id

    def run(self, mapMask, mapPos):
        self.__move( mapMask, mapPos )