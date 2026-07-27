# Functions in python

# a block of code that we need to use again and again

# ------> Types
#     1) Built In functions
#     ---> print()
#     ---> len()
#     ---> count()
#     ---> type()
#     ---> append()
#     .
#     .
#     .
    
    # 2) User define function:
    
    
# -->


# print("hellooooo")
# print("okk")
# print("done..........")
# print(10 + 20)
# print("hellooooo")
# print("okk")
# print("done..........")
# print("Hellooo")
# print("hellooooo")
# print("okk")
# print("done..........")


# -----> Code Optimization

# DRY --> do not repete yourself



# function

# def ---> define --> function

# def function_name():
#     # block of code


# declearation of function

# def say_hello():
#     print("helloo! hw are you")
#     print("what is this")
#     print("learning python...")


# # calling a function

# say_hello()

# say_hello()

# print("heyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")

# say_hello()



# def greet():
#     print("Good morning Naresh")
#     print("Hey! how are you...")


# greet()

# greet()


# Parameters & arguments

# Parameters : are veriables set at function decleration time

# def xyz(name):
#     print("Helloo........!")


# xyz("Naresh")



# def greet_me(x):
#     print("Good Morning", x)
#     print("How are you...!!!!\n")


# # arguments
# greet_me("Naresh")

# greet_me("Kriss")



# def xyz():
#     a = 10
#     b = 20
#     c = a + b
#     print(c)


# xyz()

# xyz()



# def summm(x, y):
#     zx = x + y
#     print(zx)


# summm(10, 30)

# summm(3, 5)

# def summm(x, y):
#     zx = x + y
#     print(f"the sum of {x} and {y} is : {zx}")

# summm(1000, 6773)

# summm(2, 4)

# summm(1, 6)
     
     

# Probem: write a program, to create a function for table. 




# table(4)


# def table(e):
#     for i in range(1, 11):
#         print(f"{e} x {i} = {e*i}")


# table(61)
# print()
     
# table(78)
     
     

# Types of perameters and arguments
    # 1) Postational Perameters
    # 2) Keyword Arguments
    # 3) Default Perameters
    # 4) Veriable Length Perameters
    #     1) *args
    #     2) **kwargs
    
    
# 1) Postational Perameters

# def info(name, age, number):
#     print(f"User name is {name} and user age is {age} and phone number is {number}")
    

# info("Naresh", 25, 8219836118)
    
    
# 2) Keyword Arguments    

# def info(name, age, number):
#     print(f"User name is {name} and user age is {age} and phone number is {number}")
    

# info(age = 25, name = "Naresh", number = 8219836118)



# 3) Default Perameters
#  --> we when we don't know user pass value or not


# def xyz(x = 0, y = 0, z = 0):
#     print(f"The sum of {x}, {y} and {z} is : {x+y+z}")


# xyz(23, 34, 23)



# def info(name = "dummmy", age = 10):
#     print(f"User name is {name} and age is {age}")


# info(age = 25)




# 4) Veriable Length Perameters
    #     1) *args
    #     2) **kwargs

# --> when you don't know, how many arguments user pass.


#  1) *args --> arbitrary postational arguments


# def summ(*x):
#     print("user data : ", x)
#     zx = 0
#     for i in x:
#         zx = zx + i
    
#     print("The sum is : ", zx)


# summ(1, 4, 6)


# 2) **kwargs --> keyword arbitrary postional arguemtns


# def info(**q):
#     print("User data : ", q)
#     print(q.keys())


# info(name = "Naresh", age = 25, number = 8219836118, email = "naresh@gmail.com")






        
