

class ElementoArvore:
    def __init__(self, valor):
        self.__valor_elemento = valor
        self.__filho_esquerda = None
        self.__filho_direita = None

    @property
    def valor_elemento(self):
        return self.__valor_elemento

    @valor_elemento.setter
    def valor_elemento(self, valor):
        self.__valor_elemento = valor

    @property
    def filho_esquerda(self):
        return self.__filho_esquerda

    @filho_esquerda.setter
    def filho_esquerda(self, filho):
        self.__filho_esquerda = filho

    @property
    def filho_direita(self):
        return self.__filho_direita

    @filho_direita.setter
    def filho_direita(self, filho):
        self.__filho_direita = filho
