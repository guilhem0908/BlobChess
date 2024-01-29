import pygame
from src.layer.layer_graphics import LayerGraphics
from src.layer.layer_event import LayerEvent
from src.layer.game.game_graphics import GameGraphics
from src.layer.game.game_event import GameEvent


layers_components = {
    "game": {
        "graphics": GameGraphics,
        "event": GameEvent
    }
}


class Layer:
    graphics: LayerGraphics
    event: LayerEvent

    def __init__(self, window_size: tuple[int, int]):
        self.graphics = layers_components["game"]["graphics"](window_size)
        self.event = layers_components["game"]["event"]()

    def update(self):
        ...

    def draw(self, window_surface: pygame.surface.Surface):
        ...
