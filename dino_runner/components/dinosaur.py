import pygame
from dino_runner.utils.constants import MARIO_RUN, MARIO_JUMP, JUMP_SOUND, MARIO_DUCK, RUNNING_STAR, STAR_TYPE, DEFAULT_TYPE, JUMPING_STAR, DUCKING_STAR

X_POS = 80
Y_POS = 430
JUMP_VEL = 8.5

RUN_IMG = {DEFAULT_TYPE: MARIO_RUN, STAR_TYPE:RUNNING_STAR}
JUMP_IMAGE = {DEFAULT_TYPE: MARIO_JUMP, STAR_TYPE:JUMPING_STAR}
DUCK_IMAGE = {DEFAULT_TYPE: MARIO_DUCK, STAR_TYPE:DUCKING_STAR}

class Dinosaur:
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.step_index = 0
        self.step_duck = 0
        self.jump_vel = JUMP_VEL
        self.has_power_up = False
        self.life_up = False
    
    def run(self):
        self.image = RUN_IMG[self.type][self.step_index//5]
        self.dino_rect.y = Y_POS
        self.step_index += 1
        if self.step_index == 15:
            self.step_index = 0      
        
    def jump(self):
        self.image = JUMP_IMAGE[self.type]
        
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel*4
            self.jump_vel -=0.8
        
        if self.jump_vel < -JUMP_VEL:
            self.dino_jump = False
            self.dino_rect.y = Y_POS
            self.jump_vel = JUMP_VEL
    
    def duck(self):
        self.image = DUCK_IMAGE[self.type][self.step_duck//5]
        self.dino_rect.y = 445
        self.dino_duck = False

        self.step_duck += 1
        if self.step_duck == 20:
            self.step_duck = 0
    
    def update(self, user_input):
        if user_input[pygame.K_UP] and not self.dino_jump:
            JUMP_SOUND.play()
            self.dino_jump = True
            self.dino_run = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False

        elif user_input[pygame.K_RIGHT]:
            if self.dino_rect.x < 1050:
                self.dino_rect.x += 5 
            else:
                self.dino_rect.x = 1048

        elif user_input[pygame.K_LEFT]:
            if self.dino_rect.x > 0:
                self.dino_rect.x -= 5  
            else:
                self.dino_rect.x = 2

        elif not self.dino_jump and not self.dino_duck:
            self.dino_run = True

        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()                
            
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x,self.dino_rect.y))
    