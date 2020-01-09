<<<<<<< HEAD
# DNA object
class DNA():
    import sys
    # Dit is de locatie van het script dat wordt geimporteerd in de getRNA() methode.
    sys.path.append("D:\School\Python\Course 2 Eerste Jaars\Week 5\Bonus")

    def __init__(self, sequence, header="null"):
        self.__sequence = sequence
        self.__header = header


    def __str__(self):
        return "{}{}".format(self.__header, self.__sequence)


    def setDNA(self, sequence):
        self.__sequence = sequence


    def getDNA(self):
        return self.__sequence


    def getRNA(self):
        from Data import dictionaries
        rna_dict = dictionaries("RNA")
        return "".join([rna_dict.get(nucl) for nucl in self.__sequence])


    def getLength(self):
        return len(self.__sequence)


    def getGCPercentage(self):
        string = self.__sequence.upper()
        return "{:.6}".format((string.count("G")+string.count("C"))/len(string)*100)
=======
class DNA():
    import sys
    sys.path.append("D:\School\Python\Course 2 Eerste Jaars\Week 5\Bonus")
    
    def __init__(self, sequence, header="null"):
        self.__sequence = sequence
        self.__header = header
        
    
    def __str__(self):
        return "{}{}".format(self.__header, self.__sequence)
        
               
    def setDNA(self, sequence):
        self.__sequence = sequence
        
        
    def getDNA(self):
        return self.__sequence
    
    
    def getRNA(self):
        from Data import dictionaries
        rna_dict = dictionaries("RNA")
        return "".join([rna_dict.get(nucl) for nucl in self.__sequence])
    
    
    def getLength(self):
        return len(self.__sequence)
    
    
    def getGCPercentage(self):
        string = self.__sequence.upper()
        return "{:.6}".format((string.count("G")+string.count("C"))/len(string)*100)
   
>>>>>>> 3473eac1e1983baecde5bed80d0f493b48f492fb
