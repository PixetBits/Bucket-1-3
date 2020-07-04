# for t loop : make something t times while is True.
# every loop : make something using every item in an
# list.

#Error Message
from ErrorMessage import Error

def NewForLoop(frst, lines, actI) : #

    #Loop data: c count| max cnt| question| variable| start l| end line|
    loopKey = {"m" : 0, "q" : "", "v" : "", "s" : frst + 1, "e" : 0}

    #Get the loop line
    mainL = lines[frst]

    #What is the question
    mainL = mainL.replace("for ", "")
    index = mainL.find(" times ")

    #The question to enable
    loopKey["q"] = mainL[index + len(" times "):]
    loopKey["q"] = loopKey["q"].replace("if ", "")

    #Missed keyword
    if loopKey["q"].endswith(" do:") : loopKey["q"] = loopKey["q"].replace(" do:", "")
    else : Error("[Sintax Error] Missed \"do:\" keyword.", "lin", lines[loopKey["s"]])

    line = mainL.split()

    #x[0] times[1] if[2] y[3] ~ z do:

    #The max count
    try :
        loopKey["m"] = int(line[0])

    except : #

        if line[0] in actI : loopKey["m"] = actI[line[0]]
        else : Error("[Compiler] The [times] argment need be a int.", "lin",  lines[loopKey["s"]])
    #

    #The name of variable
    loopKey["v"] = line[3]

    #Find index
    for l in range(0, len(lines)) : #

        #End of task block
        if lines[l] == "end l." and l > frst : #

            loopKey["e"] = l
            return loopKey
        #

        if l == len(lines) - 1 and loopKey["e"] == 0 : Error("[Syntax Error] No loop ender.", "lin", lines[0])
    #
#

def NewEveryLoop(frst, lines, actL) : #

    #Loop data: max cnt|var name| var list| start l| end line|
    loopKey = {"v" : "", "l" : "", "s" : frst + 1, "e" : 0}

    #Get the loop line
    line = lines[frst]

    #What is the question
    line = line.replace("every ", "")
    word = line.split()

    #every item[0] in[1] list[2] do:

    #This list do not exists
    if not word[2] in actL : Error("[Compiler Error] This is not a declareted list.", "lin", lines[frst])
    else : loopKey["l"] = word[2]

    #The name of variable
    loopKey["v"] = word[0]

    #The list of values
    loopKey["l"] = actL[word[2]]

    #Find index
    for l in range(0, len(lines)) : #

        #End of task block
        if lines[l] == "end l." and l > frst : #

            loopKey["e"] = l
            return loopKey
        #

        if l == len(lines) - 1 and loopKey["e"] == 0 : Error("[Syntax Error] No loop ender.", "lin", lines[0])
    #
#