# Bucket Programming Language
Bucket is a esoteric programing language inspired in ZOMBIE, python, lua and C#. Bucket are hight level, iperative, and terminal-oriented.
The name "Bucket" means Basic Unity-Control to Kindle Eletrical Tapes. With Bucket you can do simple scripts to read, edit, add, replace or anything a computer can do with user input. For example, a sand castle.

# Hello world in Bucket:
      
      [to Basic]
      #helloworld in Bucket:
      
      bucket open:
      show: 'Hello world!'
      end m.
      
      close.

# API Reference

The script file extention is .bk

## Create script
Your code must have the ``[to Basic]`` library declared, before all, and you should put the same name in the class and the file, example:
      
      -- example.bk --
      
      [to Basic]
      #example in Bucket:
      
      -- Your code --
      close.

## Comment
Anything between ``--`` is removed from the script, example:                                                                               

      show: 'the comentary will -- not -- desappear' --look!--
      >>> the comentary will desappear

## Bucket default functions
The classic functions inported by the ``[to Basic]`` library.

### Output
``show: `` : requires a string. Prints something in the terminal.                                                                       
You can give arguments to ``show:`` function, example: 

      show: 'value: [0] + [1] = [2]' with 2, 3, 5
      >>> value: 2 + 3 = 5

### Input
``sand`` : returns the user input.                                                                                                       
You can give arguments to ``sand:`` function, example:

      sand: with 'your value: '
      <<< value:

### Variables

``num`` : declares a number. Negatives and positives, integers or floats.                                                               
``str`` : declares a string value. A text between simple apostrophe (').                                                            
``bol`` : declates a binary value. Can be true (yes) or false (not).                                                                     

You can turn a variable into a list with the keyword ``lst`` before the data type keyword, example.                                     
``lst str as [0 : 'a', 1 : 'b', 2 : 'c']``

The list index are a 4th type of data, "text". This means you have no to convert variables to use as index. '0' is the same of 0, for example.

### Data manangement
You can change the data type of an variable, you can add or remove values, etc.

``set [name] to [value]`` : sets a new value to a variable.                                                                             
``[name]`` : variable name. ``[value]`` : other variable or value.

``make: [name] [operator] [value]`` : makes a math operation (+, -, *, /, %, ^).                                                   
``[name]`` : variable name. ``[operator]`` : math operation to do. ``[value]`` : other variable or value.                               
``+`` : add. ``-`` subtract. ``*`` : multyply. ``/`` : divide. ``%`` : rest of division. ``^`` : power.

``rise: [name]`` : increases a numeric variable by 1.                                                                       
``[name]`` : variable name.

``down: [name]`` : decreases a numeric variable by 1.                                                                       
``[name]`` : variable name.

``round [name]``: rounds a number value.                                                                                                 
``[name]`` : variable name.

``convert [name] to [type]``: converts a variable to other data type, if it's possible.                                                 
``[name]`` : variable name. ``[type]`` : the new variable type, the same of declaration keywords.

### Logic door
``if`` runs the lines bellow if the statlement is true. ``if`` block structure:                                                           
      
      if yes do:
      
      -- Something --
      end.
      
``even`` is called if the last logic block evalues to false. It runs the lines bellow if the statlement is true. ``even`` block structure: 

      if not do:
      end.
      
      even yes do:
      
      -- Something --
      end.
  
  ``else`` is called if the last logic block evalues to false. ``else`` block structure:
  
      if not do:
      end.
      
      else:
      
      -- Something --
      end.
      
  ## Logic Decay
  
      yes and yes
      >>> yes
      
      yes and not
      >>> not
      
      not and not
      >>> not
      
      yes or yes
      >>> yes
      
      yes or not
      >>> yes
      
      not or not
      >>> not
      
``and`` have a greater priority than ``or``, so it's replaced by decayed value first. Example:

      yes and yes or yes and not
      >>> yes or not
      >>> yes
      
You can understand it like this: ``(yes and yes) or (yes and not)``

## Main function and Tasks
The main function is the first and only block executed automatically. You can open the main function block with ``bucket open:`` and close it with ``end m.``.

      bucket open:
      -- your code --
      end m.

To declare a ``task`` use the keyword ``task:``, example:

      print task:
      show: 'hello'
      end t.
      
To give an argument put the variable name in the end of line, example:
      
      question task:string
      
      make: string + '?'
      show: string
      
      end t.
      
Important: you can have just one argument. If you need more, use a list as argument.

An task returns a value with the ``return:`` keyword.
To call a task wich returns a value, uses:
      
      bucket open:
      
      str retrn as 're'
      call func: to retrn
      
      show: retrn
      
      close m.
      
      func task:sub
      
      make: sub + 'turn!'
      return: sub
      
      end t.
      
      >>> return!
      
To call a task with no return use:

      call func to self.
      
