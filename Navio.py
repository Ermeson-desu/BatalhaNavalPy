from Erros import ErroDeTamanhoDoNavio

class Navio:
    def __init__(self,x:int = 1,y:int = 1,tamanho:int = 2):
        self.__x = x
        self.__y = y
        self.__tamanho = tamanho
    

    def criar(self,campo:list,sentido:str):
        # esse try está com um bug 
        try: 
            if self.__tamanho > 4:
                raise ErroDeTamanhoDoNavio("O tamanho do navio só pode ser no máximo 4")
            elif self.__tamanho <2:
                raise ErroDeTamanhoDoNavio("O tamanho do navio não pode ser menhor que 2")
            
            self.__verificar_sentido(campo,sentido)

        except ErroDeTamanhoDoNavio as e:
            print(f"Erro no tamanho do navio: {e}")
        except ErroDeTamanhoDoNavio as f:
            print(f"Erro no tamanho do navio: {f}")


    def __criar_vertical(self, campo:list):
        x = self.__x
        y = self.__y
        tamanho_navio = 0
        while tamanho_navio < self.__tamanho:
            if self.__verificar_posicao(campo,x,y) == True:
                campo[y][x] = "▄"
                y+=1 
                tamanho_navio+=1
            else:
                print("Já existe um navio nessa posição!")
                break
            

    def __criar_horizontal(self, campo:list):
        x = self.__x
        y = self.__y
        tamanho_navio = 0
        while tamanho_navio < self.__tamanho:
            if self.__verificar_posicao(campo,x,y) == True:
                campo[y][x] = "▄"
                x+=1 
                tamanho_navio+=1
            else:
                print("Já existe um navio nessa posição!")
                break


    def __verificar_posicao(self, campo:list,x:int,y:int) ->bool:
        if campo[y][x] == "~":
            return True
        else: 
            return False
    
    # cria o navio no final da tela 
    def __verificar_cantos_horizontal(self, campo:list, x:int,y:int): 
        tamanho_navio = 0
        while tamanho_navio < self.__tamanho:
            if self.__verificar_posicao(campo,x,y) == True:
                campo[y][x] = "▄"
                x-=1 
                tamanho_navio+=1
            
    # cria o navio no final da tela 
    def __verificar_cantos_vertical(self, campo:list, x:int,y:int):
        tamanho_navio = 0
        while tamanho_navio < self.__tamanho:
            if self.__verificar_posicao(campo,x,y) == True:
                campo[y][x] = "▄"
                y-=1 
                tamanho_navio+=1
    

    def __verificar_sentido(self,campo:list,sentido:str):
        if sentido == "HORIZONTAL":

            if self.__x == 10 or (self.__x >= 8 and self.__tamanho > 2):
                self.__verificar_cantos_horizontal(campo,self.__x,self.__y)
            else:
                self.__criar_horizontal(campo)

        elif sentido == "VERTICAL":

            if self.__y == 10 or (self.__y >= 8 and self.__tamanho > 2):
                self.__verificar_cantos_vertical(campo,self.__x,self.__y)
            else:
                self.__criar_vertical(campo)


