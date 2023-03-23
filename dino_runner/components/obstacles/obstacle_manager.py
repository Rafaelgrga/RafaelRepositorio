import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.monster import Monster
from dino_runner.utils.constants import LARGE_CANO, DEATH_SOUND, TORTUGA, TURTLE, BIRD, HIT

class ObstacleManager:

    def __init__(self):
        self.Bird_choice = [BIRD, TORTUGA]
        self.obstacles = []
        self.vida = 100
        
    def update(self,game):
        self.sorteio = random.randint(0, 2)
        if len(self.obstacles) == 0:
            if self.sorteio == 0:
                obstacle = (Cactus(LARGE_CANO, 390))
            elif self.sorteio == 1:
                obstacle = (Monster(random.choice(self.Bird_choice), random.randint(350, 400)))
            elif self.sorteio == 2:
                obstacle = (Monster(TURTLE, 430))

            self.obstacles.append(obstacle)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
    
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    self.vida -= 40
                    HIT.play()
                    self.obstacles.pop()
                    if self.vida < 0:
                        DEATH_SOUND.play()
                        pygame.mixer.music.stop()
                        game.death_count += 1
                        pygame.time.delay(500)
                        game.playing = False
                        break
                else:
                    HIT.play()
                    self.obstacles.remove(obstacle)
                    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
 
    def reset_obstacles(self):
        self.obstacles.clear()