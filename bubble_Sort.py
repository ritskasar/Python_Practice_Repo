# bubble sort in python . . 

def bubble_Sort(arr):
    # outer loop
    for i in range(len(arr)): 
        # inner loop . .
        for j in range(len(arr) - 1):
            # checking condition . .
            if arr[j] > arr[j + 1]:
                
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                
    print("Sorted list : ")
    # for i in range(len(arr)):
    #     arr[i] = int(arr[i])
    print(arr)
   
# list 
arr = input("Enter numbers into list : ").split()
# indexing numbers of list . .
for i in range(len(arr)):
    arr[i] = int(arr[i])

bubble_Sort(arr)
