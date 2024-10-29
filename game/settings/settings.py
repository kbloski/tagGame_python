# -*- coding: utf-8 -*-
import pygame  # type: ignore
pygame.init()

GRAVITY = 0.3

# PLAYER CONTROLS COMBINATIONS
PLAYER_CONTROLS = [
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
]
