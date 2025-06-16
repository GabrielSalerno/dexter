from PPlay.window import *
from PPlay.mouse import *
from sprites import *

mou = Mouse()

#backgroundM = backgroundMenu()

def menuIniciado(botaoP,botaoL,botaoE,janela):
    if mou.is_over_area([botaoP.x,botaoP.y],[botaoP.x+botaoP.width,botaoP.y+botaoP.height]):
        if mou.is_button_pressed(1):
            jogoIniciado = True
            menuIniciado = False
        
        # Clicando botão leaderboard
    if mou.is_over_area([botaoL.x,botaoL.y],[botaoL.x+botaoL.width,botaoL.y+botaoL.height]):
        if mou.is_button_pressed(1):
            leadearboardIniciado = True
            menuIniciado = False
        
    # Clicando botão exit
    if mou.is_over_area([botaoE.x,botaoE.y],[botaoE.x+botaoE.width,botaoE.y+botaoE.height]):
        if mou.is_button_pressed(1):
            janela.close()

    # Desenhando todos objetos do menu
    #backgroundM.draw()
    botaoP.draw()
    botaoL.draw()
    botaoE.draw()
    return jogoIniciado,menuIniciado,leadearboardIniciado
