import random
import hangman_art
import hangman_words 

#Variables
end_of_game = False
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
lives = 6

#Testing Code
print(hangman_art.logo)
print(f"Pssssst, the secret word is {chosen_word}.")

#Create blanks
display = []
for letter in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose. GAME OVER")

# Join all the elements in the lust and turn it into a string
    print(f"{' '.join(display)}")

    #Check of user has got all letters
    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(hangman_art.stages[lives])
