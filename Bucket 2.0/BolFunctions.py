"""
NewBol : create a new int. If already exists return a error.
CnBBol : check if a declaration of a bol has a good bol val.
IsABol : check if the input is an int. Return true or false.
CToBol : convert a value to int. If can not, return a error.
ifelse : if-else system for check sencences with true-false.
"""

#Error Message
from ErrorMessage import Error

def NewBol(line, actB) : #

    elin = line

    name = ""
    vall = ""

    #Remove int keyword
    data = line.replace("bol ", "")
    
    #Get the keyword index
    try : #

        index = data.index(" as ")
        vName = data[:index]
        value = data[index + len(" as "):]
    #

    except :
        Error("[Sintax Error] Missed \"as\" keyword.", "lin", elin)

    #Name
    if vName in actB : Error("[Compiler Error] This name already exits as bol.", "lin", elin)
    else : name = vName

    #Value
    if value == "yes" : vall = True
    elif value == "not" : vall = False
    elif value in actB : vall = actB[value]
    else : Error("[Compiler Error] Bad value to assignment.", "lin", elin)

    #Add variable
    return {name : vall}
#

def SetBol(line, actB) : #

    elin = line

    name = ""
    vall = ""

    #Remove int keyword
    data = line.replace("set ", "")
    
    #Get the keyword index
    index = data.index(" to ")
    name = data[:index]
    vall = data[index + len(" to "):]

    #Value
    if vall == "yes" : vall = True
    elif vall == "not" : vall = False
    elif vall in actB : vall = actB[vall]
    else : Error("[Compiler Error] Bad value to assignment.", "lin", elin)

    #Add variable
    return {name : vall}
#

def IsABol(vall, actB) : #

    if vall == "yes" or vall == "not" : return True
    elif vall in actB : return True
#

def CToBol(vall, line) : #

    #Yes
    if vall == "yes" : return True
    if vall == "Yes" : return True
    elif vall == "1" : return True
    elif vall == "true" : return True
    elif vall == "True" : return True
    
    #Not
    elif vall == "not" : return False
    elif vall == "Not" : return False
    elif vall == "0" : return False
    elif vall == "false" : return False
    elif vall == "False" : return False
    
    #Error
    else : Error("[Compiler Error] Bucket do not understand this value as bol.", "lin", line)
# 