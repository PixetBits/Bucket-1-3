# NewStr : create a new str. If already exists return a error.
# CnBFlt : check if a declaration of a int has a good int val.
# IsAStr : check if the input is an str. Return true or false.
# CToStr : convert a value to str. All values can turn in str.
# sand() : get the input (bin) from user. Can get a string on.

#Error Message
from ErrorMessage import Error

def NewStr(line, actS) : #

    #Line for error
    elin = line

    #Values
    name = ""
    vall = ""

    #str name as value/sand with arg

    #Remove str keyword
    data = line.replace(line[0:4], "")
    
    #Get the keyword index
    try : #

        index = data.index(" as ")
        vName = data[:index].strip()
        value = data[index + 4:].strip()
    #

    except :
        Error("[Sintax Error] Missed \"as\" keyword.", "lin", elin)

    #Name
    if vName in actS : Error("[Compiler Error] This name already exits as str.", "lin", elin)
    else : name = vName

    #Value

    #Other str
    if value in actS : vall = actS[value]
    
    #Normal string
    elif value.startswith("'") and value.endswith("'") : #
        
        #Empty
        if value == "''" : vall = ""
        
        #Remove apostrophos
        else : vall = value[1:len(value) - 1]
    #
    
    #Input
    elif value.startswith("sand ") : vall = Sand(value, elin, actS)

    #Error
    else : Error("[Compiler Error] Bad value to assignment.", "lin", elin)
    
    #Add variable
    return {name : vall}
#

def SetStr(line, actS) : #

    #Line for error
    elin = line

    #Values
    name = ""
    vall = ""

    #set name to value/sand with arg

    #Remove str keyword
    data = line.replace(line[0:4], "")
    
    #Get the keyword index
    try : #

        index = data.index(" to ")
        name = data[:index].strip()
        vall = data[index + 4:].strip()
    #

    except :
        Error("[Sintax Error] Missed \"to\" keyword." "lin", elin)

    #Value
    
    #Other str
    if vall in actS : vall = actS[vall]
    
    #Normal string
    elif vall.startswith("'") and vall.endswith("'") :
        
        #Empty
        if vall == "''" : vall = ""
        
        #Remove apostrophos
        else : vall = vall[1:len(vall) - 1]
    #
    
    #Input
    elif vall.startswith("sand ") : vall = Sand(vall, elin, actS)

    #Error
    else : Error("[Compiler Error] Bad value to assignment.", "lin", elin)
    
    #Update variable
    return {name : vall}
#

def IsAStr(vall, actS) : #

    if vall.startswith("'") and vall.endswith("'") : return True
    elif vall in actS : return True
    else : return False
#

def CToStr(vall) : #

    return str(vall)
#

def Sand(line, orgn, actS) : #

    elin = line
    Input = ""

    #Remove keyword
    line = line.replace("sand ", "")

    #Arg
    if "with " in line :
        
        line = line.replace("with ", "")

        if line in actS : Input = input(actS[line])
        elif line.startswith("'") and line.endswith("'") : Input = input(line.replace("'", ""))
        else : Error("[Compiler Error] sand do not recived the argment.", "lin", elin)

    #Just input
    else : Input = input()

    return Input
#