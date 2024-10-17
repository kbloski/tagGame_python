import pygame
import src.helpers.SurfaceHelper as SurfaceHelper
import src.characters.drawPlayer as drawPlayer
import src.inputHandler as inputHandler
from src.measurement_utils import roundNumber

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
        self.pos = [0,0]

        self.moveDirection = [0, 0]
        self.acceleration = 0.01
        self.speed = [0, 0]
        self.maxSpeed = [3, 3]

    def setDirection(self):
        keys = inputHandler.keyboard['keys']
        if keys[self.controlKeys['UP']]:
            self.moveDirection[1] = -1
        elif keys[self.controlKeys['DOWN']]:
            self.moveDirection[1] = 1

        if keys[self.controlKeys['LEFT']]:
            self.moveDirection[0] = -1
        elif keys[self.controlKeys['RIGHT']]:
            self.moveDirection[0] = 1

    def move(self):
        self.setDirection()
        keys = inputHandler.keyboard['keys']

        if (keys[self.controlKeys['UP']] or keys[self.controlKeys['DOWN']]):
            if self.speed[1] < self.maxSpeed[1]:
                self.speed[1] += self.acceleration
        elif (self.speed[1] > 0):
            self.speed[1] -= self.acceleration
        else:
            self.speed[1] = 0

        if (keys[self.controlKeys['LEFT']] or keys[self.controlKeys['RIGHT']]):
            if self.speed[0] < self.maxSpeed[0]:
                self.speed[0] += self.acceleration
        elif (self.speed[0] > 0):
            self.speed[0] -= self.acceleration
        else:
            self.speed[0] = 0

        self.pos[1] += self.speed[1] * self.moveDirection[1]
        self.pos[1] = roundNumber(self.pos[1])

        self.pos[0] += self.speed[0] * self.moveDirection[0]
        self.pos[0] = roundNumber(self.pos[0])


        

    def run(self):
        self.move()
        self.screen.blit(self.characterSurface, self.pos)