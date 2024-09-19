class Elemento():
    def __init__(self, valor, proximo_elemento):
        self.__valor = valor
        self.__proximo_elemento = proximo_elemento

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, novo_valor):
        self.__valor = novo_valor

    @property
    def proximo_elemento(self):
        return self.__proximo_elemento

    @proximo_elemento.setter
    def proximo_elemento(self, proximo_elemento):
        self.__proximo_elemento = proximo_elemento

class Lista():
    def __init__(self, tamanho):
        self.__primeiro_elemento = None
        self.__ultimo_elemento  = None
        self.__penultimo_elemento = None

    def inserir_frente(self, elemento):
        elemento = Elemento(elemento, None)
        if self.__primeiro_elemento is None:
            self.__primeiro_elemento = elemento
        else:
            elemento.proximo_elemento(self.__primeiro_elemento)
        self.__primeiro_elemento = elemento

    def inserir_ultimo(self, elemento):
        elemento = Elemento(elemento, None)
        if self.__primeiro_elemento is None:
            self.__primeiro_elemento = elemento
            self.__ultimo_elemento = elemento
        else:
            self.__penultimo_elemento = self.__ultimo_elemento
            self.__ultimo_elemento = elemento
            self.__ultimo_elemento.proximo_elemento(None)

    def remover_primeiro(self):
        if self.__primeiro_elemento is not None:
            primeiro_elemento = self.__primeiro_elemento
            self.__primeiro_elemento.proximo_elemento(None)
            self.__primeiro_elemento = primeiro_elemento

    def remover_ultimo(self):
        if self.__ultimo_elemento is not None:
            self.__penultimo_elemento.proximo_elemento(None)
            self.__ultimo_elemento = self.__penultimo_elemento
