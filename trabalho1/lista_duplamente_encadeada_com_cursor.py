from __future__ import annotations
from elemento import Elemento


class ListaDuplamenteEncadeadaComCursor:
    def __init__(self, tamanho_lista: int = float('inf')):
        """
        Inicializa uma lista duplamente encadeada com cursor.

        Args:
            tamanho_lista (int, opcional): O tamanho máximo da lista. Padrão é infinito.
        """
        self.__qt_elementos_na_lista = 0
        self.__tamanho_lista = tamanho_lista
        self.__primeiro_elemento = None
        self.__ultimo_elemento = None
        self.__posicao_cursor = None

    def acessar_atual(self) -> Elemento|None:
        """
        Acessa o elemento atual na posição do cursor.

        Returns:
            Elemento|None: O elemento atual ou None se a lista estiver vazia.
        """
        return self.__posicao_cursor

    def inserir_antes_do_atual(self, valor_elemento: int|float|str) -> None:
        """
        Insere um novo elemento antes do elemento na posição do cursor.

        Args:
            valor_elemento (int|float|str): O valor do novo elemento a ser inserido.
        """
        if self.__qt_elementos_na_lista < self.__tamanho_lista:
            elemento = Elemento(valor_elemento)
            if self.__qt_elementos_na_lista == 0:
                self.__primeiro_elemento = elemento
                self.__ultimo_elemento = elemento
                self.__posicao_cursor = elemento
            else:
                elemento.proximo_elemento = self.__posicao_cursor
                elemento.elemento_anterior = self.__posicao_cursor.elemento_anterior if \
                    self.__posicao_cursor != self.__primeiro_elemento else None
                self.__posicao_cursor.elemento_anterior = elemento
                if elemento.elemento_anterior is None:
                    self.__primeiro_elemento = elemento
                else:
                    elemento.elemento_anterior.proximo_elemento = elemento
            self.__qt_elementos_na_lista += 1

    def inserir_depois_do_atual(self, valor_elemento: int|float|str) -> None:
        """
        Insere um novo elemento depois do elemento atual na posição do cursor.

        Args:
            valor_elemento (int|float|str): O valor do novo elemento a ser inserido.
        """
        if self.__qt_elementos_na_lista < self.__tamanho_lista:
            elemento = Elemento(valor_elemento)
            if self.__qt_elementos_na_lista == 0:
                self.__primeiro_elemento = elemento
                self.__ultimo_elemento = elemento
                self.__posicao_cursor = elemento
            else:
                elemento.proximo_elemento = self.__posicao_cursor.proximo_elemento if \
                    self.__posicao_cursor != self.__ultimo_elemento else None
                elemento.elemento_anterior = self.__posicao_cursor
                self.__posicao_cursor.proximo_elemento = elemento
                if elemento.proximo_elemento is None:
                    self.__ultimo_elemento = elemento
                else:
                    elemento.proximo_elemento.elemento_anterior = elemento
            self.__qt_elementos_na_lista += 1

    def inserir_como_ultimo(self, valor_elemento: int|float|str) -> None:
        """
        Insere um novo elemento após o ultimo elemento na lista.

        Args:
            valor_elemento (int|float|str): O valor do novo elemento a ser inserido.
        """
        if self.__qt_elementos_na_lista < self.__tamanho_lista:
            elemento = Elemento(valor_elemento)
            if self.__qt_elementos_na_lista == 0:
                self.__primeiro_elemento = elemento
                self.__posicao_cursor = elemento
            else:
                elemento.elemento_anterior = self.__ultimo_elemento
                self.__ultimo_elemento.proximo_elemento = elemento
            self.__qt_elementos_na_lista += 1
            self.__ultimo_elemento = elemento

    def inserir_como_primeiro(self, valor_elemento: int|float|str) -> None:
        """
        Insere um novo elemento antes do primeiro elemento da lista.

        Args:
            valor_elemento (int|float|str): O valor do novo elemento a ser inserido.
        """
        if self.__qt_elementos_na_lista < self.__tamanho_lista:
            elemento = Elemento(valor_elemento)
            if self.__qt_elementos_na_lista == 0:
                self.__ultimo_elemento = elemento
                self.__posicao_cursor = elemento
            else:
                elemento.proximo_elemento = self.__primeiro_elemento
                self.__primeiro_elemento.elemento_anterior = elemento
            self.__qt_elementos_na_lista += 1
            self.__primeiro_elemento = elemento

    def inserir_na_posicao(self,
                           qt_posicoes_ha_avancar: int,
                           valor_elemento: int|float|str) -> None:
        """
        Insere um novo elemento em uma determinada posição.

        Args:
            qt_posicoes_ha_avancar (int): A posição onde o novo elemento será inserido.
            valor_elemento (int|float|str): O valor do novo elemento a ser inserido.
        """

        if self.__qt_elementos_na_lista < self.__tamanho_lista:
            elemento = Elemento(valor_elemento)
            if self.__qt_elementos_na_lista == 0:
                self.__ultimo_elemento = elemento
                self.__posicao_cursor = elemento
                self.__primeiro_elemento = elemento
            else:
                self.__avanca_cursor(qt_posicoes_ha_avancar)
                elemento.proximo_elemento = self.__posicao_cursor.proximo_elemento
                elemento.elemento_anterior = self.__posicao_cursor
                self.__posicao_cursor.proximo_elemento = elemento
                if elemento.proximo_elemento is not None:
                    elemento.proximo_elemento.elemento_anterior = elemento
                self.__ultimo_elemento = elemento if \
                    self.__posicao_cursor == self.__ultimo_elemento else self.__ultimo_elemento
            self.__qt_elementos_na_lista += 1

    def excluir_unico_elemento(self) -> None:
        """
        Remove o único elemento da lista.
        """
        if self.__qt_elementos_na_lista == 1:
            self.__primeiro_elemento = None
            self.__ultimo_elemento = None
            self.__posicao_cursor = None
            self.__qt_elementos_na_lista = 0

    def excluir_primeiro_elemento(self) -> None:
        """
        Remove o primeiro elemento da lista.
        """
        if self.__qt_elementos_na_lista:
            self.__posicao_cursor = self.__primeiro_elemento.proximo_elemento if self.__posicao_cursor == self.__primeiro_elemento else self.__posicao_cursor
            self.__primeiro_elemento = self.__primeiro_elemento.proximo_elemento
            self.__primeiro_elemento.elemento_anterior = None
            self.__qt_elementos_na_lista -= 1

    def excluir_ultimo_elemento(self) -> None:
        """
        Remove o último elemento da lista.
        """
        if self.__qt_elementos_na_lista:
            self.__posicao_cursor = self.__ultimo_elemento.elemento_anterior if self.__posicao_cursor == self.__ultimo_elemento else self.__posicao_cursor
            self.__ultimo_elemento = self.__ultimo_elemento.elemento_anterior
            self.__ultimo_elemento.proximo_elemento = None
            self.__qt_elementos_na_lista -= 1

    def excluir_atual(self) -> None:
        """
        Remove o elemento atual na posição do cursor.
        """
        if self.__qt_elementos_na_lista:
            if self.__qt_elementos_na_lista == 1:
                self.excluir_unico_elemento()
                return
            if self.__posicao_cursor == self.__primeiro_elemento:
                self.excluir_primeiro_elemento()
                self.__posicao_cursor = self.__primeiro_elemento
                return
            if self.__posicao_cursor == self.__ultimo_elemento:
                self.excluir_ultimo_elemento()
                self.__posicao_cursor = self.__ultimo_elemento
                return
            self.__posicao_cursor.proximo_elemento.elemento_anterior = \
            self.__posicao_cursor.elemento_anterior
            self.__posicao_cursor = self.__posicao_cursor.elemento_anterior
            self.__posicao_cursor.proximo_elemento = \
            self.__posicao_cursor.proximo_elemento.proximo_elemento
            self.__qt_elementos_na_lista -= 1

    def excluir_da_posicao(self, posicao: int) -> None:
        """
        Remove o elemento na posição recebida como parâmetro.

        Args:
            posicao (int): A posição do elemento a ser removido.
        """
        if self.__qt_elementos_na_lista and self.__qt_elementos_na_lista <= posicao:
            self.__avanca_cursor(posicao, True)
            self.excluir_atual()

    def excluir_elemento(self, valor_elemento: int|float|str) -> None:
        """
        Remove o elemento que possui o valor igual ao recebido como parâmetro.

        Args:
            valor_elemento (int|float|str): O valor do elemento a ser removido.
        """
        if self.__qt_elementos_na_lista and self.busca_elemento(valor_elemento):
            self.excluir_atual()

    def busca_elemento(self, valor_elemento: int|float|str) -> bool:
        """
        Procura o elemento que possui valor igual ao recebido como parâmetro.

        Args:
            valor_elemento (int|float|str): O valor do elemento a ser procurado.

        Returns:
            bool: True se o elemento foi encontrado, False caso contrário.
        """
        if self.__qt_elementos_na_lista:
            self.__posicao_cursor = self.__primeiro_elemento
            while True:
                if self.__posicao_cursor.valor == valor_elemento:
                    return True
                if self.__posicao_cursor == self.__ultimo_elemento:
                    return False
                self.__posicao_cursor = self.__posicao_cursor.proximo_elemento

    def __avanca_cursor(self, qt_posicoes_ha_avancar: int, vai_pro_inicio: bool = False) -> None:
        """
        Avança o cursor para a posição desejada.

        Args:
            qt_posicoes_ha_avancar (int): A quantidade de posições a serem avançadas.
            vai_pro_inicio (bool, opcional): Se True, o cursor começa a avançar\
                a partir do primeiro elemento.
        """
        if self.__qt_elementos_na_lista:
            self.__posicao_cursor = self.__primeiro_elemento if \
                vai_pro_inicio else self.__posicao_cursor
            for posicao in range(qt_posicoes_ha_avancar):
                if self.__posicao_cursor == self.__ultimo_elemento:
                    break
                self.__posicao_cursor = self.__posicao_cursor.proximo_elemento

    def __retrocede_cursor(self, qt_posicoes_ha_retroceder: int,  vai_pro_final: bool = False) -> None:
        """
        Retrocede o cursor para a posição desejada.

        Args:
            qt_posicoes_ha_retroceder (int): A quantidade de posições a serem retrocedidas.
            vai_pro_inicio (bool, opcional): Se True, o cursor começa a retroceder\
                a partir do ultimo elemento.
        """
        if self.__qt_elementos_na_lista:
            self.__posicao_cursor = self.__ultimo_elemento if \
                vai_pro_final else self.__posicao_cursor
            for posicao in range(qt_posicoes_ha_retroceder):
                if self.__posicao_cursor == self.__primeiro_elemento:
                    break
                self.__posicao_cursor = self.__posicao_cursor.elemento_anterior

    def ir_para_primeiro(self) -> None:
        """
        Move o cursor para o primeiro elemento da lista.
        """
        if self.__qt_elementos_na_lista:
            self.__posicao_cursor = self.__primeiro_elemento

    def ir_para_ultimo(self) -> None:
        """
        Move o cursor para o último elemento da lista.
        """
        if self.__qt_elementos_na_lista:
            self.__posicao_cursor = self.__ultimo_elemento

    def esta_cheia(self) -> bool:
        """
        Verifica se a lista está cheia.

        Returns:
            bool: True se a lista estiver cheia, False caso contrário.
        """
        return self.__qt_elementos_na_lista == self.__tamanho_lista

    def esta_vazia(self) -> bool:
        """
        Verifica se a lista está vazia.

        Returns:
            bool: True se a lista estiver vazia, False caso contrário.
        """
        return self.__qt_elementos_na_lista == 0

    def pega_posicao_elemento(self, valor_elemento: int|float|str) -> int|None:
        """
        Retorna a posição de um elemento na lista.

        Args:
            valor_elemento (int|float|str): O valor do elemento a ser buscado.

        Returns:
            int|None: A posição do elemento na lista ou None se não encontrado.
        """
        if self.__qt_elementos_na_lista:
            self.__posicao_cursor = self.__primeiro_elemento
            for posicao in range(self.__qt_elementos_na_lista):
                if self.__posicao_cursor.valor == valor_elemento:
                    return posicao + 1
                self.__posicao_cursor = self.__posicao_cursor.proximo_elemento
            return None

if __name__ == "__main__":
    a = ListaDuplamenteEncadeadaComCursor(5)
    a.inserir_como_primeiro(1)
    a.inserir_como_primeiro(2)
    a.inserir_como_primeiro(3)
    a.inserir_como_primeiro(4)
    print(a.busca_elemento(4))
    a.inserir_como_ultimo(5)
    print(a.pega_posicao_elemento(3))
    a.excluir_primeiro_elemento()
    a.excluir_ultimo_elemento()
    a.excluir_elemento(3)
