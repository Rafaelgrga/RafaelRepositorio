from dino_runner.utils.constants import MUSHROOM, STAR_TYPE #SHIELD_Type seria inecessario
from dino_runner.components.power_ups.power_up import PowerUp

class Mushroom(PowerUp):
    def __init__(self):
        super().__init__(MUSHROOM, STAR_TYPE)
        self.rect.y = 460
        

            

    