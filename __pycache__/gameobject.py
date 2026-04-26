from abc import ABC, abstractmethod

GREEN = (0, 255, 0)

class GameObject(ABC):
    def __init__(self, gridx, gridy, x, y, tile_width, tile_height, color):

        # position on the grid system
        self.gridx = gridx
        self.gridy = gridy

        # pixel pos on the display
        self.x = x
        self.y = y

        # grid tile dimensions
        self.tile_width = tile_width
        self.tile_height = self.tile_height

        #color
        self.color = color

    @abstractmethod
    def draw(self, _surface):
        pass

    @abstractmethod
    def update(self):
        pass