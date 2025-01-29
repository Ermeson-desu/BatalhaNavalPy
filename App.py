from Funcoes import *
from Navio import *

campo = [['~'for j in range(11)] for i in range(11)]

def renderizar():
    Clear()
    Letras_coordenadas(campo)
    numeros_coordenadas(campo)
    for linha in campo:
        print("  ".join(linha))   
          

if __name__ == "__main__":
    
    navio1 = Navio(5,10,3)
    navio1.criar(campo,"VERTICAL")
    renderizar()
    