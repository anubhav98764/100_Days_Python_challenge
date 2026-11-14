# Random number generator
# import random

# print("Heads and Tails..")
# random_value = random.randint(0,1)
# if random_value == 0:
#     print("Heads")
# else:
#     print("Tails")
# random.random- 0 to 1
# random.randint - any random number
# random.uniform - return a random floating number

# List
# example = 
# import random
# fruit = ["cherry","banana","mango"]
# print(fruit[1])
# random_value = random.choice(fruit) to print random value
# print(random_value)

# random_value  = random.randint(0,2)
# print(fruit[random_value])

# length of the index
# print(len(fruit))
# print(fruit[-1])

# fruit[1] = "Apple"
# fruit.append("Pear")  add something to end of the list

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[1][1])
# print(dirty_dozen[0])
# print(dirty_dozen[1])
# print(dirty_dozen[0][1])


# Rock paper game 
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
a  = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if a == "0":
    print(rock)
elif a == "1":
    print(paper)
elif a >=3 or a < 0:
    print("Invalid input!")
else:
    print(Scissors)
computer = random.randint(0 , 2)
print(f"Computer choice:{computer}")
if computer =="0":
    print(rock)
elif computer == "1":
    print(paper)
else:
    print(Scissors)
if a == 0 and computer == 2:
    print("You Wins")
elif computer > a:
    print("You lose")
elif a > computer:
    print("You Win")
elif a == computer:
    print("Draw")
else:
    print("Invalid Input")

