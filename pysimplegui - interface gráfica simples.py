from typing import Dict, Any, Union

import PySimpleGUI as sg
import pandas as pd
import xlwt



# xlwt             -> ler arquivos xls
#win32com.client   -> atualização excel

# Variaveis para Tabela - Excel (listas)
from pandas import DataFrame, Series

col_nome = []
col_idade =[]
col_cpf =[]
col_gmail =[]
col_outlook =[]
col_yahoo =[]
col_aceitacartao =[]



class TelaPython:
    def __init__(self):

        #Layout
        layout = [
            [sg.Text('Nome',size=(5,0)),sg.Input(size=(15,0),key='nome'), sg.Text('CPF',size=(5,0)),sg.Input(size=(15,0),key='cpf')],
            [sg.Text('Idade',size=(5,0)),sg.Input(size=(15,0),key='idade')],
            [sg.Text('Quais provedores de e-mails são aceitos?')],
            [sg.Checkbox('Gmail',key='gmail'),sg.Checkbox('Outlook',key='outlook'),sg.Checkbox('Yahoo',key='yahoo')],
            [sg.Text('Aceita Cartão?')],
            [sg.Radio('Sim','cartões',key='aceitaCartao'),sg.Radio('Não','cartões',key='naoaceitaCartao')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30,20))]
        ]
        #Janela
        self.janela = sg.Window("Dados do Usuário.").layout(layout)



    def Iniciar (self):
        while True:
            # Extrair os dados na tela
            self.button, self.values = self.janela.Read()

            #Extraindo dados para variáveis
            nome = self.values['nome']
            cpf = self.values['cpf']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['naoaceitaCartao']

            #Add elemento a lista
            col_nome.append(self.values['nome'])
            col_idade.append(self.values['idade'])
            col_cpf.append(self.values['cpf'])
            col_gmail.append(self.values['gmail'])
            col_outlook.append(self.values['outlook'])
            col_yahoo.append(self.values['yahoo'])
            col_aceitacartao.append(self.values['aceitaCartao'])

            # Criando Tabela Excel


            dados = {'Nome': col_nome, 'Idade': col_idade, 'CPF': col_cpf, 'Gmail':col_gmail, 'Outlook': col_outlook , 'Yahoo': col_yahoo, 'Aceita Cartão': col_aceitacartao}


            #mostrando na tela
            print(f'\nNome: {nome}')
            print(f'\nCPF: {cpf}')
            print(f'Idade: {idade} anos')
            print(f'aceita Gmail: {aceita_gmail}')
            print(f'aceita Outlook: {aceita_outlook}')
            print(f'aceita Yahoo: {aceita_yahoo}')
            print(f'\nAceita cartão: {aceita_cartao}')
            print(f'Não aceita cartão: {nao_aceita_cartao}')



            try:
                tabela_ler = pd.read_csv(r'C:\Users\Guilherme\AppData\Roaming\JetBrains\PyCharmCE2020.1\scratches\arquivoTesteGui.csv', sep =';')
                tabela = pd.DataFrame(dados)
                tabela = pd.concat([tabela_ler,tabela])
                tabela.to_csv('arquivoTesteGui.csv', sep = ';', index = False)

            except:
             tabela = pd.DataFrame(dados)
             tabela.to_csv('arquivoTesteGui.csv', sep = ';', index=False)








tela = TelaPython ()

#Executar Tela
tela.Iniciar ()

