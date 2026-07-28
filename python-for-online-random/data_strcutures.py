# Data Structures:
    # List
    # tuple
    # set
    # ---> Dictionry

# ---->
    # 1) Ordered
    # 2) Do not allow duplicate data
    # 3) Mutable

# JSON ----> javascript object notation

# --> data 


# DIctionry ----> JSON




# {} ---> data store in {}

# {key : value, key : value,  ....... }


# info = {"name" : "Naresh", "age" : 25, "number" : 8219836118}

# print(info)

# print(type(info))


# info = {
#     "name" : "Naresh", 
#     "age" : 25, 
#     "number" : 8219836118,
#     101 : "helloo"
# }


# 1) Ordered
    # key ---> value

# print(info["age"])


# info = {
#     "name" : "Naresh",
#     "age" : 25,
#     "number" : 8219836118,
#     "email" : "naresh@gmail.com"
# }


# print(info)

# print(type(info))


# 1) Ordered

# info = {
#     "name" : "Naresh",
#     "age" : 25,
#     "number" : 8219836118,
#     "email" : "naresh@gmail.com"
# }

# print(info["name"])


# info = {
#     "name" : "Naresh",
#     "age" : 25,
#     "number" : 8219836118,
#     "email" : "naresh@gmail.com"
# }

# print(info)

# print(info.keys())

# print(info.values())

# print(info.items())


# info = {
#     "name" : "Naresh",
#     "age" : 25,
#     "number" : 8219836118,
#     "email" : "naresh@gmail.com"
# }

# for x, y in info.items():
#     print(y)




# 2) Do not allow duplicate keys

# info = {
#     "name" : "Naresh",
#     "age" : 25,
#     "number" : 8219836118,
#     "email" : "naresh@gmail.com",
# }


# print(info)




# Mutable


# info = {
#     "name" : "Naresh",
#     "age" : 25,
#     "number" : 8219836118,
#     "email" : "naresh@gmail.com",
# }

# syntax
# info["address"] = "this is my addess"

# info["age"] = 100

# update()


# print(info)


# info = {
#     "name" : "Naresh",
#     "age" : 25,
#     "number" : 8219836118,
#     "email" : "naresh@gmail.com",
# }

# new_x = {
#     "name" : "Mohan",
#     "address" : "new adress"
# }

# info.update(new_x)

# print(info)


#
# Delete Elements



# info = {
#     "name" : "Naresh",
#     "age" : 25,
#     "number" : 8219836118,
#     "email" : "naresh@gmail.com",
# }


# info.popitem() # delete last key pair
# info.popitem()

# info.pop("number")

# info.clear()

# print(info)



# Problem:

# zx = [1, 2, 3, 1, 3, 4, 5, 4, 2, 4, 5, 3, 2, 3, 4, 5, 6, 7, 4, 2, 4, 5, 7, 2, 1, 1, 1, 1]

# zxx = {}

# for i in zx:
#     zxx[i] = zx.count(i)

# print(zxx)

students = {
    101 : {
        "Name" : "Kriss",
        "age" : 24,
        "email" : "kriss@gmail.com",
        "numbers" : [82190823, 982364834]
    },
    102 : {
        "Name" : "moris",
        "age" : 20,
        "email" : "moris@gmail.com",
        "numbers" : [9828364983, 29346344]
    },
    103 : {
        "Name" : "hello",
        "age" : 21,
        "email" : "hello@gmail.com",
        "numbers" : [99123333, 11111111]
    }
}

# print(students[102]["email"])

# print(students[103]["numbers"][1])





# Problem: 
    
    # 1 --- 5
# table = {}

# {
#     1 : ["1 x 1 = 1", "1 x 2 = 1......"],
#     2 : ["2 x 1 = 2. 2 x 2 = 4....."]
#     3 : 
#     4 : 
#     5 : 
# }


table = {}

for i in range(1, 6):
    table[i] = [f"{i} x {j} = {i*j}" for j in range(1, 11)]

print(table)















