#-*- coding: utf-8 -*-
import pygame
pygame.init()

DEFAULT_SIGN_SIZE = 20

def drawSign( 
        surface = None,
        text='text-sign', 
        pos = [0,0],
        signHeight= DEFAULT_SIGN_SIZE, 
        color='#000000', 
        fontFamily = "Arial", 
        antyaliansing=True
    ):
    font = pygame.font.Font(pygame.font.match_font(fontFamily), signHeight)
    textSurface = font.render( text, antyaliansing, color)
    surface.blit( textSurface, pos)

def createSignFunc( 
        text='text-sign', 
        signHeight= DEFAULT_SIGN_SIZE, 
        color='#000000', 
        fontFamily = "Arial", 
        antyaliansing=True
    ):
    font = pygame.font.Font(fontFamily, signHeight)
    textSurface = font.render( text, antyaliansing, color)
    return textSurface

class CreateSign:
    DEFAULT_SIGN_SIZE = DEFAULT_SIGN_SIZE

    def __init__(self, text='text-sign', pos = [0,0], signHeight= DEFAULT_SIGN_SIZE, color='#000000', fontFamily="Arial", antyaliansing=True):
        self.innerText = text
        self.pos = pos
        self.signHeight = signHeight
        self.color = color
        self.fontFamily = fontFamily
        self.antyaliansing = antyaliansing

        self.surface = self.__createSign(),

    def setPost(self, x, y):
        self.pos = [x,y]

    def updateSign(self, text = 'update-sign', signHeight= DEFAULT_SIGN_SIZE, color='#000000', fontFamily="Arial", antyaliansing=True):
        font = pygame.font.Font(fontFamily,)
        self.img = font.render(text,antyaliansing,color)

    def __createSign(self):
        font = pygame.font.Font( self.fontFamily, self.signHeight)
        self.surface = font.render( self.innerText, self.antyaliansing, self.color )
        
    def draw(self, surface):
        surface.blit( self.surface, self.pos )


