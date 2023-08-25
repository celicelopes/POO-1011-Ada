class Cliente:
    __cpf = str

    def __init__(self, nome = str, sobrenome = str, cpf = str):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = self.set_cpf(cpf)
        self.__conta = []
        
    def __str__(self) -> str:
        return f"{self.__nome} {self.__sobrenome} - CPF: {self.__cpf} - Banco: {self.__conta}"

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def set_cpf(self, cpf):
        if self.validadorCPF(cpf):
            return cpf
        else:
            raise ValueError('CPF Invavlido!')
    
    def linkar_conta(self, conta):
        self.__conta = conta
        return conta
    
    def validadorCPF(self,cpf):
        cont = 0
        fixa = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        n_cpf = []
        for x in cpf:
            if x.isnumeric():
                if cont < 9:
                    cont += 1
                    n_cpf.append(int(x))

        validador_n1 = list(zip(n_cpf, fixa))
        validador_n1 = [a * b for (a, b) in validador_n1]
        validador_n1 = (sum(validador_n1) * 10) % 11
        if validador_n1 == 10:
            validador_n1 = 0

        if str(validador_n1) != cpf[-2]:
            return False
        else:
            fixa = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
            n_cpf.append(validador_n1)
            validador_n2 = list(zip(n_cpf, fixa))
            validador_n2 = [a * b for (a, b) in validador_n2]
            validador_n2 = (sum(validador_n2) * 10) % 11
            if validador_n2 == 10:
                validador_n2 = 0
            if str(validador_n1) == cpf[0] or str(validador_n1) == cpf[1] or str(validador_n1) == cpf[2]:
                return False
            else:
                if str(validador_n1) + str(validador_n2) == cpf[-2:]:
                    return True
                else:
                    return False
