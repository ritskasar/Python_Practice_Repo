import math

def area(height, width, cover):
    area = height * width
    area_to_cover = math.ceil(area / cover)
    print(f"Area for use = {area_to_cover}")
  
height = int(input("Enter Height : "))
width = int(input("Enter width :"))
area(height, width, cover=5)
