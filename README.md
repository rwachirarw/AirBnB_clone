# AirBnB clone Project
Welcome to the AirBnB clone project:Before starting,
This is the console /command interpreter for the alx  Airbnb clone project. The console can be used to store objects in and retrieve objects from a JSON.
This project is designed to help you build a simplified version of the AirBnB platform and is an essential step towards creating a full web application. In this README, we will guide you through the setup usage, and key information about this project.

-----------------------------------------------------------------------------------------
This project is aimed at achieving the following key objectives:
* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function
--------------------------------------------------------------------------------
### Supported classes:
The classes that will be created are as listed belliow
* BaseModel-This class will define the attributes and methods that are common 
* User - 
* State
* City
* Amenity
* Place
* Review

### Commands:
* create - create a new object
* show - show an object in relation to its id
* destroy - destroy or eliminate an object
* all - displays  all objects create
* quit/EOF - this will exit the console the console
* help -  will display the documentation that explain the working  of commands

## How to use the console:
To start th program, you need to navigate to the project folder and  run :  `./console.py` in  shell.

#### Create
`create <class name>`
Example:
`create BaseModel`

#### Show
`show <class name> <object id>`
Example:
`show User my_id`

#### Destroy
`destroy <class name> <object id>`
Example:
`destroy Place my_place_id`

#### All
`all` or `all <class name>`
Example:
`all` or `all State`

#### Quit
`quit` or `EOF`

#### Help
`help` or `help <command>`
Example:
`help` or `help quit`

In addition,the console will supports `<class name>.<command>(<parameters>)` syntax.
Example:
`City.show(my_city_id)`

## Resources
* [cmd module](https://docs.python.org/3.8/library/cmd.html)
* [cmd module in depth](https://pymotw.com/2/cmd/)
* [uuid module](https://docs.python.org/3.8/library/uuid.html)
* [datetime](https://docs.python.org/3.8/library/datetime.html)
* [unittest module](https://docs.python.org/3.8/library/unittest.html#module-unittest)
* [Testing Your Code with the unittest Module](https://www.youtube.com/watch?v=6tNS--WetLI)
* [Making a command line prompt program in Python](https://www.youtube.com/watch?v=lffgNFRLF9M&t=16s)
* [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
* [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)
* [cmd module wiki page](https://wiki.python.org/moin/CmdModule)
* [python unittest](https://realpython.com/python-testing/)

