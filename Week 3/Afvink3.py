# -*- coding: utf-8 -*-
"""

Het programma moet uiteindelijk het volgende kunnen:

    Gegeven een willekeurige DNA sequentie, vertaal deze mbv de gekozen dictionary naar de correcte eiwitvertaling.
    Hierbij mag je er vanuit gaan dat de DNA sequentie start met ATG en dus 'in frame' is.
        Mocht je jezelf willen uitdagen, ga hier dan niet vanuit en ga op zoek naar het startcodon en tel vanaf daar de codons.

Created on Wed Nov 27 16:17:07 2019

@author: Thijs Weenink
"""

##########################################################################
# (c) 2013 HAN/Martijn van der Bruggen                                   #
# Dictionaries voor het gebruik bij de afvinkopdrachten van HBI-Cou3a    #
# Update: 24-feb-2013 voorzien van commentaar en bestandsnaam aangepast  #
##########################################################################

import random as rnd
import re

def main():
    # Aanroepen van de methodes
    choice_dict = dictionaries()
    dna_seq = dna_randomizer(1000)
    codon_seq = codons(dna_seq)
    
    # Check of codon_seq wel een lijst is en dus codons bevat
    if type(codon_seq) == list:
        protein_seq, stop_codon = dna_translate(codon_seq, choice_dict)
        
        # Prints
        if stop_codon:
            print("De proteine sequentie:\n%s.\n\nIs verkregen van de DNA sequentie:\n%s" % (protein_seq, dna_seq))
        else:
            print("De proteine sequentie:\n%s.\n\nDit eiwit is helaas niet volledig aangezien de DNA sequentie geen stop codon bevat:\n%s" % (protein_seq, dna_seq))
        
 
# Maakt van de DNA sequentie (in codons) een eiwit sequentie    
# Een AttributeError komt er als er geen "*" kan worden gevonden,
# er is dan geen stop codon in de sequentie
def dna_translate(sequentie, choice_dict):
    protein_seq_raw = "".join([choice_dict.get(codon) for codon in sequentie])
    stop_codon = True
    try:
        protein_seq_stop = re.search("\*", protein_seq_raw)
        protein_seq = protein_seq_raw[0:protein_seq_stop.start()]
    except AttributeError:
        protein_seq = protein_seq_raw
        stop_codon = False
       
    return protein_seq, stop_codon
    
    
# Zoekt het start codon in de sequentie en returns de sequentie als codons
# Returns None als er geen start codon in de sequentie wordt gevonden
def codons(sequentie):
    try:
        start_codon = re.search("atg", sequentie) 
        seq_from_start = sequentie[start_codon.start()::]
        codon_seq = re.findall(".{3}", seq_from_start)
    except AttributeError:
        print("This string doesn't contain a start codon, try again")
        return None
    
    return codon_seq
    
      
# Genereer een willekeurige dna sequentie met een gespecificeerde lengte, default = 100
def dna_randomizer(dna_length=100):
    return "".join([rnd.choice("atgc") for amount in range(dna_length)])


# Returns de opgegeven keuze voor een dictionary, default = "DNA"
def dictionaries(choice="DNA"):
    if choice == "DNA":
        return  {'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
                'ttc': 'F', 'tcc': 'S', 'tac': 'Y', 'tgc': 'C',
                'tta': 'L', 'tca': 'S', 'taa': '*', 'tga': '*',
                'ttg': 'L', 'tcg': 'S', 'tag': '*', 'tgg': 'W',
                'ctt': 'L', 'cct': 'P', 'cat': 'H', 'cgt': 'R',
                'ctc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R',
                'cta': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R',
                'ctg': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R',
                'att': 'I', 'act': 'T', 'aat': 'N', 'agt': 'S',
                'atc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S',
                'ata': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R',
                'atg': 'M', 'acg': 'T', 'aag': 'K', 'agg': 'R', 
                'gtt': 'V', 'gct': 'A', 'gat': 'D', 'ggt': 'G',
                'gtc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G',
                'gta': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G',
                'gtg': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G'
                }
    
    else:
        return  {"Ala": ["GCU", "GCC", "GCA", "GCG"],
                 "Arg": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
                 "Asn": ["AAU", "AAC"],
                 "Asp": ["GAU", "GAC"],
                 "Cys": ["UGU", "UGC"],
                 "Gln": ["CAA", "CAG"],
                 "Glu": ["GAA", "GAG"],
                 "Gly": ["GGU", "GGC", "GGA", "GGG"],
                 "His": ["CAU", "CAC"],
                 "Ile": ["AUU", "AUC", "AUA"],
                 "Leu": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],
                 "Lys": ["AAA", "AAG"],
                 "Met": ["AUG"],
                 "Phe": ["UUU", "UUC"],
                 "Pro": ["CCU", "CCC", "CCA", "CCG"],
                 "Ser": ["UCU", "UCC", "UCA", "UCG", "AGU","AGC"],
                 "Thr": ["ACU", "ACC", "ACA", "ACG"],
                 "Trp": ["UGG"],
                 "Tyr": ["UAU", "UAC"],
                 "Val": ["GUU", "GUC", "GUA", "GUG"],
                 "Start": ["AUG", "CUG", "UUG", "GUG", "AUU"],
                 "Stop" : ["UAG", "UGA", "UAA"]
                 }
        
if __name__ == "__main__":
    main()