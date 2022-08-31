

class ListaInteiros(list):

    def __setitem__(self, index, item):
        if not isinstance(item, int):
            raise ValueError('Item deve ser inteiro', item)
        super().__setitem__(index, item)

    def append(self, item):
        if not isinstance(item, int):
            raise ValueError('Item deve ser inteiro', item)
        super().append(item)


l = ListaInteiros()
l.append(1)
l.append('a')
