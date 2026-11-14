# # conditional statement
# Age  = int(input("Enter Age:"))
# if Age < 18:
#     print("Age is less than 18")
# else:
#     print("Age is greater than 18")

# height = int(input("Enter Height:"))
# if height < 120:
#     print("height should be grater than 120")
# else:
#     print("Height is correct")

# height = int(input("Enter Height:"))
# weight = int(input("Enter Weight"))
# if height < 120:
#     if weight < 40:
#         print("height and weight are not matched")
#     else:
#         print("Weight is less than 40")
# else:
#     print("Height and weight is correct")

# pizza python program
# print("Welcome to python pizza deliveries")
# size = input("what size of pizza you want ? S , M  or L:")
# pepperoni = input("Do you want to pepperoni on you pizza ? Y or N:")
# cheese = input("Do you want extra cheese on your pizza ? : Y or N:")
# bill = 0
# if size == "S":
#     bill = 15
#     print("Accept Small Pizza")
#     if pepperoni == "Y":
#         bill += 2
#         print("Pepperoni Added")
#     else:
#         print("pepperoni not added")
#     if cheese == "Y":
#         bill += 1
#         print("Cheese Added")
#     else:
#         print("Cheese not added")
#     print(f"Final Price is {bill}")

# if size == "M":
#     bill = 20
#     print("Medium Pizza Accepted")
#     if pepperoni == "Y":
#         print("pepperoni Added")
#         bill += 2
#     if cheese == "Y":
#         print("chesse Added")
#         bill += 1
#     print(f"Final price is {bill}")

# Logical operator
# height = int(input("Enter Height:"))
# weight = int(input("Enter Weight"))
# if height < 120 and weight < 40:
#     print("Height and Weight are correct ")
# else:
    # print("Check Height and Weight")
   

print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     '"=.|                  |
|___________________|__"=._o'"-._        '"=.______________|___________________
          |                '"=._o'"=._      _'"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; '"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .' ' '' ,  '"-._"-._   ". '__|___________________
          |           |o'"=._' , "' '; .". ,  "-._"-._; ;              |
 _________|___________| ;'-.o'"=._; ." ' ''."' . "-._ /_______________|_______
|                   | |o;    '"-.o'"=._''  '' " ,__.--o;   |
|___________________|_| ;     (#) '-.o '"=.'_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      '".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************''')
print("Welcome to Treasure Island")
print("Your Misssion is to be Find the Treasure")
a = input("You are at the cross road. Where do you want to go ? Type Left or Right")
if a == "right":
    print("Game Over...")
else:
    print("You have to come to lake.There is an island in the middle of the lake ")
    b = input("Type wait to wait for a boat. Type swim to swim across:").lower()
    if b == "swim":
      print("Game Over:")
    else:
        print("Wait...")
        c = input('''You arrive at the island unharmed. There is a house with 3 doors.
  One red, one yellow and one blue. Which colour do you choose?''') 
        if c =="red":
          print("Game Over..")
        elif c =="blue":
          print("Game over..")
        else:
          print("You Win")
       
