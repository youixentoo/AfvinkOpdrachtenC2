# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 15:58:29 2019

@author: gebruiker
"""

import tkinter as tk
import RekenMemory as rm
import time
import threading

# Aanroepen van de GUI
def main():
    try:
        calc = RekGUI()
        calc.startGUI()
    except Exception as exc:
        exc.with_traceback()
        print("tesT")


# De GUI van de rekenmachine
class RekGUI():

    # Init
    def __init__(self):
        # Maakt een memory object aan.
        self.memory = rm.Memory()

        # Aanmaken van de root.
        self.root = tk.Tk()
        self.root.title("Worst Calculator")

        # Entry voor het resultaat.
        self.e = tk.Entry(self.root, width=40, borderwidth=5)
        self.e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Aanmaken van de knoppen.

        self.button1 = tk.Button(self.root, text="1", padx=40, pady=20, command=lambda: self.addition(1))
        self.button2 = tk.Button(self.root, text="2", padx=40, pady=20, command=lambda: self.addition(2))
        self.button3 = tk.Button(self.root, text="3", padx=40, pady=20, command=lambda: self.addition(3))
        self.button4 = tk.Button(self.root, text="4", padx=40, pady=20, command=lambda: self.addition(4))
        self.button5 = tk.Button(self.root, text="5", padx=40, pady=20, command=lambda: self.addition(5))
        self.button6 = tk.Button(self.root, text="6", padx=40, pady=20, command=lambda: self.addition(6))
        self.button7 = tk.Button(self.root, text="7", padx=40, pady=20, command=lambda: self.addition(7))
        self.button8 = tk.Button(self.root, text="8", padx=40, pady=20, command=lambda: self.addition(8))
        self.button9 = tk.Button(self.root, text="9", padx=40, pady=20, command=lambda: self.addition(9))
        self.button0 = tk.Button(self.root, text="0", padx=40, pady=20, command=lambda: self.addition(0))

        self.buttonPlus = tk.Button(self.root, text="+", padx=40, pady=20, command=self.plus)
        self.buttonMinus = tk.Button(self.root, text="-", padx=40, pady=20, command=self.minus)
        self.buttonDivide = tk.Button(self.root, text="/", padx=40, pady=20, command=self.divide)
        self.buttonMulti = tk.Button(self.root, text="*", padx=40, pady=20, command=self.multi)

        self.buttonEqual = tk.Button(self.root, text="=", padx=39, pady=20, command=self.calculation)
        self.buttonClear = tk.Button(self.root, text="CL", padx=36, pady=20, command=self.clearAll)

        # Grid layout.

        self.button7.grid(row=1, column=0)
        self.button8.grid(row=1, column=1)
        self.button9.grid(row=1, column=2)
        self.buttonDivide.grid(row=1, column=3)

        self.button4.grid(row=2, column=0)
        self.button5.grid(row=2, column=1)
        self.button6.grid(row=2, column=2)
        self.buttonMulti.grid(row=2, column=3)

        self.button1.grid(row=3, column=0)
        self.button2.grid(row=3, column=1)
        self.button3.grid(row=3, column=2)
        self.buttonMinus.grid(row=3, column=3)

        self.buttonClear.grid(row=4, column=0)
        self.button0.grid(row=4, column=1)
        self.buttonEqual.grid(row=4, column=2)
        self.buttonPlus.grid(row=4, column=3)

        #self.root.mainloop()


    # Om de GUI te starten
    def startGUI(self):
        self.root.mainloop()


    # Zet nummers aan elkaar, om bijvoorbeeld 12 te kunnen typen.
    def concat(self, a,b):
        return "{}{}".format(a,b)


    # Methode om het nummer in de entry te koppelen aan de ingedrukte knop.
    def addition(self, number):
        currentNum = self.e.get()
        self.e.delete(0,last="end")
        self.e.insert(0, self.concat(currentNum, number))


    # Doet niks
#    def addDivider(self, method):
#        currentContent = self.e.get()
#        self.e.delete(0,last="end")
#        self.e.insert(0, currentContent+method)


    # Zet het huidige getal plus een + als actie in het geheugen (memory).
    def plus(self):
        number = self.e.get()
        self.memory.addAction([number, "+"])
        self.clear()


    # Zet het huidige getal plus een - als actie in het geheugen (memory).
    def minus(self):
        number = self.e.get()
        self.memory.addAction([number, "-"])
        self.clear()


    # Zet het huidige getal plus een / als actie in het geheugen (memory).
    def divide(self):
        number = self.e.get()
        self.memory.addAction([number, "/"])
        self.clear()


    # Zet het huidige getal plus een * als actie in het geheugen (memory).
    def multi(self):
        number = self.e.get()
        self.memory.addAction([number, "*"])
        self.clear()


    # Berekening van uitkomst op basis van de acties in het geheugen (memory).
    def calculation(self):
        # Zet het laaste getal in de entry in de geheugen.
        self.memory.addAction(self.e.get())

#        actions = ['5', '-', '6', '-', '6', '', '-']
        # Haalt de acties op uit het geheugen.
        actions = self.memory.getActions()
        startingNumber = actions[0]

#        print(self.memory)

        # Loopt over de acties heen om de uitkomst de berekenen.
        for action in actions[1:]:
            if action in ["+", "-", "/", "*"]:
                method = action
            else:
                if method == "+":
                    startingNumber = float(startingNumber) + float(action)
#                    self.replace(startingNumber)
                elif method == "-":
                    startingNumber = float(startingNumber) - float(action)
#                    self.replace(startingNumber)
                elif method == "/":
                    startingNumber = float(startingNumber) / float(action)
#                    self.replace(startingNumber)
                elif method == "*":
                    startingNumber = float(startingNumber) * float(action)
#                    self.replace(startingNumber)

        # Aanroepen methode om het resultaat te laten zien.
        self.replace(startingNumber)



    # Verwijderd alles in de entry.
    def clear(self):
        self.e.delete(0, last="end")


    # Verwijderd alles in de entry en het geheugen.
    def clearAll(self):
        self.e.delete(0, last="end")
        self.memory.clearMemory()


    # Zet een nieuw getal in de entry.
    def replace(self, number):
        self.e.delete(0, last="end")
        self.e.insert(0,number)



# Aanroepen van de main
if __name__ == "__main__":
    main()
