# Perameters & Arguments


# def x(a, b):
#     pass

# x(12, 34)


# def summ(a, b):
#     print(a + b)
    
# summ(10, 45)




# Types of arguments & perameterrs:
#     1) Postational Arguments



# def info(name, age, number):
#     print(f"user name is {name}, user age is {age} and numebr is  {number}")


# info("Naresh", 25, 8219836118)


# 2) keyword arguments


# def info(name, age, number):
#     print(f"user name is {name}, user age is {age} and numebr is  {number}")


# info(age = 25, name = "Naresh", number = 8219836118)


# 3) Default Perameters

# def summ(a = 0, b = 0, c = 0):
#     zx = a + b + c
#     print(f"The sum of {a} and {b} and {c} is : {zx}")


# summ(23)



# 4) Variable length Perameters:
#     1) *args
#         ---> Arbitrary Postational Agruments
#     2) **kwargs
#         ---> Keyword Arbitraty Postational Agruments




# def summ(*x):
#     total = 0
    
#     for i in x:
#         total = total + i # 32
    
#     print(total)


# summ(10, 20, 2, 34, 45, 34, 55, 33, 2, 1)




#  2) **kwargs
#         ---> Keyword Arbitraty Postational Agruments



def infoo(**x):
    # print(x)
    
    for a in x:
        print(a, x[a])


infoo(name = "naresh", age = 25)




# Postational Arguments
# Keyword Arguments
# Default Arguments
# Variable length arguments
#     1) *Args
#     2) **kwargs



