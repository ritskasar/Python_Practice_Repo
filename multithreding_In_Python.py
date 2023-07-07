# multithreding using python . . 

from threading import Thread
from time import sleep

class hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello ✋")
            sleep(1)
                 
class hi(Thread):
    def run(self):
        for i in range(3):
            print("Hi ✌️")
            sleep(1)
            
h1 = hello()
h2 = hi()

h1.start()
sleep(2)
h2.start()

h1.join()
h2.join()

print("Good Day . . ")