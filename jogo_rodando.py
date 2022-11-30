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

# ----- Sons e efeitos sonoros
mixer.init()
som_gameover = mixer.Sound('Sounds/som_gameover.wav')
som_impacto = mixer.Sound('Sounds/som_impacto.wav')
som_acerto = mixer.Sound('Sounds/som_acerto.wav')
som_asa = mixer.Sound('Sounds/som_asa.wav')
efeito_sonoro = mixer.Sound('Sounds/efeito_sonoro.wav')

# Dados gerais do jogo.
WIDTH = 288 # Largura da tela
HEIGHT = 512 # Altura da tela
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Variáveis
altura_tela = 0.8 * HEIGHT
velocidade = 0
inicio_jogo = False
fim_jogo = False
reiniciar = False
pontuacao = 0
pontuacao_recorde = 0
tela_de_inicio = True
acerto_cano = False
frequencia_cano = 1600 # frequência em milissegundos do aparecimento dos canos

# Classe que representa o jogador (bird)
class Bird: 
	def __init__(self, window):
		self.window = window
		self.lista = []

		for i in range(1,4):
			img = image.load(f'Assets/Bird/bird{i}.png')
			self.lista.append(img)
		
		self.reset()

	# Gravidade e movimento do jogador (bird)
	def update(self):
		# gravidade
		self.velocidade += 0.3
		if self.velocidade >= 8:
			self.velocidade = 8
		if self.rect.bottom <= altura_tela:
			self.rect.y += int(self.velocidade)
		
		if self.vivo:
			# pulo
			if mouse.get_pressed()[0] == 1 and not self.pulo:
				som_asa.play()
				self.pulo = True
				self.velocidade = -6
			if mouse.get_pressed()[0] == 0:
				self.pulo = False
			
			self.contador_asa()
			
			self.image = transform.rotate(self.lista[self.frame], self.velocidade * -2)
		else:
			if self.rect.bottom <= altura_tela:
				self.angle -= 2
			self.image = transform.rotate(self.lista[self.frame], self.angle)
		
		self.window.blit(self.image, self.rect)
		
	def contador_asa(self):
		# animação do bird
		self.contador += 1
		if self.contador > 5:
			self.contador = 0
			self.frame += 1
		if self.frame >= 3:
			self.frame = 0
			
	def movimento_asa(self):
		self.contador_asa()
		if self.posicao_asa <= -10 or self.posicao_asa > 10:
			self.inclinacao_asa *= -1
		self.posicao_asa += self.inclinacao_asa
		self.rect.y += self.inclinacao_asa
		self.rect.x = WIDTH // 2 - 20
		self.image = self.lista[self.frame]
		self.window.blit(self.image, self.rect)
		
	def reset(self):
		self.frame = 0
		self.image = self.lista[self.frame]
		self.rect = self.image.get_rect()
		self.rect.x = 60
		self.rect.y = int(altura_tela) // 2
		self.contador = 0
		self.velocidade = 0
		self.pulo = False
		self.vivo = True
		self.angle = 0
		self.meio_tela = altura_tela // 2
		self.posicao_asa = 0
		self.inclinacao_asa = 1

# Classe que representa o placar (contador de pontos)
class Placar:
	def __init__(self, x, y, window):
		self.lista_placar = []
		for placar in range(10):
			img = image.load(f'Assets/Placar/{placar}.png')
			self.lista_placar.append(img)
			self.x = x
			self.y = y

		self.window = window
		
	# Atualização do placar
	def update(self, placar):
		placar = str(placar)
		for frame, num in enumerate(placar):
			self.image = self.lista_placar[int(num)]
			self.rect = self.image.get_rect()
			self.rect.topleft = self.x - 15 * len(placar) + 30 * frame, self.y
			self.window.blit(self.image, self.rect)

# Classe que representa os canos (obstáculos)
class Cano(sprite.Sprite):
	def __init__(self, window, image, y, posicao):
		super(Cano, self).__init__()
		
		self.window = window
		self.image = image
		self.rect = self.image.get_rect()
		gap_cano = 100 // 2
		x = WIDTH

		if posicao == 1:
			self.image = transform.flip(self.image, False, True)
			self.rect.bottomleft = (x, y - gap_cano)
		elif posicao == -1:
			self.rect.topleft = (x, y + gap_cano)

	# Atualização dos canos
	def update(self, velocidade):
		self.rect.x -= velocidade
		if self.rect.right < 0:
			self.kill()
		self.window.blit(self.image,  self.rect)

# Classe que representa o chão
class Base:
	def __init__(self, window):
		self.window = window

		self.image1 = image.load('Assets/base.png')
		self.image2 = self.image1
		self.rect1 = self.image1.get_rect()
		self.rect1.x = 0
		self.rect1.y = int(altura_tela)
		self.rect2 = self.image2.get_rect()
		self.rect2.x = WIDTH
		self.rect2.y = int(altura_tela)
	
	# Atualização do terreno
	def update(self, velocidade):
		self.rect1.x -= velocidade
		self.rect2.x -= velocidade
		
		if self.rect1.right <= 0:
			self.rect1.x = WIDTH - 5
		if self.rect2.right <= 0:
			self.rect2.x = WIDTH - 5

		self.window.blit(self.image1, self.rect1)
		self.window.blit(self.image2, self.rect2)

init()
mixer.init()

# ----- Gera tela principal
window = display.set_mode((WIDTH, HEIGHT))
clock = time.Clock()
display.set_caption('Flappy Bird')

# Simbolo PyGame
programIcon = image.load('Assets/icone.jpg')
display.set_icon(programIcon)

grupo_canos = sprite.Group()
bird = Bird(window)
imagem_placar = Placar(WIDTH // 2, 50, window)
base = Base(window)

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
		
		grupo_canos.update(velocidade)
		base.update(velocidade)	
		bird.update()
		imagem_placar.update(pontuacao)
		
		if sprite.spritecollide(bird, grupo_canos, False) or bird.rect.top <= 0:
			inicio_jogo = False
			if bird.vivo:
				som_impacto.play()
				som_gameover.play()
			bird.vivo = False
			bird.theta = bird.velocidade * -2
	
		if bird.rect.bottom >= altura_tela:
			velocidade = 0
			fim_jogo = True
	
		if len(grupo_canos) > 0:
			c = grupo_canos.sprites()[0]
			if bird.rect.left > c.rect.left and bird.rect.right < c.rect.right and not acerto_cano and bird.vivo:
				acerto_cano = True
	
			if acerto_cano:
				if bird.rect.left > c.rect.right:
					acerto_cano = False
					pontuacao += 1
					som_acerto.play()

	if not bird.vivo:
		window.blit(gameover, (50,200))
		
	for e in event.get():
		if e.type == QUIT:
			rodando = False
		if e.type == KEYDOWN:
			if e.key == K_ESCAPE or \
				e.key == K_q:
				rodando = False
		if e.type == MOUSEBUTTONDOWN:
			if tela_de_inicio:
				inicio_jogo = True
				velocidade = 2
				tela_de_inicio = False

				fim_jogo = False
				ultimo_cano = time.get_ticks() - frequencia_cano
				proximo_cano = 0
				grupo_canos.empty()
				
				velocidade = 2
				pontuacao = 0

			if fim_jogo:
				tela_de_inicio = True
				bird = Bird(window)
				cano = choice([cano1, cano2])
				fundo = choice([fundo1, fundo2])



	clock.tick(FPS)
	display.update()
# ===== Finalização =====
quit()
