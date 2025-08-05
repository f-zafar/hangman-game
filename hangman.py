# Import necessary modules
import random 
from hangman_words import words
from hangman_art import logo, stages

# Display the Hangman logo
print(logo)
# Initial number of lives (wrong guesses allowed)
lives = 6 

# Randomly choose a word from the word list
chosen_word = random.choice(words)

# Create a placeholder string with underscores for each letter in the chosen word
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

# Game state variables
game_over = False
correct_letters = [] # Stores correctly guessed letters to avoid repeats

# Main game loop
while not game_over:
    print(f"********************************{lives}/6 LIVES LEFT **********************************")
    # Ask player to guess a letter and convert to lowercase
    guess = input("Guess a letter: ").lower()

    # Check if the letter was already guessed correctly before
    if guess in correct_letters:
        print(f"You've already guessed the letter {guess}")

    # Create a new display string with guessed letters revealed
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter              # Reveal the guessed letter
            correct_letters.append(guess)  # Add to correct letters
        elif letter in correct_letters:    
            display += letter              # Keep previously guessed correct letters
        else:
            display += "_"                 # Hide letters not yet guessed

    # Show the current state of the word to the player
    print("Word to guess: " + display)

    # If the guessed letter is not in the word, reduce a life
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word.You lose a life.")
        
        # If no lives are left, end the game
        if lives == 0:
            game_over = True
            print(f"**************************** It was {chosen_word}! You Lose *******************************")

    # If there are no more underscores, the player has guessed the full word
    if "_" not in display:
        game_over = True
        print("**************************** You Win *******************************")
    # Print the current hangman stage based on remaining lives
    print(stages[lives])
    
