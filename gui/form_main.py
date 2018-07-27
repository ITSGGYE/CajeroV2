# -*- coding: utf-8 -*-

from Tkinter import Label, Tk, Text, Frame, Button
import os

window = Tk()


class MainForm(object):

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
        #window.resizable(0, 0)
        #window.wm_attributes('-alpha', 0.7)
        # window.tk.call('wm', 'favicon', window._w, img)

        Label(window, text="Estimado estudiante, este es el servicio automático para impresión de certificados automáticos",
                                    font = (None, 25)).grid(row=0, column=0)

        text2 = Text(window, height=1, width=10, font = (None, 25)).grid(row=1, column=0,ipadx=10)
        text2.config('big', font=('Verdana', 20, 'bold'))

        Button(text="Cerrar", command=self.close).grid(row=2, column=0)

        window.mainloop()
