class Triangulo:
    def __init__(self, base, altura) -> None:
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) /2
