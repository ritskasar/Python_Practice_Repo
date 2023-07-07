# simple function . . 

def greet():
    print("Hello World !")
    print("Namastey India !")
    print("Annyyoungseoo Korea !")
    
greet()


# function that allows for inputs . . 

def greet_with_name(name):  # here name is parameter . .
    print(f"Hello {name}!")
    print(f"Namastey {name} !")
    print(f"Annyyoungseoo {name} !")
    
    
greet_with_name("World")  # here world is argument . .

# function with multiple inputs . .

def greeting(name, location):
    print(f"Hello {name}")
    print(f"located in {location}")
    
greeting("India", "Asia_continent")

# function with assign argument . .
def numbers(a, b, c):
    print(f"a = {a} " + f" b = {b} " + f" c = {c}")
    
numbers(a=2, b=3, c=32)


# function with outputs . .

def format_name(f_name, l_name):
    """Take first name and last name and return title case version of name."""
    return (f"{f_name.title()} {l_name.title()}")

print(format_name("taehyoung", "kim"))