

class Pessoa:
    def __new__(cls, *args):
        try:
            # Desempacotando os argumentos
            nome, matricula, curso, cidade_origem, time, salario = args

            if not isinstance(nome, str) or not nome.strip():
                raise ValueError("O nome deve ser uma string válida.")
            if not isinstance(curso, str) or not curso.strip():
                raise ValueError("O curso deve ser uma string válida.")
            if not isinstance(cidade_origem, str) or not cidade_origem.strip():
                raise ValueError("A cidade_origem deve ser uma string válida.")
            if not isinstance(time, str) or not time.strip():
                raise ValueError("O time deve ser uma string válida.")
            if not isinstance(matricula, int) or matricula <= 0:
                raise ValueError(
                    "A matrícula deve ser um número inteiro positivo.")
            if not isinstance(salario, float) or salario < 0:
                raise ValueError("O salário deve ser um número não negativo.")

            return super().__new__(cls)  # Cria a instância se tudo estiver correto
        except Exception as e:
            print(f"Erro ao criar a instância: {e}")
            return False

    def __init__(self, nome: str, matricula: int, curso: str, cidade_origem: str, time: str, salario: float):
        self.__nome = nome.upper()
        self.__matricula = int(matricula)
        self.__curso = curso.upper()
        self.__cidade_origem = cidade_origem.upper()
        self.__time = time.upper()
        self.__salario = float(salario)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, nova_matricula):
        self.__matricula = nova_matricula

    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, novo_curso):
        self.__curso = novo_curso

    @property
    def cidade_origem(self):
        return self.__cidade_origem

    @cidade_origem.setter
    def cidade_origem(self, nova_cidade_origem):
        self.__cidade_origem = nova_cidade_origem

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, novo_time):
        self.__time = novo_time

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        self.__salario = novo_salario

    def faz_dicionario(self) -> dict:
        return {
            "nome": self.__nome,
            "matricula": self.__matricula,
            "curso": self.__curso,
            "cidade_origem": self.__cidade_origem,
            "time": self.__time,
            "salario": self.__salario
        }

    @classmethod
    def faz_instancia(cls, data) -> "Pessoa":
        return cls(nome=data["nome"],
                   matricula=data["matricula"],
                   curso=data["curso"],
                   cidade_origem=data["cidade_origem"],
                   time=data["time"],
                   salario=data["salario"])
