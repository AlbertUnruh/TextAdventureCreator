from __future__ import annotations


__all__ = (
    "Button",
    "Map",
)


from typing import TYPE_CHECKING
import pygame

if TYPE_CHECKING:
    from typing import Tuple, List, Optional


class Screen:
    size: Tuple[int, int]
    _screen: pygame.Surface
    _title: str

    def __init__(
        self,
        size: Tuple[int, int] = (400, 400),
        title: str = "TextAdventureCreator",
    ):
        self.size = size
        self._title = title

    def show(self):
        self._screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self._title)
        pygame.display.flip()

    def __repr__(self):
        return f"<{self.__class__.__qualname__}: {' '.join(f'{k}={v!r}' for k, v in vars(self).items())}>"


class Button:
    _bound: pygame.Surface
    position: Tuple[int, int]
    size: Tuple[int, int]
    colors: Tuple[pygame.Color, ...]
    _color_state: int = 0

    def __init__(
        self,
        bound: Optional[pygame.Surface],
        position: Tuple[int, int],
        size: int | Tuple[int, int],
        colors: Tuple[pygame.Color, ...] | Tuple[str, ...] | Tuple[int, ...],
    ):
        if isinstance(size, int):
            size = (size, size)

        def get_color(c: pygame.Color | str | Tuple[int, ...]) -> pygame.Color:
            if isinstance(c, pygame.Color):
                return c
            return pygame.Color(c)

        self._bound = bound
        self.position = position
        self.size = size
        self.colors = tuple(map(get_color, colors))

    @property
    def _rect(self):
        return pygame.Rect(*self.position, *self.size)

    @property
    def _surface(self):
        surface = pygame.Surface(self.size)
        surface.fill(self.colors[self._color_state])
        return surface

    def show(self):
        self._bound.blit(self._surface, self.position)

    update = show

    def click(self, event) -> bool:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self._rect.collidepoint(*pygame.mouse.get_pos()):
                    self.alter_color()
                    return True
        return False

    def alter_color(self):
        self._color_state = (self._color_state + 1) % len(self.colors)

    def __repr__(self):
        return f"<{self.__class__.__qualname__}: {' '.join(f'{k}={v!r}' for k, v in vars(self).items())}>"


class Map(Screen):
    """
    For the map itself.
    """

    def __init__(
        self,
        size: Tuple[int, int],
        title: str = "TextAdventureCreator --- Map",
        buttons: List[Button, ...] = None,
    ):
        if buttons is None:
            buttons = []

        super().__init__(size=size, title=title)
        self._buttons = buttons

    def update_buttons(self, event):
        for button in self._buttons:
            if button.click(event):
                button.update()

    def create_buttons(self, *buttons: Button):
        bs = []
        for b in buttons:
            if b._bound is None:  # noqa
                b._bound = self._screen
            b.show()
            bs.append(b)
        self._buttons = bs
