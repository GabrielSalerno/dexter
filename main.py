from PPlay.window import *
from PPlay.keyboard import *
from PPlay.mouse import *
from sprites import *
from colisao import *


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
velPuloJogador = 500
velxJogador = 400
vidaJogador = 3

invencivel = False
tempo_invencivel = 0

mesa = obstaculoMesa()
gabinete = obstaculoGabinete()

menuIniciado = True
jogoIniciado = False
leadearboardIniciado = False
jogadorPulando = False

gameover = False

while(True):
    # Tela do jogo
    if jogoIniciado == True:
        # Apertar esc para voltar ao menu
        if teclado.key_pressed("esc"):
                menuIniciado = True
                jogoIniciado = False

        if not gameover:
            # Apertar seta para cima para o jogador pular
            if teclado.key_pressed("up") and not jogadorPulando:
                jogadorPulando = True
                jogadorSubindo = True
                jogadorDescendo = False

            if jogadorPulando:
                if jogadorSubindo:
                    jogador.y += velPuloJogador * janela.delta_time()* -1

                    if jogador.y <= 250:
                        jogador.y = 250
                        jogadorDescendo = True
                        jogadorSubindo = False

                if jogadorDescendo:
                    jogador.y += velPuloJogador * janela.delta_time() 

                    if jogador.y >= 400:
                        jogador.y = 400
                        jogadorDescendo = False
                        jogadorPulando = False
            
            # Apertar seta da direita para o jogador andar para frente
            if teclado.key_pressed("right"):
                jogador.x += velxJogador * janela.delta_time()
                #jogador.update()
            
            if teclado.key_pressed("left"):
                jogador.x += velxJogador * janela.delta_time() *-1

            # Colidindo jogador com as paredes
            if jogador.x < 0:
                jogador.x = 0

            if jogador.x + jogador.width > janela.width:
                jogador.x = janela.width - jogador.width

            # Colidindo jogador com obstaculo
            if jogador.collided(gabinete):
                if jogador.y + jogador.height >= gabinete.y and jogador.y + jogador.height <= gabinete.y + 10:
                    jogador.y = gabinete.y - jogador.height
                    jogadorPulando = False
                    jogadorSubindo = False
                    jogadorDescendo = False
                
                elif not invencivel:
                    vidaJogador -= 1
                    jogador.x = gabinete.x - jogador.width
                    jogador.y = gabinete.y - jogador.height
                    invencivel = True
            
            if not jogador.collided(gabinete) and jogador.y < 400 and not jogadorPulando:
                jogador.y += velPuloJogador * janela.delta_time()

                if jogador.y >= 400:
                    jogador.y = 400

            if jogador.collided(mesa):
                if jogador.y + jogador.height >= mesa.y and jogador.y + jogador.height <= mesa.y + 10:
                    jogador.y = mesa.y - jogador.height
                    jogadorPulando = False
                    jogadorSubindo = False
                    jogadorDescendo = False
                
                elif not invencivel:
                    vidaJogador -= 1
                    jogador.x = mesa.x - jogador.width
                    jogador.y = mesa.y - jogador.height
                    invencivel = True

            if invencivel:
                if tempo_invencivel >= 2:
                        invencivel = False
                        tempo_invencivel = 0

            tempo_invencivel += janela.delta_time()

        # Desenhando todos objetos do jogo
        backgroundJ.draw()
        jogador.draw()
        mesa.draw()
        gabinete.draw()
        janela.draw_text(str(vidaJogador), janela.width/2,50,size=24,color=(0,0,0),font_name="Arial")
        if vidaJogador == 0:
            gameover = True
        if gameover:
            janela.draw_text("Game over", janela.width/2,janela.height/2,size=24,color=(0,0,0),font_name="Arial")

    # Tela do learderboard
    if leadearboardIniciado == True:
        janela.set_background_color([0,0,0])

        # Apertar esc para voltar ao menu
        if teclado.key_pressed("esc"):
            menuIniciado = True
            leadearboardIniciado = False

    # Tela do menu
    #menuIniciado(botaoP,botaoL,botaoE,janela)
    
    if menuIniciado == True:
        gameover = False
        vidaJogador = 3
        jogador.x = 50
        jogador.y = 400
        jogador.set_position(jogador.x,jogador.y)

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