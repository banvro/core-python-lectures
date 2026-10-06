





# Objects: ( data types )

#   ---> Ittrable objects
#       string, list, tuple, set, dictionry


#   ---> Non Ittrable objects
#       integer, float, boolean, complex


# ---> len(), count(), indexing, slicing, loops ,--------> ittrable objects


# "hello"

# vairble_name.count(?)


# zx = 1000202000304


# _______________________________________

# take a input from user and print how many elements user pass


# Operators

# print(10 + 50)

# 1) Airthmatical Operators
#     1) +
#     2) -
#     3) *
#     4) /
#     5) %
#     6) // ---> floor divisio
#     7) ** ---> operar


# +

# print(10 + 20)

# print(4 + 9)

# print("1" + "1")

# print(12 + "90")


# - ----> subtraction

# print(4 - 8)

# * ----> multiplication

# print(4 * 7)

# print("nice " * 100)



# / -----> output ---> float

# print(5 / 4)


# print(4 / 2)

# // ----> floor division

# print(5 // 4)


# print(4 // 2)

# % --> Modulus

# print(5 % 4)

# print(10 % 2)


# print(3 ** 4)

# print(2 ** 3)


# _____________________________________

# 2.) Compersion Operaots
#     ---> always return True | False

# 1) ==
# 2) !=
# 3) >
# 4) <
# 5) >=
# 6) <=

# print(45 > 89)


# print(10 == 10)


# print(3 >= 3)



# ________________________________

# 3) Logical Operators
  # 1) and
  # 2) or
  # 3) not




# print(12 > 12 or 1 != 1 or "nice" != "nice")



# print(not(10 == 10))


# ___________________________________________

# bitwise Operators


# bit ---> 0 | 1
#   -----> smallest unit of memoery



# 1 bit --> 0 | 1
# 8 bits ----> 1 bytes
# 1024 bytes ------> 1 kb
# 1024 kb --------> 1MB
# 1024 MB --------> 1 GB
# 1024 GB --------> 1 TB
# 1024 TB --------> 1 PT



# 1) & ---> bitwise and

# print(89 & 48)

# print(210 | 97)


# 1) &
# 2) |
# 3) ~

# -(n + 1)

# print(~89)


# __________________________________________

# condational statments:
    
# if, elif, else

# syntax

# if condation:
  # codee



# if 10 == 11:
#     print("nice car")
#     print("done")
#     print("ok")
#     print("nice")


# if 10 == 11:
#     print("they are euqal")

# else:
#     print("they are not equal")


# age = int(input("Enter your age : "))

# if age > 18:
#   print("you are eligible for vaot")

# elif age == 18:
#   print("welcome this is your first  vaot")

# elif age == 19:
#   print("this is your second voat")

# else:
#   print("you are not eligible for vaot")













# Voating system


# Calculator

 ################ My Calculator ###############

# num1 = ? 10
# num2 = ? 20

#   ******** Our Options ***********
#       1. Addation
#       2. Subtraction
#       3. Multiplication
#       4. Division
#       5. Modulus
#       6. Exponantional

# choice = ?
print("********************************************")
print("############# My Calculator ################")
print("********************************************")
print()

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

print()

print("""
  ************ Our Options **************
      1. Addation
      2. Subtraction
      3. Multiplication
      4. Division
      5. Modulus
      6. Exponantional
""")
print()

choice = input("Enter your choice : ")

if choice == "1":
    zx = num1 + num2
    print(f"The sum of {num1} and {num2} is : {zx}")

elif choice == "2":
    zx = num1 - num2
    print(f"The subtraciton of {num1} and {num2} is : {zx}")

elif choice == "3":
    zx = num1 * num2
    print(f"The multiplication of {num1} and {num2} is : {zx}")

elif choice == "4":
    zx = num1 / num2
    print(f"The dibision of {num1} and {num2} is : {zx}")

elif choice == "5":
    zx = num1 % num2
    print(f"The Modulus of {num1} and {num2} is : {zx}")

elif choice == "6":
    zx = num1 ** num2
    print(f"The Exponantional of {num1} and {num2} is : {zx}")

else:
    print("Please enter valid key")













