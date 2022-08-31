from typing import Set


class Animal:

    _racas: Set[str] = set()

    @classmethod
    def quantidade_racas(cls):
        return len(cls._racas)

    def __init__(self) -> None:
        """
        Esse constructor vai ser executado cada vez que uma instância de 
        Animal ou suas classes filhas for criada.
        Neste exemplo, adicionaremos o nome da classe criada a um set da classe
        que será único para todas as instâncias.
        """
        self._racas.add(self.__class__.__name__)


class Cao(Animal):
    ...


class Gato(Animal):
    ...


print(Animal.quantidade_racas())

cao = Cao()
print(Animal.quantidade_racas())

gato = Gato()
print(Animal.quantidade_racas())

cao2 = Cao()
print(Animal.quantidade_racas())
