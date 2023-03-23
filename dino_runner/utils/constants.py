import pygame
import os

# Global Constants
TITLE = "Mario Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
FONT_STYLE = "freesansbold.ttf"

DEFAULT_TYPE = "default"
STAR_TYPE = "star"

IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

pygame.mixer.init()
SOUND = pygame.mixer.music.load(os.path.join(IMG_DIR, "Sounds/BoxCat Games - CPU Talk.mp3"))
JUMP_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sounds/8bit-jump.mp3"))
DEATH_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sounds/pacman_death.mp3"))
HIT = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sounds/hit.mp3"))

pygame.mixer.music.set_volume(0.15)
DEATH_SOUND.set_volume(0.15) 
JUMP_SOUND.set_volume(0.15)

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Mario_icon.png"))

RUNNING_STAR = [
    pygame.image.load(os.path.join(IMG_DIR, "Mario/Mario_star1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Mario/Mario_star2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Mario/Mario_star3.png"))
]


JUMPING_STAR = pygame.image.load(os.path.join(IMG_DIR, "Mario/Mario_JumpStar.png"))

DUCKING_STAR = [
    pygame.image.load(os.path.join(IMG_DIR, "Mario/Mario_DuckStar1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Mario/Mario_DuckStar2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Mario/Mario_DuckStar3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Mario/Mario_DuckStar4.png"))
]

LARGE_CANO = [
    pygame.image.load(os.path.join(IMG_DIR, "Mario/largeCano1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Mario/largeCano2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Mario/largeCano3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/bird2.png")),
]

MARIO_RUN = [
    pygame.image.load(os.path.join(IMG_DIR, "Mario/Mario_run1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Mario/Mario_run2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Mario/Mario_run3.png")),
]

MARIO_JUMP = pygame.image.load(os.path.join(IMG_DIR, "Mario/Mario_jump.png"))

MARIO_DUCK = [
    pygame.image.load(os.path.join(IMG_DIR, "Mario/Mario_duck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Mario/Mario_duck2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Mario/Mario_duck3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Mario/Mario_duck4.png")),
]

TORTUGA = [
    pygame.image.load(os.path.join(IMG_DIR, "Mario/tortuga_fly1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Mario/tortuga_fly2.png")),
]

TURTLE = [
    pygame.image.load(os.path.join(IMG_DIR, "Mario/turtle1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Mario/turtle2.png")),
]

TITLE_IMAGE = pygame.image.load(os.path.join(IMG_DIR, "Title/title.png"))
CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
STAR = pygame.image.load(os.path.join(IMG_DIR, 'Other/star.png'))
MUSHROOM = pygame.image.load(os.path.join(IMG_DIR, 'Other/mushroom.png'))
MUSHROOM_GREEN = pygame.image.load(os.path.join(IMG_DIR, 'Other/mushroom_green.png'))

GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, "Other/Mario_GameOver.png"))
BG = pygame.image.load(os.path.join(IMG_DIR, 'Mario/floor.png'))
