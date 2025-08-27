import random
import time


def timer_record():
    return time.time()


def Welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 5 chances to guess the correct number.\n")
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)\n")


def choosing_difficulty():
    while True:
        difficulty_level = input("Enter your choice: ")
        print()
        if difficulty_level == "1":
            print("Great! You have selected the easy difficulty level.")
            return 10
        elif difficulty_level == "2":
            print("Great! You have selected the medium difficulty level.")
            return 5
        elif difficulty_level == "3":
            print("Great! You have selected the diffcult difficulty level.")
            return 3   
        else:
            print("invalid input")
            continue


def game_start(chance, answer, start_time):
    num_of_attempts = 0
    while chance > num_of_attempts:
        guess =input("Enter your guess: ")
        
        if guess.isdigit() != True:
            print("Invalid input! Please enter a integer within 1-100\n")
            continue
        else:
            guess = int(guess)
            if guess < 1 or guess > 100:
                print("Invalid input! Please enter a integer within 1-100\n")
                continue
            if guess > answer:
                print(f"Incorrect! The number is less than {guess}\n")
                num_of_attempts += 1
                continue
            if guess < answer:
                print(f"Incorrect! The number is greater than {guess}\n")
                num_of_attempts += 1
                continue
            if guess == answer:
                num_of_attempts += 1
                end_time = timer_record()
                timer = end_time - start_time
                print(f"\nCongratulations! You guessed the correct number in {num_of_attempts} attempts in {timer:.2f}.")
        
    print("\nYou lose all your chance......")
    print(f"The correct answer is {answer}")


def ask_again():
    again = input("Do you want to play again?(y/n): ").lower()
    if again == "y":
        return True
        print("\n***The game restarted***")
    elif again == "n":
        print("bye")


def main():
    is_running = True
    while is_running:
        is_running = False
        Welcome_message()
        answer = random.randint(1,100)
        chance = choosing_difficulty()
        start_time = timer_record()
        print("Let's start the game!\n")
        game_start(chance, answer, start_time)
        is_running = ask_again()


if __name__ == "__main__":
    main()
