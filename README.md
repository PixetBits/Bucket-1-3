# Bucket Programming Language
Bucket is a esoteric programing language inspired in ZOMBIE, python, lua and C#. Bucket are hight level, iperative and terminal-oriented.
The name "Bucket" means Basic Unity-Control to Kindle Eletrical Tapes. With Bucket you can do simple scripts to read, edit, add, replace or anything an computer can do with user input. For example, a sand castle.

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
Your code must have the ``[to Basic]`` library declared, before all, and you should put the same name in the class and the file, e.g.
      
      -- example.bk --
      
      [to Basic]
      #example in Bucket:
      
      -- Your code --
      close.

## Comment
Anything between ``--`` is removed from the script, e.g.                                                                               

      show: 'the comentary will -- not -- desappear' --look!--
      >>> the comentary will desappear

## Join lines
To whrite two diferent lines in a single, use semicolons. e.g.

      show: 'hello ';show: 'world!'
      >>> hello world!

## Error skip
If a line can rise an error, put a ``?`` in the end of the line, e.g.

      str number as 1
      >>> [Compiler Error] This is not a string value. In line [str number as 0]
      
      str number as 1?
      >>>

## Bucket default functions
The classic functions inported by the ``[to Basic]`` library.

### Output
``show: `` : requires a string. Prints something in the terminal.                                                                       
You can give arguments to ``show:`` function, e.g. 

      show: 'value: [0] + [1] = [2]' with 2, 3, 5
      >>> value: 2 + 3 = 5

### Input
``sand`` : returns the user input.                                                                                                       
You can give arguments to ``sand:`` function, e.g.

      sand: with 'your value: '
      <<< value:

### Variables

``num`` : declares a number. Negatives and positives, integers or floats.                                                               
``str`` : declares a string value. A text between simple apostrophe (').                                                            
``bol`` : declates a binary value. Can be true (yes) or false (not).                                                                     

You can turn a variable into a list with the keyword ``lst`` and the data type between square brackets, e.g.                             

      lst[str] as [0 : 'a', 1 : 'b', 2 : 'c']

The list index are a 4th type of data, "text". This means you have no to convert variables to use as index. '0' is the same of 0, for example.

### Data manangement
You can change the data type of an variable, you can add or remove values, etc.

``set [name] to [value]`` : sets the value of ``value`` to a ``name``.                                                                 

``make: [name] [operator] [value]`` : move the result of a math operation (+, -, *, /, %, ^) between ``name`` and ``value`` to ``name``. 
opetators: ``+`` : add; ``-`` subtract; ``*`` : multyply; ``/`` : divide; ``%`` : rest of division; ``^`` : power.

``rise: [name]`` : increases ``name`` (a numeric variable) by 1.                                                                       

``down: [name]`` : decreases ``name`` (a numeric variable) by 1.                                                                  

``round [name]``: rounds the value of ``name`` (a numeric variable).

``convert [name] to [type]``: converts a ``name`` to ``type``, if it's possible.                                                 

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

## Loops
Loops are blocks of code that are repeated a given number of times following a condition. Bucket supports ``For``, ``Every`` and ``While`` loops.

### For loop
Syntax: ``for [num] times if [statlement] do: ... end l.``
For Loop tries to repeat the code ``num`` times if the ``statlement`` is true.

### Every loop
Syntax: ``every [item] in [lst] do: ... end l.``
Every loop repeats the block for every ``item`` in ``lst``.

### While loop
Syntax: ``while [statlement] do: ... end l.``
While loop repeats the code while the ``statlement`` is true.

### break.
Use the ``break.`` keyword to kill a loop.

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
      
      str val as 're'
      call func:val to val
      
      show: val
      close m.
      
      func task:sub
      
      make: sub + 'turn!'
      return: sub
      end t.
      
      >>> return!
      
To call a task with no return use:

      call func to self.
      
## Meta characters
Meta characters or Metachars are special simbles that represents a string value, like spaces or new lines.

``{n}`` New Line: breaks the line.                                                                                                       
``{s}`` Space: represents a space.                                                                                                       
``{q}`` Simple quote: represents ``'``.                                                                                                 
``{b}`` Backspace: represents backspace.                                                                                                 
``{t}`` Tab: represents tab (multiple spaces).                                                                                           

Metachar match are not implemented yet.
