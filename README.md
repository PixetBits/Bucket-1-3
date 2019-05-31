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
