

class ElementoComPrioridade:
    def __init__(self, valor: int, data_entrada: int, prioridade: int = 10):
        self.__valor = valor
        self.__prioridade = prioridade
        self.__data_entrada = data_entrada
        self.__proximo_elemento = None

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

    @property
    def proximo_elemento(self):
        return self.__proximo_elemento

    @proximo_elemento.setter
    def proximo_elemento(self, elemento):
        self.__proximo_elemento = elemento

class FilaComPrioridade:
    def __init__(self, tamanho: int = 5):
        self.__qt_elementos = 0
        self.__tamanho = tamanho
        self.__primeiro_elemento = None
        self.__ultimo_elemento = None
        self.__maior_tempo = 0

    def inserir_elemento(self, valor_elemento, prioridade_elemento):
        if self.__qt_elementos == self.__tamanho:
            return
        elemento = ElementoComPrioridade(valor_elemento, prioridade_elemento, self.__maior_tempo)
        if self.__primeiro_elemento is None:
            self.__primeiro_elemento = elemento
            self.__ultimo_elemento = elemento
        else:
            self.__ultimo_elemento.proximo_elemento = elemento
            self.__ultimo_elemento = elemento
        self.__maior_tempo += 1
        self.__qt_elementos += 1

    def remove_elemento(self):
        if self.__primeiro_elemento is None:
            return
        if self.__primeiro_elemento == self.__ultimo_elemento:
            self.__primeiro_elemento = None
            self.__primeiro_elemento = None
            self.__qt_elementos = 0
            self.__maior_tempo = 0
        elemento_com_prioridade_maxima = self.__primeiro_elemento
        elemento_atual = self.__primeiro_elemento
        elemento_anterior = None
        for i in range(self.__qt_elementos):
            if elemento_atual.proximo_elemento.prioridade > elemento_com_prioridade_maxima.prioridade:
                elemento_com_prioridade_maxima = elemento_atual
                elemento_anterior = elemento_atual
            elif elemento_atual.proximo_elemento.prioridade == elemento_com_prioridade_maxima.prioridade:
                elemento_com_prioridade_maxima = elemento_atual if elemento_atual.data_entrada < elemento_com_prioridade_maxima.data_entrada else elemento_com_prioridade_maxima
                elemento_anterior = elemento_atual
            elemento_atual = elemento_atual.proximo_elemento
        elemento_anterior.proximo_elemento = elemento_com_prioridade_maxima.proximo_elemento
        elemento_com_prioridade_maxima.proximo_elemento = None
        
