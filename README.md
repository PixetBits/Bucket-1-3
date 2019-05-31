# BucketProgrammingLanguage
Bucket means Basic Unity Control to Kindle Eletrical Tapes. With bucket you can do simple scripts to read, edit, add, replace or anything a computer can do with user input. Like a sand castle.

# Hello world in Bucket:

      [to Basic]
      #helloworld in Bucket:
      
      bucket open:
      show 'Hello world!'
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
      
      example task:
      show 'something'
      end t.
      
      close.
      
 The main file imports the example task of toy class and call it after importing. 

# Main method and tasks
The main method, ``bucket open:``, are the only place where have execution. Tasks are just functions wich can get, or not, values and "die" after run, returning a value or not. Basicly Tasks are a extention of the single method.

      bucket open:
      call print to self.
      
      int number as 10
      call other:number to number
      end m.
      
      print task:
      show 'Hello!'
      end t.
      
      other task: num
      make num + 1
      return num
      end t.

Here the Main calls the task "print" and set as a no return mode, ``to self.``. Then calls the "other", giving the value of the variable number to return to itself. 
