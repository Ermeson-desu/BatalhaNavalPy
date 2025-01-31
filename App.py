from Funcoes import *
from Navio import *
from Menu import *


navio11 = Navio()
campo = [['~'for j in range(11)] for i in range(11)]
navios_jogador1:list[Navio]=[navio11]
navios_jogador2:list[Navio]=[]
    

if __name__ == "__main__":
    

    navio11.criar(campo,"VERTICAL")
    renderizar(campo)
    