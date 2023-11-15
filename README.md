# python

1. Python documentation uses single quotes, we can use single or double, we just need to keep it consistent.

2. Most programmers and programming languages start counting from zero (0).

3. List --> a way of containing values all in the same place / variable. 
        --> it is represented by square brackets [] and the values are separated by comma (,).

4. while True --> a way of deliverately inducing a loop that by default is going to go forever.

5. Dictionaries (dict) --> data structure that allows us to associate one value with another. 
                       --> it is represented by curly braces {}, and it contains keys and values
                       --> {"key": "value"} associated by colon (:), and separated by comma (,).

6. Return --> is even stronger than break, it won't only break out of a loop, but it will also return a value for us.

7. NameError --> variables that we meant to define but somehow we didn't.

8. Accessing List Items:
        Indexing --> [0] access to the first item of the list
                 --> [1] access to the second item of the list
                 -->[-1] access to the last item of the list
                 -->[-2] access to the second last item of the list

9. Rounding floats to two decimal places. 
        e.a. 
                x = 3.14159265
                y = round(x, 2)

10. Try, Except, Else, and Finally Syntax -->
                                                try:
                                                        # Some Code.... 
                                                except:
                                                        # optional block
                                                        # Handling of exception (if required)
                                                else:
                                                        # execute if no exception
                                                finally:
                                                        # Some code .....(always executed)

11. Files access modes:
        Access modes govern the type of operations possible in the opened file. It refers to how the file will be used once its opened. These modes also define the location of the File Handle in the file. File handle is like a cursor, which defines from where the data has to be read or written in the file. There are 6 access modes in python.
                
                --> Read Only (‘r’) : Open text file for reading. The handle is positioned at the beginning of the file. If the file does not exists, raises the I/O error. This is also the default mode in which a file is opened.
                --> Read and Write (‘r+’): Open the file for reading and writing. The handle is positioned at the beginning of the file. Raises I/O error if the file does not exist.
                --> Write Only (‘w’) : Open the file for writing. For the existing files, the data is truncated and over-written. The handle is positioned at the beginning of the file. Creates the file if the file does not exist.
                --> Write and Read (‘w+’) : Open the file for reading and writing. For an existing file, data is truncated and over-written. The handle is positioned at the beginning of the file.
                --> Append Only (‘a’): Open the file for writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.
                --> Append and Read (‘a+’) : Open the file for reading and writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.

12. 