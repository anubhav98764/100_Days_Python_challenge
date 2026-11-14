# loop concept
# For loop-----
# fruit  = ["Mango","banana","Pear"]
# for fruits in fruit:
#     print(fruits)

# student_score = [100,90,100,37,93,77,75]
# # sum = 0
# for total in student_score:
#     sum += total
# print(sum)

# max score using for loop
# max_score  = 0
# for max in student_score:
#     if max > max_score:
#         max_score  = max
# print(max_score)

# Range function with for loop--
# sum = 0
# for number in range(1,101):
#     sum += number
# print(sum)

# Password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','*','+','(',')']

print("welcome to the PyPassword generator!")
n_letter = int(input("How many would you like to accept letter.."))  
n_number = int(input("How many would you like to accept number..")) 
n_symbol = int(input("How many would you like to accept symbol.."))  
# easy version
password = ""
for char in range(1 , n_letter + 1):
    password += random.choice(letters)

for char in range(1, n_number + 1):
    password += random.choice(numbers)

for char in range(1,n_symbol + 1):
    password  += random.choice(symbols)
print(password)

# hard Version
# password_list = []
# for char in range(0,n_letter):
#     password_list += random.choice(letters)
# for char in range(0,n_number):
#     password_list += random.choice(numbers)

# for char in range(0,n_symbol):
#     password_list += random.choice(symbols)
# random.shuffle(password_list) shuffle does not support empty string
# password  = ""
# for char in password_list:
#     password += char
# print(password)









