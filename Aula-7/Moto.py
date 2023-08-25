import Veiculos

class Moto(Veiculos.Veiculo):
    def __init__(self, marca: str, modelo: str, cilindradas: int) -> None:
        super().__init__(marca, modelo)
        self.__cilindradas = cilindradas

    @property
    def cilindradas(self):
        return self.__cilindradas

    @cilindradas.setter
    def cilindradas(self, cilindradas):
        self.__cilindradas = cilindradas

    def __str__(self) -> str:
        return f"Moto - {super().__str__()}, Cilindradas: {self.cilindradas}"
