# -*- coding: utf-8 -*-

from Tkinter import Label, Button, Frame
import logging


class MenuForm(Frame):

    maxlong = 0   

    def posElement(self, percent, pos):
        return (pos * percent) // 100

    def __init__(self, mainWindow, mainWidth, mainHeight):
        frame_menu = Frame(mainWindow, width=mainWidth, height=mainHeight)
        frame_menu.grid(row=0, column=0)

        lblTitle = Label(mainWindow, text="Bienvenido(a) TERÁN ANDRADE MAITE ELIZABETH", font="Helvetica 45 bold")
        lblTitle.place(x=self.posElement(50, mainWidth), y=self.posElement(20, mainHeight), anchor="center")

        lblTitle2 = Label(mainWindow, text="Presione una opción en el teclado y de 'ACEPTAR' para continuar.", font=(None, 45))
        lblTitle2.place(x=self.posElement(50, mainWidth), y=self.posElement(80, mainHeight), anchor="center")

        lblCertificadoNotas = Label(mainWindow, text="1.- Certificado de Notas", font="Helvetica 45 bold")
        lblCertificadoNotas.place(x=self.posElement(20, mainWidth), y=self.posElement(30, mainHeight), anchor="center")

        lblCertificadoMatricula = Label(mainWindow, text="2.- Certificado de Matrícula", font="Helvetica 45 bold")
        lblCertificadoMatricula.place(x=self.posElement(20, mainWidth), y=self.posElement(40, mainHeight), anchor="center")

        #keyboard.add_hotkey('1', lambda: self.print_certificado_notas())
        #keyboard.add_hotkey('2', lambda: self.print_certificado_matricula())
