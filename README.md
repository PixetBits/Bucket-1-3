# BucketProgrammingLanguage
Bucket is a esoteric programing language inspired in ZOMBIE, python, lua and C#. Bucket are hight level, iperative, and terminal-oriented.
Bucket means Basic Unity-Control to Kindle Eletrical Tapes. With Bucket you can do simple scripts to read, edit, add, replace or anything a computer can do with user input. For example, a sand castle.

# Hello world in Bucket:

      [to Basic]
      #helloworld in Bucket:
 
      bucket open:
      show: 'Hello world!'
      end m.
      
      close.

This script imports the Basic library, declares a class named by the file name (helloworld.bk), and shows a string on the main method, ``bucket open:``.

# Declare classes:

In Bucket we have two types of classes: ``in Bucket:`` and ``in PLayground:``. The ``in Bucket:`` class is the main file, and the ``in PLayground:`` are called as "Toy", a class wich can be imported by the main file.

## Main file :

      [to Basic]
      #mainclss in Bucket:
      
      with #otherclss in Sandbox.
      
      bucket open:
      call example to self.
      end m.
      
      close.
      
## Toy class :

      [to Basic]
      #otherclss in Playground:
      
      void example task:
      show: 'something'
      end t.
      
      close.
      
 The main file imports the ``example`` task from ``toy`` class and call it after importing. 

# Main method and tasks
The main method, ``bucket open:``, are the only place where have execution. Tasks are just functions wich can get, or not, values and "die" after run, returning a value or not. Basicly Tasks are a extention of the single method.

      -- Main method --
      bucket open:
      call print to self.
      
      num number as 10
      call other:number to number
      end m.
      
      -- Tasks --
      void print task:
      show 'Hello!'
      end t.
      
      num other task:num
      make num + 1
      return num
      end t.

Here the Main calls the task ``print`` in no return mode, with ``to self.`` keyword. Then calls ``other``, giving the value of the variable ``number``, and return to itself.

## Bucket default functions
Here we have the classic functions inported by the ``to Basic`` lib.

### Output
``show: `` : requires a string. Prints something in the terminal.
You can give arguments to ``show:`` function, example:
``show: 'value: [0] + [1] = [2]' with 2, 3, 5``
``>>> value: 2 + 3 = 5``

### Input
``sand`` : return the user input.
You can give arguments to ``sand:`` function, example:
``sand: with 'your value: '``
``<<< value: ``

### Variables

``num`` : declares a number. Negatives and positives, integers or floats.                                                               
``str`` : declares a string value. A text between simple apostrophe (').                                                            
``bol`` : declates a binary value. Can be true (yes) or false (not).                                                                     

You can turn a variable into a list with the keyword ``lst`` before the data type keyword, example.
``lst str as [0 : 'a', 1 : 'b', 2 : 'c']``

The list index are a 5th type of data, "text". This means you have no to convert variables to use as index. '0' is the same of 0, for example.

### Data manangement
You can change the data type of an variable, you can add or remove values, etc.

``set [name] to [value]`` : sets a new value to a variable.
* ``[name]`` : variable name. ``[value]`` : other variable or value.

``make: [name] [operator] [value]`` : multiplys, add or remove parts of an variable.   
* ``[name]`` : variable name. ``[operator]`` : math operation to do. ``[value]`` : other variable or value.

``rise: [name]`` : increases a numeric variable in an value by 1.
* ``[name]`` : variable name.

``down: [name]`` : decreases a numeric variable in an value by 1.
* ``[name]`` : variable name.

``round [name]``: rounds a number value.  
* ``[name]`` : variable name.

``convert [name] to [type]``: converts a variable to other data type, if it's possible.
* ``[name]`` : variable name. ``[type]`` : the new variable type, the same of keywords.
