import keyboard
from Funcoes import *

def cabecalho():
    print(" -------------------------------")
    print("|         BATALHA NAVAL         |")
    print(" -------------------------------\n")
    
def menu_inicial():
    while True:
        cabecalho()
        play:str ="     Pressione espaço\n\n\n"
        print("\n\n            >1-Play\n\n\n")
        print(play)
        evento = keyboard.read_event()
        if evento.name == "space":
            break

    

def nome_jogador1():
    nome = input("Nome do jogador 1: ")
    return nome
    

def nome_jogador2():
    nome = input("Nome do jogador 2: ")
    return nome

def renderizar():
    clear()
    menu_inicial()
    clear()
    cabecalho()
    nome_jogador1()

def tabela(campo):
    Letras_coordenadas(campo)
    numeros_coordenadas(campo)
    for linha in campo:
        print("  ".join(linha))   
