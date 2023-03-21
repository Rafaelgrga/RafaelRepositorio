from dino_runner.utils.constants import CLOUD, SCREEN_WIDTH

class Cloud:
    def __init__(self):
        self.image = CLOUD
        self.cloud = self.image.get_width()
        self.cloud_x = SCREEN_WIDTH
        self.cloud_y = 70

    def update(self, game_speed):
        self.cloud_x -=  game_speed
        if self.cloud_x < -self.cloud:
           self.cloud_x = SCREEN_WIDTH

    def draw(self, screen):
       screen.blit(self.image,(self.cloud_x, self.cloud_y))

         