import random

def check_guess(number, guess):
    cows = 0
    bulls = 0
    for i in range(4):
        if number[i] == guess[i]:
            cows += 1
        elif guess[i] in number:
            bulls += 1
    return cows, bulls

def main():
    number = str(random.randint(1000, 9999))
    attempts = 0
    print("Welcome to Cows and Bulls!")
    print("I have picked a 4-digit number.")
    print("Guess the number, and I will tell you how many digits are in the correct place (cows) and how many are in the wrong place (bulls).")
    print("Type 'exit' to quit the game.")

    while True:
        guess = input("Your guess: ")
        if guess.lower() == 'exit':
            print("Goodbye!")
            break

        if len(guess) != 4 or not guess.isdigit():
            print("Please enter a valid 4-digit number.")
            continue

        cows, bulls = check_guess(number, guess)
        attempts += 1
        print(f"{cows} cows, {bulls} bulls")

        if cows == 4:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        else:
            print("Try again!")

if __name__ == "__main__":
    main()
