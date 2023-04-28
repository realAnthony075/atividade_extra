import mysql.connector

class conexao:

    def connection(self):
        self.conexao = mysql.connector.conect(
            host = 'localhost',
            user = 'root',
            password = 'root',
            database = 'atividade_extra'
        )
        self.cursor = self.conexao.cursor()


    def create(self, nome, cpf, idade):
        comando = f'INSERT INTO pessoa (nome, cpf, idade) VALUES ("{nome}", "{cpf}", "{idade}")'

        self.cursor.execute(comando)
        self.conexao.comit()


    def read(self):
        comando = 'SELECT * FROM pessoa'

        self.cursor.execute(comando)
        self.resultado = self.cursor.fetchall()
        print(self.resultado)

        self.cursor.close()
        self.conexao.close()

    def update(self, id, nome, cpf, idade):
        comando= f"UPDATE pessoa SET nome = '{nome}', cpf = '{cpf}', idade = '{idade}' WHERE id = {id}"

        self.cursor.execute(comando)
        self.conexao.commit()


    def delete(self, id):
        comando = f"DELETE FROM pessoa WHERE id = '{id}'"


        self.cursor.execute(comando)
        self.conexao.commit()

        self.cursor.close()
        self.conexao.close()