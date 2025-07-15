from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.gameimage import *

mouse = Mouse()

# Sprite dos backgrounds
spriteMenu = "sprites/backgroundMenu2.png"
spriteBGLeaderboard = "sprites/leaderboard.png"

# Sprite dos botões do menu
spritePlay = "sprites/botaoPlay.png"
spriteLeaderboard = "sprites/botaoLeaderboard.png"
spriteExit = "sprites/botaoExit.png"

# Sprite dos personagens
spriteJogador = "sprites/jogadorWalkteste.png"
spriteRoboVerdeWalk = "sprites/roboVerdeWalk.png"
spriteRoboVerdeDeath = "sprites/roboVerdeDeath.png"
spriteRoboVerdeAttack = "sprites/roboVerdeAttack.png"
spriteDroneVermelhoWalk = "sprites/droneVermelhoWalk.png"
spriteDroneVermelhoDeath = "sprites/droneVermelhoDeath.png"

# Sprite obstaculos
spriteMesa = "sprites/mesa.png"
spriteGabinete = "sprites/gabinete.png"

# Sprite dos tiros
spriteTiroJogador = "sprites/tiroJogador.png"
spriteTiroInimigo = "sprites/tiroInimigo.png"

# Sprite interface
spriteInterface = "sprites/idleVidaBoneco.png"

# Funções para colocar os planos de fundo na tela
def backgroundMenu():
    backgroundM = GameImage(spriteMenu)
    return backgroundM

def backgroundLeaderboard():
    backgroundLb = GameImage(spriteBGLeaderboard)
    return backgroundLb

def backgroundJogo(spriteJogo,posx,posy):
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
    jogador = Sprite(spriteJogador,frames=6)
    jogador.set_total_duration(1000)
    jogador.x = 50
    jogador.y = 430
    jogador.set_position(jogador.x,jogador.y)
    return jogador

def personagemMenu():
    jogadorMenu = Sprite(spriteJogador,frames=6)
    jogadorMenu.set_total_duration(1000)
    jogadorMenu.x = 390
    jogadorMenu.y = 400
    jogadorMenu.set_position(jogadorMenu.x,jogadorMenu.y)
    return jogadorMenu

def obstaculoMesa(janela):
    mesa = Sprite(spriteMesa,frames=1)
    mesa.x = janela.width + 50
    mesa.y = 450
    mesa.set_position(mesa.x,mesa.y)
    return mesa

def obstaculoGabinete(janela):
    gabinete = Sprite(spriteGabinete,frames=1)
    gabinete.x = janela.width + 50
    gabinete.y = 450
    gabinete.set_position(gabinete.x,gabinete.y)
    return gabinete

def tiroJogador(jogador,jogadorx,jogadory):
    tiroJ = Sprite(spriteTiroJogador,frames=1)
    tiroJ.x = jogadorx + jogador.width
    tiroJ.y = jogadory + jogador.height/2
    tiroJ.set_position(tiroJ.x,tiroJ.y)
    return tiroJ

def roboVerdeWalk(janela):
    roboVerdeW = Sprite(spriteRoboVerdeWalk,frames=4)
    roboVerdeW.set_total_duration(1000)
    roboVerdeW.x = janela.width + 50
    roboVerdeW.y = 400
    roboVerdeW.set_position(roboVerdeW.x,roboVerdeW.y)
    return roboVerdeW

def roboVerdeDeath(janela):
    roboVerdeD = Sprite(spriteRoboVerdeDeath,frames=4)
    roboVerdeD.set_total_duration(1000)
    roboVerdeD.x = janela.width + 50
    roboVerdeD.y = 400
    roboVerdeD.set_position(roboVerdeD.x,roboVerdeD.y)
    return roboVerdeD

def roboVerdeAttack(janela):
    roboVerdeA = Sprite(spriteRoboVerdeAttack,frames=4)
    roboVerdeA.set_total_duration(1000)
    roboVerdeA.x = janela.width + 50
    roboVerdeA.y = 400
    roboVerdeA.set_position(roboVerdeA.x,roboVerdeA.y)
    return roboVerdeA

def droneVermelhoWalk(janela):
    droneVermelhoW = Sprite(spriteDroneVermelhoWalk,frames=4)
    droneVermelhoW.set_total_duration(1000)
    droneVermelhoW.x = janela.width + 50
    droneVermelhoW.y = 250
    droneVermelhoW.set_position(droneVermelhoW.x,droneVermelhoW.y)
    return droneVermelhoW

def droneVermelhoDeath(janela):
    droneVermelhoD = Sprite(spriteDroneVermelhoDeath,frames=6)
    droneVermelhoD.set_total_duration(1000)
    droneVermelhoD.x = janela.width + 50
    droneVermelhoD.y = 250
    droneVermelhoD.set_position(droneVermelhoD.x,droneVermelhoD.y)
    return droneVermelhoD

def tiroInimigo(inimigo,inimigox,inimigoy):
    tiroI = Sprite(spriteTiroInimigo,frames=1)
    tiroI.x = inimigox + inimigo.width
    tiroI.y = inimigoy + inimigo.height/2
    tiroI.set_position(tiroI.x,tiroI.y)
    return tiroI

def interfaceVida():
    interface = Sprite(spriteInterface,frames=1)
    interface.x = 50
    interface.y = 50
    interface.set_position(interface.x,interface.y)
    return interface