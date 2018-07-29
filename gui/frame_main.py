# -*- coding: utf-8 -*-

from Tkinter import Label, Button, Entry, Frame,Tk
from utils.validations import Validations
import logging


val = Validations()

_logger = logging.getLogger(__name__)


class MainForm:

    def posElement(self, percent, pos):
        return (pos * percent) // 100

    def __init__(self, mainWindow, mainWidth, mainHeight):
        frame_main = Frame(mainWindow, width=mainWidth, height=mainHeight)
        frame_main.grid(row=0, column=0)

        lblTitle = Label(mainWindow, text="Por favor ingrese su número de cédula para poder continuar.", font = (None, 25))
        lblTitle.place(x=self.posElement(50, mainWidth), y=self.posElement(20, mainHeight), anchor="center")

        #Validación de solo números
        reg = mainWindow.register(val.onlyDigits)

        txtCedula = Entry(mainWindow, font="Helvetica 60 bold", width=15, justify="center", validate="all", validatecommand=(reg, '%P'))
        txtCedula.place(x=self.posElement(50, mainWidth), y=self.posElement(50, mainHeight), anchor="center")
        txtCedula.focus()

        lblTitle2 = Label(mainWindow, text="Presione Click en 'ACEPTAR' para continuar.", font=(None, 25))
        lblTitle2.place(x=self.posElement(50,mainWidth), y=self.posElement(80, mainHeight), anchor="center")





