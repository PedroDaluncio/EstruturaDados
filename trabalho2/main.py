from diretorios.diretorio_cidade import DiretorioCidade
from diretorios.diretorio_salario import DiretorioSalario
from diretorios.diretorio_time import DiretorioTime
from model.tabela import Tabela


class Main:
    def __init__(self):
        self.diretorio_cidade = DiretorioCidade()
        self.diretorio_salario = DiretorioSalario()
        self.diretorio_time = DiretorioTime()
        self.tabela = Tabela()

    def adicionar_dado(self,
                      nome: str,
                      matricula: int,
                      curso: str,
                      cidade_origem: str,
                      time: str,
                      salario: float):
        self.tabela.adiciona_dado(nome, matricula, curso, cidade_origem, time, salario)
        self.diretorio_cidade.adiciona_dado(cidade_origem, self.tabela.id_atual -1)
        self.diretorio_salario.adiciona_dado(salario, self.tabela.id_atual -1)
        self.diretorio_time.adiciona_dado(time, self.tabela.id_atual -1)



"""
Operaçẽs: Adicionar dado na tabela -> precisa pegar dados, adicionar na tabela, e mandar certos dados para os diretorios
"""

a = Main()
a.adicionar_dado("nome", 123, "curso", 789, "time", 123.4)