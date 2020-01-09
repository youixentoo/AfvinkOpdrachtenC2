# Naam:
# Datum:
# Versie:

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand, met 5 tot 10 fasta's. Ga je runnen met het echte bestand, geef je programma dan even de tijd.


# Aanroepen van de functies
def main():
    bestand="GCF_000164845.2_Vicugna_pacos-2.0.2_rna.fna"
    try:
        headers, seqs = lees_inhoud(bestand)

        zoekwoord = input("Geef een zoekwoord op: ")
        zoeken(headers, seqs, zoekwoord)

    except FileNotFoundError:
        print("File not found or not ending in .fna.")


# Het zoeken van het opgegeven zoekwoord in de header.
def zoeken(headers, seqs, zoekwoord):
    print(headers[0:10])
    print("------\n\n-------")
    print(seqs[0:10])

    for i in range(len(headers)):
        if zoekwoord in headers[i]:
            print("Header:",headers[i])
            check_is_dna = Is_Dna(seqs[i])
            if check_is_dna:
                print("Sequentie is DNA")
                knipt(seqs[i])
            else:
                print("Sequentie is geen DNA. Er is iets fout gegaan.")


# Bestand uitlezen en de headers en sequenties eruit halen.
def lees_inhoud(bestands_naam):

    headers = []
    seqs = []
    seq = ""

    # Check of het bestand wel endigt op .fna
    if not bestands_naam.endswith(".fna"):
        raise FileNotFoundError

    bestand = open(bestands_naam)

    for line in bestand :
        line = line.strip()
        if ">" in line :
            if seq != "" :
                seqs.append(seq)
                seq = ""
                headers.append(line)
        else :
            seq += line.strip()
    seqs.append(seq)

    return headers, seqs


# Check of de sequentie wel dna is
def Is_Dna(seq):
    Dna = False
    a = seq.count("A")
    t = seq.count("T")
    c = seq.count("C")
    g = seq.count("G")
    total = a+t+c+g
    if total == len(seq):
        Dna = True
    return Dna


# Checkt voor elke regel in het bestand of deze in de sequentie knipt.
def knipt(alpaca_seq):
    bestand = open("enzymen.txt")
    for line in bestand:
        naam,seq=line.split(" ")
        seq = seq.strip().replace("^","")
        if seq in alpaca_seq:
            print(naam, "knipt in sequentie")


# Aanroepen van de main
if __name__ == "__main__":
    main()
=======
# Naam:
# Datum:
# Versie:

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand, met 5 tot 10 fasta's. Ga je runnen met het echte bestand, geef je programma dan even de tijd.

def main():
    bestand="GCF_000164845.2_Vicugna_pacos-2.0.2_rna.fna"
    try:
        headers, seqs = lees_inhoud(bestand)

        zoekwoord = input("Geef een zoekwoord op: ")
        zoeken(headers, seqs, zoekwoord)

    except FileNotFoundError:
        print("File not found or not ending in .fna.")

def zoeken(headers, seqs, zoekwoord):
    print(headers[0:10])
    print("------\n\n-------")
    print(seqs[0:10])

    for i in range(len(headers)):
        if zoekwoord in headers[i]:
            print("Header:",headers[i])
            check_is_dna = Is_Dna(seqs[i])
            if check_is_dna:
                print("Sequentie is DNA")
                knipt(seqs[i])
            else:
                print("Sequentie is geen DNA. Er is iets fout gegaan.")


def lees_inhoud(bestands_naam):

    headers = []
    seqs = []
    seq = ""

    if not bestands_naam.endswith(".fna"):
        raise FileNotFoundError

    bestand = open(bestands_naam)

    for line in bestand :
        line = line.strip()
        if ">" in line :
            if seq != "" :
                seqs.append(seq)
                seq = ""
                headers.append(line)
        else :
            seq += line.strip()
    seqs.append(seq)

    return headers, seqs


def Is_Dna(seq):
    Dna = False
    a = seq.count("A")
    t = seq.count("T")
    c = seq.count("C")
    g = seq.count("G")
    total = a+t+c+g
    if total == len(seq):
        Dna = True
    return Dna


def knipt(alpaca_seq):
    bestand = open("enzymen.txt")
    for line in bestand:
        naam,seq=line.split(" ")
        seq = seq.strip().replace("^","")
        if seq in alpaca_seq:
            print(naam, "knipt in sequentie")


if __name__ == "__main__":
    main()
>>>>>>> 3473eac1e1983baecde5bed80d0f493b48f492fb
