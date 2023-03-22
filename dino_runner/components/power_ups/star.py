from dino_runner.utils.constants import STAR, STAR_TYPE #SHIELD_Type seria inecessario
from dino_runner.components.power_ups.power_up import PowerUp

class Star(PowerUp):
    def __init__(self):
        super().__init__(STAR, STAR_TYPE)
        

