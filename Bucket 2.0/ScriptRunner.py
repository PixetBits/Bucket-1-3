#This script run the
#Bucket Script, call
#Other functions and
#manange all stuff.

#Python Libraries
from importlib import import_module as require

#Error Message
from ErrorMessage import Error

#Comments
from DellComments import Remove

#Multiclasses
from ImportLibStf import GetTasks, SupervisorDad

#Variables functions
from IntFunctions import *
from StrFunctions import *
from BolFunctions import *
from FltFunctions import *
from LstFunctions import *
from LoopsBreaker import *

#Logic Door
from LogicDoorLib import LogicBlk

#Declareted Variables
actI = {"" : "int",}
actS = {"" : "str",}
actB = {"" : "bol",}
actF = {"" : "flt",}
actL = {"" : "lst",}

#Security Variables
safeI = {"" : "int",}
safeS = {"" : "str",}
safeB = {"" : "bol",}
safeF = {"" : "flt",}
fafeL = {"" : "lst",}

#Task data
actT = {"" : "tsk",}

#Libraries added
Libs = {"" : "lib",}

#If-Maybe-Else system
ifBk = {"status" : False, "block" : "", "inside" : False}

def Runner(lines, path, name) : #

    #In a class
    onClss = False

    #In a function
    onFunc = False

    #In a loop
    onLoop = False

    #In a task, but not running
    onTask = False

#Fix-Lines-----------------------------------------------------------------------------------------------------#

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

#To-Lib--------------------------------------------------------------------------------------------------------#

    #Other libraries
    for i in range(0, len(lines)) : #

        #in Class
        if lines[i].startswith("#") : #
            
            if lines[i] == "#" + name + " in Bucket:" : onClss = True
        #

        #Math Functions
        if lines[i] == "[to MathF]" and onClss == False : Libs.update({"mathF" : require("toMathFLib")})
        elif lines[i] == "[to MathF]" : Error("[Compiler Error] Lib called after class declaration.", "lin", lines[i])

        #Add your librarie's module [0] bellow

        #----------Here----------#
    #

    onClss = False

#Multiclass----------------------------------------------------------------------------------------------------#

    for l in range(0, len(lines) - 1) : #

        #Import lines here
        if lines[l].startswith("with ") and onFunc == False : #

            clin = lines[l].replace("with ", "")
            word = clin.split()

            #with name[0] in[1] Sandbox.[2]

            #Missed keyword
            try : #

                if word[1] != "in" : Error("[Sintax Error] Missed \"in\" keyword." "lin", lines[l])
                if word[2] != "Sandbox." : Error("[Sintax Error] Missed \"Sandbox.\" keyword." "lin", lines[l])
            #

            except :
                Error("[Sintax Error] Missed keywords." "lin", lines[l])

            #Get script
            try : #
                
                #Get current path
                if path != name : path = path.replace(name + ".bk", "")
                else : path = ""

                fileD = open(path + word[0].replace("#", "") + ".bk")
                lData = fileD.readlines()
                fileD.close()
            #

            #No file with this name
            except FileNotFoundError :
                Error("Bucket cannot import an nonexistent file. Check the name and try again.", "sys")

            #Import tasks from other script
            lines = lines[:l] + GetTasks(lData, word[0]) + lines[l + 1:]
        #

        #Interface
        if lines[l].startswith("dad ") and onClss == False : #
            
            #Running *in* a dad class
            if lines[l].endswith(":") : Error("Interfaces cannot be executed.", "sys")

            clin = lines[l].replace("dad ", "")
            dadN = clin.replace(".", "")

            #Get script
            try : #

                #Get current path
                if path != name : path = path.replace(name + ".bk", "")
                else : path = ""

                fileD = open(path + dadN.replace("#", "") + ".bk")
                lData = fileD.readlines()
                fileD.close()
            #

            #No file with this name
            except FileNotFoundError :
                Error("Dad file not fount. Check the name and try again.", "sys")

            #Get all requirements
            needL = SupervisorDad(lData, dadN)

            #Check if has be done
            for i in range(0, len(needL)) : #
                
                #Get
                obligation = needL[i]

                result = any(line.startswith(obligation) for line in lines)
                if result == False : Error("[Dad error] your dad forces you had a [" + obligation + "] line.", "sys")
            #
        #
    #

#Task-Stuff----------------------------------------------------------------------------------------------------#

    taskKey = {"s" : 0, "e" : 0, "n" : "", "v" : ""}

    #Find tasks
    for l in range(0, len(lines)) : #
        
        #Start of task block
        if "task:" in lines[l] : #
            
            word = lines[l].split()

            #name[0] task:[1] arg[2]

            #Get name and line
            taskKey["s"] = l
            taskKey["n"] = word[0]

            #Get argmt name 
            if len(word) > 2 : taskKey["v"] = word[2]
        #

        #End of task block
        if lines[l] == "end t." : #

            #Set the last line
            taskKey["e"] = l
            actT.update({taskKey["n"] : taskKey})

            #Reset param
            taskKey = {"s" : 0, "e" : 0, "n" : "", "v" : ""}
        #
    #

#--------------------------------------------------------------------------------------------------------------#

    #Loop index
    loop = {"q" : "", "e" : ""}

    #Run the lines
    for l in range(0, len(lines)) : #

        #Editable line
        clin = lines[l]

        #Skip task lines
        if len(actT) > 1 : #

            for task in actT : #

                if task == "" : continue

                if l == actT[task]["s"] : onTask = True
                if l == actT[task]["e"] : onTask = False
            #
        #

        #Class
        if lines[l].startswith("#") : #

            if lines[l] == "#" + name + " in Bucket:" : onClss = True
            else : Error("[Syntax Error] The class name must be the same of the file.", "lin", lines[l])
        #

        if lines[l] == "close." : onClss = False

        #Main Function
        if lines[l] == "bucket open:" :
            
            if onClss == True : onFunc = True
            else : Error("[Syntax Error] Main out of class.", "lin", lines[l])

        if lines[l] == "end m." : onFunc = False
        
        #Task
        if lines[l].endswith("task:") :
            
            if onClss == True : onFunc = True
            else : Error("[Syntax Error] Task out of class.", "lin", lines[l])

        if lines[l] == "end t." : onFunc = False
        
        #end loop
        if lines[l] == "end l." : onLoop = False

        #In Main or Task
        if onFunc == True and (onLoop == False and onTask == False) : #

        #To-Lib------------------------------------------------------------------------------------------------#
            
            #Math Functions
            if "mathF" in Libs : clin = Libs["mathF"].Main(lines[l], actI, actF)

            #Add your librarie's module [1] bellow

            #----------Here----------#

        #If-Maybe-Else--------------------------------------------------------------------------------------------#

            #If block
            if clin.startswith("if ") : #

                word = clin.split()

                #Missed keyword
                if word[len(word) - 1] == "do:" : clin = clin.replace(" do:", "")
                else : Error("[Sintax Error] Missed \"do:\" keyword.", "lin", lines[l])

                #Rechange
                scentence = clin

                #For two args
                outOne = ""
                outTwo = ""
                
                #Keyword index
                index = ""
                joint = ""

                #Set the current logic block
                ifBk["block"] = "if"

                #Say are in a sentence
                ifBk["inside"] = True

                #And Conector
                if " and " in clin:
                    
                    #Store what the conective
                    joint = "and"

                    #Break args
                    index = clin.find(" and ")
                    clin = scentence[:index]

                #Or Conector
                if " or " in clin :
                    
                    #Store what the conective
                    joint = "or"

                    #Break args
                    index = clin.find(" or ")
                    clin = scentence[:index]

                #Break
                clin = clin.replace("if ", "")
                args = clin.split()

                #if var[0] cond[1] val[2] do:

                #An int statlement
                if args[0] in actI : outOne = LogicBlk(clin, lines[l], actI)

                #An str statlement
                elif args[0] in actS : outOne = LogicBlk(clin, lines[l], actS)

                #An bol statlement
                elif args[0] in actB : outOne = LogicBlk(clin, lines[l], actB)

                #An flt statlement
                elif args[0] in actF : outOne = LogicBlk(clin, lines[l], actF)
                    
                #Unknown var
                else : Error("This is not a declareted variable.", "lin", lines[l])
                
                #Last arg
                if index != "" : #
                    
                    #Get member
                    clin = scentence[index + len(joint) + 2:]

                    #Break
                    args = clin.split()

                    #An int statlement
                    if args[0] in actI : outTwo = LogicBlk(clin, lines[l], actI)

                    #An str statlement
                    elif args[0] in actS : outTwo = LogicBlk(clin, lines[l], actS)

                    #An bol statlement
                    elif args[0] in actB : outTwo = LogicBlk(clin, lines[l], actB)

                    #An flt statlement
                    elif args[0] in actF : outTwo = LogicBlk(clin, lines[l], actF)
                    
                    #Both need be true
                    if joint == "and" : #

                        if outOne and outTwo : ifBk["status"] = True
                        else : ifBk["status"] = False
                    #
                    
                    #One of these need be true
                    if joint == "or" : #

                        if outOne or outTwo : ifBk["status"] = True
                        else : ifBk["status"] = False
                    #
                #

                #Just one sentence
                else : ifBk["status"] = outOne
            #

            #Maybe Block
            if clin.startswith("maybe ") and ifBk["status"] == False : #
            
                word = clin.split()

                #Missed keyword
                if word[len(word) - 1] == "do:" : clin = clin.replace(" do:", "")
                else : Error("[Sintax Error] Missed \"do:\" keyword.", "lin", lines[l])

                #Rechange
                scentence = clin

                #For two args
                outOne = ""
                outTwo = ""
                
                #Keyword index
                index = ""
                joint = ""

                #Set the current logic block
                ifBk["block"] = "maybe"

                #Say are in a sentence
                ifBk["inside"] = True

                #And Conector
                if " and " in clin:
                    
                    #Store what the conective
                    joint = "and"

                    #Break args
                    index = clin.find(" and ")
                    clin = scentence[:index]

                #Or Conector
                if " or " in clin :
                    
                    #Store what the conective
                    joint = "or"

                    #Break args
                    index = clin.find(" or ")
                    clin = scentence[:index]

                #Break
                clin = clin.replace("maybe ", "")
                args = clin.split()

                #maybe var[0] cond[1] val[2] do:

                #An int statlement
                if args[0] in actI : outOne = LogicBlk(clin, lines[l], actI)

                #An str statlement
                elif args[0] in actS : outOne = LogicBlk(clin, lines[l], actS)

                #An bol statlement
                elif args[0] in actB : outOne = LogicBlk(clin, lines[l], actB)

                #An flt statlement
                elif args[0] in actF : outOne = LogicBlk(clin, lines[l], actF)
                    
                #Unknown var
                else : Error("This is not a declareted variable.", "lin", lines[l])
                
                #Last arg
                if index != "" : #
                    
                    #Get member
                    clin = scentence[index + len(joint) + 2:]

                    #Break
                    args = clin.split()

                    #An int statlement
                    if args[0] in actI : outTwo = LogicBlk(clin, lines[l], actI)

                    #An str statlement
                    elif args[0] in actS : outTwo = LogicBlk(clin, lines[l], actS)

                    #An bol statlement
                    elif args[0] in actB : outTwo = LogicBlk(clin, lines[l], actB)

                    #An flt statlement
                    elif args[0] in actF : outTwo = LogicBlk(clin, lines[l], actF)
                    
                    #Both need be true
                    if joint == "and" : #

                        if outOne and outTwo : ifBk["status"] = True
                        else : ifBk["status"] = False
                    #
                    
                    #One of these need be true
                    if joint == "or" : #

                        if outOne or outTwo : ifBk["status"] = True
                        else : ifBk["status"] = False
                    #
                #

                #Just one sentence
                else : ifBk["status"] = outOne
            #

            #Else block
            if clin.startswith("else ")  and ifBk["status"] == False : #
                
                #Set the current logic block
                ifBk["block"] = "else"

                #Say are in a sentence
                ifBk["inside"] = True
            #

            #Out of sentence
            if clin == "end." : ifBk["inside"] = False

            #Enabled system
            if clin.startswith("> ") and ifBk["inside"] == True : #

                working = False

                #True door
                if ifBk["block"] == "if" or ifBk["block"] == "maybe" :

                    if ifBk["status"] == True : working = True
                
                #False door
                elif ifBk["block"] == "else" and ifBk["status"] == False : working = True
                
                #Actions
                if working == True : clin = clin.replace("> ", "")
                
                #Error
                if clin.startswith("if") : Error("[Syntax Error] Bucket does not suport ifs inside ifs.", "lin", lines[l])
            #

        #------------------------------------------------------------------------------------------------------#

            #Declare int
            if clin.startswith("int ") : actI.update(NewInt(clin, actI))

            #Declare str
            if clin.startswith("str ") : actS.update(NewStr(clin, actS))

            #Declare bol
            if clin.startswith("bol ") : actB.update(NewBol(clin, actB))

            #Declare flt
            if clin.startswith("flt ") : actF.update(NewFlt(clin, actB))

            #Declare lst
            if clin.startswith("lst ") : actL.update(NewLst(clin, actL))
            
            #set
            if clin.startswith("set ") : #

                #Remove keyword
                name = clin.replace(clin[0:4], "")
                name = name.split()

                #set name[0] to[1] vall[2] index[3]

                #A list value
                if name[2] in actL : #
                    
                    #Update index
                    if name[3] in actI : name[3] = str(actI[name[3]])
                    if name[3] in actS : name[3] = str(actS[name[3]])
                    if name[3] in actB : name[3] = str(actB[name[3]])
                    if name[3] in actF : name[3] = str(actF[name[3]])
                    
                    #Fix bol definition
                    if name[3] == "True" : name[3] = "yes"
                    if name[3] == "False" : name[3] = "not"
                    
                    #Key error
                    if not name[3] in actL[name[2]] : Error("[Compiler Error] Index out of range.", "lin", lines[l])

                    #Update a int
                    if name[0] in actI : actI.update({name[0] : actL[name[2]][name[3]]})

                    #Update a str
                    elif name[0] in actS : actS.update({name[0] : actL[name[2]][name[3]]})

                    #Update a bol
                    elif name[0] in actB : actB.update({name[0] : actL[name[2]][name[3]]})

                    #Update a flt
                    elif name[0] in actF : actF.update({name[0] : actL[name[2]][name[3]]})

                    #Unknown varible
                    else : Error("[Compiler Error] This is not a declareted variable.", "lin", lines[l])
                #

                #Default value
                else : #

                    #Update a int
                    if name[0] in actI : actI.update(SetInt(clin, actI))

                    #Update a str
                    elif name[0] in actS : actS.update(SetStr(clin, actS))

                    #Update a bol
                    elif name[0] in actB : actB.update(SetBol(clin, actB))

                    #Update a flt
                    elif name[0] in actF : actF.update(SetFlt(clin, actF))

                    #Unknown varible
                    else : Error("This is not a declareted variable.", "lin", lines[l])
                #
            #

            #Make
            if clin.startswith("make ") : #

                #Remove keyword
                clin = clin.replace(clin[0:5], "")
                args = clin.split()

                #make var[0] ~[1] val[2]

                #Change a int
                if args[0] in actI : actI.update(Make(clin, lines[l], actI))

                #Change a str
                elif args[0] in actS : actS.update(Make(clin, lines[l], actS))

                #Change a flt
                elif args[0] in actF : actF.update(Make(clin, lines[l], actF))
                
                #bol or else
                else : Error("[Compiler Error] This variable is probably an bol. Bucket cannot change this.", "lin", lines[l])
            #

            #Rise
            if clin.startswith("rise ") : #
                
                #Remove keyword
                vall = clin.replace(clin[0:5], "")
                
                indx = vall.find(" in ")
                name = vall[:indx]

                #Cannot rise strings
                if name in actS : Error("[Compiler Error] A str cannot be summed with a number.", "lin", lines[l])

                #Cannot rise boolean
                elif name in actB : Error("[Compiler Error] A bol cannot be summed with a number.", "lin", lines[l])
                
                #a int
                elif name in actI : actI.update(Rise(clin, actI))

                #a flt
                elif name in actF : actF.update(Rise(clin, actF))

                else : Error("[Compiler Error] This variable do not exist.", "lin", lines[l])
            #

            #Down
            if clin.startswith("down ") : #
                
                #Remove keyword
                clin = clin.replace(clin[0:5], "")
                
                index = clin.find(" in ")
                name = clin[:index]


                #Cannot make down strings
                if name in actS : Error("[Compiler Error] A str cannot be decreased by number.", "lin", lines[l])

                #Cannot make down Boolean
                elif name in actB : Error("[Compiler Error] A bol cannot be decreased by number.", "lin", lines[l])
                
                #a int
                elif name in actI : actI.update(Down(clin, actI))

                #a flt
                elif name in actF : actF.update(Down(clin, actF))

                else : Error("[Compiler Error] This variable do not exist.", "lin", lines[l])
            #

            #Round
            if clin.startswith("round ") : #
                
                #Remove keyword
                clin = clin.replace(clin[0:6], "")

                #Round value if exists
                value = RoundT(clin, lines[l], actF)

                #This flt have the same name of an int    
                if value in actI : Error("[Compiler Error] You already have a int with the same name of your flt.", "lin", lines[l])
                
                #Allright
                else : #
                    
                    actI.update({clin : value})
                    del actF[clin]
                #
            #

            #Convert
            if clin.startswith("convert ") : #
                
                #Remove keyword
                clin = clin.replace(clin[0:8], "")
                
                #To int
                if clin.endswith(" to int") : #

                    #Remove keyword
                    clin = clin.replace(" to int", "")

                    #An string
                    if clin in actS : #
                        
                        actI.update({clin : CToInt(actS[clin], lines[l])})
                        del actS[clin]
                    #

                    #An boolean
                    if clin in actB : #
                        
                        actI.update({clin : CToInt(actB[clin], lines[l])})
                        del actB[clin]
                    #

                    #An float
                    if clin in actF : #
                        
                        actI.update({clin : CToInt(actF[clin], lines[l])})
                        del actF[clin]
                    #
                #

                #To str
                if clin.endswith(" to str") : #
                    
                    #Remove keyword
                    clin = clin.replace(" to str", "")

                    #An interable
                    if clin in actI : #
                        
                        actS.update({clin : CToStr(actI[clin])})
                        del actI[clin]
                    #

                    #An boolean
                    elif clin in actB : #
                        
                        actS.update({clin : CToStr(actB[clin])})
                        del actB[clin]
                    #

                    #An float
                    elif clin in actF : #
                        
                        actS.update({clin : CToStr(actF[clin])})
                        del actF[clin]
                    #

                    else : Error("[Compiler Error] This is not a declareted variable.", "lin", lines[l])
                #

                #To bol
                if clin.endswith(" to bol") : #

                    #Remove keyword
                    clin = clin.replace(" to bol", "")

                    #An interable
                    if clin in actI : #
                        
                        actB.update({clin : CToBol(actI[clin], lines[l])})
                        del actI[clin]
                    #

                    #An string
                    if clin in actS : #
                        
                        actB.update({clin : CToBol(actS[clin], lines[l])})
                        del actS[clin]
                    #

                    #An float
                    elif clin in actF : #
                        
                        actB.update({clin : CToBol(actF[clin], lines[l])})
                        del actF[clin]
                    #

                    else : Error("[Compiler Error] This is not a declareted variable.", "lin", lines[l])
                #

                #To flt
                if clin.endswith(" to flt") : #

                    #Remove keyword
                    clin = clin.replace(" to flt", "")

                    #An interable
                    if clin in actI : #
                        
                        actF.update({clin : CToFlt(actI[clin], lines[l])})
                        del actI[clin]
                    #

                    #An string
                    if clin in actS : #
                        
                        actF.update({clin : CToFlt(actS[clin], lines[l])})
                        del actS[clin]
                    #

                    #An boolean
                    elif clin in actB : Error("[Compiler Error] Bucket do not understand booleans as floats.", "lin", lines[l])
                #
            #

            #Basic BIn/BOud
            if clin.startswith("show ") : #

                #Remove keyword
                clin = clin.replace(clin[0:5], "")

                #Special codes
                if "\\s" in clin : clin = val.replace("\\s", " ")
                if "\\q" in clin : clin = val.replace("\\q", "\"")
                if "\\n" in clin : clin = val.replace("\\n", "\n")
                if "\\t" in clin : clin = val.replace("\\t", "\t")

                #With Arg
                if "with " in clin : #
                    
                    #Get the keyword index
                    index = clin.index(" with ")
                    strng = clin[:index]
                    argmt = clin[index + len(" with "):]

                    #Fix text value
                    if strng in actS : strng = actS[strng]
                    elif strng.startswith("'") and strng.endswith("'") : strng = strng.replace("'", "")
                    else : Error("[Compiler Error] Cannot print a non string.", "lin", lines[l])

                    #Replace by a int
                    if "[i]" in strng and IsAInt(argmt, actI) == True : #
                        
                        #Number
                        try : #
                            
                            int(argmt)
                            print(strng.replace("[i]", argmt))
                        #

                        #Variable
                        except ValueError :
                            print(strng.replace("[i]", str(actI[argmt])))
                    #

                    #Replace by a str
                    elif "[s]" in strng and IsAStr(argmt, actS) == True : #

                        #Text
                        if argmt.startswith("'") : #
                            
                            #Empty
                            if argmt == "''" : argmt = ""
                            
                            #Remove apostrophos
                            else : argmt = argmt[1:len(argmt) - 1]

                            print(strng.replace("[s]", argmt))
                        #

                        #Variable
                        else : print(strng.replace("[s]", actS[argmt]))
                    #
                    
                    #Replace by a bol
                    elif "[b]" in strng and IsABol(argmt, actB) == True : #
                        
                        #Value
                        if argmt == "yes" : print(strng.replace("[b]", "yes"))
                        elif argmt == "not" : print(strng.replace("[b]", "not"))
                        
                        #Variable
                        else : #
                            
                            if actB[argmt] == True : print(strng.replace("[b]", "yes"))
                            if actB[argmt] == False : print(strng.replace("[b]", "not"))
                        #
                    #

                    #Replace by a flt
                    elif "[f]" in strng and IsAFlt(argmt, actF) == True : #
                        
                        #Value
                        if argmt.endswith(".f") : argmt = argmt.replace(".f", "")

                        #Number
                        try : #
                            
                            float(argmt)
                            print(strng.replace("[f]", argmt))
                        #

                        #Variable
                        except ValueError :
                            print(strng.replace("[f]", str(actF[argmt])))
                    #

                    #Replace by a lst
                    elif "[l]" in strng and IsALst(argmt, actL) == True : #

                        #Variable
                        if argmt in actL :
                            
                            #Get list from actL
                            argmt = actL[argmt]

                            #Initidal visible list
                            toShow = "["

                            #Get just the values
                            for item in argmt : #
                                
                                if "'" in item : item = item.replace("'", "")

                                if item == "" : next
                                elif item == max(argmt.keys()) : toShow = toShow + str(argmt[item]) + "]" 
                                else : toShow = toShow + str(argmt[item]) + ", "
                            #

                            print(strng.replace("[l]", toShow))
                        #

                        #Value
                        else : print(strng.replace("[l]", argmt))
                    #

                    #Without Keyword
                    else : Error("[Compiler Error] Sitation Keyword not found.", "lin", lines[l])
                #

                #Is a str value
                elif clin.startswith("'") and clin.endswith("'") : #
                    
                    #Empty
                    if clin == "''" : clin = ""
                    
                    #Remove apostrophos
                    else : clin = clin[1:len(clin) - 1]

                    print(clin)
                #

                #Is other str
                elif clin in actS : print(actS[clin])

                #Input
                elif clin.startswith("sand") : print(Sand(clin, lines[l], actS))

                #Error
                else : Error("[Compiler Error] Bucket cannot show this.", "lin", lines[l])
            #

            #List functions

            #fin
            if clin.startswith("fin ") : #
                
                #Remove keyword
                clin = clin.replace(clin[0:4], "")

                #Get list
                word = clin.split()

                #find item[0] in[1] list[2] to[3] item[4]

                #Need a int to get str index
                if word[4] in actI and IsAStr(word[2], actS) : actI.update({word[4] : Fin(clin, lines[l], actS, actL)})
                
                #Need a str to get lst index
                elif word[4] in actS and IsALst(word[2], actL) : actS.update({word[4] : Fin(clin, lines[l], actS, actL)})
                
                #Something else
                else : Error("[Compiler Error] Type error or unknown variables.", "lin", lines[l])
            #

            #add
            if clin.startswith("add ") : #
                
                #Remove keyword
                clin = clin.replace(clin[0:4], "")

                #Get list
                word = clin.split()

                #add item[0] on[1] list[2] as[3] value[4]

                if word[2] in actL : actL[word[2]].update(Add(clin, lines[l], actL))
                else : Error("[Compiler Error] This list do not exist.", "lin", lines[l])
            #

            #del
            if clin.startswith("del ") : #
                
                #Remove keyword
                clin = clin.replace(clin[0:4], "")

                #Get list
                word = clin.split()

                #del item[0] of[1] list[2]

                if word[2] in actL : actL.update(Del(clin, lines[l], actL))
                else : Error("[Compiler Error] This list do not exist.", "lin", lines[l])
            #
            
            #siz
            if clin.startswith("siz ") : #
                
                #Remove keyword
                clin = clin.replace(clin[0:4], "")
                
                #For index
                ledr = clin
                ledr = ledr.replace("of ", "")
                
                #siz of list to var

                index = ledr.find(" to ")
                aList = ledr[:index]
                vName = ledr[index + 4:]

                #This list exists
                if aList in actL : #
                    
                    if vName in actI : actI.update(Siz(clin, lines[l], actL[aList]))
                    else : Error("[Compiler Error] Siz function returns a int, so it needs a int to assign.", "lin", lines[l])
                #

                elif aList in actS : #

                    if vName in actI : actI.update(Siz(clin, lines[l], actS[aList]))
                    else : Error("[Compiler Error] Siz function returns a int, so it needs a int to assign.", "lin", lines[l])
                #

                else : Error("[Compiler Error] This list do not exist.", "lin", lines[l])
            #

            #brk
            if clin.startswith("brk ") : #
                
                clin = clin.replace(clin[0:4], "")

                word = clin.split()

                #brk string[0] in[1] word[2] to[3] var[4]

                #Unknow vars
                if not word[0] in actS : Error("[Compiler Error] This string do not exist.", "lin", lines[l])
                if not word[4] in actL : Error("[Compiler Error] Cannot assign to a nonexistent list.", "lin", lines[l])

                #List exits
                else : actL.update(Brk(clin, lines[l], actS))
            #

            #loops

            #For Loop
            if clin.startswith("for ") : #
                
                #for x times if y ~ z do:

                loop = NewForLoop(l, lines, actI)
                
                #Return :
                #max count|question|variable|start/end line

                #No return
                if loop == None : Error("[Syntax Error] No loop ender.", "lin", lines[0])
                
                #variable type

                #Check a int
                if loop["v"] in actI : loop["v"] = actI
                
                #Check a str
                elif loop["v"] in actS : loop["v"] = actS
                
                #Check a bol
                elif loop["v"] in actB : loop["v"] = actB
                
                #Check a flt
                elif loop["v"] in actF : loop["v"] = actF
                
                #Non existent
                else : Error("[Compiler Error] This is not a variable to check.", "lin", lines[l])
                
                #For count
                for c in range(0, loop["m"]) : #

                    #For every line
                    for i in range(loop["s"], loop["e"]) : #
                        
                        #Question
                        quest = LogicBlk(loop["q"], lines[l], loop["v"])

                        #If True then ...
                        if quest == True : #
                            
                            #Run other Runner
                            LittleRun(i, lines)
                            
                            #Update var
                            if loop["v"][""] == "int" : loop["v"] = actI
                            if loop["v"][""] == "str" : loop["v"] = actS
                            if loop["v"][""] == "bol" : loop["v"] = actB
                            if loop["v"][""] == "flt" : loop["v"] = actF
                        #
                    #
                #
            #

            #For Loop
            if clin.startswith("every ") : #

                #every item in list do:
                loop = NewEveryLoop(l, lines, actL)

                #Return :
                #var name| var list| start l| end line|

                #No return
                if loop == None : Error("[Syntax Error] No loop ender.", "lin", lines[0])

                #For count

                #Remove type index
                List = {"" : "",}
                List.update(loop["l"])
                del List[""]

                #for every item in list do:
                for c in List : #
                    
                    indx = loop["l"][c]

                    #Create temporary variable
                    if type(indx) == int : actI.update({loop["v"] : indx})
                    elif type(indx) == str : actS.update({loop["v"] : indx})
                    elif type(indx) == bool : actB.update({loop["v"] : indx})
                    elif type(indx) == float : actF.update({loop["v"] : indx})

                    #For every lile
                    for i in range(loop["s"], loop["e"]) : #

                        #Run other Runner
                        LittleRun(i, lines)
                    #
                #

                #Remove temporary variable
                if loop["v"] in actI : del actI[loop["v"]]
                if loop["v"] in actS : del actS[loop["v"]]
                if loop["v"] in actB : del actB[loop["v"]]
                if loop["v"] in actF : del actF[loop["v"]]

                onLoop = True
            #

            #Tasks

            #call
            if clin.startswith("call ") : #
                
                clin = clin.replace(clin[0:5], "")

                #call name: arg to var

                index = clin.find(" to ")
                taskD = clin[:index]
                vName = clin[index + 4:]
                argmt = None

                #Task configuration
                if ":" in taskD : #

                    dataT = taskD.split(":")

                    #task[0] arg[1]

                    try : #

                        tName = dataT[0]
                        argmt = dataT[1]

                        tName = tName.strip()
                        argmt = argmt.strip()
                    #

                    except :
                        Error("[Syntax Error] no argment gived.", "lin", lines[l])
                #
                
                #Just name
                else : tName = taskD

                #Get task data
                if tName in actT : taskD = actT[tName]
                else : Error("[Compiler Error] Trying to call a unknown task.", "lin", lines[l])

                #To del the temporary var
                varT = "nil"

                #Variables beafore task
                safeI, safeS, safeB, safeF = actI, actS, actB, actF

                #argment
                if argmt != None : #

                    #No argment
                    if taskD["v"] == "" : Error("[Compiler Error] This task do not requires a argment.", "lin", lines[l])

                    #Add a temporary int
                    if IsAInt(argmt, actI) == True : #
                        
                        varT = "int"
                        actI.update({taskD["v"] : actI[argmt]})
                    #

                    #Add a temporary str
                    if IsAStr(argmt, actS) == True : #
                        
                        varT = "str"
                        actS.update({taskD["v"] : actS[argmt]})
                    #

                    #Add a temporary bol
                    if IsABol(argmt, actB) == True : #
                        
                        varT = "bool"
                        actB.update({taskD["v"] : actB[argmt]})
                    #

                    #Add a temporary flt
                    if IsAFlt(argmt, actF) == True : #
                        
                        varT = "float"
                        actF.update({taskD["v"] : actF[argmt]})
                    #
                #

                #Run
                for i in range(taskD["s"], taskD["e"]) : #
                    
                    retrn = LittleRun(i, lines)
                #

                #Dell task variables
                
                #Int's
                for i in actI :                  
                    if not i in safeI : del actI[i]
                
                #Str's
                for i in actS :                  
                    if not i in safeS : del actS[i]
                
                #Bol's
                for i in actB :                  
                    if not i in safeB : del actB[i]
                
                #Fts's
                for i in actF :                  
                    if not i in safeF : del actF[i]

                #Remove the temporary var
                if argmt != None : #
                    
                    #Remove a int
                    if varT == "int" : del actI[taskD["v"]]
                    if varT == "str" : del actS[taskD["v"]]
                    if varT == "bool" : del actB[taskD["v"]]
                    if varT == "float" : del actF[taskD["v"]]
                #

                #No return
                if retrn == None :
                    if not vName == "self." : Error("[Compiler Error] Tasks must return a value.", "lin", lines[taskD["e"]])

                #Return value
                else : #

                    #Get the return type as string
                    typ = str(type(retrn))
                    typ = typ.replace("'", "")
                    typ = typ.replace("<class ", "")
                    typ = typ[:-1]

                    #Check if var exists
                    
                    #A int
                    if vName in actI : #

                        if typ == "int" : actI.update({vName : retrn})

                        #Not the same type
                        else : Error("[Compiler Error] This variable do not acept the return type.", "lin", lines[l])
                    #

                    #A str
                    elif vName in actS : #

                        if typ == "str" : actS.update({vName : retrn})

                        #Not the same type
                        else : Error("[Compiler Error] This variable do not acept the return type.", "lin", lines[l])
                    #

                    #A bol
                    elif vName in actB : #

                        if typ == "bool" : actB.update({vName : retrn})

                        #Not the same type
                        else : Error("[Compiler Error] This variable do not acept the return type.", "lin", lines[l])
                    #
                
                    #A flt
                    elif vName in actF : #

                        if typ == "float" : actF.update({vName : retrn})

                        #Not the same type
                        else : Error("[Compiler Error] This variable do not acept the return type.", "lin", lines[l])
                    #

                    #Unknown varible
                    else : Error("[Compiler Error] This is not a declareted variable.", "lin", lines[l])
                #
            #

            #Strange line
            keywords = ["int ", "str ", "bol ", "flt ", "lst ",
                        "set ", "make ", "rise ", "down ",
                        "convert ","show ", "fin ", "add ",
                        "del ", "siz ","brk ", "for ", "every ",
                        "call", "if ", "maybe ", "else ", "> "]

            endwords = ["close.", "end m.", "end t.", "end l.", "end."]

            #Check
            true_one = any([lines[l].startswith(key) for key in keywords])
            true_two = lines[l] in endwords
            
            #Not the main function line and are in main function
            if onFunc == True and lines[l] != "bucket open:" : #
                
                #Do not start with any keywords or end some block
                if true_one == False and true_two == False : #
                    
                    #Are not a task
                    if not "task:" in lines[l] :
                        Error("[Syntax error] Strange command.", "lin", lines[l])
                #
            #
        #

        #Out of block
        elif onFunc == False : #

            #Libraries
            if lines[l] == "[to Basic]" : continue
            elif lines[l].startswith("[to ") and lines[l].endswith("]") : continue
            
            #Class stuff
            elif lines[l].startswith("dad ") : continue
            
            #Main class
            elif lines[l].endswith("in Bucket:") or clin == "close." : continue

            #One function
            elif lines[l] == "bucket open:" or clin == "end m." : continue
            
            #One Task
            elif "task:" in lines[l] or clin == "end t." : continue
            
            #Out of system block
            elif onTask == False : Error("[Syntax Error] Line out of an block.", "lin", lines[l])
        #
    #

    #No "close." line
    if lines[len(lines) - 1] != "close." : Error("[Syntax Error] Your script did not close the class block.", "lin", lines[len(lines) - 1])

    #End script
    print("\n--------------------\n")
    input("Press enter to exit.\n")
#

def LittleRun(l, lines) : #

    #Editable line
    clin = lines[l]
    
    #To-Lib----------------------------------------------------------------------------------------------------#
  
    #Math Functions
    if "mathF" in Libs : clin = Libs["mathF"].Main(lines[l], actI, actF)

    #Add your librarie's module [2] bellow

    #----------Here----------#

#If-Or-Else----------------------------------------------------------------------------------------------------#

    #If block
    if clin.startswith("if ") : #

        word = clin.split()

        #Missed keyword
        if word[len(word) - 1] == "do:" : clin = clin.replace(" do:", "")
        else : Error("[Sintax Error] Missed \"do:\" keyword.", "lin", lines[l])

        #Rechange
        scentence = clin

        #For two args
        outOne = ""
        outTwo = ""
        
        #Keyword index
        index = ""
        joint = ""

        #Set the current logic block
        ifBk["block"] = "if"

        #Say are in a sentence
        ifBk["inside"] = True

        #And Conector
        if " and " in clin:
            
            #Store what the conective
            joint = "and"

            #Break args
            index = clin.find(" and ")
            clin = scentence[:index]

        #Or Conector
        if " or " in clin :
            
            #Store what the conective
            joint = "or"

            #Break args
            index = clin.find(" or ")
            clin = scentence[:index]

        #Break
        clin = clin.replace("if ", "")
        args = clin.split()

        #if var[0] cond[1] val[2] do:

        #An int statlement
        if args[0] in actI : outOne = LogicBlk(clin, lines[l], actI)

        #An str statlement
        elif args[0] in actS : outOne = LogicBlk(clin, lines[l], actS)

        #An bol statlement
        elif args[0] in actB : outOne = LogicBlk(clin, lines[l], actB)

        #An flt statlement
        elif args[0] in actF : outOne = LogicBlk(clin, lines[l], actF)
            
        #Unknown var
        else : Error("This is not a declareted variable.", "lin", lines[l])
        
        #Last arg
        if index != "" : #
            
            #Get member
            clin = scentence[index + len(joint) + 2:]

            #Break
            args = clin.split()

            #An int statlement
            if args[0] in actI : outTwo = LogicBlk(clin, lines[l], actI)

            #An str statlement
            elif args[0] in actS : outTwo = LogicBlk(clin, lines[l], actS)

            #An bol statlement
            elif args[0] in actB : outTwo = LogicBlk(clin, lines[l], actB)

            #An flt statlement
            elif args[0] in actF : outTwo = LogicBlk(clin, lines[l], actF)
            
            #Both need be true
            if joint == "and" : #

                if outOne and outTwo : ifBk["status"] = True
                else : ifBk["status"] = False
            #
            
            #One of these need be true
            if joint == "or" : #

                if outOne or outTwo : ifBk["status"] = True
                else : ifBk["status"] = False
            #
        #

        #Just one sentence
        else : ifBk["status"] = outOne
    #

    #Maybe Block
    if clin.startswith("maybe ") and ifBk["status"] == False : #
    
        word = clin.split()

        #Missed keyword
        if word[len(word) - 1] == "do:" : clin = clin.replace(" do:", "")
        else : Error("[Sintax Error] Missed \"do:\" keyword.", "lin", lines[l])

        #Rechange
        scentence = clin

        #For two args
        outOne = ""
        outTwo = ""
        
        #Keyword index
        index = ""
        joint = ""

        #Set the current logic block
        ifBk["block"] = "maybe"

        #Say are in a sentence
        ifBk["inside"] = True

        #And Conector
        if " and " in clin:
            
            #Store what the conective
            joint = "and"

            #Break args
            index = clin.find(" and ")
            clin = scentence[:index]

        #Or Conector
        if " or " in clin :
            
            #Store what the conective
            joint = "or"

            #Break args
            index = clin.find(" or ")
            clin = scentence[:index]

        #Break
        clin = clin.replace("maybe ", "")
        args = clin.split()

        #maybe var[0] cond[1] val[2] do:

        #An int statlement
        if args[0] in actI : outOne = LogicBlk(clin, lines[l], actI)

        #An str statlement
        elif args[0] in actS : outOne = LogicBlk(clin, lines[l], actS)

        #An bol statlement
        elif args[0] in actB : outOne = LogicBlk(clin, lines[l], actB)

        #An flt statlement
        elif args[0] in actF : outOne = LogicBlk(clin, lines[l], actF)
            
        #Unknown var
        else : Error("This is not a declareted variable.", "lin", lines[l])
        
        #Last arg
        if index != "" : #
            
            #Get member
            clin = scentence[index + len(joint) + 2:]

            #Break
            args = clin.split()

            #An int statlement
            if args[0] in actI : outTwo = LogicBlk(clin, lines[l], actI)

            #An str statlement
            elif args[0] in actS : outTwo = LogicBlk(clin, lines[l], actS)

            #An bol statlement
            elif args[0] in actB : outTwo = LogicBlk(clin, lines[l], actB)

            #An flt statlement
            elif args[0] in actF : outTwo = LogicBlk(clin, lines[l], actF)
            
            #Both need be true
            if joint == "and" : #

                if outOne and outTwo : ifBk["status"] = True
                else : ifBk["status"] = False
            #
            
            #One of these need be true
            if joint == "or" : #

                if outOne or outTwo : ifBk["status"] = True
                else : ifBk["status"] = False
            #
        #

        #Just one sentence
        else : ifBk["status"] = outOne
    #

    #Else block
    if clin.startswith("else ")  and ifBk["status"] == False : #
        
        #Set the current logic block
        ifBk["block"] = "else"

        #Say are in a sentence
        ifBk["inside"] = True
    #

    #Out of sentence
    if clin == "end." : ifBk["inside"] = False

    #Enabled system
    if clin.startswith("> ") and ifBk["inside"] == True : #

        working = False

        #True door
        if ifBk["block"] == "if" or ifBk["block"] == "maybe" :

            if ifBk["status"] == True : working = True
        
        #False door
        elif ifBk["block"] == "else" and ifBk["status"] == False : working = True
        
        #Actions
        if working == True : clin = clin.replace("> ", "")
        
        #Error
        if clin.startswith("if") : Error("[Syntax Error] Bucket does not suport ifs inside ifs.", "lin", lines[l])
    #

#------------------------------------------------------------------------------------------------------#

    #Declare int
    if clin.startswith("int ") : actI.update(NewInt(clin, actI))

    #Declare str
    if clin.startswith("str ") : actS.update(NewStr(clin, actS))

    #Declare bol
    if clin.startswith("bol ") : actB.update(NewBol(clin, actB))

    #Declare flt
    if clin.startswith("flt ") : actF.update(NewFlt(clin, actB))

    #Declare lst
    if clin.startswith("lst ") : actL.update(NewLst(clin, actL))
    
    #set
    if clin.startswith("set ") : #

        #Remove keyword
        name = clin.replace(clin[0:4], "")
        name = name.split()

        #set name[0] to[1] vall[2] index[3]

        #A list value
        if name[2] in actL : #
            
            #Update index
            if name[3] in actI : name[3] = str(actI[name[3]])
            if name[3] in actS : name[3] = str(actS[name[3]])
            if name[3] in actB : name[3] = str(actB[name[3]])
            if name[3] in actF : name[3] = str(actF[name[3]])
            
            #Fix bol definition
            if name[3] == "True" : name[3] = "yes"
            if name[3] == "False" : name[3] = "not"
            
            #Key error
            if not name[3] in actL[name[2]] : Error("[Compiler Error] Index out of range.", "lin", lines[l])

            #Update a int
            if name[0] in actI : actI.update({name[0] : actL[name[2]][name[3]]})

            #Update a str
            elif name[0] in actS : actS.update({name[0] : actL[name[2]][name[3]]})

            #Update a bol
            elif name[0] in actB : actB.update({name[0] : actL[name[2]][name[3]]})

            #Update a flt
            elif name[0] in actF : actF.update({name[0] : actL[name[2]][name[3]]})

            #Unknown varible
            else : Error("[Compiler Error] This is not a declareted variable.", "lin", lines[l])
        #

        #Default value
        else : #

            #Update a int
            if name[0] in actI : actI.update(SetInt(clin, actI))

            #Update a str
            elif name[0] in actS : actS.update(SetStr(clin, actS))

            #Update a bol
            elif name[0] in actB : actB.update(SetBol(clin, actB))

            #Update a flt
            elif name[0] in actF : actF.update(SetFlt(clin, actF))

            #Unknown varible
            else : Error("This is not a declareted variable.", "lin", lines[l])
        #
    #

    #Make
    if clin.startswith("make ") : #

        #Remove keyword
        clin = clin.replace(clin[0:5], "")
        args = clin.split()

        #make var[0] ~[1] val[2]

        #Change a int
        if args[0] in actI : actI.update(Make(clin, lines[l], actI))

        #Change a str
        elif args[0] in actS : actS.update(Make(clin, lines[l], actS))

        #Change a flt
        elif args[0] in actF : actF.update(Make(clin, lines[l], actF))
        
        #bol or else
        else : Error("[Compiler Error] This variable is probably an bol. Bucket cannot change this.", "lin", lines[l])
    #

    #Rise
    if clin.startswith("rise ") : #
        
        #Remove keyword
        vall = clin.replace(clin[0:5], "")
        
        indx = vall.find(" in ")
        name = vall[:indx]

        #Cannot rise strings
        if name in actS : Error("[Compiler Error] A str cannot be summed with a number.", "lin", lines[l])

        #Cannot rise boolean
        elif name in actB : Error("[Compiler Error] A bol cannot be summed with a number.", "lin", lines[l])
        
        #a int
        elif name in actI : actI.update(Rise(clin, actI))

        #a flt
        elif name in actF : actF.update(Rise(clin, actF))

        else : Error("[Compiler Error] This variable do not exist.", "lin", lines[l])
    #

    #Down
    if clin.startswith("down ") : #
        
        #Remove keyword
        clin = clin.replace(clin[0:5], "")
        
        index = clin.find(" in ")
        name = clin[:index]


        #Cannot make down strings
        if name in actS : Error("[Compiler Error] A str cannot be decreased by number.", "lin", lines[l])

        #Cannot make down Boolean
        elif name in actB : Error("[Compiler Error] A bol cannot be decreased by number.", "lin", lines[l])
        
        #a int
        elif name in actI : actI.update(Down(clin, actI))

        #a flt
        elif name in actF : actF.update(Down(clin, actF))

        else : Error("[Compiler Error] This variable do not exist.", "lin", lines[l])
    #

    #Round
    if clin.startswith("round ") : #
        
        #Remove keyword
        clin = clin.replace(clin[0:6], "")

        #Round value if exists
        value = RoundT(clin, lines[l], actF)

        #This flt have the same name of an int    
        if value in actI : Error("[Compiler Error] You already have a int with the same name of your flt.", "lin", lines[l])
        
        #Allright
        else : #
            
            actI.update({clin : value})
            del actF[clin]
        #
    #

    #Convert
    if clin.startswith("convert ") : #
        
        #Remove keyword
        clin = clin.replace(clin[0:8], "")
        
        #To int
        if clin.endswith(" to int") : #

            #Remove keyword
            clin = clin.replace(" to int", "")

            #An string
            if clin in actS : #
                
                actI.update({clin : CToInt(actS[clin], lines[l])})
                del actS[clin]
            #

            #An boolean
            if clin in actB : #
                
                actI.update({clin : CToInt(actB[clin], lines[l])})
                del actB[clin]
            #

            #An float
            if clin in actF : #
                
                actI.update({clin : CToInt(actF[clin], lines[l])})
                del actF[clin]
            #
        #

        #To str
        if clin.endswith(" to str") : #
            
            #Remove keyword
            clin = clin.replace(" to str", "")

            #An interable
            if clin in actI : #
                
                actS.update({clin : CToStr(actI[clin])})
                del actI[clin]
            #

            #An boolean
            elif clin in actB : #
                
                actS.update({clin : CToStr(actB[clin])})
                del actB[clin]
            #

            #An float
            elif clin in actF : #
                
                actS.update({clin : CToStr(actF[clin])})
                del actF[clin]
            #

            else : Error("[Compiler Error] This is not a declareted variable.", "lin", lines[l])
        #

        #To bol
        if clin.endswith(" to bol") : #

            #Remove keyword
            clin = clin.replace(" to bol", "")

            #An interable
            if clin in actI : #
                
                actB.update({clin : CToBol(actI[clin], lines[l])})
                del actI[clin]
            #

            #An string
            if clin in actS : #
                
                actB.update({clin : CToBol(actS[clin], lines[l])})
                del actS[clin]
            #

            #An float
            elif clin in actF : #
                
                actB.update({clin : CToBol(actF[clin], lines[l])})
                del actF[clin]
            #

            else : Error("[Compiler Error] This is not a declareted variable.", "lin", lines[l])
        #

        #To flt
        if clin.endswith(" to flt") : #

            #Remove keyword
            clin = clin.replace(" to flt", "")

            #An interable
            if clin in actI : #
                
                actF.update({clin : CToFlt(actI[clin], lines[l])})
                del actI[clin]
            #

            #An string
            if clin in actS : #
                
                actF.update({clin : CToFlt(actS[clin], lines[l])})
                del actS[clin]
            #

            #An boolean
            elif clin in actB : Error("[Compiler Error] Bucket do not understand booleans as floats.", "lin", lines[l])
        #
    #

    #Basic BIn/BOud
    if clin.startswith("show ") : #

        #Remove keyword
        clin = clin.replace(clin[0:5], "")

        #Special codes
        if "\\s" in clin : clin = val.replace("\\s", " ")
        if "\\q" in clin : clin = val.replace("\\q", "\"")
        if "\\n" in clin : clin = val.replace("\\n", "\n")
        if "\\t" in clin : clin = val.replace("\\t", "\t")

        #With Arg
        if "with " in clin : #
            
            #Get the keyword index
            index = clin.index(" with ")
            strng = clin[:index]
            argmt = clin[index + len(" with "):]

            #Fix text value
            if strng in actS : strng = actS[strng]
            elif strng.startswith("'") and strng.endswith("'") : strng = strng.replace("'", "")
            else : Error("[Compiler Error] Cannot print a non string.", "lin", lines[l])

            #Replace by a int
            if "[i]" in strng and IsAInt(argmt, actI) == True : #
                
                #Number
                try : #
                    
                    int(argmt)
                    print(strng.replace("[i]", argmt))
                #

                #Variable
                except ValueError :
                    print(strng.replace("[i]", str(actI[argmt])))
            #

            #Replace by a str
            elif "[s]" in strng and IsAStr(argmt, actS) == True : #

                #Text
                if argmt.startswith("'") : #
                    
                    #Empty
                    if argmt == "''" : argmt = ""
                    
                    #Remove apostrophos
                    else : argmt = argmt[1:len(argmt) - 1]

                    print(strng.replace("[s]", argmt))
                #

                #Variable
                else : print(strng.replace("[s]", actS[argmt]))
            #
            
            #Replace by a bol
            elif "[b]" in strng and IsABol(argmt, actB) == True : #
                
                #Value
                if argmt == "yes" : print(strng.replace("[b]", "yes"))
                elif argmt == "not" : print(strng.replace("[b]", "not"))
                
                #Variable
                else : #
                    
                    if actB[argmt] == True : print(strng.replace("[b]", "yes"))
                    if actB[argmt] == False : print(strng.replace("[b]", "not"))
                #
            #

            #Replace by a flt
            elif "[f]" in strng and IsAFlt(argmt, actF) == True : #
                
                #Value
                if argmt.endswith(".f") : argmt = argmt.replace(".f", "")

                #Number
                try : #
                    
                    float(argmt)
                    print(strng.replace("[f]", argmt))
                #

                #Variable
                except ValueError :
                    print(strng.replace("[f]", str(actF[argmt])))
            #

            #Replace by a lst
            elif "[l]" in strng and IsALst(argmt, actL) == True : #

                #Variable
                if argmt in actL :
                    
                    #Get list from actL
                    argmt = actL[argmt]

                    #Initidal visible list
                    toShow = "["

                    #Get just the values
                    for item in argmt : #
                        
                        if "'" in item : item = item.replace("'", "")

                        if item == "" : next
                        elif item == max(argmt.keys()) : toShow = toShow + str(argmt[item]) + "]" 
                        else : toShow = toShow + str(argmt[item]) + ", "
                    #

                    print(strng.replace("[l]", toShow))
                #

                #Value
                else : print(strng.replace("[l]", argmt))
            #

            #Without Keyword
            else : Error("[Compiler Error] Sitation Keyword not found.", "lin", lines[l])
        #

        #Is a str value
        elif clin.startswith("'") and clin.endswith("'") : #
            
            #Empty
            if clin == "''" : clin = ""
            
            #Remove apostrophos
            else : clin = clin[1:len(clin) - 1]

            print(clin)
        #

        #Is other str
        elif clin in actS : print(actS[clin])

        #Input
        elif clin.startswith("sand") : print(Sand(clin, lines[l], actS))

        #Error
        else : Error("[Compiler Error] Bucket cannot show this.", "lin", lines[l])
    #

    #List functions

    #fin
    if clin.startswith("fin ") : #
        
        #Remove keyword
        clin = clin.replace(clin[0:4], "")

        #Get list
        word = clin.split()

        #find item[0] in[1] list[2] to[3] item[4]

        #Need a int to get str index
        if word[4] in actI and IsAStr(word[2], actS) : actI.update({word[4] : Fin(clin, lines[l], actS, actL)})
        
        #Need a str to get lst index
        elif word[4] in actS and IsALst(word[2], actL) : actS.update({word[4] : Fin(clin, lines[l], actS, actL)})
        
        #Something else
        else : Error("[Compiler Error] Type error or unknown variables.", "lin", lines[l])
    #

    #add
    if clin.startswith("add ") : #
        
        #Remove keyword
        clin = clin.replace(clin[0:4], "")

        #Get list
        word = clin.split()

        #add item[0] on[1] list[2] as[3] value[4]

        if word[2] in actL : actL[word[2]].update(Add(clin, lines[l], actL))
        else : Error("[Compiler Error] This list do not exist.", "lin", lines[l])
    #

    #del
    if clin.startswith("del ") : #
        
        #Remove keyword
        clin = clin.replace(clin[0:4], "")

        #Get list
        word = clin.split()

        #del item[0] of[1] list[2]

        if word[2] in actL : actL.update(Del(clin, lines[l], actL))
        else : Error("[Compiler Error] This list do not exist.", "lin", lines[l])
    #
    
    #siz
    if clin.startswith("siz ") : #
        
        #Remove keyword
        clin = clin.replace(clin[0:4], "")
        
        #For index
        ledr = clin
        ledr = ledr.replace("of ", "")
        
        #siz of list to var

        index = ledr.find(" to ")
        aList = ledr[:index]
        vName = ledr[index + 4:]

        #This list exists
        if aList in actL : #
            
            if vName in actI : actI.update(Siz(clin, lines[l], actL[aList]))
            else : Error("[Compiler Error] Siz function returns a int, so it needs a int to assign.", "lin", lines[l])
        #

        elif aList in actS : #

            if vName in actI : actI.update(Siz(clin, lines[l], actS[aList]))
            else : Error("[Compiler Error] Siz function returns a int, so it needs a int to assign.", "lin", lines[l])
        #

        else : Error("[Compiler Error] This list do not exist.", "lin", lines[l])
    #

    #brk
    if clin.startswith("brk ") : #
        
        clin = clin.replace(clin[0:4], "")

        word = clin.split()

        #brk string[0] in[1] word[2] to[3] var[4]

        #Unknow vars
        if not word[0] in actS : Error("[Compiler Error] This string do not exist.", "lin", lines[l])
        if not word[4] in actL : Error("[Compiler Error] Cannot assign to a nonexistent list.", "lin", lines[l])

        #List exits
        else : actL.update(Brk(clin, lines[l], actS))
    #

    #loops

    #For Loop
    if clin.startswith("for ") : #
        
        #for x times if y ~ z do:

        loop = NewForLoop(l, lines, actI)
        
        #Return :
        #max count|question|variable|start/end line

        #No return
        if loop == None : Error("[Syntax Error] No loop ender.", "lin", lines[0])
        
        #variable type

        #Check a int
        if loop["v"] in actI : loop["v"] = actI
        
        #Check a str
        elif loop["v"] in actS : loop["v"] = actS
        
        #Check a bol
        elif loop["v"] in actB : loop["v"] = actB
        
        #Check a flt
        elif loop["v"] in actF : loop["v"] = actF
        
        #Non existent
        else : Error("[Compiler Error] This is not a variable to check.", "lin", lines[l])
        
        #For count
        for c in range(0, loop["m"]) : #

            #For every line
            for i in range(loop["s"], loop["e"]) : #
                
                #Question
                quest = LogicBlk(loop["q"], lines[l], loop["v"])

                #If True then ...
                if quest == True : #
                    
                    #Run other Runner
                    LittleRun(i, lines)
                    
                    #Update var
                    if loop["v"][""] == "int" : loop["v"] = actI
                    if loop["v"][""] == "str" : loop["v"] = actS
                    if loop["v"][""] == "bol" : loop["v"] = actB
                    if loop["v"][""] == "flt" : loop["v"] = actF
                #
            #
        #
    #

    #For Loop
    if clin.startswith("every ") : #

        #every item in list do:
        loop = NewEveryLoop(l, lines, actL)

        #Return :
        #var name| var list| start l| end line|

        #No return
        if loop == None : Error("[Syntax Error] No loop ender.", "lin", lines[0])

        #For count

        #Remove type index
        List = {"" : "",}
        List.update(loop["l"])
        del List[""]

        #for every item in list do:
        for c in List : #
            
            indx = loop["l"][c]

            #Create temporary variable
            if type(indx) == int : actI.update({loop["v"] : indx})
            elif type(indx) == str : actS.update({loop["v"] : indx})
            elif type(indx) == bool : actB.update({loop["v"] : indx})
            elif type(indx) == float : actF.update({loop["v"] : indx})

            #For every lile
            for i in range(loop["s"], loop["e"]) : #

                #Run other Runner
                LittleRun(i, lines)
            #
        #

        #Remove temporary variable
        if loop["v"] in actI : del actI[loop["v"]]
        if loop["v"] in actS : del actS[loop["v"]]
        if loop["v"] in actB : del actB[loop["v"]]
        if loop["v"] in actF : del actF[loop["v"]]
    #

    #Tasks

    #call
    if clin.startswith("call ") : #
        
        clin = clin.replace(clin[0:5], "")

        #call name: arg to var

        index = clin.find(" to ")
        taskD = clin[:index]
        vName = clin[index + 4:]
        argmt = None

        #Task configuration
        if ":" in taskD : #

            dataT = taskD.split(":")

            #task[0] arg[1]

            try : #

                tName = dataT[0]
                argmt = dataT[1]

                tName = tName.strip()
                argmt = argmt.strip()
            #

            except :
                Error("[Syntax Error] no argment gived.", "lin", lines[l])
        #
        
        #Just name
        else : tName = taskD

        #Get task data
        if tName in actT : taskD = actT[tName]
        else : Error("[Compiler Error] Trying to call a unknown task.", "lin", lines[l])

        #To del the temporary var
        varT = "nil"

        #Variables beafore task
        safeI, safeS, safeB, safeF = actI, actS, actB, actF

        #argment
        if argmt != None : #

            #No argment
            if taskD["v"] == "" : Error("[Compiler Error] This task do not requires a argment.", "lin", lines[l])

            #Add a temporary int
            if IsAInt(argmt, actI) == True : #
                
                varT = "int"
                actI.update({taskD["v"] : actI[argmt]})
            #

            #Add a temporary str
            if IsAStr(argmt, actS) == True : #
                
                varT = "str"
                actS.update({taskD["v"] : actS[argmt]})
            #

            #Add a temporary bol
            if IsABol(argmt, actB) == True : #
                
                varT = "bool"
                actB.update({taskD["v"] : actB[argmt]})
            #

            #Add a temporary flt
            if IsAFlt(argmt, actF) == True : #
                
                varT = "float"
                actF.update({taskD["v"] : actF[argmt]})
            #
        #

        #Run
        for i in range(taskD["s"], taskD["e"]) : #
            
            retrn = LittleRun(i, lines)
        #

        #Dell task variables
        
        #Int's
        for i in actI :                  
            if not i in safeI : del actI[i]
        
        #Str's
        for i in actS :                  
            if not i in safeS : del actS[i]
        
        #Bol's
        for i in actB :                  
            if not i in safeB : del actB[i]
        
        #Fts's
        for i in actF :                  
            if not i in safeF : del actF[i]

        #Remove the temporary var
        if argmt != None : #
            
            #Remove a int
            if varT == "int" : del actI[taskD["v"]]
            if varT == "str" : del actS[taskD["v"]]
            if varT == "bool" : del actB[taskD["v"]]
            if varT == "float" : del actF[taskD["v"]]
        #

        #No return
        if retrn == None :
            if not vName == "self." : Error("[Compiler Error] Tasks must return a value.", "lin", lines[taskD["e"]])

        #Return value
        else : #

            #Get the return type as string
            typ = str(type(retrn))
            typ = typ.replace("'", "")
            typ = typ.replace("<class ", "")
            typ = typ[:-1]

            #Check if var exists
            
            #A int
            if vName in actI : #

                if typ == "int" : actI.update({vName : retrn})

                #Not the same type
                else : Error("[Compiler Error] This variable do not acept the return type.", "lin", lines[l])
            #

            #A str
            elif vName in actS : #

                if typ == "str" : actS.update({vName : retrn})

                #Not the same type
                else : Error("[Compiler Error] This variable do not acept the return type.", "lin", lines[l])
            #

            #A bol
            elif vName in actB : #

                if typ == "bool" : actB.update({vName : retrn})

                #Not the same type
                else : Error("[Compiler Error] This variable do not acept the return type.", "lin", lines[l])
            #
        
            #A flt
            elif vName in actF : #

                if typ == "float" : actF.update({vName : retrn})

                #Not the same type
                else : Error("[Compiler Error] This variable do not acept the return type.", "lin", lines[l])
            #

            #Unknown varible
            else : Error("[Compiler Error] This is not a declareted variable.", "lin", lines[l])
        #
    #

    #Task return
    if clin.startswith("return ") : #

        clin = clin.replace("return ", "")

        #Return variable value
        if clin in actI : return actI[clin]
        elif clin in actS : return actS[clin]
        elif clin in actB : return actB[clin]
        elif clin in actF : return actF[clin]
        else : #

            try : #
                
                if clin.startswith("'") and clin.endswith("'") : return clin.replace("'", "")
                elif clin == "yes" : return True
                elif clin == "not" : return False
                elif clin.endswith(".f") : return float(clin.replace(".f", ""))
                else : return int(clin)
            #

            except :
                Error("[Compiler Error] This is not a declareted variable.", "lin", lines[l])
        #
    #
#