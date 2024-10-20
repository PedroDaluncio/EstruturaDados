from __future__ import annotations
from elementoarvore import ElementoArvore


class ArvoreBinaria:
    def __init__(self):
        self.__raiz_principal = None
        self.__qt_elementos = 0

    def inserir_elemento(self, valor):
        if self.__raiz_principal is None:
            self.__raiz_principal = ElementoArvore(valor)
            self.__qt_elementos += 1
        else:
            self.__inserir_elemento_recursivo(valor, self.__raiz_principal)

    def __inserir_elemento_recursivo(self, valor: int|float|str, noh_arvore: ElementoArvore):
        if valor == noh_arvore.valor_elemento:
            return
        if valor < noh_arvore.valor_elemento:
            if noh_arvore.filho_esquerda is None:
                noh_arvore.filho_esquerda = ElementoArvore(valor)
                self.__qt_elementos += 1
            else:
                self.__inserir_elemento_recursivo(valor, noh_arvore.filho_esquerda)
        elif valor > noh_arvore.valor_elemento:
            if noh_arvore.filho_direita is None:
                noh_arvore.filho_direita = ElementoArvore(valor)
                self.__qt_elementos += 1
            else:
                self.__inserir_elemento_recursivo(valor, noh_arvore.filho_direita)

a = ArvoreBinaria()
a.inserir_elemento(10)
a.inserir_elemento(2)
a.inserir_elemento(3)
a.inserir_elemento(50)
a.inserir_elemento(11)
