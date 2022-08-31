from datetime import datetime


class Pessoa:

    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento
        if data_nascimento > datetime.now():
            raise ValueError('Data nascimento não pode ser futura')

    def idade(self):
        return (datetime.now() - self.data_nascimento).days/365

    def __str__(self) -> str:
        return f'{self.nome} ({self.idade():.1f} anos)'

    # def __len__(self):
    #     return len(self.nome)


p = Pessoa('Guionardo', datetime(1977, 2, 5))
print(p)
print(p.idade())
print(len(p))
