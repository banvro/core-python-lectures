

# Perameters & arguments

# function deleleration

# def info(name, age):
#     print(f"User name is {name} and user age is {age}.")


# calling a function
# info("Naresh", 25)



# def summ(a, b, c, d, e):
#     zx = a + b + c + d + e
#     print(zx)


# summ(2, 3, 4, 2, 3)



# Types of Perameters & arguments:
#     1) Posatational Peramters
#     2) Keyword arguments
#     3) Default Perameters
#     4) Veriable length Perameters
#           1) *args
#           2) **kwargs




# 1) Posatational Peramters
  # -----> where sequence metter

# def info(name, age, email):
#     print(f"""
#           User name is {name} and 
#           age is {age} and 
#           email address is {email}""")


# info("Mohan", 25, "mohan@gmail.com")




# 2) Keyword arguments

# def info(name, age, email):
#     print(f"""
#           User name is {name} and 
#           age is {age} and 
#           email address is {email}""")

# info(age = 23, name = "Ram", email = "ram@gmail.com")


# 3) Default Perameters

#   --> when we don't know user pass value for a permater or not


# def info(name = "dummy", age = 18, email = "dummy@gmail.com"):
#     print(f"""
#           User name is {name} and 
#           age is {age} and 
#           email address is {email}""")

# info(name = "mohan", email = "mohan@gmail.com")


# 4) Veriable length Perameters
#           # 1) *args
#           # 2) **kwargs

#   ---> when we don't know how many arguments user pass at function calling time

# 1) *args -> Arbitrary Posatational Arguments


# def summ(*x):
#     print("User input is : ", x)
#     # for i in x:
#     #     print(i)
#     print(sum(x))


# summ(12, 23, 34, 2, 1)


# 2) **kwargs : keyword arbutrary postational arguments


# def info(**kwargs):
#     print("User input is : ", kwargs)

# info(name = "Naresh", age = 25)



# write a program to create a function that takes n inputs from user and print the sum of all inputs

Shopping bill: Create a function that accepts a price, quantity, and optional discount percentage.

  # 1. Phone -- 18000 -- 5%
  # 2. Laptop -- 34000 - 0%
  # 3. Shirt --- 300 --- 18%

  1. Phone -- 18000 -- 5%

shoping("Phone", 18000)


shoping("Laptop", 34000, 8)

shoping("Shirt", 300, 18)






