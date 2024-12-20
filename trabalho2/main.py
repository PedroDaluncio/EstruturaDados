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

    def adicionar_dado(self):

        print("\n--- Adicionar Novo Registro ---")
        nome = input("Nome: ").strip()
        matricula = int(input("Matrícula: ").strip())
        curso = input("Curso: ").strip()
        cidade_origem = input("Cidade de Origem: ").strip()
        time = input("Time: ").strip()
        salario = float(input("Salário: ").strip())

        print("\nRegistro adicionado com sucesso!\n")

        self.tabela.adiciona_dado(
            nome, matricula, curso, cidade_origem, time, salario)
        self.diretorio_cidade.adiciona_dado(
            cidade_origem, self.tabela.id_atual - 1)
        self.diretorio_salario.adiciona_dado(salario, self.tabela.id_atual - 1)
        self.diretorio_time.adiciona_dado(time, self.tabela.id_atual - 1)

    def remover_elemento(self, identificador=None, valor=None, id_elemento=None):
        resultado = ''
        if not id_elemento and identificador is not None and valor is not None:
            resultado = self.tabela.remover_elemento(identificador, valor)
            if identificador == "cidade":
                self.diretorio_cidade.remove(valor, resultado)
            elif identificador == "salario":
                self.diretorio_salario.remove(valor, resultado)
            elif identificador == "time":
                self.diretorio_time.remove(valor, resultado)

        elif id_elemento is not None:
            resultado = self.tabela.remover_elemento(id_elemento=id_elemento)
            if identificador == "cidade":
                self.diretorio_cidade.remove(valor, id_elemento)
            elif identificador == "salario":
                self.diretorio_salario.remove(valor, id_elemento)
            elif identificador == "time":
                self.diretorio_time.remove(valor, id_elemento)

        print("Elemento removido com sucesso!\n") if resultado else print("")

    def carregar_dados(self):
        data = [
            {"nome": "João", "matricula": 123, "curso": "engenharia",
                "cidade_origem": "Florianópolis", "time": "avaí", "salario": 1000.0},
            {"nome": "Maria", "matricula": 456, "curso": "Direito",
                "cidade_origem": "Joinville", "time": "Joinville", "salario": 2000.0},
            {"nome": "José", "matricula": 789, "curso": "Medicina",
                "cidade_origem": "Blumenau", "time": "Chapecoense", "salario": 3000.0},
        ]
        self.tabela.carregar_dados(data)
        print("Dados carregados com sucesso!\n")

    def consulta_simples(self):
        resultado = ''
        valor = input("Valor a ser consultado: ").strip()
        if valor.upper() not in ["CIDADE", "TIME", "SALARIO"]:
            print("Não é possível consultar por esse valor.")
            return
        if valor.upper() == "CIDADE":
            cidade = input("Cidade: ").strip()
            resultado = self.diretorio_cidade.busca(cidade)
        elif valor.upper() == "TIME":
            time = input("Time: ").strip()
            resultado = self.diretorio_time.busca(time)
        elif valor.upper() == "SALARIO":
            salario = float(input("Salário: ").strip())
            resultado = self.diretorio_salario.busca(salario)
        print("Resultado da consulta: ", resultado)
        return resultado

    def buscar_elemento(self):
        id_elemento = int(input("ID do elemento: ").strip())
        resultado = self.tabela.busca_elemento(id_elemento=id_elemento)
        print("Resultado da busca: ", resultado)

    def exibir_todos(self):
        print("Todos os dados:")
        print("")
        for indice, pessoa in self.tabela.tabela.items():
            print(f"{indice}: {pessoa}")

    def consulta_composta(self):
        resultado1 = self.consulta_simples()
        resultado2 = self.consulta_simples()
        if resultado1 and resultado2:
            ids = []
            for res1, res2 in resultado1, resultado2:
                if res1 == res2:
                    ids.append(res1)
            print("Resultado da consulta composta: ", ids)

    def menu(self):
        while True:
            print()
            print("Menu:")
            print("1. Carregar dados")
            print("2. Consulta simples")
            print("3. Consulta composta")
            print("4. Incluir novo elemento")
            print("5. Buscar elemento por ID")
            print("6. Remover elemento por ID")
            print("7. Exibir todos os dados")
            print("8. Sair")
            print()

            escolha = input("Escolha uma opção: ").strip()
            print()

            if escolha == "1":
                self.carregar_dados()

            elif escolha == "2":
                self.consulta_simples()

            elif escolha == "3":
                self.consulta_composta()

            elif escolha == "4":
                self.adicionar_dado()

            elif escolha == "5":
                self.buscar_elemento()

            elif escolha == "3":
                print("Remover por:")
                print("1. Identificador e Valor")
                print("2. ID")
                subescolha = input("Escolha uma opção: ")

                if subescolha == "1":
                    identificador = input("Identificador (ex: nome, curso): ")
                    if identificador.upper() not in ["CIDADE", "TIME", "SALARIO"]:
                        print("Identificador inválido.")
                        continue
                    valor = input("Valor do identificador: ")
                    self.remover_elemento(
                        identificador=identificador, valor=valor)

                elif subescolha == "2":
                    id_elemento = input("ID do elemento: ")
                    self.remover_elemento(id_elemento=id_elemento)
                else:
                    print("Opção inválida.")

            elif escolha == "7":
                self.exibir_todos()

            elif escolha == "8":
                print("Saindo... Até logo!")
                break

            else:
                print("Opção inválida. Tente novamente!\n")

if __name__ == "__main__":
    aplicacao = Main()
    aplicacao.menu()
