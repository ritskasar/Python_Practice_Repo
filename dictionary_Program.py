# dictionary in python . .

programming_Dictionary = {
    "Functions": "a piece of code , you can easily use . .",
    "bug": "errors in program . ."
}

print(programming_Dictionary)  # print dictionary . .

# for print single element . .
print(programming_Dictionary["bug"]) 

# Adding new item to dictionary . .
programming_Dictionary["loop"] = "action repeatation"
print(programming_Dictionary)

# also can create a empty dictionary . .
empty_Dictionary = {}

# wipe an existing dictionary . .
# programming_Dictionary = {}
# print(programming_Dictionary)

# edit an item in dictionary . .
programming_Dictionary["bug"] = "A computer error . . ."
print(programming_Dictionary)

# loop through a dictionary . . 
for key in programming_Dictionary:
    print(key)
    print(programming_Dictionary[key])
    
    
# nesting a list in dictionary . .

travel_log = {
    # nesting dictionary in a dictionary . . 
    "India": {"cities_visited": ["mumbai", "delhi", "pune", "banglor"], 
              "total_Visits": 12},
    
    "Korea": ["seoul", "daegu", "busan"],
}
print(travel_log)


