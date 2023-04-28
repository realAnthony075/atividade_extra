
import pessoa
class Cliente(pessoa.pessoa):




    def __init__ (self, cnpj, cli_limite_cred):
        super().__init__(pessoa.nome, pessoa.cpf, pessoa.idade)

        @property
        def cnpj(self):
            return self.__cnpj

        @cnpj.setter
        def cnpj(self, cnpj):
            if cnpj == '':
                raise ValueError('CNPJ inválido')
            self.__cnpj = cnpj.upper()

        @property
        def cli_limite_cred(self):
            return self.__cli_limite_cred

        @cli_limite_cred.setter
        def cli_limite_cred(self, cli_limite_cred):
            if cli_limite_cred == '':
                 raise ValueError('Limite de crédito inválido')
            self.__cli_limite_cred = cli_limite_cred.upper()





