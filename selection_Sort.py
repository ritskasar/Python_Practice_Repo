# Selection Sort in python . . 

def selection_Sort(arr):
    
    for i in range(len(arr)):
        smallest = int(i) 
        # j = i + 1
        for j in range(i + 1, len(arr)):
            if arr[smallest] > arr[j]:
                smallest = j
         
    # swapping in python . .    
        arr[i], arr[smallest] = arr[smallest], arr[i]  
        # swapping
        # temp = arr[smallest]
        # arr[smallest] = arr[i]
        # arr[i] = temp
        
    print(f"Sorted array is: {arr}")
    
    
# list
arr = input("Enter numbers into list : ").split()
for i in range(len(arr)):
    arr[i] = int(arr[i])
    
selection_Sort(arr)