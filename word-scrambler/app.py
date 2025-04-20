import random

print("WORD SCRAMBLER")

while True:
    word = input("Enter a word to scramble (or 'exit' to quit): ")
    if word.lower() == 'exit':
        break

    scrambled_word = ''.join(random.sample(word, len(word)))
    print(f"Scrambled Word: {scrambled_word}")

    guess = input("Guess the original word: ")
    if guess.lower() == word.lower():
        print("Correct!")
    else:
        print(f"Wrong! The original word was: {word}")
    print()

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        break
print("Thanks for playing the Word Scrambler game!")