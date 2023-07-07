# from multipledispatch import dispatch

# Polymorphism in python . . 
"""In Python polymorphism is the ability of an object to take on multiple forms or act as """

# duck typing . . 
"Duck Typing means if it behaves like duck it probably is duck . . "

class pyCharm:
    def execute(self):
        print("Executing in Pycharm")
        print("compiling and running . . ")
    
# this both class have same method name execute it behaves same. .  

class MyEditor:
    def execute(self):
        print("Executing my editor...")
        print("spell ckeck . .")
        print("convension check . . ")
        print("Compile and running . . ")
        
class Laptop:
    
    def code(self, ide):
        ide.execute()
        
# ide = pyCharm()
ide = MyEditor()
lap = Laptop()
lap.code(ide)

# Operator Overloading. . .

a = 5
b = 4
print(a + b)

# using magic method . .
# this are operator overloading 
# same method name but the arguments are differrent like number of arguments and type of arguments . . .
print(int.__add__(a, b))  # add method
print(int.__sub__(a, b))  # sub method
print(int.__mul__(a, b))  # mul method


# method overloading . . .

# python dose not support method overloading in normal way . .  
class student:
    def __init__(self) -> None:
        pass
    
# in this method parameters have overloading . . .
    def sum(self, a=None, b=None, c=None):  
        s = 0
        if a is not None and b is not None and c is not None:
            s = a + b + c
        elif a is not None and b is not None:
            s = a + b
        else:
            s = a
        return s
    
s1 = student()
print(s1.sum(12, 34))

# #  method overloading in other way . .
# @dispatch(int, int)
# def A(n, m):
#     s = n + m
#     print(s)

# def A(n, m, o):
#     s = n + m - o
#     print(s)

 
# A(23, 12)
# A(23, 14, 45)


# Method Overriding . . 

class A:
    def show(self):
        print("In A show")
        
#  in this show method of class A override in class B . .
class B(A):
    def show(self):
        print("In B show")
    
a1 = B()
a1.show()

