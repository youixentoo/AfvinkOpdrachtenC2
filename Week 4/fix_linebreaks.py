<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 13:26:06 2019

@author: gebruiker
"""
import re

# Zorgt ervoor dat de linebreaks in de sequenties in het meegeven bestand,
# eruit worden gehaald. Geeft 2 lijsten terug, 1 met headers en 1 met sequenties.
def get_headers_and_sequences(file, starting_symbol):
    line = file.readline()
    headers = [line]
    sequences = []
    sequence = ""

    while line:
        line = file.readline()
        result = re.match(starting_symbol, line)
        if result == None:
            sequence += line.strip("\n")
        else:
            sequences.append(sequence)
            sequence = ""
            headers.append(line)

    sequences.append(sequence)

    return headers, sequences
