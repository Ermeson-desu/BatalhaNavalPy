from Funcoes import *
from Navio import *

campo = [['~'for j in range(11)] for i in range(11)]

if __name__ == "__main__":
    
    navio1 = Navio(5,10,5)
    navio1.criar(campo,"VERTICAL")
    renderizar(campo)
    