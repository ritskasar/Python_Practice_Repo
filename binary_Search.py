#  Binary search method using python . .

def binary_Search(arr, key):
    start = 0 
    end = len(arr) - 1 
    for i in range(len(arr)):
        # calculate mid value . .
        mid = int((start + end) / 2) 
        # get ans when mid is equal to key number
        if arr[mid] == key:
            return mid
        
        elif arr[mid] < key:
            start = mid + 1  # reset start point
            
        else:
            end = mid - 1  # reset end point . .
            
    return -1

# list
arr = input("Enter number into list with ascending order : ").split()
# indexing list 
for i in range(len(arr)):
    arr[i] = int(arr[i])
# print(arr)

key = int(input("Enter which number you want to find from list : "))

index = int(binary_Search(arr, key))

if index == -1:
    print("Not found . .")
else:
    print(f"Number is found at index {index}")