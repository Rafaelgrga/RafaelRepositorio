from dino_runner.components.obstacles.obstacle import Obstacle

class Monster(Obstacle):
    def __init__(self, images, position):
        self.type = 0
        super().__init__(images, self.type)
        self.rect.y = position

    def draw(self, screen):
        screen.blit(self.images[self.type // 5], (self.rect.x, self.rect.y))
        self.type += 1
        if self.type == 10:
            self.type = 0
