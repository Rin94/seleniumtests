class A:
    def sayhi(self):
        print("I'm in A")

class B(A):

    def sayhi(self):
        print("I'm in B")

objB=B()

objB.sayhi()

#Python does not support method overloading

def add(instanceOf,*args):
    if instanceOf=='int':
            result=0
    if instanceOf=='str':
            result=''
    for i in args:
            result+=i
    return result

res=add('int',3,4,5)
print(res)

res2=add('str',"Rolando","Mota","Del Campo")
print(res2)

"""
On the other hand, we will learn Python MRO (Method Resolution Order).
At last, we will learn complications in Multiple Inheritance in Python Programming Language.
"""

class Mother:
    pass
class Father:
    pass

class Child(Mother,Father):
    pass

print(issubclass(Child,Mother) and issubclass(Child,Father))
print(Child.__mro__)
print(Child.mro())

class A:
    id=1
class B:
    id=2
class C:
    id=3
class M(A,C,B):
    pass

M.id

class A:
    def sayhi(self):
        print("A")
class B:
    def sayhi(self):
        print("B")

class M(A,B):
        pass

m=M()
m.sayhi()