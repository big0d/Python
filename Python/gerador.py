from asyncio import events
from distutils.ccompiler import gen_lib_options
import random
import os
import site
import PySimpleGUI as sg


class GeradorSenha:
    def __init__(self):
        # layout interface
        sg.theme('DarkTeal')
        layout = [
            [sg.Text('Site: ', size=(12, 2)),
             sg.Input(key='site', size=(20, 1))],
            [sg.Text('Usuario/email: ', size=(12, 2)),
             sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Quantidade de caracteres'), sg.Combo(values=list(
                range(30)), key='totalcaracteres', default_value=1, size=(3, 1))],
            [sg.Output(size=(33, 5))],
            [sg.Button('Iniciar procedimento de geração')]
        ]
        # janela
        self.janela = sg.Window('Gerador de senha', layout)

    def Iniciar(self):
        # looping de eventos
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Iniciar procedimento de geração':
                novasenha = self.gerarsenha(valores)
                print(novasenha)
                self.salvarsenha(novasenha, valores)

    def gerarsenha(self, valores):
        charlist = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!@#$%&*'
        chars = random.choices(charlist, k=int(valores['totalcaracteres']))
        newpass = ''.join(chars)
        return newpass
    
    def salvarsenha(self, novasenha, valores):
        with open('senhas.txt', 'a', newline='') as arquivo:
            arquivo.write(f"site: {valores[site]}, usuario: {valores['usuario']}, nova senha: {novasenha}")

        print('Arquivo salvo!')


gen = GeradorSenha()
gen.Iniciar()
