# file handeling : allow to deal with text files 
    # ---> text -- read, delete, update, new text files cre
    
# open() --> help to work with text files 

# how to read a text file using python


# f = open(r"C:\Users\17nru\OneDrive\Desktop\testing.txt", "r")

# d = f.read() # read entire file data

# print(d)



# f = open(r"C:\Users\17nru\OneDrive\Desktop\testing.txt", "r")

# print(f.readline())
# print(f.readline())
# print(f.readline())

# print(f.readlines())


# how to write in text files using python

# x = open("home.txt", "w")

# x.write("whyyyyyyyyyyyy")

# x.close()

# -> create a new file if not exist 
# -> if file exist, it delete old data and add new on only
# --> it erase old data 


# a mode 

y = open(r"C:\Users\17nru\OneDrive\Desktop\pyyyy.txt", "a")

y.write("\nniceeeeeeeeeeeee")

y.close()

# --> craete a new file if not exist 
# --> do not erase old data it adds new data at the end of old data 



# Problem : 
    
# take user name, and after that user adding two numbers 


# -------- Naresh -------------------
# first number : 12
# second number : 20
# Sum of these two numbers : 32

# -------- Ramesh -------------------
# first number : 1
# second number : 2
# Sum of these two numbers : 3

# -------- Ramesh -------------------
# first number : 1
# second number : 2
# Sum of these two numbers : 3

# -------- Ramesh -------------------
# first number : 1
# second number : 2
# Sum of these two numbers : 3
