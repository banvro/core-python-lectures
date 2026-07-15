# Loops

# control statements

# veriables
# data types
# type casting
# concatenation
# print()
# input()
# len()
# count()
# operators
# condational statments
# if, elif, else
# loops
# for & while loop
# contorl statments
# break, continue , pass



# Data Structure:
#     --> Spacial Data Types in python
    
# # Array | Stack | Queue

#     List
#     tuple
#     set
#     dictionry


# List

# a = 10

# age = 25

# name = "naresh"

# addres = "My location is chandigarh"


# Data Structure : orgnize the data in proper way

# -->

# to  create a list :::   []

# zx = []  # this is a empty list

# print(type(zx))


# qw = [100, 700, 45, 12, 24 ,100, "naresh"]

# heterogeneous:
#     diffrent type of data

# homogeneous:
#     same type of data --> Array



# List:
#     --- ordereed
#     --- allow duplicate data
#     --- mutable
    
        # -6   -5    -4   -3  -2  -1   
# lst = [100, "hello", 500, 343, 23, 341]
    # 0     1          2    3   4    5
       
# print(lst)
    
# print(lst[4])
    
# slicing:
    
# veriable_name[start : end : increment]
    
# print(lst[1 : 4 : 2])


# x = [12, 34, 23, 34, 45, 4, 3, 2, 5, 6, 7]

# print(x[4 : ])


# print(x[2 : 7])

# print(x[: 5])

# default:
#     start ---> 0
#     end ---> n - 1
#     increment  ---> 1


# x = [12, 34, 23, 34, 45, 4, 3, 2, 5, 6, 7]

# print(x[-5 : ])

# print(x[ : : -1])




# List:
#     --- ordereed
#     --- allow duplicate data
#     --- mutable


# zx = [12, 34, 5, 23, 111, 23, 233]

# print(zx)

# mutable ---> allow modification

# zx = [12, 34, 5, 23, 111, 23, 233]

# 1) adding new elements

# append()
#     --> help to add element at list n the list.

# zx.append(1000)

# zx.append("helloooo")

# print(zx)


# --> insert()
#     --> when we need to add new element at a prticuler location

# zx = [12, 34, 5, 23, 111, 23, 233]

# syntax
# list_name.insert(index_number, elemnt)

# zx.insert(2, 100000)

# zx.insert(0, "helloo")

# print(zx)


# ========================

# deleting the elemtns from list

# 1) pop()
# 2) remove()
# 3) clear()

# pop()
#     --> when we need to delete last element from list


# fruits = ["Apple", "Banana", "chery", "Mango"]

# fruits.pop()
# fruits.pop()

# print(fruits)


#  2) remove()
    # --> to delete a spacific element from the list

# fruits = ["Apple", "Banana", "chery", "Mango"]

# fruits.remove("Apple")

# x = fruits.index("chery")

# print(x)

# fruits.pop(1)

# print(fruits)




# fruits = ["Apple", "Banana", "chery", "Mango"]

# clear()
#     -- it delete all elements
# fruits.clear()

# print(fruits)

# fruits = ["Apple", "Banana", "chery", "Mango"]

# fruits[2] = "Grapes"

# print(fruits)



# ----> new elements
# append()
# insert()
# extend()

# fruits = ["Apple", "Banana", "chery", "Mango"]

# zx = ["pataato", "tmato", "orange"]

# zx = "this is a car"

# fruits.append()

# fruits.extend(zx)

# print(fruits)



# fruits = ["Apple", "Banana", "chery", "Mango"]

# zx = "this is a car"


# for i in zx:
#     if i == " ":
#         continue
    
#     fruits.append(i)

# print(fruits)



# append()
# insert()
# extend() --> ittrable object elements --

# # delete
# pop()
# remove()
# clear()


# fruits = ["Mango", "Apple", "Chery", "Banana"]

# fruits = [12, 34, 45, 23, 34, 51, 1, 2, 1, 34, 45]

# fruits.sort()

# fruits.reverse()
# print(fruits[: : -1])

# print(fruits)

# fruits = [12, 34, 45, 23, 34, 51, 1, 2, 1, 34, 45]

# print(len(fruits))

# print(max(fruits))
# print(min(fruits))


# # ASCII

# x = ["abc", "Hllo", "xyz"]

# print(min(x))







