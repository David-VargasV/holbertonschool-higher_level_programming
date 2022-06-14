# 0x0C. Python - Almost a circle 💻💻💻
***

![image](https://user-images.githubusercontent.com/98335124/173697736-a0c0a121-6024-4066-b0df-851751258501.png)
***

## Learning 📜📖
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

*args and **kwargs are mostly used in function definitions. *args and **kwargs allow you to pass a variable number of arguments to a function. What does variable mean here is that you do not know before hand that how many arguments can be passed to your function by the user so in this case you use these two keywords.

JSON as we know stands for JavaScript Object Notation. It is a lightweight data-interchange format and has become the most popular medium of exchanging data over the web. The reason behind its popularity is that it is both human-readable and easy for machines to parse and generate. Also, it’s the most widely used format for the REST APIs. Python provides a built-in json library to deal with JSON objects. All you need is to import the JSON module using the following line in your Python program and start using its functionality.

The unittest unit testing framework was originally inspired by JUnit and has a similar flavor as major unit testing frameworks in other languages. It supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework.

You will also learn about:

* args and kwargs
* Serialization/Deserialization
* JSON
***

## Requirements 🔧
***

### General
#### Python Scripts
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.8.*)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should be documented: python3 -c 'print(__import__("my_module").__doc__)'
* All your classes should be documented: python3 -c 'print(__import__("my_module").MyClass.__doc__)'
* All your functions (inside and outside a class) should be documented: python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

#### Python Unit Tests
* Allowed editors: vi, vim, emacs
* All your files should end with a new line
* All your test files should be inside a folder tests
* You have to use the unittest module
* All your test files should be python files (extension: .py)
* All your test files and folders should start with test_
* Your file organization in the tests folder should be the same as your project: ex: for models/base.py, unit tests must be in: tests/test_models/test_base.py
* All your tests should be executed by using this command: python3 -m unittest discover tests
* You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base.py
* We strongly encourage you to work together on test cases so that you don’t miss any edge case
***

## Files models
* [base_py](https://github.com/David-VargasV/holbertonschool-higher_level_programming/blob/main/0x0C-python-almost_a_circle/models/base.py)
* [rectangle.py](https://github.com/David-VargasV/holbertonschool-higher_level_programming/blob/main/0x0C-python-almost_a_circle/models/rectangle.py) 
* [square.py](https://github.com/David-VargasV/holbertonschool-higher_level_programming/blob/main/0x0C-python-almost_a_circle/models/square.py)
***

## Tasks 📝
0. If it's not tested it doesn't work - All your files, classes and methods must be unit tested and be PEP 8 validated.

1. Base class - Write the first class Base:
Create a folder named models with an empty file __init__.py inside - with this file, the folder will become a Python package
Create a file named models/base.py

2. First Rectangle - Write the class Rectangle that inherits from Base

3. Validate attributes - Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded)

4. Area first - Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.

5. Display #0 - Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here.

6. __ str __ - Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>

7. Display #1 - Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y

8. Update #0 - Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute

9. Update #1 - Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes

10. And now, the Square! - Write the class Square that inherits from Rectangle

11. Square size - Update the class Square by adding the public getter and setter size

12. Square update - Update the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes

13. Rectangle instance to dictionary representation - Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle

14. Square instance to dictionary representation - Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square

15. Dictionary to JSON string - Update the class Base by adding the static method def to_json_string(list_dictionaries): that returns the JSON string representation of list_dictionaries

16. JSON string to file - Update the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file

17. JSON string to dictionary - Update the class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string

18. Dictionary to Instance - Update the class Base by adding the class method def create(cls, **dictionary): that returns an instance with all attributes already set

19. File to instances - Update the class Base by adding the class method def load_from_file(cls): that returns a list of instances
***
