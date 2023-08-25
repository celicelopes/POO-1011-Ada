class Veiculo:
    def __init__(self, marca:str, modelo: str,) -> None:
        self.__marca = marca
        self.__modelo = modelo

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    def __str__(self) -> str:
        return f"Marca: {self.marca}, Modelo: {self.modelo}"
