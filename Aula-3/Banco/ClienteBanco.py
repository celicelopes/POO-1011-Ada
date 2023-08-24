class Cliente:
    def __init__(self, nome = str, sobrenome = str, cpf = int):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__conta = str
        
    def __str__(self) -> str:
        return f"{self.__nome} {self.__sobrenome} - CPF: {self.__cpf} - Banco: {self.__conta}"
    
    def linkar_conta(self, conta):
        self.__conta = conta
        return conta
    