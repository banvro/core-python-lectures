
# Data structure:
#     List
#         --> ordered
#         --> allow duplicate data
#         --> mutable
    
#     tuple
#         --

# zx = 10

# list ---> []
# ()



# tpl = (12, 45, 6, 7, 89, 45, 23, 12, 23)


# print(tpl)

# print(type(tpl))

#     --> ordered
#     --> allow duplicate data
#     --> imutable


# tpl = (12, 45, 6, 90, 7, 89, 45, 23, 12, 23)

# index number --> indexing

# print(tpl[4])

# print(tpl[3])


# tpl = (12, 45, 6, 90, 7, 89, 45, 23, 12, 23)

# zx = tpl[2 : 7]

# zx = tpl[7 : ]

# print(tpl[-3 : ])

# print(zx)

# list | tuple | string | numpy | pandas


# tpl = (12, 45, 6, 90, 7, 89, 45, 23, 12, 23)

# syntax

# varibale_name[start : end : increment]

# print(tpl[ :  : -1])


# zx = "this is a car"

# print(zx[2 : 7])



# -----------------------------

# zx = (12, 34, 45, 12, 12, 12, 23, 4)

# print(zx)


#  --> imutable
#     ----> no modifiction


# ---------------------------------------------


# set
#     -->
#     {}
#     ---> unordered
#     ---> do not allow duplcate data
#     --> mutable


# zx = {12, 34, 45, 23, 12, 12, 23, 23, 12, 12}

# print(zx)




# zx = {12, 34, 56, 78, 89}

# mutable ---> modify

# adding new data

# -----> add

# zx.add(1000)

# zx.add(45)



# print(zx)


# zx = {12, 34, 56, 78, 89}

# pq = "hello"

# zx.update(pq)

# print(zx)


# zx = {12, 34, 56, 78, 89}

# zx.clear()

# print(zx)


# ------------------

# zx = {12, 34, 56, 78, 89}

# delete ---> remove()

# zx.remove(89)
# zx.remove(12)

# zx.remove(100) | discard
# zx.discard(100)

# remove()   |   discard()

# print(zx)



# zx = {2, 3, 5, 1, 8, 4}


# 4
# 9
# 25
# 1
# 64
# 16

# pq = {12, 100, 23, 111, 566, 34, 23, 1}

# -------------------->
# 100
# 111
# 566

# for i in pq:
#     if len(str(i)) == 3:
#         print(i)


# pq = {120, 23, 450, 67, 7, 77, 100, 1, 2, 4}

# 120
# 450
# 7
# 100
# 1
# 2
# 3


# pq = {120, 23, 450, 67, 7, 77, 100, 1, 2, 4}

# for i in pq:
#     if len(str(i)) == 3 or len(str(i)) == 1:
#         print(i)
    

# pq = [1, 55, 66, 4, 23, 6, 8999, 90, 34]

# --->

# [1, 4, 6]


# for i in pq:
#     if len(str(i)) != 1:
#         pq.remove(i)

# print(pq)

pq = [1, 55, 66, 4, 23, 6, 8999, 90, 34]

x = 0

while x < len(pq):
    if len(str(pq[x])) != 1:
        pq.remove(pq[x])
        continue

    x = x + 1


print(pq)








