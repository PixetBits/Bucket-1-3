# LogicDoor() : Returns True if the statlement is true and
# False if statlement if false or it's diferent var types.

#Errpr Message
from ErrorMessage import Error

def LogicBlk(line, elin, actV) : #

    #Break
    word = []

    #In equals
    if "equals" in line : #
        
        index = line.find("equals")
        word = [line[:index].strip(), "equals", line[index + len("equals"):].strip()]
    #

    #In unlike
    if "unlike" in line : #
        
        index = line.find("unlike")
        word = [line[:index].strip(), "unlike", line[index + len("unlike"):].strip()]
    #

    #In greater
    if "greater" in line : #
        
        index = line.find("greater")
        word = [line[:index].strip(), "greater", line[index + len("greater"):].strip()]
    #

    #In smaller
    if "smaller" in line : #
        
        index = line.find("smaller")
        word = [line[:index].strip(), "smaller", line[index + len("smaller"):].strip()]
    #

    #In amost+
    if "amost+" in line : #
        
        index = line.find("amost+")
        word = [line[:index].strip(), "amost+", line[index + len("amost+"):].strip()]
    #

    #In amost+
    if "amost-" in line : #
        
        index = line.find("amost-")
        word = [line[:index].strip(), "amost-", line[index + len("amost-"):].strip()]
    #

    #if var[0] cond[1] val[2] do:

    frstArg = ""
    scndArg = ""

    #First Arg
    try : 
        frstArg = actV[word[0]]

    except KeyError :
        Error("[Compiler Error] The first argment needs be a variable, not a value.", "lin", elin)

    #Second Arg
    try :
        scndArg = actV[word[2]]

    except KeyError : #

        #Two int's
        if actV[""] == "int" : #
            
            try :
                scndArg = int(word[2])

            except :
                Error("[Compiler Error] Both argments need be ints.", "lin", elin)
        #

        #Two str's
        elif actV[""] == "str" : #
            
            if word[2].startswith("'") and word[2].endswith("'") : scndArg = word[2].replace("'", "")
            else : Error("[Compiler Error] Both argments need be strs.", "lin", elin)
        #

        #Two bol's
        elif actV[""] == "bol" : #

            if word[2] == "yes" : scndArg = True
            elif word[2] == "not" : scndArg = False
            else : Error("[Compiler Error] Both argments need be bols.", "lin", elin)
        #

        #Two flt's
        elif actV[""] == "flt" : #

            try :

                word[2] = word[2].replace(".f", "")
                scndArg = float(word[2])
            
            except :
                Error("[Compiler Error] Both argments need be flts.", "lin", elin)
        #

        else : Error("[Compiler Error] Second argment isn't a variable or a value.", "lin", elin)
    #

    #Return centense result
    if word[1] == "equals" : return frstArg == scndArg
    if word[1] == "unlike" : return frstArg != scndArg

    if word[1] == "greater" : return frstArg > scndArg
    if word[1] == "smaller" : return frstArg < scndArg

    if word[1] == "amost+" : return frstArg >= scndArg
    if word[1] == "amost-" : return frstArg <= scndArg
#