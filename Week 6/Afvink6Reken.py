# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 15:58:29 2019

@author: gebruiker
"""

import tkinter as tk
import RekenMemory as rm
import time
import threading

def main():
    try:
        calc = RekGUI()
        calc.startGUI()
    except Exception as exc:
        exc.with_traceback()
        print("tesT")




class RekGUI():
    
    def __init__(self):
        self.memory = rm.Memory()
        
        self.root = tk.Tk()
        self.root.title("Worst Calculator")
        
        self.e = tk.Entry(self.root, width=40, borderwidth=5)
        self.e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Making of buttons
        
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
        
        # Grid layout of buttons
        
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
        
    def startGUI(self):
        self.root.mainloop()
    
    
    def concat(self, a,b):
        return "{}{}".format(a,b)
    
    
    def addition(self, number):
        currentNum = self.e.get()
        self.e.delete(0,last="end")
        self.e.insert(0, self.concat(currentNum, number))
        
        
    def addDivider(self, method):
        currentContent = self.e.get()
        self.e.delete(0,last="end")
        self.e.insert(0, currentContent+method)
        
    
    def plus(self):
        number = self.e.get()
        self.memory.addAction([number, "+"])
        self.clear()
        
    
    def minus(self):
        number = self.e.get()
        self.memory.addAction([number, "-"])
        self.clear()
    
    
    def divide(self):
        number = self.e.get()
        self.memory.addAction([number, "/"])
        self.clear()
    
    
    def multi(self):
        number = self.e.get()
        self.memory.addAction([number, "*"])
        self.clear()
    
    
    def calculation(self):
        self.memory.addAction(self.e.get())

#        actions = ['5', '-', '6', '-', '6', '', '-'] 
        actions = self.memory.getActions()
        startingNumber = actions[0]
        
#        print(self.memory)
        
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
                
        self.replace(startingNumber)
                            
        
    
    def clear(self):
        self.e.delete(0, last="end")
        
        
    def clearAll(self):
        self.e.delete(0, last="end")
        self.memory.clearMemory()
        
    def replace(self, number):
        self.e.delete(0, last="end")
        self.e.insert(0,number)
              
   
    
    
if __name__ == "__main__":
    main()
