# -*- coding: utf-8 -*-
import pygame 
pygame.init()

GRAVITY = 0.3

# PLAYER CONTROLS COMBINATIONS
PLAYER_CONTROLS_COMBINATIONS = [
    {
            "UP" : pygame.K_UP,
            "DOWN" : pygame.K_DOWN,
            "LEFT" : pygame.K_LEFT,
            "RIGHT" : pygame.K_RIGHT
    },
    {
            "UP" : pygame.K_w,
            "DOWN" : pygame.K_s,
            "LEFT" : pygame.K_a,
            "RIGHT" : pygame.K_d
    },
    # {
    #         "UP" : pygame.K_ESCAPE,
    #         "DOWN" : pygame.K_ESCAPE,
    #         "LEFT" : pygame.K_ESCAPE,
    #         "RIGHT" : pygame.K_ESCAPE
    # },
    # {
    #         "UP" : pygame.K_ESCAPE,
    #         "DOWN" : pygame.K_ESCAPE,
    #         "LEFT" : pygame.K_ESCAPE,
    #         "RIGHT" : pygame.K_ESCAPE
    # },
]
