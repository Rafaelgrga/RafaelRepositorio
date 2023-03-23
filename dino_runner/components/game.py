import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE, DEFAULT_TYPE, TITLE_IMAGE, GAME_OVER
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.cloud import Cloud
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.executing = False
        self.font = pygame.font.Font(FONT_STYLE, 22)
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.max_scores = []
        self.score = 0
        self.death_count = 0

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.cloud = Cloud()
        self.power_up_manager = PowerUpManager()
        
    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()   
        pygame.quit()

    def run(self):
        self.playing = True
        pygame.mixer.music.play(-1)
        #self.reset_game()
        while self.playing:
            self.events()
            self.update()
            self.draw()
        
    def reset_game(self):

        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.obstacle_manager.vida = 100
        self.player = Dinosaur()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                pygame.display.quit()   
                pygame.quit()

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)

        self.power_up_manager.update(self)
        self.update_points()
        self.life_points()
        self.cloud.update(self.game_speed)

    def life_points(self):
        self.mostrar_vida = self.font.render(f"Life: {self.obstacle_manager.vida} / 100", True, (0, 0, 0))
        self.screen.blit(self.mostrar_vida, (50, 50))
        if self.obstacle_manager.vida > 100:
            self.obstacle_manager.vida = 100
        
    def life_up(self):
        if self.player.life_up:
            self.obstacle_manager.vida += 40
            self.player.life_up = False
    
    def update_points(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 3
    
    def points(self):
        self.mos_pontos = self.font.render(f"Points: {self.score}", True, (0, 0, 0))
        self.screen.blit(self.mos_pontos, (900, 50))

    def max_points(self):
        self.max_scores.append(self.score)
        self.points_rank = self.font.render(f'Max Points: {max(self.max_scores)}', True, (0,0,0))
        self.screen.blit(self.points_rank, (600, 50))
    
    def count_death(self):
        self.count_morte = self.font.render(f'Death: {self.death_count}',True, (0,0,0))
               
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((100, 150, 255))
        self.draw_background()
        self.points()
        self.max_points()
        self.count_death()
        self.player.draw(self.screen)
        self.draw_power_up_time()
        self.life_points()
        self.life_up()

        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.cloud.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time_up - pygame.time.get_ticks())/1000, 2)

            if time_to_show >=0:
                font = pygame.font.Font(FONT_STYLE, 22)
                text = font.render(f"Power Up: {time_to_show}", True, (255,0,0))
                text_rect = text.get_rect()
                text_rect.x = 425
                text_rect.y = 100
                self.screen.blit(text, text_rect)
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def mostrar_texto(self, texto, pos_x, pos_y):
        text = self.font.render(texto, True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (pos_x, pos_y)
        self.screen.blit(text, text_rect)
    
    def show_menu(self):
        
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            self.screen.blit(TITLE_IMAGE, (0, 0))
            self.mostrar_texto("Choose a difficult to Start Game(Only Numbers)", half_screen_width, half_screen_height - 50)
            self.mostrar_texto("1 - Easy     2 - Medium     3 - Hard", half_screen_width, half_screen_height)
        else:
            self.screen.blit(GAME_OVER, (0, 0))
            self.mostrar_texto("Press (S) to return menu", half_screen_width, half_screen_height + 165)
            self.mostrar_texto("Press (C) to continue playing", half_screen_width, half_screen_height + 195)
            self.screen.blit(self.mos_pontos, (half_screen_width - 450, half_screen_height - 250))
            self.screen.blit(self.points_rank, (half_screen_width - 450, half_screen_height - 220))
            self.screen.blit(self.count_morte, (half_screen_width - 450, half_screen_height - 190))

        pygame.display.update()
        self.handle_events_on_menu()
    
    def difficult_change(self, game_speed):
        self.game_speed = game_speed
        self.reset_game()
        self.run()

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False
            elif event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_1] and self.death_count == 0:
                    self.difficult_change(20)
                elif pygame.key.get_pressed()[pygame.K_2] and self.death_count == 0:
                    self.difficult_change(30)
                elif pygame.key.get_pressed()[pygame.K_3] and self.death_count == 0:
                    self.difficult_change(40)
                elif pygame.key.get_pressed()[pygame.K_c] and self.death_count >= 1:
                    self.obstacle_manager.vida = 100
                    self.run()
                elif pygame.key.get_pressed()[pygame.K_s] and self.death_count >= 1:
                    self.game_speed = 20
                    self.score = 0
                    self.death_count = 0