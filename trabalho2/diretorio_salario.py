from elemento import Elemento

class DiretorioSalario:
    def __init__(self):
        self.__diretorio = {}

    def adiciona_dado(self, salario: float, id_pessoa: int):
        try:
            elemento = Elemento(int(id_pessoa))
        except ValueError:
            return None
        if salario in self.__diretorio.keys():
            elemento.proximo_elemento = self.__diretorio[salario]
        self.__diretorio[salario] = elemento

    def busca(self, salario: float):
        if salario in self.__diretorio.keys():
            elemento = self.__diretorio[salario]
            ids = []
            while elemento.proximo_elemento is not None:
                ids.append(elemento.id_pessoa)
                elemento = elemento.proximo_elemento
            return ids
        return None

    def busca_por_id(self, salario: float, id_pessoa: int):
        if salario in self.__diretorio.keys():
            elemento = self.__diretorio[salario]
            while elemento.proximo_elemento is not None:
                if elemento.id_pessoa == id_pessoa:
                    return elemento
                elemento = elemento.proximo_elemento
        return False

    def remove(self, salario: float, id_pessoa: int):
        if salario in self.__diretorio.keys() and self.__diretorio[salario]:
            elemento = self.__diretorio[salario]
            if elemento.id_pessoa == id_pessoa:
                self.__diretorio[salario] = elemento.proximo_elemento
                return True
            while elemento.proximo_elemento is not None:
                if elemento.proximo_elemento.id_pessoa == id_pessoa:
                    if elemento.proximo_elemento.proximo_elemento is not None:
                        elemento.proximo_elemento = elemento.proximo_elemento.proximo_elemento
                    else:
                        elemento.proximo_elemento = None
                    return True
                elemento = elemento.proximo_elemento

        return False
