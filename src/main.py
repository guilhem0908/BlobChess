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
        self.window = Window(self.config.window)
        self.event = Event(self.window)
        self.game: Layer = Game(self.window.surface.get_size())

    def cleanup(self):
        self.config.save()
        pygame.quit()

    def run(self):
        while True:
            self.event.process()
            self.draw()

    def draw(self):
        self.window.surface.fill((33, 33, 33))
        self.game.draw(self.window.surface)
        pygame.display.flip()


if __name__ == "__main__":
    main = Main()
    atexit.register(main.cleanup)
    main.run()
