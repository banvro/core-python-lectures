
# Lambda function

# syntax:

# lambda peramters : expresssion

# power() 

# def power(a, b):
#     zx = a ** b
#     print(zx)

# power(4, 5)


# lambda peramters : expresssion

# p = lambda a, b : print(a ** b)

# p(2, 4)


# map()
#   ---> is an built in funtion. if we wanaa use map() fuctionaly so we need to use lambda function

# fuctionaly : when we have data in an ittrable object, modify each and every element then we map()


# zx = "nice car"

# for i in zx:
#     print(i * 3)

# map() ----> syntax


# map(lambda_function, data)

# x = [2, 4, 5, 6, 2, 3, 4, 6, 1, 3, 4]

# w = map(lambda q : q ** 2, x)

# print(list(w))


# x = "this is a car"

# map()

# filter()
#   -----> functionaly : filtring the data

# filter(lambda_function , data)


# zx = "this is a car and this is a good car nice car"

# w = filter(lambda x : x != " ", zx)

# print(list(w))


# zx = [12, 35, 5, 6, 7, 8, 9, 0, 5, 3, 2, 2, 1, 3, 4, 5, 6, 3, 6, 7]

# print(list(filter(lambda q : q % 5 == 0, zx)))

# reduse()
#   : 

# from functools import reduce

# data = [1, 2, 3, 4, 1, 1, 2, 3, 4]

# print(reduce(lambda q , w : q + w, data))

# #6

# print(sum([1, 2, 3, 4, 1, 1, 2, 3, 4]))


# [2, 4, 5, 7, 8, 9]


# Genrators

# def xyz():
#     return [1, 4, 5, 7, 8, 9, 23]


# print(xyz())


# 70GB


# chunks


# def my_data():
#     for i in range(100000, 30000000, 1000):
#         yield i

# q = my_data()

# print(next(q))
# print(next(q))
# print(next(q))



# def xyzz():
#     for i in range(1, 21):
#         yield i

# q = xyzz()

# print(next(q))
# print(next(q))




zx = (q for q in range(1, 20))

print(next(zx))
print(next(zx))
print(next(zx))

for i in range(3):
    print(next(zx))




History
Varibales
data types
comments
core functions
type casting
operators
condational statments
loops - for, while, while True
control statments
data structure
list
tuple
set
dictionry
comprehension
file handling
exception handeling
regex
function
peramters & arguments
Types peramters & arguments
partial function
dacorator
lambda
map(), filter(), reduce()
genrator
multithreading

________________________

-> OOP's
  -> Streamlit
        ---> Projects


____________
Data Science
Machine leanng
Deep leaning














  





