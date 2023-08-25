import Veiculos

class Carro(Veiculos.Veiculo):
    def __init__(self, marca: str, modelo: str, portas: int) -> None:
        super().__init__(marca, modelo)
        self.__portas = portas

    @property
    def portas(self):
        return self.__portas

    @portas.setter
    def portas(self, portas):
        self.__portas = portas

    def __str__(self) -> str:
        return f"Carro - {super().__str__()}, Portas: {self.portas}"
