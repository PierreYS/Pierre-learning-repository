import random
import time

def main():
    is_running = True
    while is_running:
        is_running = False
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")
        print("You have 5 chances to guess the correct number.")
        print()
        print("Please select the difficulty level:")
        print("1. Easy (10 chances)")
        print("2. Medium (5 chances)")
        print("3. Hard (3 chances)")
        print()
        
        is_choosing = True
        answer = random.randint(1,100)
        
        while is_choosing:
            difficulty_level = input("Enter your choice: ")
            print()
            

            if difficulty_level == "1":
                print("Great! You have selected the easy difficulty level.")
                chance = 10
                is_choosing = False

            elif difficulty_level == "2":
                print("Great! You have selected the medium difficulty level.")
                chance = 5
                is_choosing = False

            elif difficulty_level == "3":
                print("Great! You have selected the diffcult difficulty level.")
                chance = 3
                is_choosing = False
                
            else:
                print("invalid input")
                continue
            
        print("Let's start the game!")
        print()
        num_of_attempts = 0
        
        while chance > num_of_attempts:
            guess =input("Enter your guess: ")
            
            if guess.isdigit() != True:
                print("Invalid input! Please enter a integer within 1-100")
                print()
                continue
            else:
                guess = int(guess)
                if guess < 1 or guess > 100:
                    print("Invalid input! Please enter a integer within 1-100")
                    print()
                    continue
                if guess > answer:
                    print(f"Incorrect! The number is less than {guess}")
                    print()
                    num_of_attempts += 1
                    continue
                if guess < answer:
                    print(f"Incorrect! The number is greater than {guess}")
                    print()
                    num_of_attempts += 1
                    continue
                if guess == answer:
                    num_of_attempts += 1
                    print()
                    print(f"Congratulations! You guessed the correct number in {num_of_attempts} attempts.")
                    again = input("Do you want to play again?(y/n): ")
                    if again == "y":
                        is_running = True
                        print()
                        print("***The game restarted***")
                        break
                    elif again == "n":
                        break
            
        else:
            print()
            print("You lose all your chance......")
            print(f"The correct answer is {answer}")
            again = input("Do you want to play again?(y/n): ")
            if again == "y":
                is_running = True
                print()
                print("***The game restarted***")
            elif again == "n":
                break
            else:
                continue

if __name__ == "__main__":
    main()

