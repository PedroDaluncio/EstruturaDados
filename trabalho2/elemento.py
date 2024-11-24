from __future__ import annotations

class Elemento:
    def __init__(self, id_pessoa: int):
        self.__id_pessoa = id_pessoa
        self.__proximo_elemento = None

    @property
    def id_pessoa(self):
        return self.__id_pessoa

    @property
    def proximo_elemento(self):
        return self.__proximo_elemento

    @proximo_elemento.setter
    def proximo_elemento(self, proximo_elemento: Elemento):
        self.__proximo_elemento = proximo_elemento
