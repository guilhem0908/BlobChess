from src.layer.layer import Layer
from src.layer.layer_event import LayerEvent
from src.layer.game.game_event import GameEvent


class Game(Layer):
    def __init__(self):
        self.event: LayerEvent = GameEvent()

    def update(self):
        ...

    def draw(self):
        ...
