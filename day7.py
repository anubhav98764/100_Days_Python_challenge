# hangman challenge

# the challenge divided into 5 parts

#  part1 ----
stages = [
   r'''
  +---+
  |   |
      |
      |
      |
      |
''',
r'''
  +---+
  |   |
  O   |
      |
      |
      |
''',
r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
''',
r'''
  +---+
  |   |
  O   |
 /|\  |
/     |
      |
''',
r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
''',
r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
''']
logo = r'''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
                   '''
print(logo)
# todo 1
import random
word_list = ["aardvark","baboon","camel"]
lives  = 5
random_word = random.choice(word_list)
print(random_word)

placeholder = ""
length = len(random_word)
for char in range(0, length):
    placeholder += "_"
print(placeholder)
# todo 2
over = False
correct_letter = []
while not over:
  guess = input("Guess a letter:").lower()
  print(f"****************************{lives}/6 LIVES LEFT****************************")
  

# todo 3

  display = ""
  for letter in random_word:
     if letter == guess:
        display += letter
        correct_letter.append(letter)

     elif letter in correct_letter:
        display += letter

     else:
        display += "_"
  print(display)

  if guess not in random_word:
     lives -= 1
     if lives == 0:
        over = True
     print("You lose !")

  if "_" not in display:
     over = True
     print("You Win!")
  print(stages[lives])
      


