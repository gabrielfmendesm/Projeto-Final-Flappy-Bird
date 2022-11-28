# ===== Inicialização =====
# ----- Importa e inicia pacotes
from pygame import *
from random import *
from config import *
from assets import *
from objetos_e_sprites import *


init()
mixer.init()

# ----- Gera tela principal
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Flappy Bird')

# ----- Código principal
rodando = True
while rodando:
    window.blit (fundo, (0,0))
    if tela_de_inicio:
        velocidade = 0
        bird.movimento_asa ()



# ===== Finalização =====
quit()
