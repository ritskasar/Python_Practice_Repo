# Inheritance in pyhton . . 

class A:
    def feature1(self):
        print("feature1 working . . ")

# single level inheritance . . 
class B(A):
    # inti function . . 
    def __init__(self):  
        print("In b init . .")
    
    def feature2(self):
        print("feature2 working . . ")
        
a1 = A()
b1 = B()

a1.feature1()
b1.feature1()
b1.feature2() 

# multi-level inheritance . . 
class C(B):
    def __init__(self):
        super().__init__()   
        print("In c init . .")
    
    # class C is subclass of class B so class c can use class b init function . .  
    # If you create object of sub class it will first try find init of sub class
    # if it is not found then it will call init of super class
    def feature3(self):
        print("feature3 working . . ")
     
c1 = C()
c1.feature3()

# multiple inheritance . .    
class D(C, B):
    def __init__(self):
        super().__init__()   
        print("In d init . .")
    
    # multiple inheritence using comma separated classes in parenthesis
    def feature4(self):
        return super().feature4()
       
d1 = D()

# multi-level Inheritance . . 
class X:
    print("Feature x working . .")
    
class Y(X):
    print("feature y working . .")
    
class Z(Y):
    print("feature z working . .")
    
# multiple inheritance . .
class W(Z, Y):
    pass
    
z1 = Z()
