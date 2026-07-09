import random

random_num = random.randint(10, 100)

print(random_num)

while True:
    choice = input("Press s for start and q for quit : ")
    
    print()
    
    c = 1
    
    if choice == "q":
        break
    
    elif choice == "s":
        print("::::::::: Game Start :::::::::::::\n")
        print("Enter your choice from 10 to 90..")
        
        while True:
            guess = int(input(f"Enter your guesss number :{c} "))
            
            if guess == random_num:
                print("\n Congralutions !You guess the numbers")
                print("your totoal attemps : ", c)
                break
                
            else:
                print("Try again ! no guees..")
                if guess < random_num:
                    print("Guess bigger")
                
                else:
                    print("think smaller")
                
                c = c + 1
            
    else:
        print("Enter valid key.. \n")