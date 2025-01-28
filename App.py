from Funcoes import *
from Navio import *

campo = [['~'for j in range(11)] for i in range(11)]

def renderizar():
    Clear()
    char = 'A'
    x = 1
    y = 0
    while x < 11:
        campo[y][x] = f"{char}"
        char = chr(ord(char) + 1)
        x += 1
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
        

    for linha in campo:
        print("  ".join(linha))   
          

if __name__ == "__main__":
    
    navio1 = Navio()
    navio1.criar_navios(campo)
    renderizar()
    