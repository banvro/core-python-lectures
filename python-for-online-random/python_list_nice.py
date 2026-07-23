
# Data Structures:
#     1) List
#     2) tuple
#     3) set
#     4) dictionry


# 1) List:

# x = 10

# a, b, c = 10, 20, 30


# print(c)


# list:
#     --> is a collection of hitrogenious type of data in a single variable.


# Homogenious
#     --> same type of data

# Hitrogeuius
#     ---> diffrent type of data


# to craete a list ---> []

 
# fruits = ["Apple", "Banana", "orange", "Grapes"]

# print(fruits)


# ---> Properties:
#         1) Ordered
#         2) allow duplicate Data
#         3) Mutable (Modfition)

# 1) Ordered
    # --> indexing, slicing

# indexing --> to get a single element by using there index number



# fruits = ["Apple", "Banana", "orange", "Grapes"]

# print(fruits)

# print(fruits[0])

# print(fruits[-1])


# indexing:--->
    # Postive or Negitive


# fruits = ["Apple", "Banana", "orange", "Grapes"]


# # Slicing---> 

# print(fruits)

# veriable_name[start : end : increment]

# xy = [12, 4, 5, 6, 34, 34, 23, 'hlo', 45, 23, 23, 11]

# print(xy[7])
# print(xy[-5])

# print(xy[4 : ])

# print(xy[4 : 8])

# default"
# start ---> 0
# end ---> n - 1
# increment ---> 1 




# xy = [12, 4, 5, 6, 34, 34, 23, 'hlo', 45, 23, 23, 11]


# print(xy[ : : -1])

# print(xy[ : 5])

# print(xy[-4 : -1 ])


# string
# list
# tuple
# numpy
# pandas




# zx = "this is a car and a good car"

# print(zx[1])

# print(zx[5 : -4])

# print(zx[-18 : -4])


# regex




# --> Ordered
# --> allow duplicate
# --> mutable

# zx = [12, 23, 4, 23, 12, 12, 12]

# print(zx)



# frts = ["Apple", "Banana", "Mango"]

# print(frts)

# print(len(frts))

# print(frts.count("Banana"))



# frts = ["Apple", "Banana", "Mango"]

# print(frts)


# x = "this is"

# print(x[-1 : -5 : ])

# print(x[-5 : ])




# frts = ["Apple", "Banana", "Mango"]

# print(frts)


# Adding new data in list

# 1) append()
#     --> always add element at end end of list

# frts = ["Apple", "Banana", "Mango"]

# frts.append("Orange")
# frts.append("Grapes")
# frts.append(1000)

# print(frts)

# print(frts[-1])


# 1 ----- 20

# [1, 2, 3, 4, 5, 6...... 20]


# zx = []


# 1 ---- 50

# odd = []
# even = []


# 1 ----- 20

# [1, 2, 3, 4, 5, 6...... 20]



# zx = []

# for i in range(1, 21):
#     zx.append(i)

# print(zx)

# evn = []
# od = []

# for i in range(1, 51):
#     if i % 2 == 0:
#         evn.append(i)
#     else:
#         od.append(i)

# print(evn)
# print(od)


# x = []

# for i in range(1, 11):
#     x.append(f"2 x {i} = {2*i}")
#     # print("2 x", i, "=", 2*i)

# print(x)


# adding new ement

# appned()

# fruits = ["Apple", "Banana", "Orange"]

# fruits.append("Mango")

# extend()
    # --> allow to add multiple elements in the last at last the data should be ittrable

# fruits = ["Apple", "Banana", "Orange"]

# new = [100, "Mango", "Grapes", 20, 50]


# fruits.extend(new)

# print(fruits)

# fruits = ["Apple", "Banana", "Orange"]

# new = "hi"

# fruits.extend(new)

# print(fruits)


# zx = [12, 34]

# pq = [100, 344, 56]

# print(zx + pq)


# append()
# extend()
# +

# x = [12, 23, 45, 56]

# y = [100, 200]

# # x.extend(y)

# q = x + y

# print(q)


# insert()
#     ---> when we need to add a new element at a prticuler location

# x = [12, 23, 45, 56]

# x.insert(2, 1000)

# print(x)

# x = [12, 23, 45, 56]

# x[1] = 1000

# print(x)




# zx = [11, 12, 12, 12, 12, 23, 34, 45, 12]

# # 12 ---> hello
# nw = []

# x = 0

# while x < len(zx):
#     if zx[x] == 12:
#         nw.append("Hello")
#     else:
#         nw.append(zx[x])
    
#     x += 1

# print(nw)


# zx = [11, 12, 12, 12, 12, 23, 34, 45, 12]

# for i in zx:
#     if i == 12:
#         print("hello")
#     else:
#         print(i)


# x = "this"
# thissiht


# car
#     carrac

# zx = "this"

# print(zx + zx[::-1])


# x = [12, 23, 34, 45, 56, 67, 7, 89, 23]


# devide in  lists

# pq = len(x) // 2

# print(x[ : pq])

# print(x[pq : ])




# x = [12, 23, 34, 45, 56, 67, 7, 89, 23]


# print(x[-1 : 8 : 2])


[1, 22, 3, 4444, 5, 666666, 7, 8888888]









