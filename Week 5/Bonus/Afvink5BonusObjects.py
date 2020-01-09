# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 09:52:07 2019

Dit bestand wordt verder niet echt aangeroepen door een ander bestand.
Alleen de uitwerking van de objecten staat hierin.

@author: gebruiker
"""
import Data
import re

# Super class voor de andere classes
class __Sequence():

    def __init__(self, sequence):
        self.__sequence = sequence


    def getSequence(self):
        return self.__sequence


    def getLength(self):
        return len(self.__sequence)


    def __str__(self):
        return self.__sequence


    # Geen getGCPercentage aangezien je zo ook een class voor eiwitten kan maken.


# DNA object
class DNA(__Sequence):

    def __init__(self, sequence):
        super().__init__(sequence)


    def getGCPercentage(self):
        string = super().getSequence().upper()
        return "{:.6}".format((string.count("G")+string.count("C"))/len(string)*100)


# RNA object
class RNA(__Sequence):

    def __init__(self, sequence):
        super().__init__(sequence)


    def getRNA(self):
        rna_dict = Data.dictionaries("RNA")
        return "".join([rna_dict.get(nucl) for nucl in super().getSequence()])


    def getGCPercentage(self):
        string = self.__sequence.upper()
        return "{:.6}".format((string.count("G")+string.count("C"))/len(string)*100)

    """
    Cant be bothered to fix this now
    def getTranslation(self):

        transDict = Data.dictionaries()
        print(super().getSequence())
        protein_seq_raw = "".join([transDict.get(codon) for codon in (super().getSequence())])

        try:
            protein_seq_stop = re.search("\*", protein_seq_raw)
            protein_seq = protein_seq_raw[0:protein_seq_stop.start()+1]
        except AttributeError:
            protein_seq = protein_seq_raw

        return protein_seq

    """
=======
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 09:52:07 2019

@author: gebruiker
"""
import Data
import re

class __Sequence():

    def __init__(self, sequence):
        self.__sequence = sequence


    def getSequence(self):
        return self.__sequence


    def getLength(self):
        return len(self.__sequence)


    def __str__(self):
        return self.__sequence


    # Geen getGCPercentage aangezien je zo ook een class voor eiwitten kan maken.



class DNA(__Sequence):

    def __init__(self, sequence):
        super().__init__(sequence)


    def getGCPercentage(self):
        string = super().getSequence().upper()
        return "{:.6}".format((string.count("G")+string.count("C"))/len(string)*100)



class RNA(__Sequence):

    def __init__(self, sequence):
        super().__init__(sequence)


    def getRNA(self):
        rna_dict = Data.dictionaries("RNA")
        return "".join([rna_dict.get(nucl) for nucl in super().getSequence()])


    def getGCPercentage(self):
        string = self.__sequence.upper()
        return "{:.6}".format((string.count("G")+string.count("C"))/len(string)*100)

    """
    Cant be bothered to fix this now
    def getTranslation(self):

        transDict = Data.dictionaries()
        print(super().getSequence())
        protein_seq_raw = "".join([transDict.get(codon) for codon in (super().getSequence())])

        try:
            protein_seq_stop = re.search("\*", protein_seq_raw)
            protein_seq = protein_seq_raw[0:protein_seq_stop.start()+1]
        except AttributeError:
            protein_seq = protein_seq_raw

        return protein_seq

    """










>>>>>>> 3473eac1e1983baecde5bed80d0f493b48f492fb
