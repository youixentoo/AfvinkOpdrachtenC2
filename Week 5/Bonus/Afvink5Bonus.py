<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 09:51:47 2019

Voorbeeld voor aantonen dat de objecten werken.

@author: gebruiker
"""
import Afvink5BonusObjects
import collections

def main():
    obj = Afvink5BonusObjects.RNA("ATGCTGACGTCACCACGTTGACCGATATC")

    print(obj)


    # Bonus informatie: for-loop met een else.
    for i in range(10):
        print(i)
        if i > 11:
            break
    else: # If it doesn't break out, it goes here
        print("g")






main()
=======
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 09:51:47 2019

@author: gebruiker
"""
import Afvink5BonusObjects
import collections

def main():
    obj = Afvink5BonusObjects.RNA("ATGCTGACGTCACCACGTTGACCGATATC")
    
    print(obj)
    
    for i in range(10):
        print(i)
        if i > 11:
            break
    else: # If it doesn't break out, it goes here
        print("g")
    

    

    
    
main()
>>>>>>> 3473eac1e1983baecde5bed80d0f493b48f492fb
