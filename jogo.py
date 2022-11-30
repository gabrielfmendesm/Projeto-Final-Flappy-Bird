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
# Simbolo PyGame
programIcon = image.load('Assets/icone.jpg')
display.set_icon(programIcon)


# ----- Código principal
rodando = True
while rodando:
	window.blit (fundo, (0,0))
	
	if tela_de_inicio:
		velocidade = 0
		bird.movimento_asa ()
		base.update (velocidade)
		
		window.blit (flappy_bird, (40, 50))
	else:
		
		if inicio_jogo and not fim_jogo:
			
			proximo_cano = time.get_ticks()
			if proximo_cano - ultimo_cano >= frequencia_cano:
				y = altura_tela // 2
				posicao_cano = choice(range(-100,100,4))
				altura = y + posicao_cano
				
				top = Cano(window, cano, altura, 1)
				bottom = Cano(window, cano, altura, -1)
				grupo_canos.add(top)
				grupo_canos.add(bottom)
				ultimo_cano = proximo_cano



# ===== Finalização =====
quit()
