class pessoa:
    def __init__(self, nome, cpf, idade):
        self.__nome = nome
        self.__cpf = cpf
        self.__idade = idade

        @property
        def nome(self):
            return self.__nome

        @nome.setter
        def nome(self, nome):
            if nome == '':
                raise ValueError('Nome inválido')
            self.__nome = nome.upper()

        @property
        def cpf(self):
            return self.__cpf

        @cpf.setter
        def cpf(self, cpf):
            if cpf == '':
                raise ValueError('CPF inválido')
            self.__cpf = cpf.upper()

        @property
        def idade(self):
            return self.__idade

        @idade.setter
        def idade(self, idade):
            if idade == '':
                raise ValueError('Idade inválida')
            self.__idade = idade.upper()


