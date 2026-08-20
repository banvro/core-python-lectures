# Function
    # ---> a block of code use at multiple location 

#                 |

# user define function    |  Built in function

# function decleration

# def say_something():
#     print("heloooooo")
#     print("how are you......")
#     print("Nice.....")


# # calling a function

# say_something()

# say_something()




# def greet_me():
#     print("Good morning Naresh")
#     print("How are you?\n")


# greet_me()


# greet_me()

# Perameters and argumets

# the varibles we set in () breackets we call these perameters

# def greet_me(x):
#     print("Good morning", x)
#     print("How are you??\n")


# # arguments
# greet_me("Naresh")

# greet_me("Mohan")


# table(4)


# def table(q):
#     for i in range(1, 11):  
#         print(q, "x", i, "=", q*i)


# table(12)



# def summ(a, b):
#     zx = a + b
#     print("the sum is : ", zx)


# summ(100, 120)

# summ(1, 2)

# --------------------

# eligible(1)


# def eligible(age):
#     if age > 18:
#         print("You are eligible")

#     else:
#         print("Not eligible")

# eligible(34)


# Types of peramters & arguments
#     1) Postatioal Permaters
#     2) Keyword arguments
#     3) Default peramters
#     4) varible length peramters
#         1) *args
#         2) **kwargs



# ) Postatioal Permaters
#  -------> sequence

# def info(name, age):
#     print(f"User name is {name} and user age is {age}")

# info("Naresh", 25)

# 2) Keyword arguments


def info(name, age):
    print(f"User name is {name} and user age is {age}")

info(age = 25, name= "Naresh")








