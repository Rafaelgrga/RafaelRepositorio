from dino_runner.utils.constants import STAR, STAR_TYPE, MUSHROOM, MUSHROOM_GREEN
from dino_runner.components.power_ups.power_up import PowerUp

Y_POS = 460

class Star(PowerUp):
    def __init__(self):
        super().__init__(STAR, STAR_TYPE)

class Mushroom(PowerUp):
    def __init__(self):
        super().__init__(MUSHROOM, STAR_TYPE)
        self.rect.y = Y_POS

class MushroomGreen(PowerUp):
    def __init__(self):
        super().__init__(MUSHROOM_GREEN, STAR_TYPE)
        self.rect.y = Y_POS

        

