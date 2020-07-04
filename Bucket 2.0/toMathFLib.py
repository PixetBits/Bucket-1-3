#Error Message
from ErrorMessage import Error

#Math functions
import math
import random as rand

def Main(line, actI, actF) : #

    #Sin
    if "sin[" in line : #
        
        #sin[x]

        sIndex = line.find("sin[")
        eIndex = line.find("]", sIndex)

        syntax = line[sIndex:eIndex + 1]

        sValue = syntax.replace("sin[", "")
        sValue = sValue.replace("]", "")

        #Value
        try : #

            #Float
            if sValue.endswith(".f") : #

                sValue = sValue.replace(".f", "")
                sValue = float(sValue)
            #

            #Int
            else : sValue = int(sValue)
        #

        #Variable
        except TypeError : #
            
            if sValue in actI : sValue = actI[sValue]
            elif sValue in actF : sValue = actF[sValue]
            else : Error("[Compiler Error] This is not a declareted variable.", "lin", line)
        #
        
        #Get sin of
        value = math.sin(sValue)

        #Even if it's an int, turn on float
        return line.replace(syntax, str(value)[:5] + ".f")
    #

    #Cos
    elif "cos[" in line : #
        
        #sin[x]

        sIndex = line.find("cos[")
        eIndex = line.find("]", sIndex)

        syntax = line[sIndex:eIndex + 1]

        sValue = syntax.replace("cos[", "")
        sValue = sValue.replace("]", "")

        #Value
        try : #

            #Float
            if sValue.endswith(".f") : #

                sValue = sValue.replace(".f", "")
                sValue = float(sValue)
            #

            #Int
            else : sValue = int(sValue)
        #

        #Variable
        except TypeError : #
            
            if sValue in actI : sValue = actI[sValue]
            elif sValue in actF : sValue = actF[sValue]
            else : Error("[Compiler Error] This is not a declareted variable.", "lin", line)
        #
        
        #Get sin of
        value = math.cos(sValue)

        #Even if it's an int, turn on float
        return line.replace(syntax, str(value)[:5] + ".f")
    #

    #Tan
    elif "tan[" in line : #
        
        #sin[x]

        sIndex = line.find("tan[")
        eIndex = line.find("]", sIndex)

        syntax = line[sIndex:eIndex + 1]

        sValue = syntax.replace("tan[", "")
        sValue = sValue.replace("]", "")

        #Value
        try : #

            #Float
            if sValue.endswith(".f") : #

                sValue = sValue.replace(".f", "")
                sValue = float(sValue)
            #

            #Int
            else : sValue = int(sValue)
        #

        #Variable
        except TypeError : #
            
            if sValue in actI : sValue = actI[sValue]
            elif sValue in actF : sValue = actF[sValue]
            else : Error("[Compiler Error] This is not a declareted variable.", "lin", line)
        #
        
        #Get sin of
        value = math.tan(sValue)

        #Even if it's an int, turn on float
        return line.replace(syntax, str(value)[:5] + ".f")
    #

    #Random
    elif "rand[" in line : #

        #rand[x][y]

        #Find function
        sIndex = line.find("rand[")
        eIndex = line.find("]", sIndex)

        #Separe
        syntax = line[sIndex:eIndex + 1]

        #Get just the numbers
        argmts = syntax.replace("rand[", "")
        argmts = argmts.replace("]", "")
        
        #Break in the comma
        argmts = argmts.split(",")
        argmts = [arg.strip() for arg in argmts]

        #[x]
        fValue = argmts[0]

        #Value
        try : #

            #Float
            if fValue.endswith(".f") : #

                fValue = fValue.replace(".f", "")
                fValue = float(fValue)
            #

            #Int
            else : fValue = int(fValue)
        #

        #Variable
        except ValueError : #
            
            if fValue in actI : fValue = actI[fValue]
            elif fValue in actF : sValue = actF[fValue]
            else : Error("[Compiler Error] This is not a declareted variable.", "lin", line)
        #

        #[y]
        sValue = argmts[1]

        #Value
        try : #

            #Float
            if sValue.endswith(".f") : #

                sValue = sValue.replace(".f", "")
                sValue = float(sValue)
            #

            #Int
            else : sValue = int(sValue)
        #

        #Variable
        except ValueError : #
            
            if sValue in actI : sValue = actI[sValue]
            elif sValue in actF : sValue = actF[sValue]
            else : Error("[Compiler Error] This is not a declareted variable.", "lin", line)
        #

        #Generate random number
        try :
            value = rand.randrange(fValue, sValue)
            
        except :
            Error("[Compiler Error] One of these variables are not int's or flt's.", "sys", line)

        if type(value) == float : return line.replace(syntax, str(value)[:5] + ".f")
        else : return line.replace(syntax, str(value))
    #

    #No keyword
    else : return line
#