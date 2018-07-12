# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 12:47:05 2018

@author: user
"""

import ntinfo as nti
import tkinter as tk

# =============================================================================
#  Window and geometry
# =============================================================================

window = tk.Tk()
window.geometry("507x280")

# =============================================================================
# greeting :)
# =============================================================================
greeting = tk.Label(window,
                     text="Hello, user! Please select what you want to do:",
                     fg="black",
                     bg="lightgrey")
greeting.grid(row=0,column=1,columnspan=2)

# =============================================================================
# Frames
# =============================================================================
frame1 = tk.Frame(window,
                  background="SlateBlue1",
                  padx=10,
                  pady=10)

label1 = tk.Label(frame1,
         text="Obtain sequences on the\ngo (no saving)").grid(row=0, column=1)

frame1.grid(row=1,column=1)

# =============================================================================

frame2 = tk.Frame(window,
                  background="coral1",
                  padx=10,
                  pady=10)


label2 = tk.Label(frame2,
                  text="Create and save sequences").grid(row=0,column=1)

frame2.grid(row=1,column=2)

# =============================================================================

frame3 = tk.Frame(window,
                 background="OliveDrab3",
                 padx=10,
                 pady=10)

lael3 = tk.Label(frame3,
                 text="Obtain information from\nexisting files").grid(row=0,column=1)

frame3.grid(row=1,column=3)

# =============================================================================
# #widget: reverse seq from input
# =============================================================================
def btn1comm(): 
    seq = input("\nEnter your sequence:\n> ")
    revv = nti.rev(seq)
    print(f"\nReversed sequence:\n{revv}")

btn1 = tk.Button(frame1,
                 text="Reverse sequence",
                 bg="lavender",
                 fg="SlateBlue4",
                 command = btn1comm)
btn1.grid(row=1,column=1)


# =============================================================================
# #widget: complementary sequence
# =============================================================================
def btn2comm(): 
    seq = input("\nEnter your sequence:\n> ")
    comp = nti.cstrand(seq)
    print(f"\nComplementary sequence:\n{comp}")

btn2 = tk.Button(frame1,
                 text="Complementary sequence",
                 bg="lavender",
                 fg="SlateBlue4",
                 command=btn2comm)
btn2.grid(row=2,column=1)

# =============================================================================
# widget: create sequence from input (*.txt)
# =============================================================================
def btn3comm():
    seqpath = input("File name:\n> ")
    nti.Sequence(seqpath,"input")

btn3 = tk.Button(frame2,
                 text="Create file from input",
                 bg="beige",
                 fg="coral4",
                 command=btn3comm)

btn3.grid(row=1,column=1)

# =============================================================================
# widget: create random sequence (*.txt)
# =============================================================================
def btn4comm():
    seqpath = input("File name:\n> ")
    nti.Sequence(seqpath,"random")

btn4 = tk.Button(frame2,
                 text="Create random sequence",
                 bg="beige",
                 fg="coral4",
                 command=btn4comm)

btn4.grid(row=2,column=1)


# =============================================================================
# widget: .data
# =============================================================================

def btn5comm():
    seqpath = input("File name:\n> ")
    temp = nti.Sequence(seqpath,"file")
    print("\n")
    temp.data()

btn5 = tk.Button(frame3,
                 text="Show sequence\ndata",
                 bg="DarkOliveGreen1",
                 fg="OliveDrab4",
                 command=btn5comm)

btn5.grid(row=2,column=1)
# =============================================================================
# widget: gc
# =============================================================================

def btn6comm():
    seqpath = input("File name:\n> ")
    temp = nti.Sequence(seqpath,"file")
    print("\n")
    print(f"GC-content of {seqpath} is {temp.gc}%")

btn6 = tk.Button(frame3,
                 text="GC-content",
                 bg="DarkOliveGreen1",
                 fg="OliveDrab4",
                 command=btn6comm)

btn6.grid(row=1,column=1)

# =============================================================================
# widget: codons!
# =============================================================================

def btn7comm():
    seqpath = input("File name:\n> ")
    temp = nti.Sequence(seqpath,"file")
    temp.codons()

btn7 = tk.Button(frame3, 
                 text="Show codon usage",
                 bg="DarkOliveGreen1",
                 fg="OliveDrab4",
                 command=btn7comm)

btn7.grid(row=3,column=1)

# =============================================================================
# widget: compare!!!
# =============================================================================
def btn8comm():
    seqpath_list = [str(seqpath) for seqpath in input('List of sequences to compare, separated by spaces\n(eg.: "example1.txt example2.txt"):\n> ').split()]
    #separa en el input segun lo que haya entre () en el split (un espacio!)
    temp = []
    for seqpath in seqpath_list:
        temp.append(nti.Sequence(seqpath,"file"))
    nti.compare(temp)
    

btn7 = tk.Button(frame3, 
                 text="Compare sequences",
                 bg="DarkOliveGreen1",
                 fg="OliveDrab4",
                 command=btn8comm)

btn7.grid(row=4,column=1)

# =============================================================================
# widget: reverse
# =============================================================================
def btn9comm():
    seqpath = input("File name:\n> ")
    temp = nti.Sequence(seqpath,"file")
    rev_temp = temp.rev()
    print(f"Reversed sequence:\n{rev_temp}")

btn7 = tk.Button(frame3, 
                 text="Reverse sequence",
                 bg="DarkOliveGreen1",
                 fg="OliveDrab4",
                 command=btn9comm)

btn7.grid(row=5,column=1)

# =============================================================================
# widget: complementary sequence
# =============================================================================
def btn10comm():
    seqpath = input("File name:\n> ")
    temp = nti.Sequence(seqpath,"file")
    comp_temp = temp.cstrand()
    print(f"Complementary sequence:\n{comp_temp}")

btn7 = tk.Button(frame3, 
                 text="Complementary sequence",
                 bg="DarkOliveGreen1",
                 fg="OliveDrab4",
                 command=btn10comm)

btn7.grid(row=6,column=1)

# =============================================================================
# widget: help(Sequence)
# =============================================================================

def btn_help_comm():
    print("""The options on the left work on input sequences.The options
on the right work on files. If they don't exist, they can be
created. 

|| Left Menu||
-> "Reverse sequence" returns the reversed sequence.
-> "Complementary sequence" returns the complementary strand

|| Central menu ||
-> "Create file from input" asks for an input by the user and
   this as a *.txt file with a given name
-> "Create random sequence" creates a random 3000-long DNA
   sequence
   
|| Right Menu ||
-> "GC-content" returns GC-content as a 5 decimal percentage
-> "Show sequence data" returns a table with the GC-content
   and the length of the sequence
-> "Show codon usage" returns a table with the codon usage
   of the sequence for each of the three possible reading
   frames
-> "Reverse sequence" returns the reversed sequence.
-> "Complementary sequence" returns the complementary strand""")

btn_help = tk.Button(window,
                     text="help(Sequence)",
                     bg="LemonChiffon1",
                     fg="LemonChiffon4",
                     command=btn_help_comm)

btn_help.grid(row=2,column=2)
# =============================================================================
# Extra: codonTable().py
# =============================================================================
#import codonTable as ct

#codons = ct.codonTable()


# =============================================================================
# Giving control to the window:
# =============================================================================
window.mainloop()
