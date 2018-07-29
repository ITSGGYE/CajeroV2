# -*- coding: utf-8 -*-

from Tkinter import Label, Button, Frame
from utils.load_json import LoadJson
import logging

_logger = logging.getLogger(__name__)


class MenuForm(Frame):

    def posElement(self, percent, pos):
        return (pos * percent) // 100

    def __init__(self, mainWindow, mainWidth, mainHeight):
        frame_menu = Frame(mainWindow, width=mainWidth, height=mainHeight)
        frame_menu.grid(row=0, column=0)

        lblTitle = Label(mainWindow, text="Bienvenido JOSÉ DUQUE", font = (None, 25))
        lblTitle.place(x=self.posElement(50, mainWidth), y=self.posElement(20, mainHeight), anchor="center")

        lblTitle2 = Label(mainWindow, text="Presione una opción y de click en 'ACEPTAR' para continuar.", font=(None, 25))
        lblTitle2.place(x=self.posElement(50, mainWidth), y=self.posElement(80, mainHeight), anchor="center")

        fileJson = LoadJson().read('parameters.json')

        options = fileJson['menu_option']
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
            cont = cont + 1
