

class ElementoComPrioridade:
    def __init__(self, valor: int, prioridade: int = 10, data_entrada: int):
        self.__valor = valor
        self.__prioridade = prioridade
        self.__data_entrada = data_entrada

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor: int):
        self.__valor = valor

    @property
    def prioridade(self):
        return self.__prioridade

    @prioridade.setter
    def prioridade(self, prioridade: int):
        self.__prioridade = prioridade

    @property
    def data_entrada(self):
        return self.__data_entrada

    @data_entrada.setter
    def data_entrada(self, data_entrada: int):
        self.__data_entrada = data_entrada

class FilaComPrioridade:
    def __init__(self, tamanho: int = 5):
        self.__qt_elementos = 0
        self.__tamanho = tamanho
        self.__primeiro_elemento = None
        self.__ultimo_elemento = None
        self.__elemento_maior_prioridade = None
        self.__maior_tempo = 0

    def inserir_elemento(self, valor_elemento, prioridade_elemento):
        if self.__qt_elementos == self.__tamanho:
            return
        elemento = ElementoComPrioridade(valor_elemento, prioridade_elemento, self.__maior_tempo)
        if self.__primeiro_elemento is None:
            self.__primeiro_elemento = elemento
            self.__ultimo_elemento = elemento
            self.__elemento_maior_prioridade = elemento
        else:
            self.__ultimo_elemento = elemento
            if elemento.prioridade > self.__elemento_maior_prioridade.prioridade:
                self.__elemento_maior_prioridade = elemento
        self.__maior_tempo += 1
        self.__qt_elementos += 1

