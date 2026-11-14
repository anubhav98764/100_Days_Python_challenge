# function and inputs

# def my_function(something):

# def greet():
#     print("Hello my name is:")
#     print("Anubhav")
#     print("I am a bcs student")
# greet()

# input with one parameter
# def greet_name(name):
#     print(f"My name is {name}")
# greet_name("Anubhav")
# input with multiple parameter

# def greet_name(name,age):
#     print(f"My name is {name}")
#     print(f"Age:{age}")
# greet_name("Anubhav",56)

logo = ''',adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88 
'''
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letters in original_text:
#         if letters in alphabet:
#           shifted_postion = alphabet.index(letters) + shift_amount
#           shifted_postion %= len(alphabet)
#           cipher_text += alphabet[shifted_postion]

#     print(f"Here's the encoded result:{cipher_text} ")
# encrypt(original_text= mess_input,shift_amount= number_input)

# def decrypt(original_text ,shift_amount):
#     output_text = ""
#     for letters in original_text:
#       shifted_position = alphabet.index(letters) - shift_amount
#       shifted_position %= len(alphabet)
#       output_text += alphabet[shifted_position]
#     print(f"Here's the decrypt result:{output_text}") 
# decrypt(original_text= mess_input,shift_amount= number_input)

def ceaser(original_text,shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode =="decode":
          shift_amount *= -1
    for letters in original_text:
             if letters not in alphabet:
                  output_text += letters
             else:
                   shifted_postion = alphabet.index(letters) + shift_amount
                   shifted_postion %= len(alphabet)
                   output_text += alphabet[shifted_postion]
   
    print(f"Here's the {encode_or_decode}d result:{output_text} ")

continue_code = True
while continue_code:
   encode_input = input("Type 'encode' to encrypt, type 'decode' to decrypt:")
   mess_input = input("Type your message:")
   number_input = int(input("Type the shift number:"))
   ceaser(original_text = mess_input,shift_amount =number_input,encode_or_decode =encode_input)
   restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
   if restart == "no":
        continue_code = False
        print("GoodBye")
   

