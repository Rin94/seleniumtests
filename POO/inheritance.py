"""
The relationship from person to a student is termed Specialization
Coversely, every student is a person, this is called Generalization

Person:

Super Class
Parent Class
Base Class

Student is

Sub Class
Child Class
Derived Class

"""

class Person:
    pass

class Student (Person):
    pass

print(issubclass(Student, Person))
print(issubclass(Person,Student))
print(isinstance(Person,Student))

"""
Single Inheritance in when a single class inherits from a class
"""
x=0
class fruit:
    def __init__(self):
        global x
        x+=1
        print("I'm a fruit")

class citrus(fruit):
    def __init__(self):
        super().__init__()
        global x
        x+=2
        print("I'm citrus")

lime=citrus()
lime
print(x)

"""
Multiple Inheritance
"""
class Color:
    pass
class Fruit:
    pass
class Orange(Color, Fruit):
    pass

print("Inheritance")
print(issubclass(Orange,Color) and issubclass(Orange,Fruit))

#Multilevel Inheritance Python

class A:
    x=1

class B(A):
    pass

class C(B):
    pass

cobj=C()
print("Multilevel")
print(cobj.x)

"""
Hierarchical Inheritance in Python
"""
class A:
    x=1

class B(A):
    pass
#ambas clases heradan de una misma clase
class C(A):
    pass

class D(B,C):
    pass

dobj=D()
print(dobj.x)

"""
Super function allows to call a method form the parent class
"""

class Vechicle:
    def start(self):
        print("Starting engine")

    def stop(self):
        print("Stopping engine")

class TwoWheeler(Vechicle):
    def say(self):
        super().start()
        print("I have two wheels")
        super().stop()

Pulsar=TwoWheeler()
Pulsar.say()