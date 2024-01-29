import pygame
from src.layer.layer_graphics import LayerGraphics
from src.const import BOARD_WIDTH_RATIO, BOARD_HEIGHT_RATIO


class GameGraphics(LayerGraphics):
    """
    Auto-calling load() and resize() for attribute setup and adjustments.
    """
    board_rect = pygame.rect.Rect(0, 0, 0, 0)
    square_size: int
    square_gap: int
    blob_size: int
    blobs_images: dict[str, list[pygame.surface.Surface]] = {}
    squares_images: dict[str, list[pygame.surface.Surface]] = {}

    def __init__(self, window_size: tuple[int, int]):
        self.load()
        self.resize(*window_size)

    def load(self):
        self.load_blobs()
        self.load_squares()

    def resize(self, window_width: int, window_height: int):
        if window_width * BOARD_WIDTH_RATIO < window_height * BOARD_HEIGHT_RATIO:
            base_square_size = window_width * BOARD_WIDTH_RATIO / 9
        else:
            base_square_size = window_height * BOARD_HEIGHT_RATIO / 8
        square_size_ratio = base_square_size // 20
        # Resize gfx attrs proportionally for optimal rendering in the window.
        self.square_size = square_size_ratio * 20
        self.square_gap = square_size_ratio * 2
        self.blob_size = square_size_ratio * 16
        self.board_rect.w = self.square_size * 9
        self.board_rect.h = self.square_size * 8
        self.board_rect.center = window_width * 0.5, window_height * 0.5
        self.resize_blobs()
        self.resize_squares()

    def load_blobs(self):
        blobs_types = ("b", "f", "g", "h", "k", "l1", "l2", "m", "n1", "n2", "n3", "o", "q", "s", "t", "u", "w")
        blobs_colors = ("g", "r")
        for blob_color in blobs_colors:
            for blob_type in blobs_types:
                blob_sheet = pygame.image.load(f"./assets/blobs/{blob_color}/{blob_type}.png").convert_alpha()
                blob_tag = blob_color + blob_type
                self.blobs_images[blob_tag] = []
                for i in range(2):
                    blob_image = pygame.Surface((16, 16), flags=pygame.SRCALPHA).convert_alpha()
                    blob_image.blit(blob_sheet, (0, 0), (16 * i, 0, 16, 16))
                    self.blobs_images[blob_tag].append(blob_image)

    def load_squares(self):
        squares_styles = ("classic",)
        for square_style in squares_styles:
            self.squares_images[square_style] = []
            for i in range(2):
                square_image = pygame.image.load(f"./assets/squares/{square_style}/{i}.png").convert()
                self.squares_images[square_style].append(square_image)

    def resize_blobs(self):
        for blob_tag in self.blobs_images:
            for i in range(2):
                self.blobs_images[blob_tag][i] = pygame.transform.scale(self.blobs_images[blob_tag][i],
                                                                        (self.blob_size,) * 2)

    def resize_squares(self):
        for square_style in self.squares_images:
            for i in range(2):
                self.squares_images[square_style][i] = pygame.transform.scale(self.squares_images[square_style][i],
                                                                              (self.square_size,) * 2)
