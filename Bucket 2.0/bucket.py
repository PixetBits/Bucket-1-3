"""
Bucket Script Runner by Mateus Morais
Current E. 2.0.0. Made in 08/05/2019.
Last version published in 08/05/2019.

Coments : -- Text --

Libraries in : [to *name*]
Script Class : #*name* in Bucket: (close.)

Main Method  : bucket open: (end m.)
Last Method  : Bucket full: (end m.)
Generic Task : *name* task: // arg (end t.)

var types (int : integers, str : strings, bol : booleans, flt : floats) [floats need be ended in ".f"]

declare vars : *type* *name* // as *value*
declare List : lst *type* *name* as [ *index* : *value*,] 

set value to : set *name* to *value*
get list val : set *variable* to *name* *index*

increment on : rise *name* in *value*
decrement on : down *name* in *value*

short in/dec : make *name* *operator* *value*

---------------------------------------------------------------------------

conditions (equals/unlike, greater/smaller, amost+/amost-)

if Structure : if *condition* do: (end.)
else if sttg : maybe *condition* do: (end.)
else setting : else do: (end.)

loop setting :

for *repeat count* times if *condition* "do: (end l.)
while *condition* do: (end l.)
every *variable* in *list* do: (end l.)

---------------------------------------------------------------------------

string definition : 'text'
string values sit : ([i] : int, [s] : str, [b] : bol, [f] : flt)

set sys out : show *string* // *string <<< (sit)* with *value* [cannot have two sit's]
get user in : sand // with *string*
"""

#Load by drag and drop
import sys

#Error Mesage
from ErrorMessage import Error

#Script Runner
from ScriptRunner import Runner

#File path replacer
from FixFileNames import Fixer

#Script Reader
def LoadFile(name, showN) : #

    #If the input have no the extention
    if name.endswith(".bk") == False : name = name + ".bk"

    # Open file and get every line
    try : #

        fileD = open(name)
        lines = fileD.readlines()
        fileD.close()
    
        Runner(lines, name, showN)
    #

    #No file with this name
    except FileNotFoundError :
        Error("Bucket needs an existent file. Check the name and try again.", "sys")

    except  OSError :
        Error("Strange characters in name file. Check it and try again.", "sys")
#

#Get name and path

try : #

    path = sys.argv[1]
    name = Fixer(path)
    print("\n--------------------\n")
#

except : #
	
    print("Bucket Interpreter 2.0. Copyright(c) BinaryBrain_ 2019 by Mateus M. Dias.")
    print("All rights reserved.\n")
    print("Open your bucket file (.bk) by name or path.\n")

    path = input("file name: ")

    name = Fixer(path)
    print("\nruning: " + name + "...")
    print("")
    print("-" * len("runing: " + name + "..."))
    print("")
#

#Open file
LoadFile(path, name)