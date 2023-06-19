from tkinter import *
from tkinter import ttk,messagebox
import json
from urllib.request import urlopen
from functools import partial

class Aplicacion():
    __ventana=None
    __dolares=None
    __pesos=None

    def __init__(self):
        self.__ventana=Tk()
        self.__ventana.title("Conversor de moneda")
        mainframe=ttk.Frame(self.__ventana,padding="5 5 12 5")
        mainframe.grid(column=0,row=0,sticky=(N,W,E,S))
        mainframe.columnconfigure(0,weight=1)
        mainframe['borderwidth']=2
        mainframe['relief']='sunken'

        url = 'https://www.dolarsi.com/api/api.php?type=dolar'
        response = urlopen (url)
        data = json.loads(response.read())
        for d in data:
            if d['casa']['nombre'] == 'Oficial':
                dolarstr = d['casa']['venta']
                dolar = float (dolarstr.replace(',','.'))


        self.__dolares=StringVar()
        self.__pesos=StringVar()
        self.__dolares.trace('w',partial(self.calcular,dolar))
        self.dolaresEntry=ttk.Entry(mainframe, width=7,textvariable=self.__dolares)
        self.dolaresEntry.grid(column=2,row=1,sticky=(W,E))
        ttk.Label(mainframe,textvariable=self.__pesos).grid(column=2,row=2,sticky=(W,E))
        ttk.Button(mainframe,text='Salir',command=self.__ventana.destroy).grid(column=3,row=3,sticky=W)
        ttk.Label(mainframe,text="dolares").grid(column=3,row=1,sticky=W)
        ttk.Label(mainframe, text="es equivalente a").grid(column=1,row=2,sticky=E)
        ttk.Label(mainframe, text="pesos").grid(column=3,row=2,sticky=W)
        self.dolaresEntry.focus()
        

        self.__ventana.mainloop()
    
    def calcular(self,dolar,*args):
        if self.dolaresEntry.get()!='':
            try:
                valor=float(self.dolaresEntry.get())
                self.__pesos.set(f"{dolar*valor:.2f}")
            except ValueError:
                messagebox.showerror(title='Error de tipo',message='Debe ingresar un valor numerico')
                self.__dolares.set('')
                self.dolaresEntry.focus()
        else:
            self.__pesos.set('')            
        