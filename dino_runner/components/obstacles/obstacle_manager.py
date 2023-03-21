import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, BIRD_RED, BIRD_GREEN, BIRD_BLUE, DEATH_SOUND

class ObstacleManager:

    def __init__(self):
        self.Bird_choice = [BIRD, BIRD_RED, BIRD_GREEN, BIRD_BLUE]
        self.obstacles = []

    ### adicionei o random para escolher entre um dos obstaculo
    ### a cada um objeto sai da screen, ele faz um sorteio entre
    ### 0 a 2 e escolhe um obstaculo para mostrar.
    def update(self,game):
        self.sorteio = random.randint(0, 2)

        if len(self.obstacles) == 0:
            if self.sorteio == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS, 325))
            elif self.sorteio == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS, 300))
            elif self.sorteio == 2:
                self.obstacles.append(Bird(random.choice(self.Bird_choice)))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                DEATH_SOUND.play()
                pygame.mixer.music.stop()
                game.death_count += 1
                pygame.time.delay(500)
                game.playing = False
                break


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
 
    def reset_obstacles(self):
        self.obstacles.clear()