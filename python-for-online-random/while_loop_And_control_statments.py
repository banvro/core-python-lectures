# Loops : 
#     for loop

# while loop

# x = "this is a car"

# for i in enumerate(x):
#     print(i)


# while loop
    # ---> ittration or repetaion
    
    
# for ---> sequence
# range()
    
    
# while ---> condation

# condation based loop


# for i in range(1, 11):
#     print(i)


# while condation:
    # block of code


# while 10 == 10:
#     print("helooooo")


# a = 1

# while a < 10:
#     print(a)
    
#     a = a + 1


# 10 ----       -4


# a = 10

# while a > -5:
#     print(a)
    
#     a = a - 1





zx = "this is a car"

# for i in zx:
#     print(i)

# a = 0

# while a < len(zx):
    
#     print(zx[a])
    
#     a += 1



# indexing

zx = "this train a car"

# print(zx[6])

# string function

# print(zx.index("r"))

# -----------------------

# control statments

# 1) break
# 2) continue
# 3) pass


# for i in range(1, 11):
#     print(i)
    
#     break

# print("heloooo")
    
    
# for i in range(1, 11):
#     if i == 5:
#         break
    
#     print(i)


# gamig

# zx = "tbda dja dask da kj q j oadn"


# for i in zx:
#     if i == "q":
#         break
#     print(i)


# Gussing game


# 2) continue  ---> skip


# for i in range(1, 10):
#     if i == 6:
#         continue
#     print(i)

# zx = "this is a car"

# for i in zx:
    
#     if i == " " or i == "i" or i == "s":
#         continue
    
#     print(i)


# pass

# for i in range(1, 11):
#     pass

# a = 10
# b = 20



# Project --> Guessing Game

# 1 -- 100

# ----> random number --> 67

# --> 90
# --> 50
# --> 60
# --> 65
# ---> 67




# while loop

# while condation:
    # code


# while True:
#     if conation:
#         break

import random


print("::::: Welcome to My Guessing Game ::::::::\n")
while True:
    choice = input("Press q for quit and s for stat game : \n")
    
    random_number = random.randint(1, 100)
    
    if choice == "q":
        print("Thank you! ")
        break
    
    elif choice == "s":
        
        print("::::: Game Start :::::::::")
        c = 1
        
        while True:
            guess = int(input(f"Enter your Guess No. {c}: "))
            
            if guess == random_number:
                print("you Won!!")
                print("Total Attempts to won match : \n", c)
                break
        
            else:
                print("Try Again!!!!!")
                c = c + 1
                
                if guess < random_number:
                    print("Think Bigger\n")
                
                else:
                    print("Think Lower.!\n")
                
    
    else:
        print("Please enter a vaild key.\n")





