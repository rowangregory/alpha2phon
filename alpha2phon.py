import sys
phonetics = {"A": "Alfa", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo", "F": "Foxtrot", "G": "Golf", "H": "Hotel",
             "I": "India", "J": "Juliet", "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar", "P": "Papa",
             "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango", "U": "Uniform", "V": "Victor", "W": "Whiskey",
             "X": "X-ray", "Y": "Yankee", "Z": "Zulu", "1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five",
             "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine", "10": "Ten", "Ø": "Zero"}
howToUse = '''alpha2phon is a terminal utility to turn characters into their NATO phonetic versions.
usage: alpha2phon [ARGUMENTS]'''
# Join each phoneticized argument to the "output" variable
output = []
if len(sys.argv) != 1: # Has the user provided more than one argument?
    for argument in sys.argv[1:]:
        #Debug purposes: print(argument)
        for convertedLetter in argument:
            #Debug purposes: print(convertedLetter)
            output.append(phonetics[convertedLetter.upper()])
    # Display all the words in a normal manner, not everyone understands ["H", "E", ...]
    print(" ".join(output))
else: # No? Alright then, display how it should be used.
    print(howToUse)
