class Navio:
    def __init__(self,x:int = 1,y:int = 1,tamanho:int = 2):
        self.__x = x
        self.__y = y
        self.__tamanho = tamanho
    
    def criar_navios(self,campo:list):
        x = self.__x
        y = self.__y
        i = 0
        while i < self.__tamanho:
            campo[y][x] = "▄"
            y+=1 
            i+=1
    