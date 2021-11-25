import random
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list
from replit import clear

lives = 6
game_over = False
display = []

chosenWord = random.choice(word_list)
for _ in range(len(chosenWord)):
    display += "_"

print (logo)
print ("welcome to Hangman! Press Enter to start.")
print (stages[6])

while not game_over:
    guess = input("Guess a letter: ").lower()
    clear() 
    if guess in display:
        print (f"You have already guessed '{guess}', lose a life.")
        lives -= 1
        if lives == 0:
            game_over = True
            print (f"You lose, the answer was {chosenWord}.")



    for position in range(len(chosenWord)):
        letter = chosenWord[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosenWord:
        lives -=1
        if lives == 0:
            print (f"You lose. The answer was {chosenWord}")
    print (f"{' '.join(display)}")

    if display == chosenWord:
        game_over = True
        print ("You win!")
    print (stages[lives])