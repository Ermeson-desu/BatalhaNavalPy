class ErroDeTamanhoDoNavio(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem
        super().__init__(mensagem)