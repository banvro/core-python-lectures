class board Notes : https://miro.com/app/board/uXjVH2fXI4Y=/?share_link_id=932856626642
digital notes : https://theagleye.com/n/python/nested-if-else-in-python


--------------------------------------------------------------------------------------------------------------------------------
Code:

gate_pin = 1234
room_pin = 9800


u_gate_pin = int(input("Enter gate pin : "))


if gate_pin == u_gate_pin:
    print("open gate...!")
    
    room = int(input("Enter room pin : "))
    
    if room == room_pin:
        print("Room open!")
        print("welcome....:)")
    
    else:
        print("wrong room pin..!")

else:
    print("Wrong pin..!")


# --------------------------------------------------------------------------------------------------------------------------------


print("My Greading system\n")

percentage = int(input("Enter percantage : "))

if percentage > 34:
    if percentage > 90:
        if percentage > 95:
            print("Excelent :) A Grade..!")
        else:
            print("A Grade")
    elif percentage > 80:
        print("B Grade")
    
    elif percentage > 70:
        print("C grade")
    
    elif percentage > 60:
        print("D Grade")
    
    else:
        print("F Grade")
else:
    print("Fail")



# --------------------------------------------------------------------------------------------------------------------------------
