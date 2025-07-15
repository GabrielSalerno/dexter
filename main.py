from PPlay.window import *
from PPlay.keyboard import *
from PPlay.mouse import *
from PPlay.sound import *
from random import randint
from sprites import *
from constantes import *
from arquivo import *

janela = Window(1280,720)
janela.set_title("Dexter Run")

teclado = Keyboard()
mou = Mouse()

musicaFundo = Sound("sounds/magicFx.wav")
musicaFundo.set_repeat(True)
musicaFundo.play()

backgroundM = backgroundMenu()
backgroundLb = backgroundLeaderboard()

backgroundJ1 = backgroundJogo("sprites/backgroundJogo.png",0,0)
backgroundJ2 = backgroundJogo("sprites/backgroundJogo.png",backgroundJ1.width,0)

botaoP = botaoPlay(janela)
botaoL = botaoLeaderboard(janela)
botaoE = botaoExit(janela)

interface100 = interfaceVida("sprites/idleVidaBoneco.png")
interface75 = interfaceVida("sprites/idleVidaBoneco-1.png")
interface35 = interfaceVida("sprites/idleVidaBoneco-2.png")
interface00 = interfaceVida("sprites/idleVidaBoneco-3.png")

jogador = personagemPrincipal()
jogadorMenu = personagemMenu()

tirosJogador = list()

mesas = list()
gabinetes = list()

drones = list()
robos = list()
tirosInimigos = list()

while(True):
    # Tela do jogo
    if jogoIniciado == True:
        # Apertar esc para voltar ao menu
        if teclado.key_pressed("esc"):
                menuIniciado = True
                jogoIniciado = False

        if not gameover:
            # Iniciando o tempo percorrido
            tempoTotal += janela.delta_time()

            if int(tempoTotal // tempoAumentarDif) > tempoAumentarDif:
                contadorDif += 1
                
                velxCenario += 50
                velxObstaculo += 50
                velxInimigos += 50

                if (disMinObsIni >= 150):
                    disMinObsIni -= 15
            
                if(recargaInimigo >= 7):
                    recargaInimigo -= 1
                if(recargaObstaculo >= 4):
                    recargaObstaculo -=1

            # Tempo de recarga obstaculo iniciado
            recargaObstaculo += janela.delta_time()

            # Tempo de recarga monstro iniciado
            recargaInimigo += janela.delta_time()
            tempoUltimoTiroInimigo += janela.delta_time()

            # Tempo de recarga tiro do jogador
            tempoUltimoTiro += janela.delta_time()

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

                    if jogador.y <= alturaPulo:
                        jogador.y = alturaPulo
                        jogadorDescendo = True
                        jogadorSubindo = False

                if jogadorDescendo:
                    jogador.y += velPuloJogador * janela.delta_time() 

                    if jogador.y >= posxJogadorInicial:
                        jogador.y = posxJogadorInicial
                        jogadorDescendo = False
                        jogadorPulando = False
            
            # Apertar seta da direita para o jogador andar para frente
            if teclado.key_pressed("right"):
                jogador.x += velxJogador * janela.delta_time()
            
            if teclado.key_pressed("left"):
                jogador.x += velxJogador * janela.delta_time() *-1
            
            # Obstaculos se movendo
            if recargaObstaculo >= 5:
                valorAleatObstaculo = randint(1,10)
                recargaObstaculo = 0
            
            if valorAleatObstaculo > 5:
                mesa = obstaculoMesa(janela)
                mesas.append(mesa)
                mesaMovendo=True
                valorAleatObstaculo = 0
            elif valorAleatObstaculo <= 5 and valorAleatObstaculo>0:
                gabinete = obstaculoGabinete(janela)
                gabinetes.append(gabinete)
                gabineteMovendo = True
                valorAleatObstaculo = 0
            
            if mesaMovendo:
                if len(mesas) > 0:
                    for mesa in mesas:
                        mesa.x += velxObstaculo * janela.delta_time() *-1
                else:
                    mesaMovendo = False
                for c in range(len(mesas)-1,-1,-1):
                    if mesas[c].x + mesas[c].width < 0:
                        del mesas[c] # Apagar mesa quando sai da tela
                    
            if gabineteMovendo:
                if len(gabinetes)>0:
                    for gabinete in gabinetes:
                        gabinete.x += velxObstaculo * janela.delta_time() *-1
                else:
                    gabineteMovendo = False
                for c in range(len(gabinetes)-1,-1,-1):
                    if gabinetes[c].x + gabinetes[c].width < 0:
                        del gabinetes[c] # Apagar gabinete quando sai da tela

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
                    
                    elif invencivel:
                        jogador.x = gabinete.x - jogador.width
                        jogador.y = gabinete.y - jogador.height

            
                if not jogador.collided(gabinete) and jogador.y < posxJogadorInicial and not jogadorPulando:
                    jogador.y += velPuloJogador * janela.delta_time()

                    if jogador.y >= posxJogadorInicial:
                        jogador.y = posxJogadorInicial

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
                    
                    elif invencivel:
                        jogador.x = mesa.x - jogador.width
                        jogador.y = mesa.y - jogador.height
                    
                if not jogador.collided(mesa) and jogador.y < posxJogadorInicial and not jogadorPulando:
                    jogador.y += velPuloJogador * janela.delta_time()

                    if jogador.y >= posxJogadorInicial:
                        jogador.y = posxJogadorInicial
                
            if not invencivel:
                for c in range(len(robos)-1,-1,-1):
                    if jogador.collided(robos[c]):
                        vidaJogador -= 1
                        jogador.x = robos[c].y
                        jogador.y = robos[c].x
                        invencivel = True
                for c in range(len(drones)-1,-1,-1):
                    if jogador.collided(drones[c]):
                        vidaJogador -= 1
                        jogador.x = drones[c].y
                        jogador.y = drones[c].x
                        invencivel = True

            for c in range(len(tirosJogador)-1,-1,-1):
                for mesa in mesas:
                    if mesa.collided(tirosJogador[c]):
                        del tirosJogador[c]
                for gabinete in gabinetes:
                    if gabinete.collided(tirosJogador[c]):
                        del tirosJogador[c]


            if teclado.key_pressed("space") and tempoUltimoTiro >= recargaTiro:
                tiroJ = tiroJogador(jogador,jogador.x,jogador.y)
                tirosJogador.append(tiroJ)
                tempoUltimoTiro = 0
            
            if len(tirosJogador)>0:
                for tiro in tirosJogador:
                    tiro.x += velxTiro * janela.delta_time()
            
            for c in range(len(tirosJogador)-1,-1,-1):
                if tirosJogador[c].x + tirosJogador[c].width > janela.width:
                    del tirosJogador[c]
            
            if recargaInimigo >= 10:
                valorAleatInimigo = randint(1,10)
                recargaInimigo = 0

            if valorAleatInimigo > 5:
                drone = droneVermelhoWalk(janela)
                drones.append(drone)
                droneMovendo=True
                valorAleatInimigo = 0
            elif valorAleatInimigo <= 5 and valorAleatInimigo>0:
                robo = roboVerdeWalk(janela)
                robos.append(robo)
                roboMovendo = True
                valorAleatInimigo = 0

                
            if droneMovendo:
                if len(drones) > 0:
                    for drone in drones:
                        drone.x += velxInimigos * janela.delta_time() *-1
                        drone.update()
                else:
                    droneMovendo = False
                for c in range(len(drones)-1,-1,-1):
                    if drones[c].x + drones[c].width < 0:
                        del drones[c] # Apagar drone quando sai da tela
                        
            if roboMovendo:
                if len(robos)>0:
                    for robo in robos:
                        robo.x += velxInimigos * janela.delta_time() *-1
                        robo.update()
                else:
                    roboMovendo = False
                for c in range(len(robos)-1,-1,-1):
                    if robos[c].x + robos[c].width < 0:
                        del robos[c] # Apagar robo quando sai da tela
            
            # Inimigos colidindo
            for t in range(len(tirosJogador)-1,-1,-1):
                tiro = tirosJogador[t]
                for c in range(len(robos)-1,-1,-1):
                    if robos[c].collided(tiro):
                        del robos[c]
                        inimigosDestruidos += 1
                        del tirosJogador[t]
            for t in range(len(tirosJogador)-1,-1,-1):
                tiro = tirosJogador[t]
                for c in range(len(drones)-1,-1,-1):
                    if drones[c].collided(tiro):
                        del drones[c]
                        inimigosDestruidos += 1
                        del tirosJogador[t]

            for robo in robos:
                for mesa in mesas:
                    if robo.collided(mesa):
                        robo.x = mesa.x + mesa.width
                        robo.y = mesa.y + mesa.width
                for gabinete in gabinetes:
                    if robo.collided(gabinete):
                        robo.x = gabinete.x + gabinete.width
                        robo.y = gabinete.y + gabinete.width
            for drone in drones:
                for mesa in mesas:
                    if drone.collided(mesa):
                        drone.x = mesa.x + mesa.width
                        drone.y = mesa.y + mesa.width
                for gabinete in gabinetes:
                    if drone.collided(gabinete):
                        drone.x = gabinete.x + gabinete.width
                        drone.y = gabinete.y + gabinete.width

            # Jogador colidindo com tiro inimigo
            if tempoUltimoTiroInimigo >= recargaTiroInimigo:
                inimigosPossiveis = robos + drones
                if len(inimigosPossiveis)>0:
                    atirador = inimigosPossiveis[randint(0,len(inimigosPossiveis)-1)]
                    tiroI = tiroInimigo(atirador,atirador.x,atirador.y)
                    tirosInimigos.append(tiroI)
                tempoUltimoTiroInimigo = 0
            
            if len(tirosInimigos)> 0:
                for tiroI in tirosInimigos:
                    tiroI.x += velxTiroInimigo * janela.delta_time() *-1
            
            if len(tirosInimigos)>0:
                for tiroI in tirosInimigos:
                    if tiroI.collided(jogador) and not invencivel:
                        vidaJogador -= 1
                        invencivel = True
                        tirosInimigos.remove(tiroI)
                    elif tiroI.x + tiroI.width < 0:
                        tirosInimigos.remove(tiroI)

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
        
        for tiroJ in tirosJogador:
            tiroJ.draw()

        for robo in robos:
            robo.draw()
        
        for drone in drones:
            drone.draw()
        
        for tiroI in tirosInimigos:
            tiroI.draw()

        janela.draw_text(f"{tempoTotal:.0f}s",janela.width-50,25,size=24,color=(0,0,0),font_name="Arial")

        if (vidaJogador== 3):
            interface100.draw()
        elif (vidaJogador==2):
            interface75.draw()
        elif (vidaJogador == 1):
            interface35.draw()
        elif (vidaJogador == 0):
            interface00.draw()

        jogador.update()
        
        if vidaJogador <= 0:
            gameover = True
            # Calculo dos pontos
            pontos = int(tempoTotal) + (2*inimigosDestruidos)
            janela.draw_text(f"Pontuação:{pontos}", janela.width/2,janela.height/2+50,size=24,color=(0,0,0),font_name="Arial")
            janela.draw_text("Game over", janela.width/2,janela.height/2,size=24,color=(0,0,0),font_name="Arial")

            if not rankingRegistrado:
                nome = input("Nome: ")
                criarRanking(nome,pontos)
                rankingRegistrado = True
            jogo_iniciado = False

    # Tela do learderboard
    if leadearboardIniciado == True:
        backgroundLb.draw()
        janela.draw_text("TOP 5 RANKING", janela.width/2 - 120, 150, size=30, color=(255, 255, 255))
        ranking = lerRanking()
        y = 200
        for i, (nome, pontuacao, data) in enumerate(ranking):
            texto = f"{i+1}. {nome} - {pontuacao} pts - {data}"
            janela.draw_text(texto, janela.width/2 - 170, y, size=25, color=(255, 255, 255))
            y += 50

        # Apertar esc para voltar ao menu
        if teclado.key_pressed("esc"):
            menuIniciado = True
            leadearboardIniciado = False

    # Tela do menu
    
    if menuIniciado == True:
        # Reiniciando variáveis do jogo
        gameover = False
        inimigosDestruidos = 0
        vidaJogador = 3
        jogador.x = 50
        jogador.y = posxJogadorInicial
        jogador.set_position(jogador.x, jogador.y)

        # Resetando listas
        mesas.clear()
        gabinetes.clear()
        robos.clear()
        drones.clear()
        tirosJogador.clear()
        tirosInimigos.clear()

        # Resetando tempos e contadores
        tempoTotal = 0
        contadorDif = 0
        recargaObstaculo = 0
        recargaInimigo = 0
        tempoUltimoTiro = 0
        tempoUltimoTiroInimigo = 0
        tempo_invencivel = 0

        # Resetando velocidades
        velxCenario = 200
        velxObstaculo = 200
        velxInimigos = 200

        # Resetando flags de controle
        mesaMovendo = False
        gabineteMovendo = False
        droneMovendo = False
        roboMovendo = False
        invencivel = False

        # Resetar valores aleatórios se necessário
        valorAleatObstaculo = 0
        valorAleatInimigo = 0


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
        jogadorMenu.draw()
        jogadorMenu.update()
        botaoP.draw()
        botaoL.draw()
        botaoE.draw()

    janela.update()