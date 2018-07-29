# -*- coding: utf-8 -*-

from Tkinter import Tk, Button
import keyboard
from gui import frame_main
from gui import frame_menu
import os

mainWindow = Tk()


class MainFrame:

    def __init__(self):
        mainWindow.title("Cajero Automático")
        mainWindow.attributes("-topmost", True)
        #mainWindow.attributes("-fullscreen", True)
        mainWindow.wait_visibility(mainWindow)
        mainWindow.resizable(0, 0)
        mainWindow.wm_attributes('-alpha', 0.8)
        # mainWindow.tk.call('wm', 'favicon', window._w, img)
    
        mainWidth = mainWindow.winfo_screenwidth()
        mainHeight = mainWindow.winfo_screenheight()
    
        keyboard.add_hotkey('enter', lambda: self.showMenuFrame(mainWidth, mainHeight))
        keyboard.add_hotkey('esc', lambda: self.close())
        keyboard.add_hotkey('a', lambda: self.showMainFrame(mainWidth, mainHeight))
    
        self.showMainFrame(mainWidth, mainHeight)

        btnCerrar = Button(mainWindow, text="Cerrar", command=self.close)
        btnCerrar.place(x=self.posElement(0, mainWidth), y=self.posElement(0, mainHeight))

    
        mainWindow.mainloop()

    def showMainFrame(self, w, h):
        frame_main.MainForm(mainWindow, w, h)
        mainWindow.update()

    def showMenuFrame(self, w, h):
        frame_menu.MenuForm(mainWindow, w, h)
        mainWindow.update()

    def closeEvent(self, event):
        mainWindow.destroy()

    def close(self):
        mainWindow.destroy()
        os._exit(0)

    def posElement(self, percent, pos):
        return (pos * percent) // 100