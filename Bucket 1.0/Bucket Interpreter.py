
#_Bucket Compiler by Pixet Bits {Version : 1.0.0.0}_---------------------------#

import random as rand

#Libraries
LibCtrls = {"[B]" : False, "[F]" : False, "[C]" : False}

#Objects
SfSystVr = {"FLCnt" : 0}

ActivInt = {}
ActivStr = {}
ActivBol = {}
ActivFlt = {}
IfElseSy = {"Result" : "", "inCent" : "", "isIf" : "", "isEl" : False, "Enable" : False}
ActivMth = {"inMain" : False, "inTask" : False, "CallIt" : False}
ActivTsk = {}

#_Principal_-------------------------------------------------------------------#

def Compiler(FileName) : #

    Name = FileName.replace(".bk", "")

    try :
        
        File = open(FileName)
        Lines = File.readlines()
        File.close()

    except FileNotFoundError : Error("File ["+Name+"] not found", "")

    #Tab and Enter
    Lines = [l.replace("  ", "") for l in Lines]
    Lines = [l.replace("\n", "") for l in Lines]
    Lines = [l.replace("\t", "") for l in Lines]

    #Blank lines and Coments
    Lines = [l for l in Lines if l != ""]
    Lines = [l for l in Lines if not l.startswith("//")]

    if Lines[0] != "[to Basic]" : Error("All Bucket classes need [to Baisc] library", Lines[0])
    
    for y in range(0, len(Lines)) :

        #Tab error
        if Lines[y].startswith(" ") : Error("Tab error", Lines[y])

        #Class Error
        if Lines[y].endswith("in Bucket :") :

            if Lines[y].startswith(Name) : continue
            else : Error("Namespace of class is wrong", Lines[y])
            
        #Vars
        if Lines[y].startswith("int ") : Int(Lines[y])
        if Lines[y].startswith("str ") : Str(Lines[y])
        if Lines[y].startswith("bol ") : Bol(Lines[y])
        if Lines[y].startswith("flt ") : Flt(Lines[y])

        #Methods
        if "task :" in Lines[y] : NewTask(Lines, y)
    #
    
    Runner(Lines)
#

def Runner(lines) : #
    
    for x in range(0, len(lines)) : #

        #bucket open
        if lines[x] == "bucket open :" : ActivMth["inMain"] = True

        #any task
        if "task :" in lines[x] : ActivMth["inTask"] = True

        #Output
        if lines[x].startswith("show ") :
            
            if ActivMth["inMain"] == True : Show(lines[x])
            elif ActivMth["inTask"] == True : continue
            else : Error("Funtion out of an method", lines[x])

        #Call an Task
        if lines[x].startswith("call ") :

            if ActivMth["inMain"] == True : TaskCtrl(lines, lines[x])
            else : Error("Only 'bucket open' can call tasks", lines[x])

        #Set
        if lines[x].startswith("set ") :
            
            if ActivMth["inMain"] == True : Set(lines[x])
            elif ActivMth["inTask"] == True : continue
            else : Error("Funtion out of an method", lines[x])

        #Make
        if lines[x].startswith("make ") :
            
            if ActivMth["inMain"] == True : Make(lines[x])
            elif ActivMth["inTask"] == True : continue
            else : Error("Funtion out of an method", lines[x])

        #Up
        if lines[x].startswith("up ") :

            if ActivMth["inMain"] == True : Up(lines[x])
            elif ActivMth["inTask"] == True : continue
            else : Error("Funtion out of an method", lines[x])

        #Convert
        if lines[x].startswith("convert ") :

            if ActivMth["inMain"] == True : Convert(lines[x])
            elif ActivMth["inTask"] == True : continue
            else : Error("Funtion out of an method", lines[x])
        
        #If-Else system

        #If
        if lines[x].startswith("if ") :

            if ActivMth["inMain"] == True :

                IfElseSy["inCent"] = True
                IfElseSy["isIf"] = True
                IfElseSy["Result"] = If(lines[x])
                
            elif ActivMth["inTask"] == True : continue
            else : Error("Funtion out of an method", lines[x])

        #Else
        elif lines[x].startswith("else ") and IfElseSy["Result"] == False :

            if ActivMth["inMain"] == True :

                IfElseSy["inCent"] = True
                IfElseSy["isEl"] = True
                
            elif ActivMth["inTask"] == True : continue
            else : Error("Funtion out of an method", lines[x])

        #End of statlement
        
        #Do System
        if lines[x].startswith("do : ") and IfElseSy["inCent"] == True : #

            line = lines[x].replace("do : ", "")

            #Is if?
            if IfElseSy["isIf"] == True and IfElseSy["Result"] == True : IfElseSy["Enable"] = True

            #Is Else?
            if IfElseSy["isEl"] == True and IfElseSy["Result"] == False : IfElseSy["Enable"] = True

            #Then
            if IfElseSy["Enable"] == True :
                
                #Functions
                if line.startswith("show ") : Show(line)
                if line.startswith("call ") : ActivMth["CallIt"] = True
                if line.startswith("set ") : Set(line)
                if line.startswith("up ") : Up(line)

                #Errors
                if line.startswith("int ") : Error("If-else systems cannot declare vars", line)
                if line.startswith("str ") : Error("If-else systems cannot declare vars", line)
                if line.startswith("bol ") : Error("If-else systems cannot declare vars", line)
                if line.startswith("flt ") : Error("If-else systems cannot declare vars", line)
        #

        #Compiler errors
        elif lines[x].startswith("do : ") and not IfElseSy["inCent"] == False : Error("Do out o if statlement", lines[x])

        #For loop
        if lines[x].startswith("for ") :

            lLine = lines[x].replace("for ", "")
            limit = lLine.find("times ")
            count = lLine[:limit]

            #N° Times
            try : count = int(count)
            except ValueError :

                if count in ActivInt : count = ActivInt[count]
                else : Error("For loop needs an int", lines[x])

            #Loop
            ForLoop(lines, x, count, lLine.replace(lLine[:limit + 6], ""))
                    
        #Enders
        if lines[x] == "finish" :

            IfElseSy["inCent"] = False
            IfElseSy["Enable"] = False
            
            IfElseSy["isIf"] = False
            IfElseSy["isEl"] = False
            
        if lines[x] == "end l." : ActivMth["inMain"] = False
        if lines[x] == "end t." : ActivMth["inTask"] = False
    #

    return 0
#

def Error(ErrorType, Line) : #
    
    print("\nCompiler error {"+ErrorType+"}\nin line : \""+str(Line)+"\"")
    return 0
#

#_If-Else System_--------------------------------------------------------------#

def If(string) : #

    String = (string.replace("if ", "")).replace("then :", "")
    String = String.replace(" ", "")
    
    limit = ""

    isG = False
    isL = False
    isE = False

    isGoE = False
    isLoE = False

    #Common
    if ">" in String :

        isG = True
        limit = String.find(">")
        
        
    if "<" in string :

        isL = True
        limit = String.find("<")

    #Equal
    if "==" in String :

        isE = True
        limit = String.find("==")

    #Or Equal's
    if "<=" in String :

        isGoE = True
        limit = String.find("<=")
        
    if ">=" in String :

        isLoE = True
        limit = String.find(">=")

#------------------------------------------------------------------------------#

    #This is greather than?
    if isG == True :

        FstArg = String[:limit]
        SstArg = String[limit + 1:]

        #1st Arg

        #Declareted Vars
        if FstArg in ActivInt : FstArg = ActivInt[FstArg]
        elif FstArg in ActivFlt : FstArg = ActivFlt[FstArg]

        #Int
        elif not FstArg.endswith(".f") :
        
            try : FstArg = int(FstArg)
            except ValueError : Error("Unknow value", string)

        #Float
        else :

            FstArg = FstArg.replace(".f", "")
            
            try : FstArg = float(FstArg)
            except ValueError : Error("Unknow value", string)

#------------------------------------------------------------------------------#

        #2st Arg

        #Declareted Vars
        if SstArg in ActivInt : SstArg = ActivInt[SstArg]
        elif SstArg in ActivFlt : SstArg = ActivFlt[SstArg]

        #Int
        elif not SstArg.endswith(".f") :
        
            try : SstArg = int(SstArg)
            except ValueError : Error("Unknow value", string)

        #Float
        else :

            SstArg = SstArg.replace(".f", "")
            
            try : SstArg = float(SstArg)
            except ValueError : Error("Unknow value", string)

        #Finally
        if FstArg > SstArg : return True
        else :return False

#------------------------------------------------------------------------------#

    #This is less than?
    elif isL == True :
        
        FstArg = String[:limit]
        SstArg = String[limit + 1:]

        #1st Arg

        #Declareted Vars
        if FstArg in ActivInt : FstArg = ActivInt[FstArg]
        elif FstArg in ActivFlt : FstArg = ActivFlt[FstArg]

        #Int
        elif not FstArg.endswith(".f") :
        
            try : FstArg = int(FstArg)
            except ValueError : Error("Unknow value", string)

        #Float
        else :

            FstArg = FstArg.replace(".f", "")
            
            try : FstArg = float(FstArg)
            except ValueError : Error("Unknow value", string)

#------------------------------------------------------------------------------#

        #2st Arg

        #Declareted Vars
        if SstArg in ActivInt : SstArg = ActivInt[SstArg]
        elif SstArg in ActivFlt : SstArg = ActivFlt[SstArg]

        #Int
        elif not SstArg.endswith(".f") :
        
            try : SstArg = int(SstArg)
            except ValueError : Error("Unknow value", string)

        #Float
        else :

            SstArg = SstArg.replace(".f", "")
            
            try : SstArg = float(SstArg)
            except ValueError : Error("Unknow value", string)

        #Finally
        if FstArg < SstArg : return True
        else : return False

#------------------------------------------------------------------------------#

    elif isE == True :

        FstArg = String[:limit]
        SstArg = String[limit + 2:]

        #1st Arg

        #Declareted Vars
        if FstArg in ActivInt : FstArg = ActivInt[FstArg]
        elif FstArg in ActivStr : FstArg = ActivStr[FstArg]
        elif FstArg in ActivFlt : FstArg = ActivFlt[FstArg]

        #String
        elif FstArg.startswith("'") : FstArg = FstArg.replace("'", "")
        elif FstArg.startswith("\"") : Error("Strings must be in ''", string)

        #Int
        elif not FstArg.endswith(".f") :
        
            try : FstArg = int(FstArg)
            except ValueError : Error("Unknow value", string)

        #Float
        else :

            FstArg = FstArg.replace(".f", "")
            
            try : FstArg = float(FstArg)
            except ValueError : Error("Unknow value", string)

#------------------------------------------------------------------------------#

        #2st Arg

        #Declareted Vars
        if SstArg in ActivInt : SstArg = ActivInt[SstArg]
        elif SstArg in ActivStr : SstArg = ActivStr[SstArg]
        elif SstArg in ActivFlt : SstArg = ActivFlt[SstArg]

        #String
        elif SstArg.startswith("'") : SstArg = SstArg.replace("'", "")
        elif SstArg.startswith("\"") : Error("Strings must be in ''", string)

        #Int
        elif not SstArg.endswith(".f") :
        
            try : SstArg = int(SstArg)
            except ValueError : Error("Unknow value", string)

        #Float
        else :

            SstArg = SstArg.replace(".f", "")
            
            try : SstArg = float(SstArg)
            except ValueError : Error("Unknow value", string)
        
        #Finally
        if FstArg == SstArg : return True
        else : return False
    
    else : Error("Bucket cannot check this", string)
#

#_Funtions_--------------------------------------------------------------------#

def Show(string) : #

    String = string.replace("show ", "")

    #Errors
    if String.startswith(" ") : Error("Spacement error", string)
    if String.startswith("\"") : Error("Strings must be in ''", string)

    if String.startswith("'") :

        String = String.replace("'", "")

        #Int Arg
        if "[i]" in String :

            if "with " in String : limit = String.find("with ")
            else : Error("An [i] needs an value", string)

            value = String[limit + 5:]
            String = String.replace(String[limit:], "")

            if value in ActivInt : String = String.replace("[i]", str(ActivInt[value]))
            else : Error("[i] need an int", string)

        #Float Arg
        elif "[f]" in String :

            if "with " in String : limit = String.find("with ")
            else : Error("An [f] needs an value", string)

            value = String[limit + 5:]
            String = String.replace(String[limit:], "")

            if value in ActivFlt : String = String.replace("[f]", str(ActivFlt[value]))
            else : Error("[f] need an int", string)

        #String Arg
        if "[s]" in String :

            if "with " in String : limit = String.find("with ")
            else : Error("An [s] needs an value", string)

            value = String[limit + 5:]
            String = String.replace(String[limit:], "")

            if value in ActivStr : String = String.replace("[s]", str(ActivStr[value]))
            else : Error("[s] need an int", string)

    elif String in ActivStr : String = ActivStr[String]
    else : Error("show needs an string", string)

    print(String)
#

def Sand(string) : #

    if not " with " in string : Error("Sand-construction error", string)

    String = string.replace(" sand", "")
    limit = String.find("with ")
    value = String[limit + 5:]

    if value.startswith("'") : value = value.replace("'", "")
    elif value.startswith("\"") : Error("Strings must be in ''", string)
    elif value in ActivStr : value = ActivStr[value]
    else : Error("This is not an argument to sand", string)
    
    if value != String[limit - 5:] : return input(value)
#

def Set(string) : #

    isAnInt = False
    isAnFlt = False
    isAnStr = False
    isAnBol = False

    String = string.replace("set ", "")
    limit = String.find(" = ")
    VName = String[:limit]
    value = String[limit + 3:]

    #Var Type
    if VName in ActivInt : isAnInt = True
    elif VName in ActivFlt : isAnFlt = True
    elif VName in ActivStr : isAnStr = True
    elif VName in ActivBol : isAnBol = True
    else : Error("Using an inexistent var", string)

    #Int
    if isAnInt == True :

        #Default
        try :
            
            value = int(value)
            ActivInt.update({VName : int(value)})

        except ValueError :

            #Magic Functions
            if value.startswith("random ") :

                value = Random(value)
                ActivInt.update({VName : value})

            #Declareted Var
            elif value in ActivInt : ActivInt.update({VName : ActivInt[value]})
            else : Error("Using an inexistent var", string)

    #Float
    if isAnFlt == True :

        #Default
        try :

            if value.endswith(".f") :

                value = value.replace(".f", "")
                
                value = float(value)
                ActivInt.update({VName : int(value)})

        except ValueError :

            #Declareted Var
            if value in ActivFlt : ActivFlt.update({VName : ActivFlt[value]})
            else : Error("Using an inexistent var", string)

    #String
    if isAnStr == True :

        #Default
        if value.startswith("'") : ActivStr.update({VName : value})
        elif value.startswith("\"") : Error("Strings must be in ''", string)

        #Magic Functions
        elif value == "sand" :

            value = input()
            ActivStr.update({VName : value})

        elif value.startswith("sand with") :

            value = Sand(value)
            ActivStr.update({VName : value})

        #Declareted Var
        elif value in ActivInt : ActivInt.update({VName : ActivStr[value]})
        else : Error("Using an inexistent var", string)

    #Bool
    if isAnBol == True :

        #Default
        if value == "yes" : ActivBol.update({VName : True})
        elif value == "not" : ActivBol.update({VName : False})

        #Declareted Var
        elif value in ActivInt : ActivInt.update({VName : ActivStr[value]})
        else : Error("Using an inexistent var", string)
    
    return 0
#

def Make(string) : #

    String = string.replace("make ", "")
    String = String.replace(" ", "")
    limit = 0

    #Type
    isAnInt = False
    isAnFlt = False
    isAnStr = False

    #Make
    Incremnt = False
    Decremnt = False
    Multiply = False
    Division = False
    LastVall = False
    PowerInt = False

    #Operators
    if "+" in String :

        limit = String.find("+")
        Incremnt = True
    
    if "-" in String :

        limit = String.find("-")
        Decremnt = True
        
    if "*" in String :

        limit = String.find("*")
        Multiply = True
        
    if "/" in String :

        limit = String.find("/")
        Division = True
        
    if "%" in String :

        limit = String.find("%")
        LastVall = True
        
    if "^" in String :

        limit = String.find("^")
        PowerInt = True

    VrName = String[:limit]
    FstArg = String[:limit]
    SstArg = String[limit + 1:]

    #1st Arg

    #Int
    if FstArg in ActivInt :

        FstArg = ActivInt[FstArg]
        isAnInt = True

    #Float
    elif FstArg in ActivFlt :

        FstArg = ActivInt[FstArg]
        isAnFlt = True

    #String
    elif FstArg in ActivStr :

        FstArg = ActivStr[FstArg]
        isAnFlt = True

    else : Error("Make needs an var to change", string)
    
    #2st Arg

    #Int
    if not SstArg.startswith("'") and not SstArg.endswith(".f") :
        
        try : SstArg = int(SstArg)
        except ValueError :


            #Declareted Var
            if SstArg in ActivInt : SstArg = ActivInt[SstArg]
            elif SstArg in ActivFlt : SstArg = ActivFlt[SstArg]
            elif SstArg in ActivStr : SstArg = ActivInt[SstArg]
            else : Error("This is not an value", string)

    #String
    elif SstArg.startswith("'") :

        SstArg = SstArg.replace("'", "")

    #Float
    elif SstArg.endswith(".f") :

        SstArg = SstArg.replace(".f", "")

        try : float(SstArg)
        except ValueError : Error("This is not an float", string)

    else : Error("This is not an value", string)

    #+++
    if Incremnt == True :

        try :

            if isAnInt == True : ActivInt.update({VrName : FstArg + SstArg})
            if isAnFlt == True : ActivFlt.update({VrName : FstArg + SstArg})
            if isAnStr == True : ActivStr.update({VrName : FstArg + SstArg})
            
        except TypeError : Error("Bucket cannot increment this", string)

    #---
    elif Decremnt == True :

        try :

            if isAnInt == True : ActivInt.update({VrName : FstArg - SstArg})
            if isAnFlt == True : ActivFlt.update({VrName : FstArg - SstArg})
            
        except TypeError : Error("Bucket cannot decrement this", string)

    #***
    elif Multiply == True :

        try :

            if isAnInt == True : ActivInt.update({VrName : FstArg * SstArg})
            if isAnFlt == True : ActivFlt.update({VrName : FstArg * SstArg})
            if isAnStr == True : ActivStr.update({VrName : FstArg * SstArg})
            
        except TypeError :

            print(FstArg, SstArg)
            Error("Bucket cannot multiply this", string)
        
    #///
    elif Division == True :

        try :

            #Is an int or float
            result = FstArg / SstArg
            if isinstance(result, int) : ActivInt.update({VrName : result})
            else : ActivFlt.update({VrName : result})
            
        except TypeError : Error("Bucket cannot divide this", string)
            
    #%%%
    elif LastVall == True :

        try :

            if isAnInt == True : ActivInt.update({VrName : FstArg % SstArg})
            if isAnFlt == True : ActivFlt.update({VrName : FstArg % SstArg})
            
        except TypeError : Error("Bucket cannot math this", string)
            
    #^^^
    elif PowerInt == True :

        try :

            if isAnInt == True : ActivInt.update({VrName : FstArg ** SstArg})
            if isAnFlt == True : ActivFlt.update({VrName : FstArg ** SstArg})

        except TypeError : Error("Bucket cannot power this", string)

    #Incorrect estructure
    else : Error("Make have no this operator", string)
#

def Up(string) : #

    isAnInt = False
    isAnFlt = False

    String = string.replace("up ", "")
    String = String.replace(" ", "")

    limit = String.find("in")
    VName = String[:limit]
    value = String[limit + 2:]

    #Var Type
    if VName in ActivInt : isAnInt = True
    elif VName in ActivFlt : isAnFlt = True
    else : Error("Bucket cannot up an not int or not float", string)

    #Int
    if not value.endswith(".f") :

        try :

            value = int(value)
            ActivInt.update({VName : ActivInt[VName] + value})

        except ValueError :

            if value in ActivInt : ActivInt.update({VName : ActivInt[VName] + ActivInt[value]})
            else : Error("Unknow value", string)
    #Float
    else :

        try :

            value = value.replace(".f", "")
            value = float(value)

            ActivFlt.update({VName : ActivFlt[VName] + value})

        except ValueError :

            if value in ActivFlt : ActivFlt.update({VName : ActivFlt[VName] + ActivFlt[value]})
            else : Error("Unknow value", string)
    
    return 0
#

def Convert(string) : #

    String = string.replace("convert ", "")
    String = String.replace(" ", "")
    
    sLimit = String.find("in")
    Convrt = String[:sLimit]
    toType = String[sLimit + 2:]

    #Convert to int
    if toType == "int" :

        try :

            value = ""

            #Float
            if Convrt in ActivFlt :

                value = ActivFlt[Convrt]
                del ActivFlt[Convrt]

            #String
            if Convrt in ActivStr :

                value = ActivStr[Convrt]
                del ActivStr[Convrt]

            #Bool
            if Convrt in ActivBol :

                value = ActivBol[Convrt]

                if value == "yes" : value = "1"
                if value == "not" : value = "0"

                del ActivBol[Convrt]

            ActivInt.update({Convrt : int(value)})
            
        except ValueError : Error("Bucket cannot convert this", string)

    #Convert to float
    elif toType == "flt" :
        
        try :

            value = ""

            #Int
            if Convrt in ActivInt :

                value = ActivInt[Convrt]
                del ActivInt[Convrt]

            #String
            if Convrt in ActivStr :

                value = ActivStr[Convrt]
                del ActivStr[Convrt]

            #Bool
            if Convrt in ActivBol :

                value = ActivBol[Convrt]

                if value == "yes" : value = "1"
                if value == "not" : value = "0"

                del ActivBol[Convrt]

            ActivInt.update({Convrt : float(value)})
            
        except ValueError : Error("Bucket cannot convert this", string)

    elif toType == "str" :

        value = ""

        #Int
        if Convrt in ActivInt :

            value = ActivInt[Convrt]
            del ActivInt[Convrt]

        #Float
        if Convrt in ActivFlt :

            value = ActivFlt[Convrt]
            del ActivFlt[Convrt]

        #Bool
        if Convrt in ActivBol :

            value = ActivBol[Convrt]
            del ActivBol[Convrt]

        ActivStr.update({Convrt : str(value)})

    elif toType == "bol" :

        #Int
        if Convrt in ActivInt :

            value = ActivInt[Convrt]

            if value == 1 : value = True
            elif value == 0 : value = False
            
            del ActivInt[Convrt]

        #String
        if Convrt in ActivStr :

            value = ActivStr[Convrt]

            if value == "yes" : value = True
            elif value == "not" : value = False
            
            del ActivStr[Convrt]

        ActivBol.update({Convrt : value})

    else : Error("This is not and type in Bucket", string)  
#

def Random(string) : #

    Working = True

    #Error
    if not "between" in string :

        Working = False
        Error("random-construction error", string)

    #Initidal control
    String = string.replace("random ", "")
    String = String.replace("between ", "")
    
    limit = String.find(" and ")

    FstArg = String[:limit]
    SstArg = String[limit + 5:]

    #1st Arg
    try : FstArg = int(FstArg)
    
    except ValueError :

        if FstArg in ActivInt : FstArg = ActivInt[FstArg]
        else : Working = False

    #2st Arg
    try : SstArg = int(SstArg)
    
    except ValueError :

        if SstArg in ActivInt : SstArg = ActivInt[SstArg]
        else : Working = False

    if Working == False : Error("random needs two int's", string)
    else : return rand.randrange(FstArg, SstArg)
#

#_Var Types_-------------------------------------------------------------------#

def Int(string) : #

    String = string.replace("int ", "")
    String = String.replace(" ", "")

    limit = String.find("=")
    varNm = String[:limit]
    value = String[limit + 1:]

    #Var already exists
    if varNm in ActivInt : Error("vars with the same name", string)
    else :

        try :

            value = int(value)
            ActivInt.update({varNm : value})

        except ValueError :

            #Errors
            if value.startswith("sand ") : Error("int's cannot have a string value", string)
            if value.startswith("random ") : Error("Magic functions cannot be starter value", string)
            
            #Value is other intriger
            elif value in ActivInt : ActivInt.update({varNm : ActivInt[value]})
            else : Error("Unknow value", string)

    return 0
#

def Str(string) : #

    String = string.replace("str ", "")

    limit = String.find(" = ")
    varNm = String[:limit]
    value = String[limit + 3:]

    #Var already exists
    if varNm in ActivStr : Error("Vars with the same name", string)
    else :

        #String
        if value.startswith("'") :

            value = value.replace("'", "")
            ActivStr.update({varNm : value})

        #Wrong type
        elif value.startswith("\"") : Error("Strings must be in ''", string)

        #Magic Functions
        elif value == "sand" :

            value = input()
            ActivStr.update({varNm : value})

        elif value.startswith("sand with") :

            value = Sand(value)
            ActivStr.update({varNm : value})

        #Value is other string
        elif value in ActivStr : ActivStr.update({varNm : ActivStr[value]})
        else : Error("Value error", string)

    return 0
#

def Bol(string) : #

    String = (string.replace("bol ", "")).replace(" ", "")

    limit = String.find("=")
    varNm = String[:limit]
    value = String[limit:]

    #Var already exists
    if varNm in ActivStr : Error("Vars with the same name", string)
    else :

        #Default Values
        if value == "yes" : ActivBol.update({varNm : True})
        elif value == "not" : ActivBol.update({varNm : False})
            
        #Value is other bool
        elif value in ActivBol : ActivBol.update({varNm : ActivBol[value]})
        else : Error("Value error", string)

    return 0       
#

def Flt(string) : #

    String = (string.replace("flt ", "")).replace(" ", "")

    limit = String.find("=")
    varNm = String[:limit]
    value = String[limit:]

    if value.endswith(".f") : value = value.replace(".f", "")
    else : Error("Floats need end in '.f'", string)

    #Var already exists
    if varNm in ActivInt : Error("Vars with the same name", string)
    else :

        try :

            value = float(value)
            ActivFlt.update({varNm : value})

        except ValueError :
            
            #Value is other float
            if value in ActivFlt : ActivFlt.update({varNm : ActivFlt[value]})
            else : Error("Value error", string)

    return 0
#

#_Task_------------------------------------------------------------------------#

def ForLoop(lines, index, count, condition) : #

    condition = condition.replace("do :", "")

    EndLine = False
    end = 0
    x = index

    #End
    while EndLine == False :

        if lines[x] == "over l." :

            end = x
            EndLine = True

        else : x += 1

    SfSystVr["FLCnt"] = 0

    #Loop
    while If(condition) == True and SfSystVr["FLCnt"] < count + 1 : #

        for n in range(index, end) :

            line = lines[n]

            #Functions
            if line.startswith("show ") : Show(line)
            if line.startswith("call ") : ActivMth["CallIt"] = True
            if line.startswith("set ") : Set(line)
            if line.startswith("up ") : Up(line)

            #Errors
            if line.startswith("int ") : Error("For loops cannot declare vars", line)
            if line.startswith("str ") : Error("For loops cannot declare vars", line)
            if line.startswith("bol ") : Error("For loops cannot declare vars", line)
            if line.startswith("flt ") : Error("For loops cannot declare vars", line)

    SfSystVr["FLCnt"] += 1
    #      
#

def NewTask(lines, fIndex) : #

    NameLimt = lines[fIndex].find(" task :")
    TaskName = lines[fIndex][:NameLimt]
    EndLines = 0

    for l in range(fIndex, len(lines)) :

        if lines[l] == "end t." :

            EndLines = l
            break

        else : next

    ActivTsk.update({TaskName : str(fIndex)+"."+str(EndLines)})
#

def TaskCtrl(lines, string) : #

    TskNm = string.replace("call ", "")

    #Non existent task
    if not TskNm in ActivTsk : Error("Non declareted task", string)

    limit = ActivTsk[TskNm].find(".")
        
    for x in range(int(ActivTsk[TskNm][:limit]), int(ActivTsk[TskNm][limit + 1:])) :

        #Functions
        if lines[x].startswith("show ") : Show(lines[x])
        if lines[x].startswith("set ") : Set(lines[x])
        if lines[x].startswith("up ") : Up(lines[x])
        if lines[x].startswith("convert ") : Convert(lines[x])
        
        #If-Else

        #If
        if lines[x].startswith("if ") :

            IfElseSy["inCent"] = True
            IfElseSy["isIf"] = True
            IfElseSy["Result"] = If(lines[x])

        #Else
        elif lines[x].startswith("else ") and IfElseSy["Result"] == False :

            IfElseSy["inCent"] = True
            IfElseSy["isEl"] = True

        #End of statlement
        
        #Do System
        if lines[x].startswith("do : ") and IfElseSy["inCent"] == True : #

            line = lines[x].replace("do : ", "")

            #Is if?
            if IfElseSy["isIf"] == True and IfElseSy["Result"] == True : IfElseSy["Enable"] = True

            #Is Else?
            if IfElseSy["isEl"] == True and IfElseSy["Result"] == False : IfElseSy["Enable"] = True

            #Then
            if IfElseSy["Enable"] == True :
                
                #Functions
                if line.startswith("show ") : Show(line)
                if line.startswith("set ") : Set(line)
                if line.startswith("up ") : Up(line)

                #Errors
                if line.startswith("int ") : Error("If-else systems cannot declare vars", line)
                if line.startswith("str ") : Error("If-else systems cannot declare vars", line)
                if line.startswith("bol ") : Error("If-else systems cannot declare vars", line)
                if line.startswith("flt ") : Error("If-else systems cannot declare vars", line)
        #

        #Compiler errors
        elif lines[x].startswith("do : ") and not IfElseSy["inCent"] == False : Error("Do out o if statlement", lines[x])
        if lines[x].startswith("call ") : Error("Only 'bucket open' can call tasks", lines[x])

        #For loop
        if lines[x].startswith("for ") :

            lLine = lines[x].replace("for ", "")
            limit = lLine.find("times ")
            count = lLine[:limit]

            #N° Times
            try : count = int(count)
            except ValueError :

                if count in ActivInt : count = ActivInt[count]
                else : Error("For loop needs an int", lines[x])

            #Loop
            ForLoop(lines, x, count, lLine.replace(lLine[:limit + 6], ""))
        
        #Ender
        if lines[x] == "finish" :

            IfElseSy["inCent"] = False
            IfElseSy["Enable"] = False
            
            IfElseSy["isIf"] = False
            IfElseSy["isEl"] = False
    #

    return 0 
#

#_Start_-----------------------------------------------------------------------#

FileN = input("Open File : ")
Compiler(FileN)
