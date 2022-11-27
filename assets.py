from pygame import *
from random import *


# ----- Imagens
# Fundos de tela
fundo1 = image.load('Assets/background-day.png')
fundo2 = image.load('Assets/background-night.png')
fundo = choice([fundo1, fundo2])

# Canos
cano1 = image.load('Assets/pipe-green.png')
cano2 = image.load('Assets/pipe-red.png')
cano = choice([cano1, cano2])

# Gameover e Flappy Bird
gameover = image.load('Assets/gameover.png')
flappy_bird = image.load('Assets/flappybird.png')
flappy_bird = transform.scale(flappy_bird, (200,80))

# ----- Sons

