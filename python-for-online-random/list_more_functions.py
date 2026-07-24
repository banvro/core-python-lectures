# List
    # ---> Ordered
    # ---> Duplicate allow--
    # --> Mutable
    

# Add

# fruits = ["Apple", "Banana", "orange", "Mengo"]

# print(fruits)

# to detete
# pop()
#     ---> it removes the last element
    
# fruits = ["Apple", "Banana", "orange", "Mengo"]

# fruits.pop()
# fruits.pop()


# print(fruits)


# pop() is also working with index number


# zx = [12, 34, 45, 56, 34, 23, 12, 34, 45]

# zx.pop(3)

# print(zx)

# remove()
#     ---> deleting elements by there element

zx = [12, 34, 45, 56, 34, 23, 12, 34, 45]

# zx.remove(45)
# zx.remove(45)

# zx.clear()

# print(zx)

# print(zx.index(45))

pop() --> delete last element
pop(index_number) --> delete indexed ele
remove(element) --> remove by element
clear() ---> delete all elements
index(elen) --> get index of an element


# zx = [12, 34, 5, 5, 67, 78]

# print(zx[: : -1])

# zx.reverse()

# print(zx)


# zx = [12, 34, 5, 5, 67, 78]

# zx.sort()

# zx.reverse()

# print(zx)


# zx = "this is a car"


# # print(list(zx))

# # split()

# pq = zx.split()

# print(pq)



# zx = ["this", "is", "a", "ca"]

# print(zx)

# pq = "--".join(zx)

# print(pq)


# List Comprehension



# zx = []

# for i in range(1, 11):
#     zx.append(i)

# print(zx)


# pq = list(range(1, 21, 2))

# print(pq)


# List Comprehension
#     --> allow to genrate data in list


# [expression loop condation]


# zx = [q * 9 for q in range(1, 11)]

# print(zx)


# x = [f"2 x {i} = {2*i}" for i in range(1, 11)]

# print(x)


# q = [x + 100 for x in range(1, 50) if x % 3 == 0]

# print(q)


# q = "this is"

# pq = [u * 3 for u in q]

# print(pq)





# data = "this"


# w = [i * 6 for i in data]

# print(w)


# zx = "1000120300230003040004"

# e = [int(i) for i in zx if i != "0"]

# print(e)


# [t_value if condation else f_value for_loop]




# zx = "1000120300230003040004"

# qw = [i if i != "0" else "Hello" for i in zx]

# print(qw)


# [1, 2, 333, 4, 55555, 6, 7777777, 8, 999999999]


# zx = []

# for i in range(1, 10):
#     if i % 2 == 0:
#         print(i)
#     else:
#         print(i * str(i))
# print(zx)




# print([ 
#         i 
#         if i % 2 == 0 
#         else 
#         int(i * str(i))
#         for i in range(1, 10)
#         ])



# 1 --- 20

# odd | even

# [odd, even, odd, even, ]


# tuple

    # --> ordered
    # ---> allow duplcaite data
    # ---> imutable

# ()

zx = (12, 34, 45, 56, 67, 78, 4, 34)















