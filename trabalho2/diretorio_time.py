from elemento import Elemento


class DiretorioSalario:
    def __init__(self):
        self.__diretorio = {}

    def adiciona_dado(self, time: str, id_pessoa: int):
        time = time.upper()
        try:
            elemento = Elemento(int(id_pessoa))
        except ValueError:
            return None
        if elemento in self.__diretorio:
            elemento.proximo_elemento = self.__diretorio[time]
        self.__diretorio[time] = elemento

    def busca(self, time: str):
        time = time.upper()
        if self.__diretorio[time]:
            elemento = self.__diretorio[time]
            ids = []
            while elemento is not None:
                ids.append(elemento.id_pessoa)
                elemento = elemento.proximo_elemento
            return ids
        return None

    def busca_por_id(self, time: str, id_pessoa: int):
        time = time.upper()
        if self.__diretorio[time]:
            elemento = self.__diretorio[time]
            while elemento is not None:
                if elemento.id_pessoa == id_pessoa:
                    return elemento
                elemento = elemento.proximo_elemento
        return False

    def remove(self, time: str, id_pessoa: int):
        time = time.upper()
        if self.__diretorio[time]:
            elemento = self.__diretorio[time]
            if elemento.id_pessoa == id_pessoa:
                self.__diretorio[time] = elemento.proximo_elemento
                return True
            while elemento is not None:
                if elemento.proximo_elemento.id_pessoa == id_pessoa:
                    if elemento.proximo_elemento.proximo_elemento is not None:
                        elemento.proximo_elemento = elemento.proximo_elemento.proximo_elemento
                    else:
                        elemento.proximo_elemento = None
                    return True
                elemento = elemento.proximo_elemento
        return False
