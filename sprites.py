from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.gameimage import *

mouse = Mouse()

# Sprite dos backgrounds
spriteMenu = "sprites/backgroundMenu.png"
spriteJogo = "sprites/backgroundJogo.png"

# Sprite dos botões do menu
spritePlay = "sprites/botaoPlay.png"
spriteLeaderboard = "sprites/botaoLeaderboard.png"
spriteExit = "sprites/botaoExit.png"

# Sprite dos personagens
spriteJogador = "sprites/jogador.png"

# Funções para colocar os planos de fundo na tela
def backgroundMenu():
    backgroundM = GameImage(spriteMenu)
    return backgroundM

def backgroundJogo():
    backgroundJ = GameImage(spriteJogo)
    return backgroundJ

# Funções para colocar os botões na tela
def botaoPlay(janela):
    botaoP = Sprite(spritePlay,frames=1)
    botaoP.x = (janela.width/2)-(botaoP.width/2)
    botaoP.y = janela.height/2
    botaoP.set_position(botaoP.x,botaoP.y)
    return botaoP

def botaoLeaderboard(janela):
    botaoL = Sprite(spriteLeaderboard,frames=1)
    botaoL.set_position((janela.width/2)-(botaoL.width/2),janela.height/2+70)
    return botaoL

def botaoExit(janela):
    botaoE = Sprite(spriteExit,frames=1)
    botaoE.set_position((janela.width/2)-(botaoE.width/2),janela.height/2+140)
    return botaoE

# Funções para colocar os personagens na tela
def personagemPrincipal():
    jogador = Sprite(spriteJogador,frames=1)
    jogador.x = 50
    jogador.y = 400
    jogador.set_position(jogador.x,jogador.y)
    return jogador