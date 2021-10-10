import sys, pygame 
from pygame.locals import *
pygame.init()

size = width, height = 600, 600
screen = pygame.display.set_mode(size)

backgroundColor = 50, 72, 95
screen.fill(backgroundColor)
colorLine = 41, 61, 82 

line_pos1 = (200, 0)
line_pos2 = (400, 0)
lineH = pygame.Surface((20,600))
lineH.fill((colorLine))

line_pos3 = (0, 200)
line_pos4 = (0, 400)
lineW = pygame.Surface((800,20))
lineW.fill((colorLine))

lines = [line_pos1, line_pos2, line_pos3, line_pos4]

campo1 = Rect((0,0), (200, 200))
campo2 = Rect((200,0), (200, 200))
campo3 = Rect((400,0), (200, 200))
campo4 = Rect((0,200), (200, 200))
campo5 = Rect((200,200), (200, 200))
campo6 = Rect((400,200), (200, 200))
campo7 = Rect((0,400), (200, 200))
campo8 = Rect((200,400), (200, 200))
campo9 = Rect((400,400), (200, 200))

campos = [campo1, campo2, campo3, campo4,
campo5, campo6, campo7, campo8, campo9]

marcacao = [ 
  0,1,2,
  3,4,5,
  6,7,8
]
player = 1
escolha = 'X'
jogadas = 0

def desenho(pos):
  global player
  
  x,y = pos
  if player == 2:
    player = 1
    originalO = pygame.image.load("zero.png").convert_alpha()
    O = pygame.transform.scale(originalO, (100, 100))
    screen.blit(O, (x - 50, y - 50))
  else:
    player = 2
    originalX = pygame.image.load("x.png").convert_alpha()
    X = pygame.transform.scale(originalX, (100, 100))
    screen.blit(X, (x - 50, y - 50))

def confirmar(indice):
  global escolha
  global jogadas
  if marcacao[indice] == "X" or marcacao[indice] == "O":
    #print(marcacao)
    return 0
  else:
    if(player == 1):
      marcacao[indice] = escolha
      escolha = 'O'
    if(player == 2):
      marcacao[indice] = escolha
      escolha = 'X'
    jogadas += 1
    return 1


def ganhador(campo):
  if campo == 1:
    valor = marcacao[0]
    if((marcacao[1] == valor and marcacao[2] == valor)
    or (marcacao[3] == valor and marcacao[6] == valor)
    or (marcacao[4] == valor and marcacao[8] == valor)):
      if(valor == 'X'): 
        return 1
      if(valor == 'O'):
        return 2
  if campo == 2:
    valor = marcacao[1]
    if((marcacao[0] == valor and marcacao[2] == valor)
    or (marcacao[4] == valor and marcacao[7] == valor)):
      if(valor == 'X'):
        return 1
      if(valor == 'O'):
        return 2
  if campo == 3:
    valor = marcacao[2]
    if((marcacao[0] == valor and marcacao[1] == valor)
    or (marcacao[5] == valor and marcacao[8] == valor)
    or (marcacao[4] == valor and marcacao[6] == valor)):
      if(valor == 'X'):
        return 1
      if(valor == 'O'):
        return 2
  if campo == 4:
    valor = marcacao[3]
    if((marcacao[0] == valor and marcacao[6] == valor)
    or (marcacao[4] == valor and marcacao[5] == valor)):
      if(valor == 'X'):
        return 1
      if(valor == 'O'):
        return 2
  if campo == 5:
    valor = marcacao[4]
    if((marcacao[0] == valor and marcacao[8] == valor)
    or (marcacao[3] == valor and marcacao[5] == valor)
    or (marcacao[1] == valor and marcacao[7] == valor)
    or (marcacao[2] == valor and marcacao[6] == valor)):
      if(valor == 'X'):
        return 1
      if(valor == 'O'):
        return 2
  if campo == 6:
    valor = marcacao[5]
    if((marcacao[2] == valor and marcacao[8] == valor)
    or (marcacao[3] == valor and marcacao[4] == valor)):
      if(valor == 'X'):
        return 1
      if(valor == 'O'):
        return 2    
  if campo == 7:
    valor = marcacao[6]
    if((marcacao[0] == valor and marcacao[3] == valor)
    or (marcacao[4] == valor and marcacao[2] == valor)
    or (marcacao[7] == valor and marcacao[8] == valor)):
      if(valor == 'X'):
        return 1
      if(valor == 'O'):
        return 2
  if campo == 8:
    valor = marcacao[7]
    if((marcacao[1] == valor and marcacao[4] == valor)
    or (marcacao[6] == valor and marcacao[8] == valor)):
      if(valor == 'X'):
        return 1
      if(valor == 'O'):
        return 2
  if campo == 9:
    valor = marcacao[8]
    if((marcacao[6] == valor and marcacao[7] == valor)
    or (marcacao[2] == valor and marcacao[5] == valor)):
      if(valor == 'X'):
        return 1
      if(valor == 'O'):
        return 2


def campoClicado():
  for i in campos:
    if event.type == MOUSEBUTTONDOWN and i.collidepoint(posClick):
      if(i == campo1):
        if(confirmar(0) == 1):
          desenho([100, 100])
          if(ganhador(1) == 1):
            print("O Ganhador foi o jogador número 1")
            return 0
          if(ganhador(1) == 2):
            print("O Ganhador foi o jogador número 2")
            return 0
      if(i == campo2):
        if(confirmar(1) == 1):
          desenho([300, 100])
          if(ganhador(2) == 1):
            print("O Ganhador foi o jogador número 1")
            return 0
          if(ganhador(2) == 2):
            print("O Ganhador foi o jogador número 2")
            return 0
      if(i == campo3):
        if(confirmar(2) == 1):
          desenho([500, 100])
          if(ganhador(3) == 1):
            print("O Ganhador foi o jogador número 1")
            return 0
          if(ganhador(3) == 2):
            print("O Ganhador foi o jogador número 2")
            return 0
      if(i == campo4):
        if(confirmar(3) == 1):
          desenho([100, 300])
          if(ganhador(4) == 1):
            print("O Ganhador foi o jogador número 1")
            return 0
          if(ganhador(4) == 2):
            print("O Ganhador foi o jogador número 2")
            return 0
      if(i == campo5):
        if(confirmar(4) == 1):
          desenho([300, 300])
          if(ganhador(5) == 1):
            print("O Ganhador foi o jogador número 1")
            return 0
          if(ganhador(5) == 2):
            print("O Ganhador foi o jogador número 2")
            return 0
      if(i == campo6):
        if(confirmar(5) == 1):
          desenho([500, 300])
          if(ganhador(6) == 1):
            print("O Ganhador foi o jogador número 1")
            return 0
          if(ganhador(6) == 2):
            print("O Ganhador foi o jogador número 2")
            return 0
      if(i == campo7):
        if(confirmar(6) == 1):
          desenho([100, 500])
          if(ganhador(7) == 1):
            print("O Ganhador foi o jogador número 1")
            return 0
          if(ganhador(7) == 2):
            print("O Ganhador foi o jogador número 2")
            return 0
      if(i == campo8):
        if(confirmar(7) == 1):
          desenho([300, 500])
          if(ganhador(8) == 1):
            print("O Ganhador foi o jogador número 1")
            return 0
          if(ganhador(8) == 2):
            print("O Ganhador foi o jogador número 2")
            return 0
      if(i == campo9):
        if(confirmar(8) == 1):
          desenho([500, 500])
          if(ganhador(9) == 1):
            print("O Ganhador foi o jogador número 1")
            return 0
          if(ganhador(9) == 2):
            print("O Ganhador foi o jogador número 2")
            return 0

clock = pygame.time.Clock()

a = 1
while True:
  clock.tick(20)
  posClick = pygame.mouse.get_pos()
  for event in pygame.event.get():
    if event.type == pygame.QUIT or jogadas == 9 or a == 0: sys.exit()
    if event.type == MOUSEBUTTONDOWN:
      a = campoClicado()
      #print(marcacao)


  screen.blit(lineH, line_pos1)
  screen.blit(lineH, line_pos2)
  screen.blit(lineW, line_pos3)
  screen.blit(lineW, line_pos4)
  pygame.display.flip()
