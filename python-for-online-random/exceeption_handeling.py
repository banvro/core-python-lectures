# OOPs
# Exception Handeling
# Regex
# string functions



# Exception Handeling

# Errors:
#     Types of errors
#         1) Syntax Error
#         2) Logical Error
#         3) Run time error

# Syntax Error:
#     developer end

# if 10 == 10
#     print("helllooo")

# a = 10
# b   30

# zx = a + b


#  2) Logical Error


# a = 10
# b = 0

# c = a / b

# print(c)




# 3) Run time error (user end)


# dob_year = int(input("Enter your born year : "))

# age = 2026 - dob_year

# print(age)


# zx = 100
# print("heyyy")
# print(zx + zx)
# print("ok")
# print("done")
# print(hey)
# print("goooooooo")
# print("nice coeeee")
# print("working")
# print("done")


# Exception Handleng

# Exception Handeling


# try:
#     # doutable code

# except Exception:
#     # if try --> block ---> error

# else:
#     # if -- try --> having no error

# finally:
#     # --> indecate exception handeling done

# print("heyyyyyyyy")
# print("start")
# print("how are you")
# try:
#     age = int(input("Enter you age : "))

# except Exception as e:
#     print("Error Handleed...!!!!!!!!!", e)

# else:
#     print("User age is : ", age)

# finally:
#     print("Exception handleing donee..")

# print("important codee....")
# print("workingggg")
# print("goooooooooo")
# print("done.....")




try:
    num1 = input("Enter first number : ")
    num2 = input("Enter second number : ")
    zx = int(num1) / int(num2)
    print("deviion is : ", zx)
    
    dob = int(input("Enter your dob_year : "))
    
    age = 2026 - dob
    print("User age is : ", age)

except ZeroDivisionError:
    print("You are not able to devde vales with 0")

except ValueError:
    print("Please Enter vaild Value")

except Exception:
    print("Error handeled")
    
# print("thank you........")



#  age = 10

if 10 == 10:
print("helloo")














