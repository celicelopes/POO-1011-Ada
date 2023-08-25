class Conta:
    def __init__(self, agencia : int, conta: int, saldo = 0):
        self.__agencia = agencia
        self.__conta = conta
        self.__saldo = saldo
        self.__cliente = str
        
    def __str__(self) -> str :
        return f"Agencia: {self.__agencia} - Conta: {self.__conta} - Saldo: {self.__saldo}"
    
    def linkar_cliente(self, cliente):
        if len(cliente.__conta) < 2:
            self.__cliente = cliente
            return cliente.linkar_conta(self)
        else:
            raise Exception('Cliente ja possui conta cadastrada')

    def deposito(self, valor):
        self.__saldo += valor
        
    def saque(self, valor):
        if 0 < valor <= self.__saldo :
            self.__saldo -= valor
            return valor
        else:
            print(f"Saldo insuficiente \n Saldo {self.__saldo}")
