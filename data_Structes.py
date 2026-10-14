
# List:
#   --> Ordered
#   --> allow duplicate data
#   --> Mutable (Able to modify)

# to create a list -----> []

# fruits = ["Apple", "Banana", "Orange", 100, 500]

# print(fruits)

#   --> Ordered
  # indexing | Slicing

# indexing :---> 


# fruits = ["Apple", "Banana", "Orange", 100, 500]

# print(fruits)
# print(fruits[2])

# indexing:
#     ---> POstive indexing
#     ---> Negitive Indexing

# fruits = ["Apple", "Banana", "Orange", 100, 500]

# print(fruits[2])
# print(fruits[-3])


# Slicing : 

# fruits = ["Apple", "Banana", 450, 89, "Orange", 100, 500]

# slicnig
# data_name[start_index : end_inedx : increment]

# print(fruits[2 : 5 : 1])

# print(fruits[-5 : -2 : 1])


# fruits = ["Apple", "Banana", 450, 89, "Orange", 100, 500]


# print(fruits[1 : 6 : 2])


# fruits = ["Apple", "Banana", 450, 89, "Orange", 100, 500]

# fruits.insert(1, 2000)

# print(fruits)


# How to delete elements from list?

# 1) pop()
# 2) remove()
# 3) clear()

# fruits = ["Apple", "Banana", 450, 89, "Orange", 100, 500]

# fruits.pop()
# fruits.pop()

# pop() : help to delete the last element from list

# pop(index_number) : help to delete a perticuler element using thir index number

# fruits.pop(2)

# print(fruits)


# xyz = [12, 34, 56, 67, 89, 100, 7]

# xyz.pop(4)

# print(xyz)



# 2) --- > remove() --> help us to delete element by their name
# xyz = [12, 34, 56, 67, 89, 100, 7]

# xyz.remove(56)

# print(xyz)

# xyz = [12, 34, 56, 67, 89, 100, 7]

# clear() ---> help to remove all the elements from list

# xyz.clear()

# print(xyz)


# "akjbdkasbdkabkdask"
# [12, 34, 45, 56, 67]
# (12, 34, 45, 56, 67)

# extends() --> help us to add multple elements in list

# zx = [12, 34, 45, 56, 67, 9, 100, 4]

# zx.append([500, 6])

# print(zx[-1][0])


# x = [12, [34, 4, "hello"], [1, 2, 100, 6], "ok", 5]

# print(x[2][-2])


# x = [12, 34, 56, 67, 8]

# y = (12, 34, 111, 111111, 11)

# print(x + y)

# x.extend(y)

# print(x)


# x = [12, 34, 56, 67, 8]

# q = x.index(67)

# print(q)


# x = [12, 34, 56, 67, 8]

# x.sort()

# x.reverse()

# print(x)

# _____________________________________

# tuple:
#     -----> Ordered
#     -----> Allow duplicate data
#     -----> Immutable

# -----> ()

# xz = (12, 34, 5, 67, 7, 45, "hello", "1.4")

# ______________________________________________

# set :
#   -----> Unorderd
#   -----> do not allow duplcaite data
#   -----> Muatble

# -----> to craete a set {}


# zx = {"helo", "Nice", 100, 3434, "Nice", 100, "ok"}

# print(zx)


#   -----> Muatble
  # 1) adding new data in set

    # 1) add()
    # 2) update()

# zx = {"helo", 100, 3434, "Nice", "ok"}

# zx.add(5000)

# qw = (45, 788)
# qw = "Nice"
# qw = [90, 3, 500, 6]

# zx.update(qw)

# print(zx)


# zx = {"helo", 100, 3434, "Nice", "ok"}



# Delete elements from set

# 1) pop()
# 2) remove()
# 3) discard()
# 4) clear()

# zx = {"helo", 100, 3434, "Nice", "ok"}

# zx.pop()

# zx.remove(3434

# zx.clear()

# print(zx)

# remove   |   discard

# zx = {"helo", 100, 3434, "Nice", "ok"}

# zx.remove(5)
# zx.discard(100)

# print(zx)



# add()
# update()
# pop()
# remove()_
# discard()
# clear()

# Mathamatical function

# union() : 

# zx = {12, 34, 45, 65, 34, 23, 23, 12}

# pq = {12, 34, 45, 1, 1, 2, 34, 2, 12}

# q = zx.union(pq)

# print(q)



# zx = {12, 34, 45, 65, 34, 23, 23, 12}

# pq = {12, 34, 45, 1, 1, 2, 34, 2, 12}

# q = zx.intersection(pq)

# print(q)

# zx = {12, 34, 45, 65, 34, 23, 23, 12}

# pq = {12, 34, 45, 1, 1, 2, 34, 2, 12}

# q = zx.difference(pq)
# 
# q = pq.difference(zx)

# print(q)



# __________________________________

#   dictionry:
#     ----> ordered
#     ----> do not allow duplicate key
#     ----> mutable

# to create a dict : {}

# emppty

# lst = []
# tpl = ()
# st = set()
# dict = {}


# ----------> {key : value, key : value, .....}

# info = {
#   "Name" : "Programography",
#   "Age" : 25,
#   "Number" : 8219836118,
#   "Email" : "programography@gmail.com"
# }

# we get any value by using their key 

# print(info["Email"])
# print(info["Name"])



# info = {
#   "Name" : "Programography",
#   "Age" : 25,
#   "Number" : 8219836118,
#   "Email" : "programography@gmail.com"
# }

# get only keys

# print(info.keys())

# values only

# print(info.values())

# info = {
#   "Name" : "Programography",
#   "Age" : 25,
#   "Number" : 8219836118,
#   "Email" : "programography@gmail.com",
#   "Age" : 20
# }

# print(info)


# info = {
#   "Name" : "Programography",
#   "Age" : 25,
#   "Number" : 8219836118,
#   "Email" : "programography@gmail.com"
# }

# to add data in dictionry

# info["Address"] = "this is my address"

# replacing element with this appreoch

# info["Age"] = 500

# print(info)




# info = {
#   "Name" : "Programography",
#   "Age" : 25,
#   "Number" : 8219836118,
#   "Email" : "programography@gmail.com"
# }

# update()

# qw = {
#   "address" : "this is my address",
#   "Pin_Code" : 120883
# }

# info.update(qw)

# print(info)


# delete data from dicitonry


# info = {
#   "Name" : "Programography",
#   "Age" : 25,
#   "Number" : 8219836118,
#   "Email" : "programography@gmail.com"
# }

# popitem() : to delete last key pair relationsip

# info.popitem()

# delete a prticuler key pair relationhip
# pop(key)
# info.pop("Name")

# print(info)


# info = {
#   "Name" : "Programography",
#   "Age" : 25,
#   "Number" : 8219836118,
#   "Email" : "programography@gmail.com"
# }


# backup_info = info.copy()

# info.clear()

# print(backup_info)

# print(info)


info = {
  "Name" : "Programography",
  "Age" : 25,
  "Number" : 8219836118,
  "Email" : "programography@gmail.com"
}

# print(info.items())

for i, j in info.items():
    print(i, "----->", j)



