import random

print("Hello! Its Nice to see you")

# Create your word list 
word = ("hacker", "bounty", "legal", "random", "virus")

# Create an empty list
# for each letter in the seceret_word add a "_" that will be printed to the console
# Example if the word is Hacker "_","_","_","_","_","_"

# Randomly choose a word from the list you have created 
secret_word = random.choice(word)
# print(secret_word)

# add a print statement tell the user they get 7 guesses
print("you get 7 guesses")
display_word = []
for letter in secret_word:
    display_word += "_"
print(display_word)

# Create a variable as an int starting at 0 and when it gets to the number 7 the game ends
# 1 use a while loop so your game keeps going the word has been guessed 
# ask the user to guess a letter
# Bonus make the program take the input from the user and make it lowercase
num = 0
game_over = False
while not game_over:

    guess = input("Guess the Letter\n").lower() 

    # Check if the letter is in the word 
    # Loop through each of the letters in the choosen word
    # if the letter is in the word replace the "_" with the letter 
    # it should look like this "_","a","c","_","_","r"

    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            display_word[position] = letter
    if guess not in secret_word:
        num +=1
        guesses_left = 7 - num 
        print("You have {guesses_left} guess left")
        if num >= 7:
            print("You Lose")
            game_over = True
    print(display_word)

    if "_" not in display_word:
        print("You Win")
        game_over = True