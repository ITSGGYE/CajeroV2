# -*- coding: utf-8 -*-

from Tkinter import Label, Button, Frame
from utils.load_json import LoadJson
import logging, os
import keyboard

import pdfkit


class MenuForm(Frame):

    options_pdf = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
    }

    fileJson = LoadJson().read('parameters.json')

    options = fileJson['general']
    printer = options[0]['printer']

    logging.warning('printer: ' + printer)

    def print_certificado_notas(self):
        pdfkit.from_file('reports/certificado_notas.html', 'reports/certificado_notas.pdf', options=self.options_pdf)
        os.system('lp -d ' + self.printer + ' reports/certificado_notas.pdf')

    def print_certificado_matricula(self):
        pdfkit.from_file('reports/certificado_matricula.html', 'reports/certificado_matricula.pdf', options=self.options_pdf)
        os.system('lp -d ' + self.printer + ' reports/certificado_matricula.pdf')

    def posElement(self, percent, pos):
        return (pos * percent) // 100

    def __init__(self, mainWindow, mainWidth, mainHeight):
        frame_menu = Frame(mainWindow, width=mainWidth, height=mainHeight)
        frame_menu.grid(row=0, column=0)

        lblTitle = Label(mainWindow, text="Bienvenido(a) TERÁN ANDRADE MAITE ELIZABETH", font=(None, 20))
        lblTitle.place(x=self.posElement(50, mainWidth), y=self.posElement(20, mainHeight), anchor="center")

        lblTitle2 = Label(mainWindow, text="Presione una opción en el teclado y de 'ACEPTAR' para continuar.", font=(None, 25))
        lblTitle2.place(x=self.posElement(50, mainWidth), y=self.posElement(80, mainHeight), anchor="center")

        lblCertificadoNotas = Label(mainWindow, text="1.- Certificado de Notas", font=(None, 25))
        lblCertificadoNotas.place(x=self.posElement(20, mainWidth), y=self.posElement(30, mainHeight), anchor="center")

        lblCertificadoMatricula = Label(mainWindow, text="2.- Certificado de Matrícula", font=(None, 25))
        lblCertificadoMatricula.place(x=self.posElement(20, mainWidth), y=self.posElement(40, mainHeight), anchor="center")

        keyboard.add_hotkey('1', lambda: self.print_certificado_notas())
        keyboard.add_hotkey('2', lambda: self.print_certificado_matricula())

        #fileJson = LoadJson().read('parameters.json')

        '''options = fileJson['menu_option']
        buttonWidth = options[0]['width']
        buttonHeight = options[0]['height']

        i = 30
        cont = 0

        for value in fileJson['menu']:
            if cont <= 2:
                Button(mainWindow, text=value['name'], width=buttonWidth, height=buttonHeight).place(
                    x=self.posElement(20, mainWidth), y=self.posElement(i, mainHeight))
            elif cont <= 5:
                if i == 60:
                    i = 30
                Button(mainWindow, text=value['name'], width=buttonWidth, height=buttonHeight).place(
                    x=self.posElement(40, mainWidth), y=self.posElement(i, mainHeight))
            elif cont <= 8:
                if i == 60:
                    i = 30
                Button(mainWindow, text=value['name'], width=buttonWidth, height=buttonHeight).place(
                    x=self.posElement(60, mainWidth), y=self.posElement(i, mainHeight))

            i = i+10
            cont = cont + 1'''
