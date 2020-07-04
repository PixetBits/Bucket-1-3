# NewInt : creates a new int. If already exists return a error.
# CnBInt : checks if a declaration of a int has a good int val.
# IsAInt : checks if the input is an int. Return true or false.
# CToInt : converts a value to int. If cannot, return an error.
# make() : makes a operation with a variable and another value.

#Error Message
from ErrorMessage import Error

def NewInt(line, actI) : #

    #Error line
    elin = line

    #Values
    name = ""
    vall = ""

    #int name as value

    #Remove int keyword
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
    if vName in actI : Error("[Compiler Error] This name already exits as int.", "lin", elin)
    else : name = vName

    #Value
    try :
        vall = int(value)
    
    except ValueError : #

        if value in actI : vall = actI[value]
        else : Error("[Compiler Error] Bad value to assignment.", "lin", elin)
    #

    #Add variable
    return {name : vall}
#

def SetInt(line, actI) : #

    #Error line
    elin = line

    #Values
    name = ""
    vall = ""

    #set name to value

    #Remove int keyword
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
    try :

        vall = int(vall)
    
    except ValueError :

        if vall in actI : vall = actI[vall]
        else : Error("[Compiler Error] Bad value to assignment.", "lin", elin)
    
    #Update variable
    return {name : vall}
#

def IsAInt(vall, actI) : #

    #An number
    try : #

        int(vall)
        return True
    #

    #An variable
    except ValueError : #

        if vall in actI : return True
        else : return False
    #
#

def CToInt(vall, line) : #

    try : #
        
        #An flt
        if vall.endswith(".f") : #
            
            vall = vall.replace(".f")
            return round(int(vall))
        #

        #Other else
        else : return int(vall)
    #

    except ValueError:
        Error("[Compiler Error] Bucket cannot convert this.", "lin", line)
#

def Make(line, elin, actV) : #

    #Booleans
    if actV[""] == "bol" : Error("Booleans are binary, so they cannot be different of 0 or 1.", "lin", elin)

    arg = line.split()

    #make var[0] ~[1] val[2]

    #Variable to change
    try : #

        var = actV[arg[0]]
        val = ""
        opr = arg[1]
    #

    #No operator
    except IndexError :
        Error("[Syntax Error] No operator in the scentence.", "lin", elin)

    #Value

    try :
        val = actV[arg[2]]
    
    except KeyError : #

        #int's
        if actV[""] == "int" : val = int(arg[2])

        #str's and int's
        elif actV[""] == "str" : #

            if opr == "*" : #

                try :    
                    val = int(arg[2])
                
                except :
                    Error("[Syntax Error] Cannot multiply a string by other type except int.", "lin", elin)
            #

            #Default value
            elif opr == "+" : val = arg[2].replace("'", "")
            elif opr == "-" : val = arg[2].replace("'", "")
        #

        #Remove sufix of flt's
        elif actV[""] == "flt" : #
            
            arg[2] = arg[2].replace(".f", "")
            val = float(arg[2])
        #

        #Not an variable or value
        else : Error("[Compiler Error] Just variables of the same type or str's and int's.", "lin", elin)
    #

    #Special codes
    if "\\s" in val : val = val.replace("\\s", " ")
    if "\\q" in val : val = val.replace("\\q", "\"")
    if "\\n" in val : val = val.replace("\\n", "\n")
    if "\\t" in val : val = val.replace("\\t", "\t")

    #sum
    if opr == "+" : return {arg[0] : var + val}
    
    #sub
    if opr == "-" : #
        
        #An string
        if actV[""] == "str" : return {arg[0] : var.replace(val, "")}
        
        #Other else
        else : return {arg[0] : var - val}
    #

    #mul
    if opr == "*" : return {arg[0] : var * val}

    #div
    if opr == "/" : #
        
        if actV[""] == "str" : Error("[Compiler Error] Cannot divide an string.", "lin", elin)
        else : return {arg[0] : var / val}
    #

    #res
    if opr == "%" : #

        if actV[""] == "str" : Error("[Compiler Error] Cannot divide an string.", "lin", elin)
        else : return {arg[0] : var % val}
    #

    #Elv
    if opr == "^" : #

        if actV[""] == "str" : Error("[Compiler Error] Cannot elevate an string.", "lin", elin)
        else : return {arg[0] : var ** val}
    # 
#

def Rise(line, actV) : #

    #Error line
    elin = line

    #Remove rise keyword
    line = line.replace("rise ", "")

    #Get the keyword index
    try : #

        index = line.find(" in ")
        vName = line[:index]
        value = line[index + len(" in "):]
    #

    except :
        Error("[Sintax Error] Missed \"in\" keyword." "lin", elin)

    if not vName in actV : Error("[Compiler Error] Bucket cannot rises a non existent variable.", "lin", elin)
    
    else : #

        try : #

            #Two int's
            if actV[""] == "int" : return {vName : actV[vName] + int(value)} 

            #Two int's
            if actV[""] == "flt" : #
                
                if value.endswith(".f") : return {vName : actV[vName] - float(value.replace(".f", ""))}
                else : Error("[Compiler Error] Just values of the same tyipe.", "lin", elin)
            #
        #

        except TypeError :

            Error("This is not a numeric value.", "lin", elin)
    #
#

def Down(line, actV) : #

    #Error line
    elin = line

    #Remove rise keyword
    line = line.replace("rise ", "")

    #Get the keyword index
    try : #

        index = line.find(" in ")
        vName = line[:index]
        value = line[index + len(" in "):]
    #

    except :
        Error("[Sintax Error] Missed \"in\" keyword." "lin", elin)

    if not vName in actV : Error("[Compiler Error] Bucket cannot make down a non existent variable.", "lin", elin)
    
    else : #
        
        try : #
            
            #Two int's
            if actV[""] == "int" : return {vName : actV[vName] - int(value)} 

            #Two int's
            if actV[""] == "flt" : #
                
                if value.endswith(".f") : return {vName : actV[vName] - float(value.replace(".f", ""))}
                else : Error("[Compiler Error] Just values of the same tyipe.", "lin", elin)
            #
        #

        except TypeError :

            Error("This is not a numeric value.", "lin", elin)
    #
#