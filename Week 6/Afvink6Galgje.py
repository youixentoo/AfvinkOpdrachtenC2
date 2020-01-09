<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 15:32:24 2019

Nooit afgemaakt

@author: gebruiker
"""

import tkinter as tk

class GalgjeGUI():

    def __init__(self):
        x = 1

root = tk.Tk()

e = tk.Entry(root, width=50, borderwidth=5)
e.pack()


def buttonClick():


    label = tk.Label(root, text=e.get())
    label.pack()



def main():


    label1 = tk.Label(root, text='label text')
    button1 = tk.Button(root, text="button", command=buttonClick, bg="blue", fg="#0fff00")

    label1.pack()
    button1.pack()



#    label1.grid(row=0,column=0)
#    button1.grid(row=1,column=1)




    root.mainloop()












if __name__ == "__main__":
    main()
=======
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 15:32:24 2019

@author: gebruiker
"""

import tkinter as tk

class GalgjeGUI():
    
    def __init__(self):
        x = 1

root = tk.Tk()

e = tk.Entry(root, width=50, borderwidth=5)
e.pack()


def buttonClick():
    
    
    label = tk.Label(root, text=e.get())
    label.pack()



def main():
    
    
    label1 = tk.Label(root, text='label text')
    button1 = tk.Button(root, text="button", command=buttonClick, bg="blue", fg="#0fff00")
    
    label1.pack()
    button1.pack()
    
    
    
#    label1.grid(row=0,column=0)
#    button1.grid(row=1,column=1)
    
    
    
    
    root.mainloop()
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()
>>>>>>> 3473eac1e1983baecde5bed80d0f493b48f492fb
