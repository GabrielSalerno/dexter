from PPlay.window import *
from PPlay.keyboard import *
from PPlay.mouse import *
from random import randint
from sprites import *
from colisao import *


janela = Window(1280,720)
janela.set_title("Dexter Run")

teclado = Keyboard()
mou = Mouse()

backgroundM = backgroundMenu()

backgroundJ1 = backgroundJogo(0,0)
backgroundJ2 = backgroundJogo(backgroundJ1.width,0)
velxCenario = 225

botaoP = botaoPlay(janela)
botaoL = botaoLeaderboard(janela)
botaoE = botaoExit(janela)

jogador = personagemPrincipal()
velPuloJogador = 500
velxJogador = 400
vidaJogador = 3

invencivel = False
tempo_invencivel = 0

mesas = list()
gabinetes = list()
velxObstaculo = velxCenario

menuIniciado = True
jogoIniciado = False
leadearboardIniciado = False
jogadorPulando = False

mesaMovendo = False
gabineteMovendo = False

recargaObstaculo = 5

valorAleat = 0

gameover = False

while(True):
    # Tela do jogo
    if jogoIniciado == True:
        # Apertar esc para voltar ao menu
        if teclado.key_pressed("esc"):
                menuIniciado = True
                jogoIniciado = False

        if not gameover:
            # Tempo de recarga obstaculo iniciado
            recargaObstaculo += janela.delta_time()

            # Fazendo loop no cenario de fundo
            backgroundJ1.x += velxCenario * janela.delta_time() * -1
            backgroundJ2.x += velxCenario * janela.delta_time() * -1

            if backgroundJ1.x+backgroundJ1.width < 0:
                backgroundJ1.x = backgroundJ2.x + backgroundJ2.width
            if backgroundJ2.x+backgroundJ2.width < 0:
                backgroundJ2.x = backgroundJ1.x + backgroundJ1.width

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
            
            # Obstaculos se movendo
            if recargaObstaculo >= 5:
                valorAleat = randint(1,10)
                recargaObstaculo = 0
            
            if valorAleat > 5:
                mesa = obstaculoMesa(janela)
                mesas.append(mesa)
                print("mesa")
                mesaMovendo=True
                valorAleat = 0
            elif valorAleat<=5 and valorAleat>0:
                gabinete = obstaculoGabinete(janela)
                gabinetes.append(gabinete)
                print("gabinete")
                gabineteMovendo = True
                valorAleat = 0
            
            if mesaMovendo:
                if len(mesas) > 0:
                    for mesa in mesas:
                        mesa.x += velxObstaculo * janela.delta_time() *-1
                else:
                    mesaMovendo = False
                for c in range(len(mesas)-1,-1,-1):
                    if mesas[c].x + mesas[c].width < 0:
                        del mesas[c] # Apagar mesa qando sai da tela
                    
            if gabineteMovendo:
                if len(gabinetes)>0:
                    for gabinete in gabinetes:
                        gabinete.x += velxObstaculo * janela.delta_time() *-1
                else:
                    gabineteMovendo = False
                for c in range(len(gabinetes)-1,-1,-1):
                    if gabinetes[c].x + gabinetes[c].width < 0:
                        del gabinetes[c] # Apagar gabinete qando sai da tela

            # Colidindo jogador com as paredes
            if jogador.x < 0:
                jogador.x = 0

            if jogador.x + jogador.width > janela.width:
                jogador.x = janela.width - jogador.width

            # Colidindo jogador com obstaculo
            for gabinete in gabinetes:
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

            for mesa in mesas:
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
                    
                if not jogador.collided(mesa) and jogador.y < 400 and not jogadorPulando:
                    jogador.y += velPuloJogador * janela.delta_time()

                    if jogador.y >= 400:
                        jogador.y = 400


        # Desenhando todos objetos do jogo
        backgroundJ1.draw()
        backgroundJ2.draw()

        # Jogador pisca invencivel
        if invencivel:
            tempo_invencivel += janela.delta_time()
            if int(tempo_invencivel*8)%2==0:
                jogador.draw()
            if tempo_invencivel>2:
                invencivel = False
                tempo_invencivel = 0
        else:
            if not gameover:
                jogador.draw()

        for mesa in mesas:
            mesa.draw()

        for gabinete in gabinetes:
            gabinete.draw()

        janela.draw_text(str(vidaJogador), janela.width/2,50,size=24,color=(0,0,0),font_name="Arial")

        janela.draw_text("{:.1f}".format(recargaObstaculo),50,50,size=24,color=(0,0,0),font_name="Arial")

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
        # Reiniciando o jogo
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