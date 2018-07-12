# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 10:53:47 2018

@author: user
"""

class Sequence():
    """========================================================================
    Sequence object contains a sequence as the self.seq string. It
    allows modification of said string and provides information about it.
    
    methods: .seq, .seqpath, .gc, .data, .cstrand, .rev, .codons
    
    also used by: compare()
    
    source values: file (tries to open a file), 
                   input (asks for input and creates a file automatically),
                   random (creates a file containing a random sequence)
    ========================================================================"""
                   

    def __init__(self,seqpath,source="file"):
        """self.seqpath, self.gc and self.seq are automatically defined"""
                       
        self.seqpath=seqpath #unnecessary, maybe delete later
            
        def _create_from_input_(seqpath):
            new=input("Enter sequence:\n> ")
            seq=""
            for nt in new:
                if nt == "\n" or nt == " ":
                    pass
                else:
                    seq += nt
            file = open(seqpath, 'w')
            print(seq,file=file)
            print(f"{seqpath} registered. See help(Sequence) for methods to check information about the sequence.")
            file.close()
            return seq
            
        def _create_random_(seqpath):
            seq = randomseq(3000)
            file = open(seqpath, 'w')
            print(seq,file=file)
            print(f"{seqpath} registered. See help(Sequence) for methods to check information about the sequence.")
            file.close()
            return seq

        # =====================================================================
        #         OPTION 1 - try to open a file. it offers other options
        # =====================================================================
        if source == "file":            
            try:
                file = open(self.seqpath)
                seq=""
                for nt in file.read():
                    if nt == "\n":
                        pass
                    else:
                        seq += nt
                print(f"{seqpath} registered. See help(Sequence) for methods to check information about the sequence.")
                file.close()

            except:
                rep = input(f"File {self.seqpath} doesn't exist. Create from sequence? (y/n)\n> ")
                if rep.upper() == "Y":
                    seq = _create_from_input_(self.seqpath)
            
                else:
                    rep = input("Create file with random sequence? (y/n)\n> ")
                    if rep.upper() == "Y":
                        seq = _create_random_(self.seqpath)
                        
        # =====================================================================
        #         OPTION 2 - create file from input
        # =====================================================================
        elif source == "input":
            seq = _create_from_input_(self.seqpath)

        # =====================================================================
        #         OPTION 3 - create file with random sequence
        # =====================================================================
        elif source == "random":
            seq = _create_random_(self.seqpath)
                
        self.seq = seq        
        self.gc = self._gc_()
        
    def _gc_(self,decimals=5):
        """Returns GC-content as a percentage. It's possible to specify the
        desired decimals."""
        gc = 0
        at = 0
        
        for nt in self.seq.upper():
            if nt == "G" or nt == "C":
                gc += 1
            elif nt == "A" or nt == "T":
                at += 1
                
        contgc = round(gc / len(self.seq) * 100,decimals)
        
        return contgc
    
    
        
    def data(self):
        """Prints basic information: length and GC-content"""
        
        import pandas as pd
                
        data = pd.DataFrame({"Length" : len(self.seq),"GC-content (%)" : self.gc},index=["Value"])
        
        print(data)
        
        
        
        
    def cstrand(self):
        """Returns the complementary strand of the given sequence as a string"""
        
        nt = {"A":"T","T":"A","G":"C","C":"G"}
        strand = ""

        for letter in self.seq:
            strand += nt.get(letter.upper())

        return strand    
    
    
    
    
    def rev(self):
        """Returns the sequence in reverse order"""
        
        i = 0
        rev = ""
        
        while i < len(self.seq):
            i += 1
            rev += self.seq[-i]
        
        return rev
            
    
    
    def codons(self):
        """Goes over the three possible reading frames of the sequence and 
        returns the codon count of each one of them. Highlights stop codons."""

        from collections import Counter
        import pandas as pd

        frame1 = []
        frame2 = []
        frame3 = []

        i = 0

        while True:
            frame1.append(self.seq[i:i+3].upper()) #when i = 0, it takes nt 0,1 and 2
            frame2.append(self.seq[i+1:i+4].upper()) #when i = 0, it takes nt 1, 2 and 3
            frame3.append(self.seq[i+2:i+5].upper()) #when i = 0, it takes nt 2, 3 and 4

            i+=3

            if not frame3[-1]: #when it's done reading self.seq
                break

        fdict1 = Counter(frame1)
        fdict2 = Counter(frame2)
        fdict3 = Counter(frame3)

        f1 = pd.DataFrame(fdict1, index = ["Frame 1"])
        f2 = pd.DataFrame(fdict2, index = ["Frame 2"])
        f3 = pd.DataFrame(fdict3, index = ["Frame 3"])

        df = f1.transpose().join(f2.transpose(),how="outer")
        df = df.join(f3.transpose(),how="outer") #puts together the 3 RF


#        def highlight_codons(s):
#            """Highlights the stop codon counts: the correct reading frame has
#            only one"""
#            color = 'turquoise'
#            return 'background-color: %s' % color
#
#        df = df.style.applymap(highlight_codons, subset=pd.IndexSlice[["TAG","TAA","TGA"], :])
#        
# un-comment for jupyter notebook only!!
        from IPython.display import display
        
        with pd.option_context('display.max_rows', None): #shows the whole table
            display(df)
    
    
    
    
#These functions are not Sequence methods:    
def compare(list):
    """Returns a bar graph with GC-content values of a list of Sequence objects
    side by side with the GC-content of the genome of model organisms"""

    import pandas as pd
    import matplotlib.pyplot as plt

    species = {"Plasmodium falciparum":[20],
               "Arabidopsis thaliana":[36],
               "Saccharomyces cerevisiae":[38],
               "Streptomyces coelicolor":[72]
              }
    
    index = 0
    for i in list:
        index += 1 #this is just a given tag for each object of the list
        species[str(index)] = [i.gc]

    
    df = pd.DataFrame(data=species)
        
    df.plot(kind='bar',title="GC-content comparison",colormap="viridis_r",grid=True)
    
    plt.show()

    
    
def randomseq(length=3000):
    """Creates random DNA sequences of a given length"""
    
    import random
    
    nt = 'AGCT'
    seq = ''
    for i in [int((4*random.random())) for i in range(length)]:
        seq += nt[i]
    
    return seq



#These functions directly take a string as an argument and not a Sequence object
def cstrand(seq):
    """Returns the complementary strand of the given sequence as a string"""

    nt={"A":"T","T":"A","G":"C","C":"G"}
    strand=""

    for letter in seq:
        if letter == "\n":
            pass
        strand += nt.get(letter.upper())

    return strand


def rev(string):
    """Returns the sequence in reverse order"""

    i = 0
    rev = ""

    while i < len(string):
        i += 1
        rev += string[-i]

    return rev