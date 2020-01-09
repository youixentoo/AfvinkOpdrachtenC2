# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 10:07:23 2019

@author: gebruiker
"""

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

    elif choice == "RNA":
        return  {"T": "A", "t": "a", "A": "U", "a": "u", "G": "C", "g": "c", "C": "G", "c": "g"}

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
=======
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 10:07:23 2019

@author: gebruiker
"""

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

    elif choice == "RNA":
        return  {"T": "A", "t": "a", "A": "U", "a": "u", "G": "C", "g": "c", "C": "G", "c": "g"}

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
>>>>>>> 3473eac1e1983baecde5bed80d0f493b48f492fb
                 }
