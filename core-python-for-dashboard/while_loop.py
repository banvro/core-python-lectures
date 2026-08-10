Notes : https://miro.com/app/board/uXjVHzG2xNQ=/?share_link_id=159893013863


# while 10 == 10:
#     print("hellooo.....!")

# for i in range(1, 11):
#     print(i)

# x = 1

# while x < 10:
#     print(x)
    
#     x = x + 1



# for i in range(1, 11):
#     print("2 x", i, "=", 2*i)


# x = 1

# while x < 11:
#     print("2 x", x, "=", 2*x)
    
#     x = x + 1



# x = 10

# while x > 0:
#     print(x)
    
#     x = x - 1




import random

num = random.randint(10, 90) #10

guess = 1

A = 0

while guess != num:
    if guess > num:
        print("Think Lower!")
    else:
        print("Think bigger..!")
        
    guess = int(input("Enter Guess : "))
    
    A = A + 1

print("Totoal Attempts : ", A)

    




