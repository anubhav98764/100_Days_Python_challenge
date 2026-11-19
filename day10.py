# Functions with output
# def format_name(f_name , l_name):
#     format_f_name = f_name.title()
#     format_l_name = l_name.title()
#     return f"{format_f_name} {format_l_name}"

# output = format_name("Anubhav","singh")
# print(output)

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = (function_2(function_1("DiNesh")))
print(output)