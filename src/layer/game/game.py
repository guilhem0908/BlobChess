import pygame
from src.layer.layer import Layer
from src.layer.game.game_graphics import GameGraphics
from src.layer.game.game_event import GameEvent
from src.layer.game.game_state import GameState


class Game(Layer):
    graphics: GameGraphics
    event: GameEvent

    def __init__(self, window_size: tuple[int, int]):
        super().__init__(window_size)
        self.state = GameState()
        self.squares_style = "classic"
        self.blobs_colors = ("g", "r")

    def update(self):
        ...

    def draw(self, window_surface: pygame.surface.Surface):
        self.draw_board(window_surface)

    def draw_board(self, window_surface):
        for row in range(8):
            for column in range(9):
                x = self.graphics.board_rect.x + column * self.graphics.square_size
                y = self.graphics.board_rect.y + row * self.graphics.square_size
                # -- squares --
                square_image = self.graphics.squares_images[self.squares_style][(row + column) % 2]
                window_surface.blit(square_image, (x, y))
                # -- blobs --
                blob_tag = self.state.get_blob_tag(row, column)
                if blob_tag:
                    blob_image = self.graphics.blobs_images[self.blobs_colors[int(blob_tag[0])] + blob_tag[1:]][0]
                    window_surface.blit(blob_image, (x + self.graphics.square_gap, y + self.graphics.square_gap))
