import pygame
import src.helpers.SurfaceHelper as SurfaceHelper
import src.characters.drawPlayer as drawPlayer
import src.inputHandler as inputHandler
from src.measurement_utils import roundNumber
import src.settings as settings

class Player:
    def __init__(self, screen):
        self.controlKeys = {
            "UP" : pygame.K_UP,
            "DOWN" : pygame.K_DOWN,
            "LEFT" : pygame.K_LEFT,
            "RIGHT" : pygame.K_RIGHT
        }
        self.screen = screen
        self.characterSurface = drawPlayer.drawCharacter()
        self.pos = [500,500]

        self.moveDirection = [0, 0]
        self.acceleration = 0.05
        self.jumpPower = 10
        self.speed = [0, 0]
        self.maxSpeed = [4, 5]

    def setDirection(self):
        keys = inputHandler.keyboard['keys']
        if keys[self.controlKeys['UP']] and not self.moveDirection[1]:
            self.moveDirection[1] = -1
        elif keys[self.controlKeys['DOWN']] and not self.moveDirection[1]:
            self.moveDirection[1] = 1

        if keys[self.controlKeys['LEFT']]:
            self.moveDirection[0] = -1
        elif keys[self.controlKeys['RIGHT']]:
            self.moveDirection[0] = 1

    def move(self):
        self.setDirection()
        keys = inputHandler.keyboard['keys']

        # ACCELERATION HORIZONTAL
        if (keys[self.controlKeys['LEFT']] or keys[self.controlKeys['RIGHT']]):
            if self.speed[0] < self.maxSpeed[0]:
                self.speed[0] += self.acceleration
        elif (self.speed[0] > 0):
            self.speed[0] -= self.acceleration
        else:
            self.moveDirection[0] = 0
            self.speed[0] = 0

        # ACCELERATION VERTICALL

        if (keys[self.controlKeys['UP']]) and self.speed[1] == 0:
            self.speed[1] = self.jumpPower

        print(self.speed, self.moveDirection)

        # Gravity
        if (self.pos[1] < self.screen.get_height() - 100):
            if not self.moveDirection[1]:
                self.moveDirection[1] = 1
            if self.moveDirection[1] == -1 and self.speed[1] > 0:
                self.speed[1] -= settings.GRAVITY
            elif self.moveDirection[1] == 1:
                self.speed[1] += settings.GRAVITY

        elif (self.moveDirection[1] and self.moveDirection[1] != -1 and self.speed[1]):
            self.speed[1] = 0


        if (self.speed[1] <= 0 and self.moveDirection[1] == -1):
            self.moveDirection[1] = 1
            self.speed[1] = settings.GRAVITY
        



        # Clear moveDirection
        if self.speed[0] <= 0 and self.moveDirection[0]:
            self.moveDirection[0] = 0

        if self.speed[1] <= 0 and self.moveDirection[1]:
            self.moveDirection[1] = 0

        # Change postion
        self.pos[1] += self.speed[1] * self.moveDirection[1]
        self.pos[1] = roundNumber(self.pos[1])

        self.pos[0] += self.speed[0] * self.moveDirection[0]
        self.pos[0] = roundNumber(self.pos[0])


    def run(self):
        self.move()
        self.screen.blit(self.characterSurface, self.pos)