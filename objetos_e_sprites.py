from pygame import *
from random import *
from assets import *
from config import *

# Informação da tela
window = display.set_mode((WIDTH, HEIGHT))


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
				self.velocidade = -5
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
		espaco_cano = 100 // 2
		x = WIDTH

		if posicao == 1:
			self.image = transform.flip(self.image, False, True)
			self.rect.bottomleft = (x, y - espaco_cano)
		elif posicao == -1:
			self.rect.topleft = (x, y + espaco_cano)

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

# Variáveis dos objetos e sprites
grupo_canos = sprite.Group()
bird = Bird(window)
imagem_placar = Placar(WIDTH // 2, 50, window)
base = Base(window)