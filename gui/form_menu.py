# -*- coding: utf-8 -*-

from Tkinter import Label, Tk, Button
from utils.read_config import Config
import os
import logging

_logger = logging.getLogger(__name__)

window = Tk()


class MenuForm:

    def close(self):
        window.destroy()
        os._exit(0)

    def closeEvent(self, event):
        self.window.destroy()

    def __init__(self):
        window.title("Cajero Automático")
        window.attributes("-topmost", True)
        window.attributes("-fullscreen", True)
        window.wait_visibility(window)

        lblTitle = Label(window, text="Bienvenido JOSÉ DUQUE", font = (None, 25))
        lblTitle.place(x=(window.winfo_screenwidth() // 2), y=((window.winfo_screenheight() * 20) // 100), anchor="center")

        lblTitle2 = Label(window, text="Presione la opción con el (#) y 'ACEPTAR' para continuar.", font=(None, 25))
        lblTitle2.place(x=(window.winfo_screenwidth() // 2), y=((window.winfo_screenheight() * 80) // 100),
                       anchor="center")

        config = Config()
        logging.warning(config.getConfig())

        Button(text="Cerrar", command=self.close).grid(row=2, column=0)

        window.mainloop()
