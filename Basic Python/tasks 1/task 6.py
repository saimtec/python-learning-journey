# 6.Cows And Bulls   
# Create a program that will play the “cows and bulls” game with the user. The game works like this:
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the
# user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed 
# correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” 
# and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the 
# number of guesses the user makes throughout the game and tell the user at the end.




import random

def number():
    return str(random.randint(1000, 9999))

def cows_bulls(user_guess, secret_number):
    cows = 0
    bulls = 0
    for i in range(4):
        if user_guess[i] == secret_number[i]:
            cows += 1
        elif user_guess[i] in secret_number:
            bulls += 1
    return cows, bulls

def play_game():
    secret_number = number()
    attempts = 0
    print("Welcome to Cows and Bulls Game!")
    print("You can type 'exit' at any time to quit the game.")
    
    while True:
        user_guess = input("Enter your 4-digit guess: ")
        
        if user_guess.lower() == "exit":
            print("You have exited the game. Goodbye!")
            break
        
        if len(user_guess) != 4 or not user_guess.isdigit():
            print("Invalid input. Please enter a valid 4-digit number.")
            continue
        
        attempts += 1
        cows, bulls = cows_bulls(user_guess, secret_number)
        print(f"{cows} cows, {bulls} bulls")
        
        if cows == 4:
            print(f"Congrats! You've guessed the correct number {secret_number} in {attempts} attempts!")
            break

if __name__ == "__main__":
    play_game()
