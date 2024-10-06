from __future__ import annotations
from elemento import Elemento


class ListaDuplamenteEncadeadaComCursor:
    def __init__(self, tamanho_lista: int = float('inf')):
        self.__qt_elementos_na_lista = 0
        self.__tamanho_lista = tamanho_lista
        self.__primeiro_elemento = None
        self.__ultimo_elemento = None
        self.__posicao_cursor = None

    def acessar_atual(self) -> Elemento|None:
        return self.__posicao_cursor

    def inserir_antes_do_atual(self, valor_elemento: int|float|str) -> None:
        if self.__qt_elementos_na_lista < self.__tamanho_lista:
            elemento = Elemento(valor_elemento)
            if self.__qt_elementos_na_lista == 0:
                self.__primeiro_elemento = elemento
                self.__ultimo_elemento = elemento
                self.__posicao_cursor = elemento
            else:
                elemento.proximo_elemento = self.__posicao_cursor
                elemento.elemento_anterior = self.__posicao_cursor.elemento_anterior if self.__posicao_cursor != self.__primeiro_elemento else None
                self.__posicao_cursor.elemento_anterior = elemento
                if elemento.elemento_anterior is None:
                    self.__primeiro_elemento = elemento
                else:
                    elemento.elemento_anterior.proximo_elemento = elemento
            self.__qt_elementos_na_lista += 1

    def inserir_depois_do_atual(self, valor_elemento: int|float|str) -> None:
        if self.__qt_elementos_na_lista < self.__tamanho_lista:
            elemento = Elemento(valor_elemento)
            if self.__qt_elementos_na_lista == 0:
                self.__primeiro_elemento = elemento
                self.__ultimo_elemento = elemento
                self.__posicao_cursor = elemento
            else:
                elemento.proximo_elemento = self.__posicao_cursor.proximo_elemento if self.__posicao_cursor != self.__ultimo_elemento else None
                elemento.elemento_anterior = self.__posicao_cursor
                self.__posicao_cursor.proximo_elemento = elemento
                if elemento.proximo_elemento is None:
                    self.__ultimo_elemento = elemento
                else:
                    elemento.proximo_elemento.elemento_anterior = elemento
            self.__qt_elementos_na_lista += 1

    def inserir_como_ultimo(self, valor_elemento: int|float|str) -> None:
        if self.__qt_elementos_na_lista < self.__tamanho_lista:
            elemento = Elemento(valor_elemento)
            if self.__qt_elementos_na_lista == 0:
                self.__primeiro_elemento = elemento
                self.__posicao_cursor = elemento
            else:
                elemento.proximo_elemento = None
                elemento.elemento_anterior = self.__ultimo_elemento
                self.__ultimo_elemento.proximo_elemento = elemento
            self.__qt_elementos_na_lista += 1
            self.__ultimo_elemento = elemento

    def inserir_como_primeiro(self, valor_elemento: int|float|str) -> None:
        if self.__qt_elementos_na_lista < self.__tamanho_lista:
            elemento = Elemento(valor_elemento)
            if self.__qt_elementos_na_lista == 0:
                self.__ultimo_elemento = elemento
                self.__posicao_cursor = elemento
            else:
                elemento.proximo_elemento = self.__primeiro_elemento
                elemento.elemento_anterior = None
                self.__primeiro_elemento.elemento_anterior = elemento
            self.__qt_elementos_na_lista += 1
            self.__primeiro_elemento = elemento

    def inserir_na_posicao(self, qt_posicoes_ha_avancar: int, valor_elemento: int|float|str) -> None:
        if self.__qt_elementos_na_lista < self.__tamanho_lista:
            elemento = Elemento(valor_elemento)
            if self.__qt_elementos_na_lista == 0:
                self.__ultimo_elemento = elemento
                self.__posicao_cursor = elemento
                self.__primeiro_elemento = elemento
            else:
                for posicao in range(qt_posicoes_ha_avancar):
                    if self.__posicao_cursor == self.__ultimo_elemento:
                        break
                    self.__posicao_cursor = self.__posicao_cursor.proximo_elemento
                elemento.proximo_elemento = self.__posicao_cursor.proximo_elemento
                elemento.elemento_anterior = self.__posicao_cursor
                self.__posicao_cursor.proximo_elemento = elemento
                if elemento.proximo_elemento is not None:
                    elemento.proximo_elemento.elemento_anterior = elemento
                self.__ultimo_elemento = elemento if self.__posicao_cursor == self.__ultimo_elemento else self.__ultimo_elemento
            self.__qt_elementos_na_lista += 1
            print(self.__primeiro_elemento, self.__ultimo_elemento, self.__posicao_cursor)

if __name__ == "__main__":
    a = ListaDuplamenteEncadeadaComCursor(5)
    a.inserir_na_posicao(5, 20)
    a.inserir_na_posicao(5, 30)
    a.inserir_na_posicao(5, 50)
    a.inserir_na_posicao(5, 70)
