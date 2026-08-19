

# Data Structures:
#     list
#     tuple
#     set
#     dictionry


# Comprehension
#     : ---->  genrate data in single line

# syntax
# [expression   loop    condation ]


# genrate data from 1 to 10 in list

# zx = []

# for i in range(1, 11):
#     zx.append(i)

# print(zx)

# [expression   loop    condation ]

# zx = [i * 2 for i in  range(1, 11)]

# print(zx)



# genrate data from  1 --  50 
# or store only the elements divided by 2


# [expression loop condation]

# zx = [i for i in range(1, 51) if i % 2 == 0]

# print(zx)


# [1, 22, 333, 4444, 55555, 666666, 7777777]

# print(3 * "helooo")

# zx = [int(i * str(i)) for i in range(1, 8)] 

# print(zx)



# [9, 88, 777, 6666, 55555, 444444, 3333333]


# zx = [(10 - i) * str(i) for i in range(1, 8)]

# print(zx)





# zx = [int(i * str(10-i)) for i in range(1, 8)]

# print(zx)


# zx = 10200023002030000203000034000304000000

# lst = []

# new_zx = str(zx)

# for i in new_zx:
#     if i != "0":
#         lst.append(int(i))
    
# print(lst)


# zx = 10200023002030000203000034000304000000


# lst = [int(i) for i in str(zx) if i != "0"]

# print(lst)

# ----------------------------------------------


# list comprehension
# set comprehension
# dict comprehension

# zx = {q for q in range(1, 8)}

# print(zx)


# {1 : 1, 2 : 4, 3 : 9, 4 : 16}

# zx = {i : i ** 2 for i in range(1, 7)}


# print(zx)




['2 x 1 = 2', '2 x 2 = 4', '2 x 3 = 6', '2 x 4 = 8', ........., '2 x 10 = 20']











