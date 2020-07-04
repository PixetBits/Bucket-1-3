#Error Message
from ErrorMessage import Error

#Comments
from DellComments import Remove

def GetTasks(lines, name) : #

#Fix-Lines------------------------------------------------------------------------------------------------------#

    #Remove comments
    for l in range(0, len(lines)) : #
    
        if "--" in lines[l] : lines[l] = Remove(lines[l])
    #

    #Remove strange chars
    lines = [l.replace("\n", "") for l in lines]
    lines = [l.replace("\t", "") for l in lines]
    lines = [l.replace("  ", "") for l in lines]
    lines = [l.strip() for l in lines]

    #Non usable lines
    lines = [l for l in lines if l != ""]

#---------------------------------------------------------------------------------------------------------------#

    #Declare class
    if lines[0].startswith("#") : #

        if lines[0] == name + " in Playground:" : del lines[0]
        else : Error("[Syntax Error] The class name must be the same of the file.", "lin", lines[l])
    #

    #No class
    else : Error("[Compiler Error] No class declareted.", "sys")

    #End
    if lines[len(lines) - 1] == "close." : del lines[len(lines) - 1]
    else : Error("[Syntax Error] Class block was not closet.", "sys")

    #Then
    return lines
#

def SupervisorDad(lines, name) : #

#Fix-Lines------------------------------------------------------------------------------------------------------#

    #Remove comments
    for l in range(0, len(lines)) : #
    
        if "--" in lines[l] : lines[l] = Remove(lines[l])
    #

    #Remove strange chars
    lines = [l.replace("\n", "") for l in lines]
    lines = [l.replace("\t", "") for l in lines]
    lines = [l.replace("  ", "") for l in lines]
    lines = [l.strip() for l in lines]

    #Non usable lines
    lines = [l for l in lines if l != ""]

#---------------------------------------------------------------------------------------------------------------#

    #Outside

    #Declare class
    if lines[0].startswith("dad ") : #

        if lines[0] == "dad " + name + ":" : del lines[0]
        else : Error("[Syntax Error] The class name must be the same of the file.", "lin", lines[l])
    #

    #No class
    else : Error("[Compiler Error] No class declareted.", "sys")

    #End
    if lines[len(lines) - 1] == "close." : del lines[len(lines) - 1]
    else : Error("[Syntax Error] Class block was not closed.", "sys")

    #Inside

    #You shoud have:
    if lines[0] == "shoud:" : del lines[0]
    else : Error("This dad has no obligations.", "sys")

    #End
    if lines[len(lines) - 1] == "close s." : del lines[len(lines) - 1]
    else : Error("[Syntax Error] Shoud block was not closed.", "sys")

    #Then
    return lines
#