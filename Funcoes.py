import os
from Menu import *
# limpa o console
def clear():
    os.system('cls')


def Letras_coordenadas(campo:list):
    char = 'A'
    x = 1
    y = 0
    campo[0][0] = "  "
    while x < 11:
        campo[y][x] = f"{char}"
        char = chr(ord(char) + 1)
        x += 1


def numeros_coordenadas(campo:list):
    x = 0
    y = 0
    i = 1
    while y < 10:
        y +=1
        if y ==10:
            campo[y][x] = f"{i}"
        else:    
            campo[y][x] = f" {i}"
        i+=1

def renderizar(campo):
    clear()
    menu_inicial()
    # Letras_coordenadas(campo)
    # numeros_coordenadas(campo)
    # for linha in campo:
    #     print("  ".join(linha))   
          