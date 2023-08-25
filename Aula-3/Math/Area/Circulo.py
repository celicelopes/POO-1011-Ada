from math import pi

class Circulo:
    def __init__(self, raio) -> None:
        self.raio = raio

    def area(self)-> float:
        return pi * (self.raio **2)
