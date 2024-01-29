import pygame
from pygame.locals import *
from src.const import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE
from src.system.config import ConfigWindow


class Window:
    surface: pygame.surface.Surface
    _backup_window_size: tuple[int, int]

    def __init__(self, config: ConfigWindow):
        self.config = config
        self._apply_mode()
        pygame.display.set_caption(WINDOW_TITLE)

    def _to_fullscreen(self):
        self.surface = pygame.display.set_mode(flags=FULLSCREEN)

    def _to_windowed(self):
        self.surface = pygame.display.set_mode(self.config.size, RESIZABLE)

    def _apply_mode(self):
        self._to_fullscreen() if self.config.fullscreen else self._to_windowed()

    def resize(self, width: int, height: int):
        self._backup_window_size = self.config.size
        self.config.size = max(width, WINDOW_WIDTH), max(height, WINDOW_HEIGHT)
        self._to_windowed()

    def maximize(self):
        self.config.size = self._backup_window_size

    def toggle_fullscreen(self):
        self.config.fullscreen = not self.config.fullscreen
        self._apply_mode()
