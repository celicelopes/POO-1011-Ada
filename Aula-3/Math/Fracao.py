class Fracao:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    
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
            return f"{soma}/{fracao.denominador}"
        else:
            return f"{(self.numerador*fracao.denominador) + (self.denominador*fracao.numerador)}/{self.denominador* fracao.denominador}"
    
    def subtracao(self, fracao):
        if self.denominador == fracao.denominador:
            subtracao = self.numerador - fracao.numerador
            return f"{subtracao}/{fracao.denominador}"
        else:
            return f"{(self.numerador*fracao.denominador) - (self.denominador*fracao.numerador)}/{self.denominador* fracao.denominador}"
    
    def multiplicacao(self, fracao):
        return f"{self.numerador * fracao.numerador}/{self.denominador * fracao.denominador}"
    
    def divisao(self, fracao):
        return f"{self.numerador * fracao.denominador}/{self.denominador * fracao.numerador}"
