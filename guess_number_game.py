import random

def guess_number_game():
    print("Welcome to the Guess the Number Game!\n")

    player_name = input("Please enter your name: ").strip().capitalize()
    if not player_name:
        player_name = "Player"

    print(f"\nHello, {player_name}! ")
    print("I'm thinking of a number between 1 and 100...")
    print("Try to guess it in as few attempts as possible!\n")

    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False  # Status

    while not guessed:
        try:
            guess = int(input("Enter your guess (1–100): "))
            if not (1 <= guess <= 100):
                print("❗ Please enter a number within the range 1 to 100.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"\n Congrats {player_name}! You guessed it right! ")
                print(f"The number was {secret_number}.")
                print(f"You did it in {attempts} attempts.")

        except ValueError:
            print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    guess_number_game()
