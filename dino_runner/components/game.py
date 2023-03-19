import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.fonte = pygame.font.SysFont("arial", 30, True, True)
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.pontos = 0
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self) 
        #Adicionei no update a função para atualização dos points no loop.
        self.points()  
    
### Criei uma função que vai ser usado como points no jogo do Dino
### nela eu chamei o metodo render do pygame para atribuir a mensagem e a cor das letras
### e usei a condição para cada 100 pontos o game_speed aumentar + 1. 
    def points(self):
        self.mos_pontos = self.fonte.render(f"{self.pontos}", True, (0, 0, 0))
        self.pontos += 1
        if self.pontos % 100 == 0:
            self.game_speed += 1
            
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()

        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        pygame.display.flip()

    def draw_background(self):
        # Aqui usei o método blit para desenhar a pontuação na tela
        self.screen.blit(self.mos_pontos, (1000, 50))
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
