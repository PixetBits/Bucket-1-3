#Exit
from sys import exit as end

def Error(message, type, *line) : #

    if type == "sys" : print(message)

    if type == "lin" :
        
        line = str(line)

        line = line.replace("('", "")
        line = line.replace("',)", "")

        line = line.replace("(\"", "")
        line = line.replace("\",)", "")

        print("\n" + message + "\nLine [" + line + "].")

    EndL()
#

def EndL() : #

    input("\nPress enter to exit.\n")
    end()
#