import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.obstacles.cloud import Cloud

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
        self.y_pos_bg = 380
        self.max_scores = []
        self.pontos = 0
        self.death_count = 0
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.cloud = Cloud()
        
    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()   
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.reset_game()
        while self.playing:
            self.events()
            self.update()
            self.draw()
        
    
    def reset_game(self):
        self.obstacle_manager.reset_obstacles()

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
        
        
        self.update_points()
        self.cloud.update(self.game_speed)
    
    # A cada 100 pontos o game fica mais rápido
    def update_points(self):
        self.pontos += 1
        if self.pontos % 100 == 0:
            self.game_speed += 3
    
    # Contador de pontos durante o jogo
    def points(self):
        self.mos_pontos = self.font.render(f"Points: {self.pontos}", True, (0, 0, 0))
        self.screen.blit(self.mos_pontos, (900, 50))

    # Armazena a pontuação maxima
    def max_points(self):
        self.max_scores.append(self.pontos)
        self.points_rank = self.font.render(f'Max Points: {max(self.max_scores)}', True, (0,0,0))
        self.screen.blit(self.points_rank, (600, 50))
    
    # Contador de mortes
    def count_death(self):
        self.count_morte = self.font.render(f'Death: {self.death_count}',True, (0,0,0))
               
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.points()
        self.max_points()
        self.count_death()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.cloud.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    #
    def mostrar_texto(self, texto, pos_x, pos_y):
        text = self.font.render(texto, True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (pos_x, pos_y)
        self.screen.blit(text, text_rect)
    
    def show_menu(self):
        self.screen.fill((255,255,255))

        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            self.mostrar_texto("Press (S) to start playing", half_screen_width, half_screen_height)
        else:
            self.mostrar_texto("Press (S) to new playing", half_screen_width, half_screen_height - 25)
            self.mostrar_texto("Press (C) to continue playing", half_screen_width, half_screen_height + 25)
            self.screen.blit(self.mos_pontos, (half_screen_width - 450, half_screen_height - 250))
            self.screen.blit(self.points_rank, (half_screen_width - 450, half_screen_height - 220))
            self.screen.blit(self.count_morte, (half_screen_width - 450, half_screen_height - 190))

        pygame.display.update()

        self.handle_events_on_menu()

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False
            elif event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_s] and self.death_count == 0:
                    pygame.mixer.music.play(-1)
                    self.run()
                elif pygame.key.get_pressed()[pygame.K_c] and self.death_count >= 1:
                    pygame.mixer.music.play(-1)
                    self.run()
                elif pygame.key.get_pressed()[pygame.K_s] and self.death_count >= 1:
                    pygame.mixer.music.play(-1)
                    self.death_count = 0
                    self.game_speed = 20
                    self.pontos = 0
                    self.run()

