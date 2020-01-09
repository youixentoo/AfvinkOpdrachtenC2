# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 09:10:02 2017

@author: thijs
"""
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter


def main():
    data = getData()
    showPlot(data)
    
# Haalt alle data op uit het bestand
def getData():
    rawData = open("yeast_genes.csv").readlines()
    data = [line.split(",")[1].strip("\n") for line in rawData]
    
    """
    Bovenste is hetzelfde als:
        
    data = []
    
    for line in rawData:
        relevantData = line.split(",")[1].strip("\n")
        data.append(relevantData)
    
    """
    # Telt alle data en zet deze om tot een dictionary
    outputData = Counter(data)
    #print(outputData)
    return outputData

# Maakt het barplot en laat deze zien. Maakt er ook een .png van.
# data is de dictionary van de Counter.
def showPlot(data):
    
    fig = plt.bar(range(len(data)), data.values(), align="center")
    
    # Verticale x-as labels was niet echt mooi, -79 was beter leesbaar
    # Horizontale x-as labels werkt al helemaal niet
    plt.xticks(range(len(data)), data.keys(), rotation=-79)
    
    # Kleuren van de verschillende data
    for i in range(len(data)):
        # Ietwat hard-coded voor kleuren
        colors = ["red","blue","green","yellow","purple","orange"]
        fig[i].set_color(colors[i])
    
    # Maakt de legenda en de titels aan
    plt.legend(fig,data.keys())
    plt.title("Gen statussen")
    plt.ylabel("Aantal genen")
    plt.xlabel("Type status")
    
    # Slaat de plot op als een .png, bbox_inches zorgt ervoor dat de x-as volledig op het plaatje komt.
    plt.savefig("Afvink2.png", bbox_inches="tight")
    
    
    plt.show()
    
main()

#####################
# Alternatief voor bbox_inches:

#from matplotlib import rcParams

# Anders komt niet alles op het .png plaatje te staan
#rcParams.update({'figure.autolayout': False})



