class Fracao:

    __numerador = None
    __denominador = None

    def __init__(self, numerador: int, denominador: int):
        self.numerador = numerador
        self.denominador = denominador

    @property
    def denominador(self):
        return self.__denominador

    @denominador.setter
    def denominador(self, denominador):
        if denominador == 0:
            raise ValueError('Denominador nao pode ser zero!')
        else:
            self.__denominador = denominador

    @property
    def numerador(self):
        return self.__numerador

    @numerador.setter
    def numerador(self, numerador):
        self.__numerador = numerador

    def __add__(self, fracao):
        if self.denominador == fracao.denominador:
            soma = self.numerador + fracao.numerador
            return Fracao(soma,fracao.denominador)
        else:
            return Fracao((self.numerador*fracao.denominador) + (self.denominador*fracao.numerador),(self.denominador* fracao.denominador))
    
    def __sub__(self, fracao):
        if self.denominador == fracao.denominador:
            subtracao = self.numerador - fracao.numerador
            return Fracao(subtracao,fracao.denominador)
        else:
            return Fracao(((self.numerador*fracao.denominador) - (self.denominador*fracao.numerador)),(self.denominador* fracao.denominador))
    
    def __mul__(self, fracao):
        return Fracao((self.numerador * fracao.numerador),(self.denominador * fracao.denominador))
    
    def __truediv__(self, fracao):
        return Fracao((self.numerador * fracao.denominador),(self.denominador * fracao.numerador))

    @property
    def visualizar(self):
        return f"{self.numerador}/{self.denominador}"

    def __gt__(self, outro):
        return self.__numerador > outro.__denominador

    def __ge__(self, outro):
        return self.__numerador >= outro.__denominador

    def __lt__(self, outro):
        return self.__numerador < outro.__denominador

    def __le__(self, outro):
        return self.__numerador <= outro.__denominador

    def __eq__(self, outro):
        return self.__numerador == outro.__denominador

    def __ne__(self, outro):
        return self.__numerador != outro.__denominador
