import string

#A very, very simple data aggregator
#it reads each individual "[letter]Players" file in the directory and outputs one aggregated text file

def compileAllDataSets():
    filename = "allPlayers"
    writeTo = open(filename, 'w')
    alphabet = list(string.ascii_lowercase)
    for letter in alphabet:
        filenameOpen = letter + "Players"
        readFrom = open(filenameOpen, 'r')
        for line in readFrom:
            writeTo.write(line)
        readFrom.close()
    writeTo.close()
