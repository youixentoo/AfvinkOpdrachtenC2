# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 14:06:25 2019

@author: gebruiker
"""

import re

import fix_linebreaks


# Aanroepen van de functies
def main():
    headers, sequences = lees_fasta_bestand()
    irriteer_en_controleer(sequences, headers)


# Inlezen van het bestand en het ophalen van de headers en sequenties.
def lees_fasta_bestand():
    file_name = "Mus_musculus.GRCm38.pep.all.fa"
    location = "Data"
    file = open(location+"/"+file_name)
    return fix_linebreaks.get_headers_and_sequences(file, ">")


# Kijkt per sequentie (data) eerst of dit een eiwit sequentie is.
# Als dat zo is, dan wordt er gekeken of het consensus patroon aanwezig is.
# Is het laatste ook waar, dan wordt de sequentie en header geprint.
def irriteer_en_controleer(data, headers):
    if not len(data) == 0:
        for index, sequentie in enumerate(data):
            if is_eiwitsequentie(sequentie):
                if consensus(sequentie):
                    print("%s%s\n\n" % (headers[index], sequentie))


# Checkt of de sequentie een eiwit sequentie is.
def is_eiwitsequentie(sequentie):
    result = re.search("^[ARNDCQEGHILKMFPSTWYV]*$", sequentie)
    if result == None:
        return False
    else:
        #print("Geen eiwitsequentie")
        return True


# Checkt of de consensus in de sequentie voor komt.
def consensus(sequentie):
    result = re.search("MCNSSC[MV]GGMNRR", sequentie)
    if not result == None:
        return True
    else:
        return False


# Aanroepen van de main.
if __name__ == "__main__":
    main()
=======
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 14:06:25 2019

@author: gebruiker
"""

import re

import fix_linebreaks


def main():
    headers, sequences = lees_fasta_bestand()
    irriteer_en_controleer(sequences, headers)


def lees_fasta_bestand():
    file_name = "Mus_musculus.GRCm38.pep.all.fa"
    location = "Data"
    file = open(location+"/"+file_name)
    return fix_linebreaks.get_headers_and_sequences(file, ">")


def irriteer_en_controleer(data, headers):
    if not len(data) == 0:
        for index, sequentie in enumerate(data):
            if is_eiwitsequentie(sequentie):
                if consensus(sequentie):
                    print("%s%s\n\n" % (headers[index], sequentie))


def is_eiwitsequentie(sequentie):
    result = re.search("^[ARNDCQEGHILKMFPSTWYV]*$", sequentie)
    if result == None:
        return False
    else:
        #print("Geen eiwitsequentie")
        return True


def consensus(sequentie):
    result = re.search("MCNSSC[MV]GGMNRR", sequentie)
    if not result == None:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
>>>>>>> 3473eac1e1983baecde5bed80d0f493b48f492fb
