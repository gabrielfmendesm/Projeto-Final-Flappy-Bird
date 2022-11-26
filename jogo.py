# ===== Inicialização =====
# ----- Importa e inicia pacotes
from pygame import *
from random import *
from config import *


init()
mixer.init()

# ----- Gera tela principal
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Flappy Bird')

