class Endereco:

    def __init__(self, cep, logradouro, numero,  cidade, uf, complemento='', bairro=''):
        self.cep = cep
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf


class Pessoa:

    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco


class PessoaFisica(Pessoa):

    def __init__(self, nome, endereco, cpf):
        self.cpf = cpf
        super().__init__(nome, endereco)

    def __str__(self) -> str:
        return f'Pessoa: {self.nome} ({self.cpf})'

    def __repr__(self) -> str:
        return f'PessoaFisica("{self.nome}",None,"{self.cpf}")'

    def __eq__(self, o: object) -> bool:
        if self.__class__ != o.__class__:
            return False
        return (self.nome == o.nome) and (self.cpf == o.cpf)


class Email(str):

    def __init__(self, email):
        self._email = email
        self._validate()

    def _validate(self):
        if '@' in self._email:
            return True
        raise ValueError('Email inválido', self._email)

    def __eq__(self, __x: object) -> bool:
        if isinstance(__x, str):
            return self._email == __x
        if self.__class__ == __x.__class__:
            return self._email == __x._email
        raise ValueError('Impossível comparar', self.__class__, __x.__class__)


endereco = Endereco('89010000', 'R 7', '1234', 'Blumenau', 'SC')


# p = PessoaFisica('Guionardo', endereco, '99999999999')
# print(id(p))
# p2 = PessoaFisica('Guionardo', None, '99999999999')
# print(id(p2))

# print(p == p2)
# print(p == 10)

email = Email('guionardo@gmail.com')

print(email == 'guionardo@gmail.com')
email2 = Email('guionardo')
