import atexit
import pygame
from system.config import Config
from system.window import Window
from system.event import Event
from layer.layer import Layer
from layer.game.game import Game


class Main:
    def __init__(self):
        pygame.init()
        self.config = Config()
        self.config.load()
        self.window = Window(self.config.window)
        self.event = Event(self.window)
        self.game: Layer = Game()

    def cleanup(self):
        self.config.save()
        pygame.quit()

    def run(self):
        while True:
            self.event.process()


if __name__ == "__main__":
    main = Main()
    atexit.register(main.cleanup)
    main.run()
