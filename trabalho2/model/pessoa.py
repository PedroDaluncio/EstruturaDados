

class Pessoa:
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
