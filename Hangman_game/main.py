import random
import art


logo_text= "hangman"
logo = art.text2art(text=logo_text, font="block")
print(logo)

stages =     [
    """
       +---+
       |   |
               |
               |
               |
               |
    =========""",
    """
       +---+
       |   |
       O   |
               |
               |
               |
=========""",
    """
       +---+
       |   |
       O   |
       |   |
               |
               |
    =========""",
    """
       +---+
       |   |
       O   |
      /|   |
               |
               |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\  |
               |
               |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\  |
      /    |
               |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\  |
      / \  |
               |
    =========""",
]

wordlist= ["book", "balloon", "apple","cupboard", "cassava", "yellow", "baboon", "camel"]

lives = 6

random_word= random.choice(wordlist)

placeholder = ""
word_length = len(random_word)
for position in range(word_length):
    placeholder += "_"


game_over = False
correct_letters = []
while not game_over:

    print(f"You have {lives} left!")
    guess = input("Enter a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""
    for letter in random_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess:" + display)


    if guess not in random_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f" It was {random_word}. You lose!")

    if "_" not in display:
        game_over = True
        print("You win")


    print(stages[lives])

