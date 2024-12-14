from model.elemento import Elemento


class DiretorioCidade:
    def __init__(self):
        self.__diretorio = {}

    def adiciona_dado(self, cidade: str, id_pessoa: int):
        cidade = cidade.upper()
        try:
            elemento = Elemento(int(id_pessoa))
        except ValueError:
            return None
        if elemento in self.__diretorio:
            elemento.proximo_elemento = self.__diretorio[cidade]
        self.__diretorio[cidade] = elemento

    def busca(self, cidade: str):
        cidade = cidade.upper()
        if self.__diretorio[cidade]:
            elemento = self.__diretorio[cidade]
            ids = []
            while elemento is not None:
                ids.append(elemento.id_pessoa)
                elemento = elemento.proximo_elemento
            return ids
        return None

    def busca_por_id(self, cidade: str, id_pessoa: int):
        cidade = cidade.upper()
        try:
            if self.__diretorio[cidade]:
                elemento = self.__diretorio[cidade]
                while elemento is not None:
                    if elemento.id_pessoa == id_pessoa:
                        return elemento
                    elemento = elemento.proximo_elemento
        except (KeyError, AttributeError):
            print("Cidade não encontrada")
            return False

    def remove(self, cidade: str, id_pessoa: int):
        cidade = cidade.upper()
        try:
            if self.__diretorio[cidade]:
                elemento = self.__diretorio[cidade]
                if elemento.id_pessoa == id_pessoa:
                    self.__diretorio[cidade] = elemento.proximo_elemento
                    return True
                while elemento is not None:
                    if elemento.proximo_elemento.id_pessoa == id_pessoa:
                        if elemento.proximo_elemento.proximo_elemento is not None:
                            elemento.proximo_elemento = elemento.proximo_elemento.proximo_elemento
                        else:
                            elemento.proximo_elemento = None
                        return True
                    elemento = elemento.proximo_elemento
        except (KeyError, AttributeError):
            print("Cidade não encontrada")
            return False
