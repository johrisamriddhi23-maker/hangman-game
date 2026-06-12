import random

words = ["orange", "tiger", "height", "plant", "river"]

word = random.choice(words)

guessed_letters = []
wrong_attempts = 6
display = ["_"] * len(word)

print("Welcome to Hangman Game")


while wrong_attempts > 0 and "_" in display:
    print("\nWord:", " ".join(display))
    print("Wrong attempts left:", wrong_attempts)

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("Already guessed!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print("Correct guess!")
    else:
        wrong_attempts -= 1
        print("Wrong guess!")
A simple text-based Hangman game using Python
if "_" not in display:
    print("\nYou Win! The word was:", word)
else:
    print("\n You Lose! The word was:", word)