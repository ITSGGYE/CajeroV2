# -*- coding: utf-8 -*-

from Tkinter import Label, Button, Entry, Frame,Tk, END
from utils.validations import Validations
import logging, os
from gui import frame_menu
from utils.load_json import LoadJson
import pdfkit
from pad4pi import rpi_gpio
import time


val = Validations()

_logger = logging.getLogger(__name__)


class MainForm:
                
        maxlong = 0
        estado = 0
        
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

        #logging.warning('printer: ' + printer)
        
        def print_certificado_notas(self):
            pdfkit.from_file('reports/certificado_notas.html', 'reports/certificado_notas.pdf', options=self.options_pdf)
            os.system('lp -d ' + self.printer + ' reports/certificado_notas.pdf')

        def print_certificado_matricula(self):
            pdfkit.from_file('reports/certificado_matricula.html', 'reports/certificado_matricula.pdf', options=self.options_pdf)
            os.system('lp -d ' + self.printer + ' reports/certificado_matricula.pdf')
                
        def posElement(self, percent, pos):
                return (pos * percent) // 100

        def __init__(self, mainWindow, mainWidth, mainHeight):
                               
                frame_main = Frame(mainWindow, width=mainWidth, height=mainHeight)
                frame_main.grid(row=0, column=0)
                
                lblTitle = Label(mainWindow, text="Ingrese su número de cédula", font = (None, 45))
                lblTitle.place(x=self.posElement(50, mainWidth), y=self.posElement(20, mainHeight), anchor="center")

                #Validación de solo números
                #reg = mainWindow.register(val.onlyDigits)
                #reg = mainWindow.register()

                #txtCedula = Entry(mainWindow, font="Helvetica 60 bold", width=15, justify="center", validate="all", validatecommand=(reg, '%P'))
                txtCedula = Entry(mainWindow, font="Helvetica 120 bold", width=15, justify="center")
                txtCedula.place(x=self.posElement(50, mainWidth), y=self.posElement(50, mainHeight), anchor="center")
                txtCedula.focus()

                lblTitle2 = Label(mainWindow, text="Presione Click en 'ENTER' para continuar.", font=(None, 45))
                lblTitle2.place(x=self.posElement(50,mainWidth), y=self.posElement(80, mainHeight), anchor="center")
                
        
                # Setup Keypad
                KEYPAD = [
                                ["3","2","1","A"],
                                ["6","5","4","B"],
                                ["9","8","7","C"],
                                ["0",".","X","D"]
                ]

                # same as calling: factory.create_4_by_4_keypad, still we put here fyi:
                ROW_PINS = [16, 20, 21, 5] # BCM numbering; Board numbering is: 7,8,10,11 (see pinout.xyz/)
                COL_PINS = [6, 13, 19, 26] # BCM numbering; Board numbering is: 12,13,15,16 (see pinout.xyz/)


                factory = rpi_gpio.KeypadFactory()

                # Try keypad = factory.create_4_by_3_keypad() or 
                # Try keypad = factory.create_4_by_4_keypad() #for reasonable defaults
                # or define your own:
                keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)
                                                
                
                def printkey(key):
                        
                        if self.estado == 0:
                                if self.maxlong < 10:
                                        if(key=='1' or key=='2' or key=='3' or key=='4' or key=='5' or key=='6' or key=='7' or key=='8' or key=='9' or key=='0'):
                                                txtCedula.insert(END, key)
                                elif key=='D':
                                        #FIXME Validar número de cédula
                                                
                                        self.estado = 1
                                        
                                        frame_menu.MenuForm(mainWindow, mainWidth, mainHeight)
                                        mainWindow.update()
                                        print "show"
                                        
                                if key=='X' or key=='A':
                                        txtCedula.delete(0, 'end')
                                        
                                self.maxlong = len(txtCedula.get())
                                
                        elif self.estado == 1:
                                if(key=='1'):
                                        self.print_certificado_notas()
                                elif key=='2':
                                        self.print_certificado_matricula()
                                        
                        print(key)
                
                keypad.registerKeyPressHandler(printkey)
                
                
