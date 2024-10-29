#-*- coding: utf-8 -*-
import pygame # type: ignore
pygame.init()

DEFAULT_SIGN_SIZE = 20

def createSignSurface( 
        text='text-sign', 
        signHeight= DEFAULT_SIGN_SIZE, 
        color='#000000', 
        fontFamily = "Arial", 
        antyaliansing=True
    ):
    font = pygame.font.Font(pygame.font.match_font(fontFamily), signHeight)
    textSurface = font.render( str(text), antyaliansing, color)
    return textSurface


def drawSign( 
        surface = None,
        text='text-sign', 
        pos = [0,0],
        signHeight= DEFAULT_SIGN_SIZE, 
        color='#000000', 
        fontFamily = "Arial", 
        antyaliansing=True
    ):
    surface.blit( createSignSurface(text, signHeight, color, fontFamily, antyaliansing), pos)


class CreateSign:
    DEFAULT_SIGN_SIZE = DEFAULT_SIGN_SIZE

    def __init__(self, text='text-sign', pos = [0,0], signHeight= DEFAULT_SIGN_SIZE, color='#000000', fontFamily="Arial", antyaliansing=True):
        self.innerText = text
        self.pos = pos
        self.signHeight = signHeight
        self.color = color
        self.fontFamily = fontFamily
        self.antyaliansing = antyaliansing
        self.surface = self.__createSign()

    def setPost(self, x, y):
        self.pos = [x,y]

    def updateSign(self, text, signHeight, color, fontFamily, antyaliansing):
        if text:
            self.innerText = text
        if signHeight:
            self.signHeight = signHeight
        if color: 
            self.color = color
        if fontFamily:
            self.fontFamily = fontFamily
        if antyaliansing:
            self.antyaliansing = antyaliansing
        self.__createSign()

    def __createSign(self):
        self.surface = createSignSurface( self.innerText, self.signHeight, self.color, self.fontFamily, self.antyaliansing)
        
    def draw(self, surface):
        surface.blit( self.surface, self.pos )


