from random import choice

def draw(score):
    if score == 1:
        print("|\n"
            "|\n"
            "|\n"
            "|\n"
            "|\n")
    elif score == 2:
        print("|\n"
            "|\n"
            "|\n"
            "|\n"
            "|\n"
            "___________\n")
    elif score == 3:
        print("______\n"
            "|\n"
            "|\n"
            "|\n"
            "|\n"
            "|\n"
            "___________\n")
    elif score == 4:
        print("______\n"
            "|      |\n"
            "|      |\n"
            "|\n"
            "|\n"
            "|\n"
            "___________\n")
    elif score == 5:
        print("______\n"
            "|      |\n"
            "|      O\n"
            "|\n" 
            "|\n"
            "|\n"
            "___________\n")
    elif score == 6:
        print("______\n"
            "|      |\n"
            "|      O\n"
            "|     /|\\\n" 
            "|\n"
            "|\n"
            "___________\n")
    elif score == 7:
        print("______\n"
            "|      |\n"
            "|      O\n"
            "|     /|\\\n" 
            "|     / \\\n"
            "|\n"
            "___________\n")
        

print(" ------------------------------------------------") 
print("|                                                |")
print("|                                                |")
print("|    Welcome to a game of Hangman!!!             |")
print("|                                                |")
print("|                                                |")
print(" ------------------------------------------------")

words = ["hello", "there", "school", "food", "ist", "IST", "clothes", "friends"]

chosen_word = choice(words)

#astrik is length of the chosen word

HIDDEN_LETTER = '*'

#length of the chosen word len(chosen_word)
displayed_word = HIDDEN_LETTER * len(chosen_word)

print(displayed_word)

TOTAL_ALLOWED_GUESS = 7
wrong_attempt = 0
count = 0

while wrong_attempt < TOTAL_ALLOWED_GUESS:
    guess_letter = input("Guess a letter: ")
    count += 1

    print("Guess count: " + str(count))

    if guess_letter in chosen_word:
        offset = 0
        while offset < len(chosen_word):
            try:
                i = chosen_word.index(guess_letter, offset)
                offset = i + 1
                displayed_word = displayed_word[:i] + guess_letter + displayed_word[i+1:]
            except ValueError as e:
                break   
    else:
         wrong_attempt += 1 

    print(displayed_word)
    draw(wrong_attempt)

    if HIDDEN_LETTER not in displayed_word:
        print("Congratulations! YOU WON!")
        break

else:
    print("You have lost :(")
    