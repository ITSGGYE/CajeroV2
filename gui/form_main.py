# -*- coding: utf-8 -*-

from Tkinter import Label, Tk, Button, Entry, Toplevel
import form_menu
import os
import logging


_logger = logging.getLogger(__name__)

window = Tk()


class MainForm:

    def close(self):
        window.destroy()
        os._exit(0)

    def closeEvent(self, event):
        self.window.destroy()

    def loadFormMenu(self):
        Toplevel(form_menu)

    def __init__(self):
        window.title("Cajero Automático")
        window.attributes("-topmost", True)
        #window.attributes("-fullscreen", True)
        window.wait_visibility(window)
        #window.resizable(0, 0)
        #window.wm_attributes('-alpha', 0.7)
        # window.tk.call('wm', 'favicon', window._w, img)

        lblTitle = Label(window, text="Por favor ingrese su número de cédula para poder continuar.", font = (None, 25))
        lblTitle.place(x=(window.winfo_screenwidth() // 2), y=((window.winfo_screenheight() * 20) // 100), anchor="center")

        txtCedula = Entry(window, font="Helvetica 60 bold", width=15, justify="center")
        txtCedula.place(x=(window.winfo_screenwidth() // 2), y=(window.winfo_screenheight() // 2), anchor="center")
        txtCedula.focus()

        lblTitle2 = Label(window, text="Presione Click en 'ACEPTAR' para continuar.", font=(None, 25))
        lblTitle2.place(x=(window.winfo_screenwidth() // 2), y=((window.winfo_screenheight() * 80) // 100),
                       anchor="center")

        logging.warning(window.winfo_screenwidth())

        Button(window, text="Cerrar", command=self.close).grid(row=0, column=0)
        Button(window, text="Menu", command=self.loadFormMenu).grid(row=2, column=0)

        window.mainloop()

