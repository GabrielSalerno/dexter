#from PPlay.window import *

def colisaoJO(jogador,obstaculo):
    if jogador.y + jogador.height >= obstaculo.y and jogador.y + jogador.height <= obstaculo.y + 10:
        jogador.y = obstaculo.y - jogador.height
        jogadorPulando = False
        jogadorSubindo = False
        jogadorDescendo = False
                
    elif not invencivel:
        vidaJogador -= 1
        jogador.x = obstaculo.x - jogador.width
        jogador.y = obstaculo.y - jogador.height
        invencivel = True
    return jogadorPulando,jogadorSubindo,jogadorDescendo
