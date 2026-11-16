# Dictionaries - store key and values 
# {key : value}

programming_dictionaries = {
    "Bug" : "An error in a program that prevent the program by running as expected",
    "Function": "A piece of code that can easily call over and over again."
}
# print(programming_dictionaries)

programming_dictionaries["Loop"] = "the action of doing something overand over again"
# print(programming_dictionaries)

# Wipe an existing dictionaries
programming_dictionaries = {}
print(programming_dictionaries)

# edit in dictionaries
programming_dictionaries["Bug"] = "A moth in a computer"
print(programming_dictionaries)

# Loop through a dictionaries
for dict in programming_dictionaries:
    # print(dict) print only key
    # print(programming_dictionaries[key]) - print whole key and value

# nested list in dictionaries
# student_data = {
#         "subjects": ["Math", "Science", "English"],
#         "scores": [85, 90, 78]
#     }
# print(student_data["subjects"][0])

# nested list inside list
# nested_list = ["A","B",["C","D"]]
# print(nested_list[2][1])

# multiple key and value in dictionaries
 student_data = {
    "Alice": {
        "subjects": ["Math", "Science", "English"],
        "scores": [85, 90, 78]
    },
    "Bob": {
        "subjects": ["History", "Math", "Art"],
        "scores": [88, 76, 92]
    }
}
print(student_data["Bob"]["subjects"][2])

