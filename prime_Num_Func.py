def primeNum(num):
    isPrime = True
    for i in range(2, num - 1):
        if num % i == 0:
            isPrime = False
            break
        
    if isPrime:
        print("Number is prime . . ")
    else:
        print("Number is not prime . . ")
        
        
num = int(input("Enter any number : "))
primeNum(num)