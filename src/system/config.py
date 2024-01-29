from src.const import CONFIG_FILE_PATH
from configparser import ConfigParser


class ConfigWindow:
    fullscreen: bool
    size: tuple[int, int]


class Config:
    """
    Auto-calling load() for attribute setup.
    """
    fps: int

    def __init__(self):
        self.window = ConfigWindow()
        self._config_parser = ConfigParser()
        self.load()

    def load(self):
        self._config_parser.read(CONFIG_FILE_PATH)
        self.window.fullscreen = self._config_parser.getboolean("window", "fullscreen")
        window_width = self._config_parser.getint("window", "width")
        window_height = self._config_parser.getint("window", "height")
        self.window.size = window_width, window_height
        self.fps = self._config_parser.getint("main", "fps")

    def save(self):
        self._config_parser.read(CONFIG_FILE_PATH)
        self._config_parser["window"]["fullscreen"] = str(self.window.fullscreen)
        window_width, window_height = self.window.size
        self._config_parser["window"]["width"] = str(window_width)
        self._config_parser["window"]["height"] = str(window_height)
        self._config_parser["main"]["fps"] = str(self.fps)
        with open(CONFIG_FILE_PATH, 'w') as file:
            self._config_parser.write(file)
