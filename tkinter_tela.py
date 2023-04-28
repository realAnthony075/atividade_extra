import tkinter as tk

import mysql.connector


janela = tk.Tk()

#conexao com o banco
conexao = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= 'root',
    database= 'atividade_extra')


class Interface:
    def __init__(self, conexao):
        self.conexao = conexao

        self.janela = tk.Tk()
        self.janela.title('Gerenciador de Pessoas')

        self.label_nome = tk.Label(self.janela, text='Nome:')
        self.label_nome.grid(row=0, column=0)

        self.entry_nome = tk.Entry(self.janela)
        self.entry_nome.grid(row=0, column=1)

        self.label_cpf = tk.Label(self.janela, text='CPF:')
        self.label_cpf.grid(row=1, column=0)

        self.entry_cpf = tk.Entry(self.janela)
        self.entry_cpf.grid(row=1, column=1)

        self.label_idade = tk.Label(self.janela, text='Idade:') 
        self.label_idade.grid(row=2, column=0)

        self.entry_idade = tk.Entry(self.janela)
        self.entry_idade.grid(row=2, column=1)

        self.button_inserir = tk.Button(self.janela, text='Inserir', command=self.inserir)
        self.button_inserir.grid(row=3, column=0)

        self.button_atualizar = tk.Button(self.janela, text='Atualizar', command=self.atualizar)
        self.button_atualizar.grid(row=3, column=1)

        self.button_excluir = tk.Button(self.janela, text='Excluir', command=self.excluir)
        self.button_excluir.grid(row=3, column=2)

        self.frame_resultado = tk.Frame(self.janela)
        self.frame_resultado.grid(row=4, column=0, columnspan=3)

        self.label_resultado = tk.Label(self.frame_resultado, text='Resultado:')
        self.label_resultado.grid(row=0, column=0)

        self.text_resultado = tk.Text(self.frame_resultado, height=10, width=50)
        self.text_resultado.grid(row=1, column=0)

        self.carregar_resultado()

        self.janela.mainloop()

    def carregar_resultado(self):
        resultado = self.conexao.read()
        texto = ''
        for linha in resultado:
            texto += f'{linha[0]} {linha[1]} {linha[2]}\n'
        self



