marks = [98, 99, 100, "Maths"]
print(marks)
print(marks[1])   # in list print by index number . .
print(marks[-1: -3])   # also indexing in negative . .
print(marks[0: 2])

# using for loop in list . . 
for score in marks:
    print(score)
    
# nesting dictionary in list . . 
travel_log = [
    {
        "country": "India", 
        "cities_visited": ["Mumbai", "Delhi", "pune"], 
        "total_visits": 10
    },
    {
        "country": "korea", 
        "cities_visited": ["seoul", "daegu", "busan"], 
        "total_visits": 5 
    }
]

# function for dictionary elements. . .
def add_new_country(country, cities_visited, total_visits):
    new_country = {}
    new_country["country"] = country
    new_country["cities_visited"] = cities_visited
    new_country["total_visits"] = total_visits
    travel_log.append(new_country)

# calling function . . 
add_new_country("USA", ["New York", "Chicago", "Los Angeles", "Boston"], 10)
print(travel_log)