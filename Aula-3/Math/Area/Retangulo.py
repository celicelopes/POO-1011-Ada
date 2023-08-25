class Retangulo:
    def __init__(self,ladoa, ladob) -> None:
        self.ladoa = ladoa
        self.ladob = ladob

    def area(self) -> float:
        return (self.ladoa * self.ladob)
