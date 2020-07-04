# Renove all lines wich starts with "--" and ends with "--".

#Error
from ErrorMessage import Error

#wildcard
import re

def Remove(line) : #

    opnC = ""
    clsC = ""
    
    #Fix spaces
    words = line.split()

    for word in words : #

        if word.startswith("--") and word != "--" : line = line.replace(word, word.replace("--", "-- "))
        if word.endswith("--") and word != "--" : line = line.replace(word, word.replace("--", " --"))
    #

    #Definition
    opnD = re.compile("-- .")
    clsD = re.compile(". --")

    #Get slices
    opnC = opnD.findall(line)
    clsC = clsD.findall(line)

    opnC = line.find(opnC[0])
    clsC = line.find(clsC[len(clsC) - 1]) + len(clsC[len(clsC) - 1])

    #Remove
    line = line.replace(line[opnC:clsC], "")

    return line
#