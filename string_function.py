# String : 
#     ---> is a simple data type
#     ---> string is immutable (not able modify)

# ----> having mutiple functions that return a new string

# data = "Programography Coaching Instetite"

# 1) upper()
    # ---> convert to upper case

# print(data.upper())

# 2) capitalize()
    # ---> capital first letter in a string


# zx = "this is a car and a good car"

# print(zx.capitalize())

# 3) lower()
  # ---> 

# zx = "Nice car How Are YOU"

# print(zx.lower())


# ---> title()

# zx = "This is a workd PROgramo HELLO Python"

# print(zx.title())



# x = "THis IS Fine GOOD to SEE You"


# reverse ---> 

# print(x.swapcase())


# count() --> 

# zx = "This is bus tain and plan showroom"

# print(zx.count("is"))

# searching ---


# zx = "Python is a good programming langge"

# find()

# print(zx.find("good"))

# print(zx.find("r"))

# print(zx.find("zyz"))


# zx = "Python is a good programming langge"

# rfind()
  # ---> highest index number 


# print(zx.rfind("g"))


# index()

# zx = "Hello Python"

# print(zx.index("P"))
# print(zx.index("o"))

# print(zx.rindex("o"))



# zx = ["Mr. Jhone", "Car", "Hello", "Mr. Mohan", "Mr. Khan"]

# try... get only words start wth MR.

# for i in zx:
#     if i[: 3] == "Mr.":
#         print(i)


# for i in zx:
#     if i.startswith("Mr."):
#         print(i)


# zx = ["Mr. Jhone", "Car", "Hello", "Mr. Mohan", "Mr. Khan"]

# for i in range(len(zx)):
#     print(zx[i])


# endswith()
#     ---


# zx = ["file.txt", "file2.pdf", "file3.pdf", "file4.py"]

# for i in zx:
#     if i.endswith(".pdf"):
#         print(i)


# zx = "Apple banana Mengo Python Java"

# split() -----> string to list conversion

# print(zx.split())

# split(split_by, how_many_splits)



# zx = "Nice, car work, done"

# print(zx.split(","))

# zx = "Nice Car. Car color is red. Python is not a car"

# print(zx.split("."))

# zx = "Nice- work- done car- ye wo"


# print(zx.split("-", 1))

# zx = "Hello world python programing"

# print(zx.split(" ", 3))

# zx = "Hello world python programing"

# print(zx.rsplit(" ", 1))





# data = """Pytho
# is a proragmming\n lanague
# why you lean python
# Good langaue"""

# print(data.splitlines())

# partition --- only one sapration

# zx = "10+20+90"

# in tuple

# print(zx.partition("+"))
# print(zx.rpartition("+"))




# join()

# conversion --> list to string

# zx = ["Apple", "Banan", "Mango", "Python"]

# p = ""

# for i in zx:
#     p = p + i + " "

# print(p)

# zx = ["Apple", "Banan", "Mango", "Python"]

# print("-".join(zx))
# print(" * ".join(zx))
# print(" ".join(zx))





# strip()
  # ----> to remove something from a string

# d = "yyyHelloyyy"

# print(d.strip("y"))


# x = "   Python  "

# print(x)

# print(x.strip())



# d = "yyyHelloyyy"

# print(d.strip("y"))
# print(d.lstrip("y"))
# print(d.rstrip("y"))


# zx = "Python is a programing lagae to build website. Python run with AI. Python Use AI"


# print(zx.replace("Python", "Java"))
# print(zx.replace("Python", "Java", 2))


# marketrans()
  # -----> mapping

# zx = str.maketrans("bacdef", "109862")

# print("efd".translate(zx))

# center

 # -----------python--------------

print("Hello world".center(26, "-"))
print("Hello world".ljust(26, "-"))
print("Hello world".rjust(26, "-"))



