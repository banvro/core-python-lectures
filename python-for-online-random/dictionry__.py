
# Data Structures:
#   1) list
#   2) tuple
#   3) set
#   4) dictionry

# dictionry:
#       1) ordered
#       2) do not allow duplicate data
#       3) mutable

# set ---> {12, 34, 5, 'hello'} 

# dicitorny -> key : value relationsip

# info = {key1 : value1, key2 : value2, ... . .}


# stu = {"name" : "naresh", 
#        "age" : 25, 
#        "number" : 87234732, 
#        "email" : "naresh@gmail.com",
#        1 : 2342334,
#        5 : "heiiiii"
#       }

# print(type(stu))

# print(stu)



# stu = {"name" : "naresh", 
#        "age" : 25, 
#        "number" : 87234732, 
#        "email" : "naresh@gmail.com",
#        1 : 2342334,
#        5 : "heiiiii"
#       }


# print(stu)

# get keys only-----------------
# print(stu.keys())


# get only values------------

# print(stu.values())



# stu = {"name" : "naresh", 
#        "age" : 25, 
#        "number" : 87234732, 
#        "email" : "naresh@gmail.com",
#        1 : 2342334,
#        5 : "heiiiii"
#       }

# print(stu, "\n")

# print(stu.items())


# for i in stu:
#     print(i)


# stu = {"name" : "naresh", 
#        "age" : 25, 
#        "number" : 87234732, 
#        "email" : "naresh@gmail.com",
#        1 : 2342334, 5 : "heiiiii"
#       }

# for i, j in stu.items():
#     print(i, j)



# dictionry:
#       1) ordered
#       2) do not allow duplicate data
#       3) mutable


# stu = {"name" : "naresh", 
#        "age" : 25, 
#        "number" : 87234732, 
#        "email" : "naresh@gmail.com"
#       }

# print(stu)

  # 1) ordered : we able to get any value by using there index number

# print(stu["email"])

# print(stu["name"])



# stu = {"name" : "naresh", 
#        "age" : 25, 
#        "number" : 87234732, 
#        "email" : "naresh@gmail.com",
#        "age" : 56,
#        "number" : 9899999999
#       }


# print(stu)

# 3) mutable --> able to moodify

# stu = {"name" : "naresh", 
#        "age" : 25, 
#        "number" : 87234732, 
#        "email" : "naresh@gmail.com",
#       }

# how to replace the value by using key

# stu["number"] = 99999999

# add new key pair replation in dictiony

# stu["address"] = "this is my office address"

# stu = {"name" : "naresh", 
#        "age" : 25, 
#        "number" : 87234732, 
#        "email" : "naresh@gmail.com",
#       }

# update() ----> way to add key pair relationship in dict

# stu.update({"hi" : "helloooo"})

# stu.update({"hi" : "helloooo", "new" : "newwwwwwww"})

# print(stu)


# how to remove realtionsip

# stu = {"name" : "naresh", 
#        "age" : 25, 
#        "number" : 87234732, 
#        "email" : "naresh@gmail.com",
#       }

# stu.pop("number")
# stu.pop("email")

# stu.clear()


# print(stu)


# list- --- []
# tuple ------()
# set -----> set()
# dict -----> {}


# problem : 

# {1 : 1, 2 : 22, 3 : 333, 4 : 4444, 5 : 55555, 6 : 66666}


# zx = {}

# for i in range(1, 7):
#   zx[i] = int(i * str(i))

# print(zx)


# 1 ----------- 60

# {
#   even : [2, 4, 6, 8.....],
#   odd : [1, 3, 5, 7, .............]
# }


x = {}
x["even"] = []
x["odd"] = []

for i in range(1, 61):
  
  if i % 2 == 0:
      x["even"].append(i)
  else:
      x["odd"].append(i)


print(x)












