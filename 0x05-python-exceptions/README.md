# 0x05. Python - Exceptions
***

![image](https://user-images.githubusercontent.com/98335124/169899935-7d11f2da-c4c6-4d5d-a689-fc72e4a3928b.png)
***

## Learning
* The **try** block lets you test a block of code for errors.
* The **except** block lets you handle the error.
* The **else** block lets you execute code when there is no error.
* The **finally** block lets you execute code, regardless of the result of the try- and except blocks.

When an error occurs, or exception as we call it, Python will normally stop and generate an error message, these exceptions can be handled using the try statement.
You can use the else keyword to define a block of code to be executed if no errors were raised. The finally block, if specified, will be executed regardless if the try block raises an error or not, this can be useful to close objects and clean up resources. As a Python developer you can choose to throw an exception if a condition occurs, to throw (or raise) an exception, use the raise keyword. The raise keyword is used to raise an exception. You can define what kind of error to raise, and the text to print to the user.
***

## Requirements
***

### General
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.8.*)
* All your files must be executable
* The length of your files will be tested using wc
***

## Tasks
0. Safe list printing - Write a function that prints x elements of a list.
1. Safe printing of an integers list - Write a function that prints an integer with "{:d}".format().
2. Print and count integers - Write a function that prints the first x elements of a list and only integers.
3. Integers division with debug - Write a function that divides 2 integers and prints the result.
4. Divide a list - Write a function that divides element by element 2 lists.
5. Raise exception - Write a function that raises a type exception.
6. Raise a message - Write a function that raises a name exception with a message.
