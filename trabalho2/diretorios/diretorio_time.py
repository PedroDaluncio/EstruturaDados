from model.elemento import Elemento


class DiretorioTime:
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
        try:
            if self.__diretorio[time]:
                elemento = self.__diretorio[time]
                ids = []
                while elemento is not None:
                    ids.append(elemento.id_pessoa)
                    elemento = elemento.proximo_elemento
                return ids
        except (KeyError, AttributeError):
            print("Não há elementos para o time informado")
            return None


    def busca_por_id(self, time: str, id_pessoa: int):
        time = time.upper()
        try:
            if self.__diretorio[time]:
                elemento = self.__diretorio[time]
                while elemento is not None:
                    if elemento.id_pessoa == id_pessoa:
                        return elemento
                    elemento = elemento.proximo_elemento
        except (KeyError, AttributeError):
            print("Não há elementos para o time informado")
            return None

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
