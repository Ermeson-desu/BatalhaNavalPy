import keyboard
from Funcoes import *
from Navio import *

campo = [['~'for j in range(11)] for i in range(11)]

navio12 = Navio()
navio13 = Navio()
navio14 = Navio() 
navio15 = Navio()

navio21 = Navio()
navio22 = Navio()
navio23 = Navio()
navio24 = Navio()
navio25 = Navio()

def cabecalho():
    print(" -------------------------------")
    print("|         BATALHA NAVAL         |")
    print(" -------------------------------\n")
    
def tela_inicial():
    while True:
        cabecalho()
        play:str ="     Pressione espaço\n\n\n"
        print("\n\n            >1-Play\n\n\n")
        print(play)
        evento = keyboard.read_event()
        if evento.name == "space":
            break

def tabela():
    Letras_coordenadas(campo)
    numeros_coordenadas(campo)
    for linha in campo:
        print("  ".join(linha))   


def nome_jogador1()->str:
    clear()
    cabecalho()
    nome = input("Nome do jogador 1: ")
    return nome
    

def nome_jogador2()->str:
    clear()
    cabecalho()
    nome = input("Nome do jogador 2: ")
    return nome

def renderizar():
    menu_inicial()
    escolher_local_navio()

def menu_inicial():
    render_telainicial()
    nome_jogador1()
    nome_jogador2()

def render_telainicial():
    clear()
    tela_inicial()

def escolher_local_navio():
    print("Digite as coordenadas de onde vai ficar seus navios.")
    while True:
        try:
            entrada_usuario = input("Digite números separado por [, ] vírgulas ex.: [a,1] : ")
            coordenadas = entrada_usuario.split(",")
            x = int(coordenadas[1])
            y = 3
            i = 0
            while i < 11:
                num_vefica = ord("A") + i

                if coordenadas[0].upper() == chr(num_vefica):
                    y = num_vefica - (num_vefica - (i+1))
                    break
                i += 1 
            navio11 = Navio(y,x)
            break
        except:
            print("Valor inválido, por favor, digite somente números.")
    navio11.criar(campo,"VERTICAL")
    print()
    tabela()


