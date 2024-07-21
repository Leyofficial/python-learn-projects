from random import randint


def get_number_of_dices():
    while True:
        try:
            num_dices = int(input("Give a number of dices in the game [1 - 10]: "))
            if 1 <= num_dices <= 10:
                return num_dices
            else:
                print("The number should be between 1 and 10.")
        except ValueError:
            print("Value should be a number only.")


def get_random_score(num_of_dices):
    MIN = 1
    MAX = 6
    return sum(randint(MIN, MAX) for _ in range(num_of_dices))


def play_game():
    ai_score = 0
    my_score = 0

    num_dices = get_number_of_dices()
    ai_score += get_random_score(num_dices)
    my_score += get_random_score(num_dices)

    if ai_score < my_score:
        print(f"You won! {ai_score} < {my_score} your score is bigger")
    elif my_score < ai_score:
        print(f"You lost! Your score is {my_score} < {ai_score}")
    else:
        print(f"Draw! Score is the same {my_score} = {ai_score}")


def main():
    while True:
        play_game()
        ask_to_continue = input("Do you want to play again? [Yes, No]: ").strip().lower()
        if ask_to_continue == "no":
            break


if __name__ == "__main__":
    main()
