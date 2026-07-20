# List
#     []
#     1) ordered
#     2) allow duplicate data
#     3) mutable  
    
# tuple()
#     ()
#     1) ordered
#     2) allow duplidate data
#     3) imutable


# zx = [12, 34, 45, 56, 67, 78]

# print(zx)

# x = (12, 444, 323, 455, 2)

# print(x)



# 3) set:
#     {}
#     1) unordered
#     2) do not allow duplciate elements
#     3) mutable
    
    
# xyz = {100, 200, "hello", 100, 20, 100, 20}  
# print(xyz)
    
    
    
# add()

# y = {12, 34, 45, 56, 67, 233}

# y.add(1000)
# y.add(2)

# print(y)
    
    
    
# 1) pop()

# y = {12, 34, 45, 56, 67, 233}

# y.pop() --> delete any random element

# y.remove(56) --> delete a prticuler ement

# y.clear()

# print(y)


# []
# ()
# set()



# y = {12, 34, 45, 56, 67, 233}

# y.remove(100)

# y.discard(50)

# print(y)



# x = {12, 34, 5, 23, 11, 233}

# y = {1, 12, 11, 56, 22}


# q = x.difference(y)

# q = x.intersection(y)




# print(q)


# x = {12, 34, 5, 23, 11, 233}

# y = {12, 5, 11}


# z = y.issuperset(x)

# z = y.issubset(x)

# print(z)


# x = {12, 34, 5, 23, 11, 233}

# y = {1, 4, 7, 8, 12, 11, 12, 11}

# q = x.union(y)

# print(q)


# x.update(y)

# print(x)

# ----------------------------------------

# dictionry ----> json

# { key : value, key : value}
    # 1) ordered
    # 2) do not allow duplicate keys
    # 3) mutable


# info = {"name" : "naresh", 
#         "age" : 25,
#         "number" : 8219836118}

# print(info["name"])

# info = {"name" : "naresh", 
#         "age" : 25,
#         "number" : 8219836118,
#         "age" : 10
# }
        
# print(info)



# info = {"name" : "naresh", 
#         "age" : 25,
#         "number" : 8219836118,
#         "adress" : "this is my address"
# }
        
# print(info.keys())

# print()

# print(info.values())

# print()

# print(info.items())


# info = {"name" : "naresh", 
#         "age" : 25,
#         "number" : 8219836118,
#         "adress" : "this is my address"
# }

# print(info.items())
# for x in info:
#     print(x, " : ", info[x])


# for x, y in info.items():
#     print(x, y)


# info = {"name" : "naresh", 
#         "age" : 25,
#         "number" : 8219836118,
#         "adress" : "this is my address"
# }


# adding
# info["course"] = "Data Science"
# info[1] = 1000
# info["age"] = 50


# print(info)


# info = {"name" : "naresh", 
#         "age" : 25,
#         "number" : 8219836118,
#         "adress" : "this is my address"
# }

# x = {"course" : "data scicne", "x" : "helloo"}


# info.update(x)

# print(info)

# info = {"name" : "naresh", 
#         "age" : 25,
#         "number" : 8219836118,
#         "adress" : "this is my address"
# }

# info.pop("age")
# info.pop("adress")

# info.popitem()

# info.clear()


# print(info)


# [] ---> empty list
# () ---> empty tuple
# set() ---> empty set
# {} ----> empty ditiory


# x = (10, )

# print(x, type(x))



# students


# stu_data = {
#     101 : {"Name" : "Naresh",
#         "age" : 25,
#         "number" : [9812893981, 98263433]
#     },
#     102 : {"Name" : "kriss",
#         "age" : 20,
#         "number" : [98236489, 111111111]
#         },
#     103 : {"Name" : "Mohan",
#         "age" : 12,
#         "number" : [9283824, 239864384]
#     }
# }

# print(stu_data[102]["number"][1])

# print(stu_data[101]["age"])



# stu_data = {
#     101 : {"Name" : "Naresh",
#         "age" : 25,
#         "number" : [9812893981, 98263433]
#     },
#     102 : {"Name" : "kriss",
#         "age" : 20,
#         "number" : [98236489, 111111111]
#         },
#     103 : {"Name" : "Mohan",
#         "age" : 12,
#         "number" : [9283824, 239864384]
#     }
# }

# for x, y in stu_data.items():
#     # print(y)
#     # for p, q in y.items():
#     #     print(q)
    
#     print(y["Name"], y["number"][0])






# zx = [12, (102, 1, 1, 23), 100, 45, {10, 34, 45, 56}, 1000]


# # print(zx[1][-1])

# # print(zx[4])

# for i in zx[4]:
#     print(i)




# x = [12, 34, 45, 67, 34, 56, 67, 45, 45, 12]


# q = set(x)

# w = list(q)

# print(w)

pq = []

x = [12, 34, 45, 67, 34, 56, 67, 45, 45, 12]

for i in x:
    
    if i not in pq:
        pq.append(i)


print(pq)


