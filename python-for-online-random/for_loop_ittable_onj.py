

# For loop
#     1 ----- 50
#         3 ----> fizz
#         5 ----> buzz
#         3 & 5 ----> fizzbuzz

# 1
# 2
# fizz
# 4
# buzz
# fizz..
# ..

# .
# 15


# for i in range(1, 51, 1):
    
#     if i % 3 == 0 and i % 5 == 0:
#         print("fizzbuzz")
    
#     elif i % 5 == 0:
#         print("buzzz")
    
#     elif i % 3 == 0:
#         print("fizz")
    
#     else:
#         print(i)


# -----------------------------------

# for loop with ittrable objects
#     : string, list, tple, set, dicitory


# syntax:

# for veriable_name in ittrable_data:
    # block of code

# zx = "this is a car"

# for e in zx:
#     print(e)
#     print("niceeeeeeeeeeeeeeee")
#     print(e, e)
#     print("________________________")



# zx = 123432122

# x = str(zx)

# for i in x:
#     print(i)


# print("9" * 9)

# 1
# 2 2
# 3 3 3 
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6
# 7 7 7 7 7 7 7
# 8 8 8 8 8 8 8 8
# 9 9 9 9 9 9 9 9 9



# for i in range(1, 10, 1):
#     print(i * f"{str(i)} ")


# range(start, end, increment)

# default values
    # start ----> 0
    # end -----> n - 1
    # increment ---> 1

# for i in range(7, 20, 2):
#     print(i)

# for i in range(8, 3, -1):
#     print(i)

# --------------------------------------

# Star Patterns


# for loop ---- nested for loop


# for i in range(1, 4):
#     print(i)
#     for i in range(1, 10):
#         print("heloooooooo")


# * * * * * *
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 


# for i in range(6, 0, -1):
#     print(i * "* ")




# @ 
# @ @
# @ @ @
# @ @ @ @
# @ @ @ @ @
# @ @ @ @ @ @
# @ @ @ @ @ @ @
# @ @ @ @ @ @ @ @



# @ * * * * * * *
# @ @ * * * * * * 
# @ @ @ * * * * *
# @ @ @ @ * * * * 
# @ @ @ @ @ * * * 
# @ @ @ @ @ @ * * 
# @ @ @ @ @ @ @ *
# @ @ @ @ @ @ @ @

for i in range(1, 8):
    print(i * "@ " + (8 - i) * "* ")

