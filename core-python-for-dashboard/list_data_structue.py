# Data Structure In Python (Spacial Type of data Types) : 

  # 1) List
  # 2) Tuple
  # 3) Set
  # 4) Dicionry 

# 1) List 

#   1991 ---> Array
#       --> famous ---> because of speed.

# zx = 10
# name = "Naresh"


# [12, 45, 67, 1, 4, 5, 6, 7]

# x, y = 20, 30

# print(y)

# List:
#   --> is a collection of multiple elements in a single varibale. the data we store in list is hitrogenious.

# [] --> squere brackets

# x = [23, 100, 90, "hello", True, "Nice", 1.9]

# print(type(x))

# print(x)

# 3 main keypoints:
#     1) Ordered
#     2) Allow duplicate data
#     3) Mutable ---> (able to modify)

# 1) Ordered: we can apply indexing or slicing

# xyz = [12, 34, 55, 22, 111, 230, 89, 90]

# print(xyz[2])


# print(xyz[-3])

# print(xyz[2 : 6])


# Slicing syntax

# varibale_name[start_index : end_index  : step]


# xyz = [12, 34, 55, 22, 111, 230, 89, 90]

# [12, 55, 111, 89]

# print(xyz[ : : -1])



# 2) Allow duplicate data

# x = [12, 34, 56, 34, 12, 12, 23, 34, 12]

# print(x)



# Mutable : 
#   ---> Able to modify

# zx = [12, 34, 45, 56, 6, 7]

# how to add new elements in list?
# ---> we have 2 diifrent functions
      # 1) append(): help to add a new element at the end of a list


# zx.append("hello")
# zx.append(6500)

# # replace eleemnts
# zx[2] = "nice"

# print(zx)




# 2) insert() : help to add a new element at a prticuler location

# zx = [12, 34, 45, 56, 6, 7]

# zx.insert(2, "helloo")
# zx.insert(0, 10000)

# print(zx)





# We also able to delete elements from list.

# zx = [12, 34, 5, 67, 7, "hello", True, "Nice"]

# 1) pop(): to delete last element from list

# zx.pop()
# zx.pop()

# # ------------

# zx.pop(1)

zx = [12, 34, 5, 67, 7, "hello", True, "Nice"]


# remove() : we direclt pass element we wana delete

# zx.remove(67)

# zx = [12, 34, 5, 67, 7, "hello", True, "Nice"]

# empty the list

# zx.clear()

# print(zx)



# x = []


