# Dictionry:
#     ---> 
#     ---> Ordered
#     ---> do not allow duplicate data
#     ---> mutable

# {}

# {key : value, key : value, key : value}

# info = {
#     "name" : "Naresh", 
#     "age" : 25, 
#     "phone" : 8219836118,
#     "address" : {
#         "street" : 123,
#         "State" : "Punjab",
#         "Country" : "India"
#     }
# }


# print(info["address"]["Country"])


# info = {
#     "name" : "Naresh", 
#     "age" : 25, 
#     "phone" : 8219836118,
#     "address" : "this is adddress",
#     "age" : 34
# }

# print(info)

#  ---> mutable

# info = {
#     "name" : "Naresh", 
#     "age" : 25, 
#     "phone" : 8219836118,
#     "address" : "this is adddress",
# }

# info["email"] = "naresh@gmail.com"

# update()

# qw = {"email" : "myemail@gmail.com", "marks" : 89}


# info.update(qw)

# print(info)


# info = {
#     "name" : "Naresh", 
#     "age" : 25, 
#     "phone" : 8219836118,
#     "address" : "this is adddress",
# }

# info.pop("phone")
# info.popitem()

# info["name"] = "Kriss"


# print(info)

# info = {
#     "name" : "Naresh", 
#     "age" : 25, 
#     "phone" : 8219836118,
#     "address" : "this is adddress",
# }


# print(info.keys())

# print(info.values())

# print(info.items())


# info = {
#     "name" : "Naresh", 
#     "age" : 25, 
#     "phone" : 8219836118,
#     "address" : "this is adddress",
# }

# for k, v in info.items():
#     print(k,"------>", v)



# zx = {}

# # {1 : 1, 2 : 4, 3 : 9, 4 : 16, 5  :25}

# for i in range(1, 6):
#     zx[i] = i ** 2

# print(zx)



x = {}

# {1 : 1, 2 : 22, 3 : 3, 4 : 4444, 5 : 5, 6 : 666666,  : 7, 8 : 8888888, 9 : 9}


for i in range(1, 10):
    if i % 2 == 0:
        x[i] = int(i * str(i))
    else:
        x[i] = i

print(x)






