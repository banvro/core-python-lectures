# Data Structure in Python
    # list:
    #   ----> orderd
    #   ----> allow duplicate data
    #   ----> mutable

# zx = [12, 5, 56, 7, 33, "helloo"]

# indexing, slicing len(), count(), for loop

# ____________________________

# 2) tuple
#     ---> ordered
#     ---> allow duplicate data
#     ---> imutable



# list ---> []

# tuple ---> ()

# zx = (12, 45, "helloo", 10.3, 4, 56, 65)


# print(type(zx))

# print(zx[2])

# ______________________________________
#     list:
#       ----> orderd
#       ----> allow duplicate data
#       ----> mutable

# 2) tuple
#     ---> ordered
#     ---> allow duplicate data
#     ---> imutable

# set :
#     1) unorderd
#     2) do no allow duplicate data
#     3) mutable

# ----> {}

# zx = {12, 34, 5, 3, 3, 12, 12, 23, 12, 5, 2}


# 1) new eleemnt add krne hain
# 1) add() : to add new element in set

# zx = {19, 34, 45, 67, 788}

# zx.add(1000)

# update()
 # --> when we need to add multiple elements at once

# ---> ittable

# zx = {19, 34, 45, 67, 788}

# zx.update([12, 4, 1, 2, 3])
# zx.update((12, 34, 6, "hello", "noice"))

# zx.update("helloooo")


# print(zx)


# deleting an elements

# zx = {19, 34, 45, 67, 788}

# pop() --> set delete any random element

# zx.pop()

# zx.remove(19)

# zx.clear()

# print(zx)


# zx = {19, 34, 45, 67, 788}

# zx.remove(100)

# remove()  |  discard()

# zx.discard(13)

# print(zx)


# how to create emplty


# zx = []

# pq = ()

# x = set()



# zx = (12, )

# print(type(zx))


# problem : genrate this outut

# [1, 2, 333, 4, 55555, 6, 7777777, 8, 999999999]

# zx = []

# for i in range(1, 10):
#     if i % 2 == 0:
#         zx.append(i)
#     else:
#       zx.append(int(i * str(i)))

# print(zx)

# print(9 * "9")


[9, 88, 777, 6666, 55555, 444444, 3333333, 222222222, 1111111111]















