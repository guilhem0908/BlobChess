import sys
import pygame
from src.system.window import Window


class Event:
    def __init__(self, window: Window):
        self.window = window

    def process(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    sys.exit()
                case pygame.VIDEORESIZE:
                    self.window.resize(event.w, event.h)
                case pygame.WINDOWMAXIMIZED:
                    self.window.maximize()
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_F11:
                            self.window.toggle_fullscreen()
                            # Clear video resize event from the queue
                            # because Window.apply_mode() generates a video resize event.
                            pygame.event.clear(pygame.VIDEORESIZE)
                case pygame.MOUSEBUTTONDOWN:
                    ...
