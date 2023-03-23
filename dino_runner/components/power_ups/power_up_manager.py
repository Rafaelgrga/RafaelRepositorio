import random
import pygame

from dino_runner.components.power_ups.star import Star, Mushroom, MushroomGreen

class PowerUpManager:
    def __init__(self):
        self.stars = []
        self.mushrooms = []
        self.green_mushrooms = []
        self.when_appears = 130
        self.when_mush_appears = 200
        self.when_mushgreen_appears = 50
    
    def star_power_up(self, score):
        if len(self.stars) == 0 and self.when_appears == score:
            self.when_appears += random.randint(200, 300)
            self.stars.append(Star())

    def mushroom_power_up(self, score):
        if len(self.mushrooms) == 0 and self.when_mush_appears == score:
            self.when_mush_appears += random.randint(400, 500)
            self.mushrooms.append(Mushroom())

    def mushroom_life_up(self, score):
        if len(self.green_mushrooms) == 0 and self.when_mushgreen_appears == score:
            self.when_mushgreen_appears += random.randint(250, 300)
            self.green_mushrooms.append(MushroomGreen()) 

    def update(self, game):
        player = game.player
        self.star_power_up(game.score)

        for star in self.stars:

            if player.dino_rect.colliderect(star.rect):
                star.start_time = pygame.time.get_ticks()
                player.shield = True
                player.has_power_up = True
                player.type = star.type
                player.power_up_time_up = star.start_time + (star.duration * 1000)
                self.stars.remove(star)
            else:
                star.update(game.game_speed, self.stars)
            
        self.mushroom_power_up(game.score)

        for mushroom in self.mushrooms:
            if player.dino_rect.colliderect(mushroom.rect):
                game.game_speed -= 10
                self.mushrooms.remove(mushroom)
            else:
                mushroom.update(game.game_speed, self.mushrooms)
                
        self.mushroom_life_up(game.score)

        for mushroomGreen in self.green_mushrooms:
            
            if player.dino_rect.colliderect(mushroomGreen.rect):
                player.life_up = True
                self.green_mushrooms.remove(mushroomGreen)
            else:
                mushroomGreen.update(game.game_speed, self.green_mushrooms)
    
    def draw(self, screen):
        for star in self.stars:
            star.draw(screen)

        for mushroom in self.mushrooms:
            mushroom.draw(screen)

        for green_mushroom in self.green_mushrooms:
            green_mushroom.draw(screen)
    
    def reset_power_ups(self):
        self.when_appears = 130
        self.when_mush_appears = 200
        self.when_mushgreen_appears = 50
        self.stars.clear()
        self.mushrooms.clear()
        self.green_mushrooms.clear()
            
    
    