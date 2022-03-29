from __future__ import annotations


__all__ = (
    "SettingsMain",
    "ExternalMap",
    "Map",
)


from attr import define, field
from typing import TYPE_CHECKING
import pygame

if TYPE_CHECKING:
    from typing import Tuple


@define()
class SettingsMain:
    """
    For the main menu.
    E.g. for the file to store the map.
    """

    size: Tuple[int, int] = field(default=(400, 400))
    _screen: pygame.Surface = field(default=None, init=False)

    def show(self):
        self._screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("TextAdventureCreator --- Settings")
        pygame.display.flip()


@define()
class ExternalMap:
    """
    For the map creation.
    E.g. if a field can be entered (a room for example).
    """

    size: Tuple[int, int] = field(default=(400, 400))
    _screen: pygame.Surface = field(default=None, init=False)

    def show(self):
        self._screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("TextAdventureCreator --- External Map")
        pygame.display.flip()


@define()
class Map:
    """
    For the map itself.
    """

    size: Tuple[int, int] = field(default=(400, 400))
    _screen: pygame.Surface = field(default=None, init=False)

    def show(self):
        self._screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("TextAdventureCreator --- Map")
        pygame.display.flip()
