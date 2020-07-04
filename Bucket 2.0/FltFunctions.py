# NewFlt : creates a new flt. If already exists return a error.
# SetFlt : updates the value of an flt. If cannot return error.
# IsAFlt : checks if the input is an flt. Return true or false.
# CToFlt : converts a value to flt. If can not, return a error.
# roundT : turns a flt in a int and return the int val rounded.

#Error Message
from ErrorMessage import Error

def NewFlt(line, actF) : #

    #Line for error
    elin = line

    #Values
    name = ""
    vall = ""

    #flt name as value.f

    #Remove flt keyword
    data = line.replace(line[0:4], "")
    
    #Get the keyword index
    try : #
    
        index = data.find(" as ")
        vName = data[:index].strip()
        value = data[index + 4:].strip()
    #

    except :
        Error("[Sintax Error] Missed \"as\" keyword.", "lin", elin)

    #Name
    if vName in actF : Error("[Compiler Error] This name already exits as flt.", "lin", elin)
    else : name = vName

    #Value
    try :

        value = value.replace(".f", "")
        vall = float(value)
    
    except ValueError :

        if value in actF : vall = actF[value]
        else : Error("[Compiler Error] Bad value to assignment.", "lin", elin)
    
    #Add variable
    return {name : vall}
#

def SetFlt(line, actF) : #

    #Line for error
    elin = line

    #Values
    name = ""
    vall = ""

    #set name to value

    #Remove int keyword
    data = line.replace(line[0:4], "")
    
    #Get the keyword index
    index = data.find(" to ")
    name = data[:index].strip()
    vall = data[index + 4:].strip()

    #Value
    try :

        vall = vall.replace(".f", "")
        vall = float(vall)
    
    except ValueError :

        if vall in actF : vall = actF[vall]
        else : Error("[Compiler Error] Bad value to assignment.", "lin", elin)
    
    #Update variable
    return {name : vall}
#

def IsAFlt(vall, actF) : #

    #An number
    try :

        vall = vall.replace(".f", "")
        float(vall)
        return True

    #An variable
    except ValueError :

        if vall in actF : return True
        else : return False
#

def CToFlt(vall, line) : #

    try :

        return float(vall)

    except ValueError:

        Error("[Compiler Error] Bucket cannot convert this.", "lin", line)
#

def RoundT(vall, line, actF) : #

    #round var

    #An existent flt
    if vall in actF : return round(actF[vall])
    else : Error("[Compiler Error] Cannot round a nonexistent variable.", "lin", line)
#