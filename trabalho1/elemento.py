from __future__ import annotations


class Elemento:
    def __init__(self, valor: int|str|float,
                 proximo_elemento: Elemento = None,
                 elemento_anterior: Elemento = None):
        self.__valor = valor
        self.__elemento_anterior = elemento_anterior
        self.__proximo_elemento = proximo_elemento

    @property
    def valor(self) -> int|str|float:
        """
        método que retorna o valor do elemento

        Returns:
            valor (int|str|float): valor atual do elemento
        """
        return self.__valor

    @valor.setter
    def valor(self, novo_valor: int|str|float) -> None:
        """
        método que atualiza o valor do elemento

        Parameters:
            novo_valor ( int|str|float): novo valor do elemento
        """
        self.__valor = novo_valor

    @property
    def elemento_anterior(self) -> Elemento|None:
        """
        método que retorna o elemento anterior na lista

        Returns:
            elemento anterior (Elemento|None): elemento anterior na lista
        """
        return self.__elemento_anterior

    @elemento_anterior.setter
    def elemento_anterior(self, novo_elemento_anterior: Elemento|None) -> None:
        """
        método que atualiza o elemento anterior

        Parameters:
            novo elemento anterior (Elemento|None): novo elemento anterior na lista
        """
        self.__elemento_anterior = novo_elemento_anterior

    @property
    def proximo_elemento(self) -> Elemento|None:
        """
        método que retorna o próximo elemento na lista

        Returns:
            próximo elemento (Elemento|None): próximo elemento na lista
        """
        return self.__proximo_elemento

    @proximo_elemento.setter
    def proximo_elemento(self, novo_proximo_elemento: Elemento|None) -> None:
        """
        método que atualiza o próximo elemento na lista

        Parameters:
            novo proximo elemento (Elemento|None): novo próximo elemento na lista
        """
        self.__proximo_elemento = novo_proximo_elemento
