from __future__ import annotations
import json
from model.pessoa import Pessoa


class Tabela:
    def __init__(self):
        self.__tabela = self._abre_tabela()
        self.__id_atual = len(self.__tabela.keys()) + 1

    def adiciona_dado(self,
                      nome: str,
                      matricula: int,
                      curso: str,
                      cidade_origem: str,
                      time: str,
                      salario: float):

        if str(self.__id_atual) not in self.__tabela.keys():
            pessoa = Pessoa(nome, int(matricula), curso,
                                cidade_origem, time, float(salario))
            if pessoa is None: return ValueError("Erro ao instanciar pessoa, um dos valores não é do tipo esperado")
            self.__tabela[self.__id_atual] = pessoa
            self._salva_tabela(self.__tabela)

        self.__id_atual += 1

    def busca_elemento(self,
                       identificador: str | list,
                       valor: str | int | float | list,
                       qt_elementos_ha_buscar: int = 1):
        elementos = []

        if not self.__tabela:
            print("A tabela está vazia!")
            return

        if isinstance(valor, str):
            valor = valor.upper()

        for indice, elemento in self.__tabela.items():
            if getattr(elemento, identificador) == valor:
                if qt_elementos_ha_buscar == 1:
                    return elemento, indice
                if len(elementos) < qt_elementos_ha_buscar:
                    elementos.append([indice, elemento])
                else:
                    break

    def remover_elemento(self,
                         identificador: str = None,
                         valor: str | int | float = None,
                         id_elemento: int = None):

        if not id_elemento and identificador is not None and valor is not None:
            _, indice = self.busca_elemento(identificador, valor)
            self.__tabela.pop(indice, None)
            self._salva_tabela(self.__tabela)
        elif id_elemento is not None:
            self.__tabela.pop(str(id_elemento), None)
            self._salva_tabela(self.__tabela)
        else:
            print("Critérios de busca inválidos!")
            return None

    def _abre_tabela(self) -> dict:
        try:
            with open('/home/pedro/Documentos/codigos/aulaEstruturaDados/trabalho2/model/tabela.json',
                      'r', encoding="UTF-8") as file:
                data = json.load(file)
                return {indice: Pessoa.faz_instancia(pessoa) for indice, pessoa in data.items()}
        except json.decoder.JSONDecodeError:
            return {}
        except BaseException as erro:
            print(f"Erro ao abrir a tabela: {erro}")
            return None

    def _salva_tabela(self, tabela: dict) -> None:
        try:
            with open('/home/pedro/Documentos/codigos/aulaEstruturaDados/trabalho2/model/tabela.json',
                      'w', encoding="UTF-8") as file:
                json.dump({indice: pessoa.faz_dicionario()
                          for indice, pessoa in tabela.items()}, file, indent=4)
        except BaseException as erro:
            print(f"Erro ao salvar a tabela: {erro}")

    @property
    def tabela(self):
        return self.__tabela

    @property
    def id_atual(self):
        return self.__id_atual


a = Tabela()
a.busca_elemento('nome', 'pedro')
