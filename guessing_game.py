# python

# Java ------------ C

# # Array

# 2006 ----> numpy

# Numpy ---> Python ----> Array
#                   -----> C

# AI ---------> Numarical Data

# # Hello <------- verctor

# data scicne
#     -> Numpy
#     -> Pandas
#     -> Matplotlib 
#     -> Seaborn
#     -> Plotly

# ML
#     ---> Supervised learing
#     ---> Unsupervised Learning
#     ---> Reinforsemen learning
# -------------------> Matamatics


# DL ------> NN
#     ---> Tensor
#     ---> Perceptrons
#     ---> ANN
#     ---> CNN
#     ---> GENAI
# -----
# -----
#     NLP
#     ---
#     ----

# GenAI
#     ----> RAG
#     ----> --

# AI Agents
#     ----> 

# Agentic AI ---> automation
#     ---->



# # 6 
#     # 10000

# # Graph datbase --> 


# ___________________________________________



# Game:

# Guessing game

# 10 ------- 50
#     ---------> genrate a radom number

# random = 45

# -----> 30
#     ----> 

# 40
#     ---->

# 49
# ------>
# 45


import random

zx = random.randint(10, 80)


print("""
    ###############################################
    ###############    Guessing Game   ############
    ###############################################
""")


print("""
        ## Instructions
            1. You need to guess number between 10 to 80
            2. We track your number of attempts
            
    """)
print()

while True:

    choice = input("Press s for start and q for quit the game : ")
    print()

    if choice == "s":
        print("############################")
        print("#########  Start ###########")
        print("############################")

        attemps = 0
        
        while True:
            print()
            user_inp = int(input("Enter your guess : "))
            attemps = attemps + 1

            if user_inp == zx:
                print("\n Congratulations! You WON the game !!\n\n")
                print(f"Totle attempts taken to guess : {attemps}")
                print()
                break

            elif user_inp > zx:
                print("\n Please think lower..!\n")

            else:
                print("\n Think bigger..........")

        

    elif choice == "q":
        print("\n Thank you for playing our game\n\n")
        break

    else:
        print("Please Enter valid key..!\n\n")






    



