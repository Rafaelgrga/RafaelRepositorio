import random
import pygame

from dino_runner.components.power_ups.mushroom import Mushroom

class MushroomManager:
    def __init__(self):
        self.mush_ups = []
        self.when_appears = 0
    
    def generate_power_up(self, score):
        
        if len(self.mush_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(250,350)
            self.mush_ups.append(Mushroom())

    def update(self, game):
        self.generate_power_up(game.score)
    
        for mush_up in self.mush_ups:
            mush_up.update(game.game_speed, self.mush_ups)

            player = game.player
            if player.dino_rect.colliderect(mush_up.rect):
                game.game_speed -= 10
                mush_up.start_time = pygame.time.get_ticks()
                self.mush_ups.remove(mush_up)
    
    def draw(self, screen):
        for shoes_up in self.mush_ups:
            shoes_up.draw(screen)
        
    
    def reset_power_ups(self):
        self.mush_ups.clear()
        self.when_appears = random.randint(200,300)