class Fila:
    def __init__(self, tamanho_fila):
        self.__tamanho = tamanho_fila
        self.__fila = [None] * tamanho_fila
        self.__indice_entrar = 0
        self.__qt_pessoas = 0

    def entrar(self, elemento):
        if self.__qt_pessoas < self.__tamanho:
            self.__fila[self.__indice_entrar] = elemento
            self.__indice_entrar += 1
            if self.__indice_entrar == self.__tamanho:
                self.__indice_entrar = 0
            self.__qt_pessoas += 1
        print(self.__fila)

    def sair(self):
        if self.__qt_pessoas > 0:
            self.__fila[0] = None
            self.__qt_pessoas -= 1
            self.arruma_fila()
            self.__indice_entrar = self.__qt_pessoas
        print(self.__fila)

    def esta_cheia(self):
        for elemento in self.__fila:
            if elemento is None:
                return False
        return True

    def esta_vazia(self):
        for elemento in self.__fila:
            if elemento is not None:
                return False
        return True

    def arruma_fila(self):
        indice = 0
        for elemento in self.__fila[1:]:
            self.__fila[indice] = elemento
            indice += 1
        self.__fila[-1] = None
