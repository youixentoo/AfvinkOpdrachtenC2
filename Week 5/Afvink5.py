# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 15:56:24 2019

@author: gebruiker
"""
import sys
sys.path.append("D:\School\Python\Course 2 Eerste Jaars\Week 4") # File path to import the linebreaks fixing script

from Afvink5Objects import DNA
import fix_linebreaks


# Aanroepen van de functies
def main():
    filename = "Felis_catus.Felis_catus_8.0.cdna.all.fa"

    dna_list = file_processor(filename)

    highest_gc_obj = find_highest_gc(dna_list)

    print("The sequence with the highest GC% has this GC%: {}\nThis transcript: {}\nAnd this length: {}".format(
            highest_gc_obj.getGCPercentage(), highest_gc_obj.getRNA(), highest_gc_obj.getLength()))


    highest_length_obj = find_highest_length(dna_list)

    print("")
#    print("Iteration based highest length: ",highest_length_obj.getLength()) # Controle voor dna_list.sort([...])
#
#    print("First index of dna_list: ",dna_list[0].getLength()) # Wat er in de 1e index staat

    dna_list.sort(key=lambda DNA: DNA.getLength(), reverse=True) #https://docs.python.org/3/howto/sorting.html#sortinghowto

    print("First index of dna_list after sorting: ",dna_list[0].getLength()) # Wat er na sorteren in de 1e index staat
    print(dna_list[0])


# Zoekt het object met de grootste lengte in de lijst.
def find_highest_length(dna_list):
    highest_length = 0
    highest_length_obj = DNA("")

    for dna_obj in dna_list:
        gc_length = dna_obj.getLength()
        # Als het huidige object een grotere lengte heeft dan degene die is opgeslagen,
        # dan wordt het huidige object opgeslagen.
        if float(gc_length) > int(highest_length):
            highest_length = gc_length
            highest_length_obj = dna_obj

    return highest_length_obj


# Zoekt het object met het hoogste GC percentage in de lijst.
def find_highest_gc(dna_list):
    highest_gc = 0
    highest_gc_obj = DNA("")

    for dna_obj in dna_list:
        gc_per = dna_obj.getGCPercentage()
        # Als het huidige object een hoger GC% heeft dan degene die is opgeslagen,
        # dan wordt het huidige object opgeslagen.
        if float(gc_per) > float(highest_gc):
            highest_gc = gc_per
            highest_gc_obj = dna_obj

    return highest_gc_obj


# Leest het bestand in en maakt een lijst met headers en sequenties.
# Deze twee lijsten worden gecombineerd tot een lijst met DNA() objecten.
def file_processor(filename):
    dna_list = []
    with open(filename) as file:
        headers, sequences = fix_linebreaks.get_headers_and_sequences(file, ">")

        # enumerate() geeft naast de sequentie, ook de index van het item in de lijst mee,
        # handig als twee lijsten gecombineerd moeten worden tot 1.
        for index, sequence in enumerate(sequences):
            dna_list.append(DNA(sequence, headers[index]))

        return dna_list


# Aanroepen van de main
if __name__ == "__main__":
    main()
