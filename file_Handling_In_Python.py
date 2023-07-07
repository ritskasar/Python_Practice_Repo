# file handling in python . . 

# to read data from file . . 
file = open('MyData.txt', 'r')
print(file.readline())

# to write data into file . . 
file = open('abc', 'w')
file.write("Hello World ! ")

# to append / or more add data into file . . 
file = open('abc', 'a')
file.write("Welcome to the coding world . . .")
file = open('abc', 'r')
print(file.readline())

# to read img-file
pic1 = open('pic.jpg', 'rb')
# to write img-file . . 
pic2 = open('MyPic.jpg', 'wb')

# converting pic1 img-file to pic2 img-file . .
for i in pic1:
    pic2.write(i)

