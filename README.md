# ntinfo
ntinfo includes functions similar to those of CUSP and the Reverse Complement online tool. This script also comes with a supplementary GUI (ntitk.py). Saved as a \*.lnk file, everything is just a click away (including help).

⚠️ This repository was first uploaded on *Jul 13, 2018* (the history was rewritten later). It was my first Python project - actually, my first ever project, even before my Master's, so don't judge

## Details

ntinfo includes the Sequence class, which matches \*.txt (not \*.fa) files that contain DNA sequences. If you try to create a Sequence object from a file that doesn't exist, you can create it on the go from a given sequence or from a random sequence instantly created (with the "randomseq()" function).

Sequence methods:
- .seqpath (returns the file path of the object)
- .seq (returns the sequence)
- .gc (returns GC-content as a 5 decimal percentage)
- .cstrand() (returns the complementary strand)
- .rev() (returns the reversed sequence)
- .data() (returns a table with the GC-content and the length of the sequence)
- .codons() (returns a table with the codon usage of the sequence for each of the three possible reading frames,
   has commented code with highlights stop codons but only works in Jupyter)

ntinfo also includes:
- compare(): its argument is a list of Sequence objects. It plots them side by side with some fixed values (model organisms)
- randomseq(length): returns a random DNA sequence
- cstrand(str): returns the complementary sequence of a given string
- rev(str): returns the complementary sequence of a given string


## Getting Started
Just copypaste the files wherever you want/have your modules.

### Prerequisites
Requisites for ntinfo.py:
> python 3

> IPython.display, collections

> matplotlib, pandas, random (Anaconda recomended)

Requirements for the GUI:
> tkinter (eg. "conda install tk". You may find this link useful: https://stackoverflow.com/questions/20044559/how-to-pip-or-easy-install-tkinter)


## Built With
conda:  4.5.4

python: 3.6.4
