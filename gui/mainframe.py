# -*- coding: utf-8 -*-

from Tkinter import Tk, Button
from gui import frame_main
from gui import frame_menu
#from database.conexion import MySQL as mysql_connect
#from database.conexion import PostgreSQL as psg_connect
from utils.load_json import LoadJson
import logging
import os
import tkMessageBox

mainWindow = Tk()

try:
    fileJson = LoadJson().read('parameters.json')
    options = fileJson['general']
except Exception, e:
    tkMessageBox.showerror('Error', 'No se pudo cargar el archivo json')


class MainFrame:

    #Seleccionar Base de Datos desde archivo de parámetros
    '''def dbSelect(self):

        database = options[0]['db']

        if database == 'mysql':
            mysql = mysql_connect()

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT IdAlumno, AlumnoCedula, AlumnoApellidos, AlumnoNombres FROM alumnos LIMIT 10")
            logging.warning(cursor.fetchall())
            conn.close()

        elif database == 'postgres':
            postgres = psg_connect()
            return postgres.connect()
        else:
            None'''

    def __init__(self):
        fullscreen = options[0]['fullscreen']

        if fullscreen == True:
            mainWindow.attributes("-fullscreen", True)

        mainWindow.title("Cajero Automático")
        mainWindow.attributes("-topmost", True)
        mainWindow.wait_visibility(mainWindow)
        mainWindow.resizable(0, 0)
        mainWindow.wm_attributes('-alpha', 0.7)
        # mainWindow.tk.call('wm', 'favicon', window._w, img)
    
        mainWidth = mainWindow.winfo_screenwidth()
        mainHeight = mainWindow.winfo_screenheight()

        #keyboard.add_hotkey('enter', lambda: self.showMenuFrame(mainWidth, mainHeight))
        #keyboard.add_hotkey('esc', lambda: self.close())
        #keyboard.add_hotkey('a', lambda: self.showMainFrame(mainWidth, mainHeight))
    
        self.showMainFrame(mainWidth, mainHeight)

        #btnCerrar = Button(mainWindow, text="Cerrar", command=self.close)
        #btnCerrar.place(x=self.posElement(0, mainWidth), y=self.posElement(0, mainHeight))

        #btnTest = Button(mainWindow, text="Test", command=self.dbSelect)
        #btnTest.place(x=self.posElement(0, mainWidth), y=self.posElement(5, mainHeight))

    
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
