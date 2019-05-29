# BucketProgrammingLanguage
Bucket means Basic Unity Control to Kindle Eletrical Tapes.
With bucket you can do simple scripts to read, edit, add, replace
or anything a computer can do. Like a sand castle.

Example:

  ``[to Basic]

  #helloworld in Bucket:

      bucket open:
    
          show 'Hello world!'
      end m.
  close.``

You can just have one main file, but how may toys (imported scripts)
you want.

Comands:
``[to Basic]`` : declares the main library.
``[to MathF]`` : imports mathematical stuff.
``#name in Bucket`` : declares the the script as main class (replace name
by the file name). Close the class block with ``close.``.

``bucket open:`` : the main method. It's the first method called by Bucket.
Close with ``end m.``.

``show`` : prints a string. You can put cits (citations) in the string, like
``[i]`` to cit ints, ``[s]`` to strings, ``[b]`` to boolans and ``[f]`` to
floats. Bucket replaces the sit by the value after ``with`` keyword. Example:

``
show 'int bol = [i]' with 3
``


