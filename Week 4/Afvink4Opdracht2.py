# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 16:15:25 2019

@author: gebruiker
"""
import re
import time

import fix_linebreaks

# Aanroepen van de functies, met de tijd dat het duurt om deze uit te voeren.
def main():
    startRead = time.time()
    headers, sequences = lees_fasta_bestand()
    endRead = time.time()

    startIt = time.time()
    DNA_it =isDNA_iteratief(sequences[0])
    endIt = time.time()

    startReg = time.time()
    DNA_reg = isDNA_regex(sequences[0])
    endReg = time.time()

    print("Iteration method says DNA=%s, Regex method says DNA=%s" % (DNA_it, DNA_reg))
    print("Time to read and process the file: %s\n\nIteration time: %s\nRegex time: %s" % (str(endRead-startRead), str(endIt - startIt), str(endReg-startReg)))


# Inlezen van het bestand en het ophalen van de data.
def lees_fasta_bestand():
    file_name = "Mus_musculus.GRCm38.dna.chromosome.19.fa" # Had na een kwartier geen zin meer om op chrom 1 te wachten
    location = "Data"
    file = open(location+"/"+file_name)

    return fix_linebreaks.get_headers_and_sequences(file, ">")


# Checkt iteratief of de sequentie uit dna bestaat.
def isDNA_iteratief(sequentie):
    dna = True
    for nucl in sequentie:
        if not nucl in "ATGC":
            dna = False

    return dna


# Checkt met een regex of de sequentie uit dna bestaat.
def isDNA_regex(sequentie):
    result = re.search("^[ATGC]*$", sequentie)
    if result == None:
        return False
    else:
        return True


# Aanroepen van de main.
if __name__ == "__main__":
    main()
=======
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 16:15:25 2019

@author: gebruiker
"""
import re
import time

import fix_linebreaks

def main():
    startRead = time.time()
    headers, sequences = lees_fasta_bestand()
    endRead = time.time()

    startIt = time.time()
    DNA_it =isDNA_iteratief(sequences[0])
    endIt = time.time()

    startReg = time.time()
    DNA_reg = isDNA_regex(sequences[0])
    endReg = time.time()

    print("Iteration method says DNA=%s, Regex method says DNA=%s" % (DNA_it, DNA_reg))
    print("Time to read and process the file: %s\n\nIteration time: %s\nRegex time: %s" % (str(endRead-startRead), str(endIt - startIt), str(endReg-startReg)))


def lees_fasta_bestand():
    file_name = "Mus_musculus.GRCm38.dna.chromosome.19.fa" # Had na een kwartier geen zin meer om op chrom 1 te wachten
    location = "Data"
    file = open(location+"/"+file_name)

    return fix_linebreaks.get_headers_and_sequences(file, ">")


def isDNA_iteratief(sequentie):
    dna = True
    for nucl in sequentie:
        if not nucl in "ATGC":
            dna = False

    return dna


def isDNA_regex(sequentie):
    result = re.search("^[ATGC]*$", sequentie)
    if result == None:
        return False
    else:
        return True


if __name__ == "__main__":
    main()
>>>>>>> 3473eac1e1983baecde5bed80d0f493b48f492fb
