from __future__ import annotations

import pygame

from TextAdventureCreator import Map

pygame.init()


ta_map = Map()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
