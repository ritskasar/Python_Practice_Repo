# linear search in python . . 

def linear_Search(arr, key):
    for i in range(len(arr)):  # main logic for linear search
        if arr[i] == key:
            return i  
    return -1
    
# making random list . . 
arr = input("Enter number into list : ").split()
# assign indexing to numbers in list . .
for i in range(0, len(arr)):
    arr[i] = int(arr[i])
# print(arr)

key = int(input("Enter which number you want to find : "))
# call linear_search function
index = int(linear_Search(arr, key))

if index == -1:
    print("Number not found")
else:
    print(f"Index of number is {index}")