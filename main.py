from PPlay.window import *
from PPlay.keyboard import *
from PPlay.mouse import *
from sprites import *
from movimentos import *

janela = Window(1280,720)
janela.set_title("Dexter Run")

teclado = Keyboard()
mou = Mouse()

backgroundM = backgroundMenu()
backgroundJ = backgroundJogo()

botaoP = botaoPlay(janela)
botaoL = botaoLeaderboard(janela)
botaoE = botaoExit(janela)

jogador = personagemPrincipal()
velPuloJogador = 320

menuIniciado = True
jogoIniciado = False
leadearboardIniciado = False
jogadorPulando = False

while(True):
    # Tela do jogo
    if jogoIniciado == True:

        # Apertar esc para voltar ao menu
        if teclado.key_pressed("esc"):
            menuIniciado = True
            jogoIniciado = False

        if teclado.key_pressed("up") and not jogadorPulando:
            jogadorPulando = True
            jogadorSubindo = True
            jogadorDescendo = False

        if jogadorPulando:
            if jogadorSubindo:
                jogador.y += velPuloJogador * janela.delta_time()* -1

                if jogador.y <= 300:
                    jogador.y = 300
                    jogadorDescendo = True
                    jogadorSubindo = False

            if jogadorDescendo:
                jogador.y += velPuloJogador * janela.delta_time() 

                if jogador.y >= 400:
                    jogador.y = 400
                    jogadorDescendo = False
                    jogadorPulando = False


        # Desenhando todos objetos do jogo
        backgroundJ.draw()
        jogador.draw()

    # Tela do learderboard
    if leadearboardIniciado == True:
        janela.set_background_color([0,0,0])

        # Apertar esc para voltar ao menu
        if teclado.key_pressed("esc"):
            menuIniciado = True
            leadearboardIniciado = False

    # Tela do menu
    if menuIniciado == True:
        # Clicando botão play
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
        backgroundM.draw()
        botaoP.draw()
        botaoL.draw()
        botaoE.draw()

    janela.update()