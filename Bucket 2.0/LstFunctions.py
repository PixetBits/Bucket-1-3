# NewLst : creates a new lst. If already exists return a error.
# IsALst : checks if the input is an int. Return true or false.
# CToLst : converts a value to int. If can not, return a error.
# fin()  : returns the key of a item in a list or a string.
# add()  : adds a value in a list or string.
# del()  : dels a value from a list or string.
# siz()  : returns the size of a list or string.
# brk()  : breaks in words\items a list or string.

#Error Message
from ErrorMessage import Error

def NewLst(line, actL) : #
    
    #Line for error
    elin = line

    #Values
    name = ""
    vall = {}

    #lst tipe name as items

    #Remove lst keyword
    data = line.replace(line[0:4], "")

    #Get the keyword index
    index = data.find(" as ")
    vName = data[:index].strip()
    value = data[index + 4:].strip()

    #Type

    try : #

        words = vName.split()
        ltype = words[0]
        vName = words[1]
    #

    except :
        Error("[Sintax Error] Missing list type after variable name.", "lin", elin)

    #Name
    if vName in actL : Error("[Compiler Error] This name already exits as lst.", "lin", elin)
    else : name = vName
    
    #Value

    #Other list
    if value in actL : #
        
        other = actL[value]

        if other[""] == ltype : vall = other
        else : Error("Your value is a list of other type.", "lin", elin)
    #

    else : #

        #Have no square brackets
        if not "[" in value or not "]" in value : Error("[Syntax Error] No square brackets to init the list.", "lin", elin)
        
        else : #

            #Remove square brackets
            value = value.replace("[", "")
            value = value.replace("]", "")

            #Break in words
            value = value.split(",")

            #value = index : value

            #Set value and index
            for item in value : #
            
                index = item.find(":")

                lstI = item[:index].strip()
                lstV = item[index + 1:].strip()

                try : #
                    
                    #A list of int's
                    if ltype == "int" : lstV = int(lstV)
                    
                    #A list of str's
                    if ltype == "str" : #
                        
                        if lstV.startswith("'") and lstV.endswith("'") : #
                            
                            #Empty
                            if lstV == "''" : lstV = ""
                            
                            #Remove apostrophos
                            else : lstV = lstV[1:len(lstV) - 1]
                        #
                        
                        else : Error("[Compiler Error] This is not a str value.", "lin", elin)
                    #

                    #A list of bol's
                    if ltype == "bol" : #

                        if lstV == "yes" : lstV = True
                        elif lstV == "not" : lstV = False
                        else : Error("[Sintax Error] This is not a bol value.", "lin", elin)

                    #A list of flt's
                    if ltype == "flt" : #
                        
                        if lstV.endswith(".f") :

                            lstV = lstV.replace(".f", "")
                            lstV = float(lstV)
                        
                        else : Error("[Sintax Error] This is not a flt value.", "lin", elin)
                    #

                    #Add value
                    vall.update({lstI : lstV})
                #

                except :
                    Error("[Sintax Error] One of these values are not a " + ltype + ".", "lin", elin)
            #
        #
    #

    #Add list type
    vall.update({"" : ltype})

    #Add variable
    return {name : vall}
#

def IsALst(vall, actL) : #

    #A declareted lst
    if vall in actL : return True
    
    #A unpacked list
    elif vall.startswith("[") and vall.endswith("]") :

        if ":" in vall : return True
        elif vall == "[]" : return True
    
    else : return False
#

def Fin(line, elin, actS, actL) : #

    word = line.split()
    #item[0] in[1] list[2] to[3] var[4]

    #Missed keywords
    if not word[1] == "in" : Error("[Sintax Error] Missed \"in\" keyword.", "lin", elin)
    if not word[3] == "to" : Error("[Sintax Error] Missed \"to\" keyword.", "lin", elin)

    #Check item

    #A str
    if word[0].startswith("'") and word[0].endswith("'") : word[0] = word[0].replace("'", "")

    #A variable
    elif word[0] in actS : word[0] = actS[word[0]]
    
    #Nothing
    else : Error("[Compiler Error] This value is not a str to find.", "lin", elin)

    #If is asking for a char in strg
    if word[2] in actS : #

        #Return index if it exists
        if word[0] in actS[word[2]] : return actS[word[2]].find(word[0])
        else : return ""
    #

    #If is asking for a item in list
    if word[2] in actL : #
        
        #Ask for every item
        for index in actL[word[2]].keys() : #
            
            if actL[index] == word[0] : return index
        #

        return -1
    #
#

def Add(line, elin, actL) : #

    word = line.split()

    #add item[0] on[1] list[2] as[3] value[4]
    
    #Missed keywords
    if not word[1] == "on" : Error("[Sintax Error] Missed \"on\" keyword." "lin", elin)
    if not word[3] == "as" : Error("[Sintax Error] Missed \"as\" keyword." "lin", elin)

    #Existent item
    elif word[0] in actL[word[2]] : Error("[Compiler Error] Your list already have this item.", "lin", elin)
    
    #Alright
    else : #
        
        try : #

            #Add to a int list
            if actL[word[2]][""] == "int" : return {word[0] : int(word[4])}

            #Add to a str list
            elif actL[word[2]][""] == "str" :
                
                if word[4].startswith("'") and word[4].endswith("'") : return {word[0] : word[4].replace("'", "")}
                else : Error("[Compiler Error] This is not a string list's item.", "lin", elin)

            #Add to a int list
            elif actL[word[2]][""] == "bol" :
                
                if word[5] == "yes" : return {word[0] : True}
                elif word[5] == "not" : return {word[0] : False}
                else : Error("[Compiler Error] This is not a boolean list's item.", "lin", elin)

            #Add to a int list
            elif actL[word[3]][""] == "flt" : return {actL[word[3]][word[0]] : float(word[5].replace(".f", ""))}
        #

        except TypeError :
            Error("[Compiler Error] Your list do not suport this value.", "lin", elin)
    #
#

def Del(line, elin, actL) : #

    word = line.split()

    #del index[0] of[1] list[2]

    #Missed keywords
    if not word[1] == "of" : Error("[Sintax Error] Missed \"of\" keyword." "lin", elin)
    
    #Delete the variable
    elif word[0] in actL[word[2]] : del actL[word[2]][word[0]]
    else : Error("[Compiler Error] Your list do not have this item.", "lin", elin)

    return actL
#

def Siz(line, elin, cLst) : #

    word = line.split()
    #of[0] list[1] ~[2] var[3]

    #Missed keywords
    if not word[0] == "of" : Error("[Sintax Error] Missed \"of\" keyword." "lin", elin)
    if not word[2] == "to" : Error("[Sintax Error] Missed \"to\" keyword." "lin", elin)

    #Return size
    if type(cLst) == str : return {word[3] : len(cLst)}
    else : return {word[3] : len(cLst) - 1}
#

def Brk(line, elin, actS) : #

    word = line.split()

    #brk string[0] in[1] word[2] to[3] var[4]

    #Wrong keywords
    if word[1] != "in" : Error("[Sintax Error] Missed \"in\" keyword." "lin", elin)
    if word[3] != "to" : Error("[Sintax Error] Missed \"to\" keyword." "lin", elin)

    #Create dict
    keywd = word[2].replace("'", "")
    
    #Special codes
    if keywd == "\\s" : keywd = " "
    if keywd == "\\q" : keywd = "\""
    if keywd == "\\n" : keywd = "\n"
    if keywd == "\\t" : keywd = "\t"

    spltd = actS[word[0]].split(keywd)

    index = 0
    retrn = {"0" : "0",}

    for w in spltd : #

        retrn[str(index)] = w
        index = index + 1
    #

    #If not
    return {word[4] : retrn}
#