# a = "Anubhav"
# print(a[0])
# print(type(a))

# a = 3.14
# print(type(a))

# a = True
# print(type(a))

# print("My age:",str(12))

# print(3*(3+3)/3-3)

# a = 2.6667544
# print(round(a,2))

score  = 0

# score += 1
# print(score)
# print("Your score is:",str(score))
# print(f"My score {score} is bad")

# a = int("5") / int(2.7)
# print(type(a))

# project
print("Welcome to the tip calculator!")
a = int(input("What was the total bill?"))
z = int(input("How much tip would you like yo give? 10 ,12 ,15:"))
y = z/100
total = a * y + a
b = int(input("How many people to split the bill?:"))
c = total / b
print("Each person should pay:",round(c))