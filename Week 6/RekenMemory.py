# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 16:30:27 2019

@author: gebruiker
"""

class Memory():
    
    def __init__(self):
        self.__actions = []
        
        
    def addAction(self, action):
        try:
            if not action[0] == '':
                if type(action) == type(str()):
                    self.__actions.append(action)
                else:
                    for item in action:
                        self.__actions.append(item)
        except IndexError:
            pass
        except Exception as exc:
            exc.with_traceback()
            
        
    def getActions(self):
        return self.__actions
        
    
    def clearMemory(self):
        self.__actions = []
        
        
    def __str__(self):
        return " ".join(self.__actions)