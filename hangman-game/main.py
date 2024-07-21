from random import choice
from picture import hanged_man


print("\n Welcome to Hangman! \n")
miss_times = 0


def select_word():
    with open("words.txt", mode="r") as words:
        word_list = words.readlines()
    return choice(word_list).strip()


letters = [item for item in select_word()]
guessed_letters = ['_' for _ in range(len(letters))]
used_letters = []
print(letters)

print(f'Your word is: {" ".join(guessed_letters)}')


def check_letter(word, guessed_letter):
    global miss_times
    if guessed_letter in word:
        for i, letter in enumerate(word):
            if letter == guessed_letter:
                guessed_letters[word.index(letter, i)] = letter
    else:
        print("\n Sorry, it's not there.")
        miss_times += 1
        print(hanged_man[miss_times - 1])
        used_letters.append(guessed_letter)
    return guessed_letters


while miss_times < 7:
    q = input("\n Guess the letter: ")
    if len(q) > 1:
        print("You can use only one letter")
        continue
    res = check_letter(letters, q)
    if guessed_letters == letters:
        print("\n Congrats! You did it!")
        break
    print(f'Your word is: {" ".join(guessed_letters)}')
    print(f"Current guessed letters: {", ".join(used_letters)}")
else:
    print(f"\n Sorry, you lost! The word was {"".join(letters)}")
