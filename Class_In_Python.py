# class in python . . 

# creating new class..
class computer:
    # creating function . . 
    def config(self): 
        print("i5, 16gb, 1TB")
        
# creating opject of class . .    
com1 = computer()
com2 = computer()

# call class with object . . 
computer.config(com1)

# calling function using class object . . 
com2.config()


# creat new class . . 
class Car:
    wheels = 4   # class / special variable . .
    # declaration of new init function . .
    
    @staticmethod
    def __init__(self):
        # instance variable . .
        self.mil = 10 
        self.com = "BMW"
    
    class feature:
        def power(self):
            return 'powerful'
            
# c1 = Car()
# c1.mil = 11
# print(c1.mil, c1.com, c1.wheels)
# Car.feature(c1)
# print(c1.feature)


