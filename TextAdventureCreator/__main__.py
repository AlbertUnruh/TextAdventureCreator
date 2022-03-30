from __future__ import annotations

import pygame

from TextAdventureCreator import Map, Button

pygame.init()


ta_map = Map((400, 400))
ta_map.show()

ta_map.create_buttons(Button(None, (0, 0), 20, ("red", "green", "blue", "yellow")))

print(ta_map)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # update buttons
        ta_map.update_buttons(event)

    pygame.display.flip()
