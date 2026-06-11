import sys
normal = {"A": "Alfa", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo", "F": "Foxtrot", "G": "Golf", "H": "Hotel",
             "I": "India", "J": "Juliet", "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar", "P": "Papa",
             "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango", "U": "Uniform", "V": "Victor", "W": "Whiskey",
             "X": "X-ray", "Y": "Yankee", "Z": "Zulu", "1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five",
             "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine", "10": "Ten", "Ø": "Zero"}
variant = {"A": "Alfa", "B": "Bravo", "C": "Charlie", "D": "[Delta, David, Dixie]", "E": "Echo", "F": "[Foxtrot, Fox]", "G": "Golf", "H": "[Hawk, Hotel]",
             "I": "[India, Indigo]", "J": "Juliet", "K": "Kilo", "L": "[Lima, London]", "M": "Mike", "N": "November", "O": "Oscar", "P": "Papa",
             "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango", "U": "Uniform", "V": "Victor", "W": "Whiskey",
             "X": "X-ray", "Y": "Yankee", "Z": "Zulu", "1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five",
             "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine", "10": "Ten", "Ø": "Zero"}
def convert(type, stringLocation):
    for argument in sys.argv[stringLocation:]:
        #Debug purposes: print(argument)
        for convertedLetter in argument:
            #Debug purposes: print(convertedLetter)
            output.append(type[convertedLetter.upper()])
        # Display all the words in a normal manner, not everyone understands ["H", "E", ...]
    print(" ".join(output))
howToUse = '''alpha2phon is a terminal utility to turn characters into their NATO phonetic versions.
usage: alpha2phon [ -v ] [STRINGS]...

Options:
    -v			print out possible alternative variants to letters (i.e. Indigo instead of India, David instead of Delta, etc.)

By default, alpha2phon acts as if there were only the strings given as arguments.'''
# Join each phoneticized argument to the "output" variable
output = []
if len(sys.argv) != 1: # Has the user provided more than one argument?
    match sys.argv[1]:
        case "-v":
            convert(variant, 2)
        case _:
            convert(normal, 1)
else: # No? Alright then, display how it should be used.
    print(howToUse)
