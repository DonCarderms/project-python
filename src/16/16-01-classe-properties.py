

class Carro:

    def __init__(self, marca, modelo, portas):
        self._marca_ = marca
        self._modelo = modelo
        self._portas = portas

    @property
    def marca(self):
        return self._marca_

    @marca.setter
    def marca(self, value:str):
        self._marca_ = value.upper()

    @property
    def modelo(self):
        return self._modelo

    def __str__(self) -> str:
        return f'Carro: {self.marca} {self.modelo}'


carro = Carro('VW', 'Golf', 4)
print(carro)


carro.marca = 'Ford'
print(carro)
