import random
from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self, images):
        self.type = 0
        super().__init__(images, self.type)
        self.rect.y = random.randint(250, 320)

### Chamei a função Draw  para desenhar o passaro na janela
### E usei o próprio self.type como um contador variando entre 0 e 1
### para a troca de imagem.
    def draw(self, screen):
        screen.blit(self.images[self.type // 5], (self.rect.x, self.rect.y))
        self.type += 1
        if self.type == 10:
            self.type = 0
