import random

random_Num = random.randint(1, 10)
print(random_Num)

random_Float = random.random()
print(random_Float)


# Heads and Tales game using random

random_Side = random.randint(0, 1)
if random_Side == 1:
    print("Heads")
else:
    print("Tales")
    
    