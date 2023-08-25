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

    def calcula_mmc(self, num2):
        if self.numerador > num2:
            maior = self.numerador
        else:
            maior = num2
        while True:
            if maior % self.numerador == 0 and maior % num2 == 0:
                return maior
            else:
                maior += 1
                
    def calcula_numerador(mmc, denominador, numerador):
        return (mmc / denominador) * numerador

    def soma(self, fracao):
        if self.denominador == fracao.denominador:
            soma = self.numerador + fracao.numerador
            return Fracao(soma,fracao.denominador)
        else:
            return Fracao((self.numerador*fracao.denominador) + (self.denominador*fracao.numerador),(self.denominador* fracao.denominador))
    
    def subtracao(self, fracao):
        if self.denominador == fracao.denominador:
            subtracao = self.numerador - fracao.numerador
            return Fracao(subtracao,fracao.denominador)
        else:
            return Fracao(((self.numerador*fracao.denominador) - (self.denominador*fracao.numerador)),(self.denominador* fracao.denominador))
    
    def multiplicacao(self, fracao):
        return Fracao((self.numerador * fracao.numerador),(self.denominador * fracao.denominador))
    
    def divisao(self, fracao):
        return Fracao((self.numerador * fracao.denominador),(self.denominador * fracao.numerador))

    @property
    def visualizar(self):
        return f"{self.numerador}/{self.denominador}"
