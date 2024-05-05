class SuperClasse:
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return f'Valor: {self.valor}'

    def __repr__(self):
        return f'SuperClasse({self.valor})'

    def __len__(self):
        return len(str(self.valor))

    def __getitem__(self, index):
        return str(self.valor)[index]

    def __setitem__(self, index, value):
        valor_str = list(str(self.valor))
        valor_str[index] = value
        self.valor = ''.join(valor_str)

    def __delitem__(self, index):
        valor_str = list(str(self.valor))
        del valor_str[index]
        self.valor = ''.join(valor_str)

    def __iter__(self):
        return iter(str(self.valor))

    def __next__(self):
        return next(iter(str(self.valor)))

    def __contains__(self, item):
        return item in str(self.valor)

    def __call__(self):
        return f'Chamando SuperClasse com valor: {self.valor}'

    def __eq__(self, other):
        return self.valor == other.valor

    def __lt__(self, other):
        return self.valor < other.valor

    def __gt__(self, other):
        return self.valor > other.valor

    def __add__(self, other):
        return SuperClasse(self.valor + other.valor)

    def __sub__(self, other):
        return SuperClasse(self.valor - other.valor)

    def __mul__(self, other):
        return SuperClasse(self.valor * other)

    def __div__(self, other):
        return SuperClasse(self.valor / other)

    def __enter__(self):
        print('Entrando no contexto')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('Saindo do contexto')


# Testando a superclasse
if __name__ == "__main__": # __name__ is a special variable that is used to determine if a script is being run as the main program or it is being run as an imported module.
    print(f"The name of class is: {__name__}")
    super_instancia = SuperClasse(12345)

    print(str(super_instancia))  # Saída: Valor: 12345
    print(repr(super_instancia))  # Saída: SuperClasse(12345)
    print(len(super_instancia))  # Saída: 5
    print(super_instancia[2])  # Saída: 3
    super_instancia[2] = '6'
    print(super_instancia)  # Saída: Valor: 12645
    del super_instancia[1]
    print(super_instancia)  # Saída: Valor: 1645
    print(list(super_instancia))  # Saída: ['1', '6', '4', '5']
    print('1' in super_instancia)  # Saída: True
    print(super_instancia())  # Saída: Chamando SuperClasse com valor: 1645

    outra_instancia = SuperClasse(12345)
    print(super_instancia == outra_instancia)  # Saída: True
    print(super_instancia < outra_instancia)  # Saída: False
    print(super_instancia + outra_instancia)  # Saída: Valor: 164512345
    print(super_instancia - outra_instancia)  # Saída: Valor: 0
    print(super_instancia * 2)  # Saída: Valor: 16451645
    print(super_instancia / 2)  # Saída: Valor: 822.5

    with super_instancia:
        print('Executando no contexto')
