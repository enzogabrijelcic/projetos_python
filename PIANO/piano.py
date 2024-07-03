import time
import pygame
from pygame.locals import * #importando coisas necessarias

# Inicialização do Pygame
pygame.init()#inicializa o programa no pygame

# Definindo as dimensões da janela
largura = 800
altura = 200
tamanho_tecla = 60

# Definindo cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Criando a janela
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Piano Simples")

# Carregando sons das teclas
sons = {
    K_a: pygame.mixer.Sound("PIANO/do.wav"),
    K_s: pygame.mixer.Sound("PIANO/re.wav"),
    K_d: pygame.mixer.Sound("PIANO/mi.wav"),
    K_f: pygame.mixer.Sound("PIANO/fa.wav"),
    K_g: pygame.mixer.Sound("PIANO/sol.wav"),
    K_h: pygame.mixer.Sound("PIANO/la.wav"),
    K_j: pygame.mixer.Sound("PIANO/si.wav")
}

do =pygame.mixer.Sound("PIANO/do.wav")
re = pygame.mixer.Sound("PIANO/re.wav")
mi = pygame.mixer.Sound("PIANO/mi.wav")
fa = pygame.mixer.Sound("PIANO/fa.wav")
sol = pygame.mixer.Sound("PIANO/sol.wav")
la = pygame.mixer.Sound("PIANO/la.wav")
si = pygame.mixer.Sound("PIANO/si.wav")

def roda_musica():
    mi.play()
    time.sleep(0.5)
    fa.play()
    time.sleep(0.5)
    sol.play()
    time.sleep(0.5)
    do.play()
    time.sleep(0.5)
    si.play()
    time.sleep(0.5)
    la.play()
    time.sleep(0.5)
    sol.play()
    time.sleep(0.5)
    mi.play()
    time.sleep(0.5)
    do.play() #como aurora precursora
    time.sleep(0.5)
    sol.play()
    time.sleep(0.5)
    sol.play()
    time.sleep(0.5)
    fa.play()
    time.sleep(0.5) #do farol
    re.play()
    time.sleep(0.5)
    mi.play()
    time.sleep(0.5)
    do.play()
    time.sleep(0.5)
    re.play()
    time.sleep(0.5)
    sol.play()
    time.sleep(0.5) #da divindade
    mi.play()
    time.sleep(0.5)
    fa.play()
    time.sleep(0.5)
    sol.play()
    time.sleep(0.5)
    do.play()
    time.sleep(0.5) #foi o vinte
    si.play()
    time.sleep(0.5)
    la.play()
    time.sleep(0.5)
    do.play()
    time.sleep(0.5)
    do.play()
    time.sleep(0.5) #de setembro
    si.play()
    time.sleep(0.5)
    la.play()
    time.sleep(0.5)
    sol.play()
    time.sleep(0.5)
    si.play()
    time.sleep(0.5) #o precursor
    si.play()
    time.sleep(0.5)
    la.play()
    time.sleep(0.5)
    sol.play()
    time.sleep(0.5)
    fa.play()
    time.sleep(0.5)
    mi.play()
    time.sleep(0.5)
    mi.play()
    time.sleep(0.5) #da liberdade

roda_musica()
# Loop principal
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            executando = False
        elif evento.type == KEYDOWN:
            if evento.key in sons:
                sons[evento.key].play()

    # Desenhar o piano na tela
    janela.fill(branco)
    for i, (tecla, som) in enumerate(sons.items()):
        pygame.draw.rect(janela, preto if i % 2 == 0 else branco, (i * tamanho_tecla, 0, tamanho_tecla, altura))
    pygame.display.flip()

# Finalizando o Pygame
pygame.quit()
