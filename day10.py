# Functions with output
# def format_name(f_name , l_name):
#     format_f_name = f_name.title()
#     format_l_name = l_name.title()
#     return f"{format_f_name} {format_l_name}"

# output = format_name("Anubhav","singh")
# print(output)

# def function_1(text):
    # Doctstring is used to write multiline comments to document your code
    # """take a text and return in the form of concatenate"""
    # return text + text

# def function_2(text):
#     return text.title() 
    # return is a end of the function

# output = (function_2(function_1("DiNesh")))
# print(output)

# Project of Day 10
# Create a 4 function that is add,substract,multiply and divide
import art


def add(n1 , n2):
    return n1 + n2
def substract(n1 , n2):
    return n1 - n2
def multiply(n1 , n2):
    return n1 * n2
def divide(n1 , n2):
    return n1 / n2
# add a these 4 functions inside dictionary.keys +,-,*,/
operations = {
    "+" : add,
    "-" : substract,
    "*": multiply,
    "/" : divide
}
# use the dicitionary to perform the operation
# print(operations["*"](4,5))
def calculator():
    print(art.logo)
    should_continue = True
    num1 = float(input("What's your First Number ? :"))
    while  should_continue:
        for symbol in operations:
           print(symbol)
        operation_symbol = input("Pick an operation:")
        num2 = float(input("What's your Second Number ? :"))
        answer = operations[operation_symbol](num1 , num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:").lower()
        if choice == "y":
          num1 = answer
        else:
          should_continue = False
          print("\n" * 20)
          calculator()
calculator()


