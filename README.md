# AirBnB Clone

![hbnb image](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220806%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220806T223525Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=cee3349af2a5df862898b092559491add2ff554e91dc5df0bd9c040a241d09f5)

## Description
The AirbnB clone is a **web application project** that consists of four(4) different parts:

- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## The Console
This part of the project is to create a *console (a command interpreter)* that uses
file storage system to manipulate data
The goal of the *console* part fo the project is to:
- create a data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will
give us an abstraction between “My object” and “How they are stored and persisted”.
This means: from your *console code (the command interpreter itself)* and from the
*front-end and RestAPI* you will build later, you won’t have to pay attention (take care)
of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The *console* will be a tool to validate this storage engine.

![console image](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220806%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220806T223525Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=28e5262b207e8292282c7430e27755d77c976d26225200189cb47975323eb623)


## Execution
The *console(shell)* should work like this in **interactive mode**

```
~$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  create  help  quit

Undocumented commands:
======================
all  destroy  show  update

(hbnb) help quit
Quit command to exit the program
(hbnb) quit
~$
```

But also in **non-interactive mode**: (like the Shell project in C)

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

- All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash
