from Funcoes import *
from Navio import *
from Menu import *

campo = [['~'for j in range(11)] for i in range(11)]

if __name__ == "__main__":
    
    navio1 = Navio(10,10,4)
    navio1.criar(campo,"HORIZONTAL")
    cabecalho()
    renderizar(campo)
    