from elemento import Elemento

class DiretorioSalario:
    def __init__(self):
        self.__diretorio = {(0, 1000): None,
                            (1000, 2000): None,
                            (2000, 3000): None,
                            (3000, 4000): None,
                            (4000, 5000): None,
                            (5000, 6000): None,
                            (6000, 7000): None,
                            (7000, 8000): None,
                            (8000, 9000): None,
                            (9000, 10000): None,
                            (10000, 11000): None,
                            (11000, 12000): None,
                            (12000, 13000): None,
                            (13000, 14000): None,
                            (14000, 15000): None,
                            (15000, 16000): None,
                            (16000, float('inf')): None}

    def _verifica_faixa(self, salario: float):
        for lim_inf, lim_sup in self.__diretorio.keys():
            if lim_inf <= salario < lim_sup:
                return (lim_inf, lim_sup)
        return None

    def adiciona_dado(self, salario: float, id_pessoa: int):
        try:
            elemento = Elemento(int(id_pessoa))
        except ValueError:
            return None
        faixa = self._verifica_faixa(salario)
        if faixa:
            elemento.proximo_elemento = self.__diretorio[faixa]
        self.__diretorio[faixa] = elemento

    def busca(self, salario: float):
        faixa = self._verifica_faixa(salario)
        if faixa:
            elemento = self.__diretorio[faixa]
            ids = []
            while elemento is not None:
                ids.append(elemento.id_pessoa)
                elemento = elemento.proximo_elemento
            return ids
        return None

    def busca_por_id(self, salario: float, id_pessoa: int):
        faixa = self._verifica_faixa(salario)
        if faixa:
            elemento = self.__diretorio[faixa]
            while elemento is not None:
                if elemento.id_pessoa == id_pessoa:
                    return elemento
                elemento = elemento.proximo_elemento
        return False

    def remove(self, salario: float, id_pessoa: int):
        faixa = self._verifica_faixa(salario)
        if faixa:
            elemento = self.__diretorio[faixa]
            if elemento.id_pessoa == id_pessoa:
                self.__diretorio[faixa] = elemento.proximo_elemento
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
