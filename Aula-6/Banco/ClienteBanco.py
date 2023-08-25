import collections


class Cliente:

    __lista_cliente = []

    def __init__(self, nome = str, sobrenome = str, cpf = int):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__conta = str
        Cliente.__lista_cliente.append(self)

    @classmethod
    def busca(cls, nome) -> str:
        nomes_encontrados = [cliente.__nome for cliente in cls.__lista_cliente if cliente.__nome == nome]
        return nomes_encontrados[0] if nomes_encontrados else "Nome nao encontrado"
