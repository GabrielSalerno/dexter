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
spriteMesa = "sprites/mesa.png"
spriteGabinete = "sprites/gabinete.png"

# Funções para colocar os planos de fundo na tela
def backgroundMenu():
    backgroundM = GameImage(spriteMenu)
    return backgroundM

def backgroundJogo(posx,posy):
    backgroundJ = Sprite(spriteJogo,frames=1)
    backgroundJ.x=posx
    backgroundJ.y=posy
    backgroundJ.set_position(backgroundJ.x,backgroundJ.y)
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
    botaoL.x = (janela.width/2)-(botaoL.width/2)
    botaoL.y = janela.height/2+70
    botaoL.set_position(botaoL.x,botaoL.y)
    return botaoL

def botaoExit(janela):
    botaoE = Sprite(spriteExit,frames=1)
    botaoE.x = (janela.width/2)-(botaoE.width/2)
    botaoE.y = janela.height/2+140
    botaoE.set_position(botaoE.x,botaoE.y)
    return botaoE

# Funções para colocar os personagens na tela
def personagemPrincipal():
    jogador = Sprite(spriteJogador,frames=1)#8
    #jogador.set_total_duration(1000)
    jogador.x = 50
    jogador.y = 400
    jogador.set_position(jogador.x,jogador.y)
    return jogador

def obstaculoMesa(janela):
    mesa = Sprite(spriteMesa,frames=1)
    mesa.x = janela.width + 50
    mesa.y = 525
    mesa.set_position(mesa.x,mesa.y)
    return mesa

def obstaculoGabinete(janela):
    gabinete = Sprite(spriteGabinete,frames=1)
    gabinete.x = janela.width + 50
    gabinete.y = 525
    gabinete.set_position(gabinete.x,gabinete.y)
    return gabinete