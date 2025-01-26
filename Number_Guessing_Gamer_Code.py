import random

print() #For Spacing #For Spacing
user_name = input("Please enter your first name: \n")

print(f"Let's play a higher-lower guessing game, {user_name}! \n")


print(f"""{user_name}, after you enter the number range, you get to guess what numRigber I picked! Up for the challenge? \n""")


while True:
  # Check for exit before entering the game loop
  direction = input(f"{user_name}, type 'exit' to quit or press 'Enter' or any key to continue: \n")
  if direction.lower() == "exit":
    print(f"{user_name}, hate to see you go! Mahalo for playing! \n")
    exit()  # Exit the program

  try:
    min_range = int(input(f" {user_name}, enter the minimum number: \n"))
    max_range = int(input(f" {user_name}, enter the maximum number: \n"))

    # Check if min_range is less than max_range
    if min_range < max_range:
      break  # Exit the loop if valid range
    else:
      print(f"{user_name} sorry, the minimum number must be lower than the maximum number.\n")
  except ValueError:
    print(f"{user_name} invalid input. Please enter numbers for both minimum and maximum range.\n")


random_number = random.randint(min_range, max_range)

while True:  
    try:
        user_guess = int(input("Guess a number between {} and {}: ".format(min_range, max_range)))
        if user_guess == random_number:  
            break  
                # Provide feedback based on guess proximity
        if abs(user_guess - random_number) <= 2:
            print(f" {user_name} you're getting Warmer!\n")
        elif user_guess < random_number:
            print(f" {user_name} nope, too low.\n")
        elif abs(user_guess - random_number) >= 3:
            print(f" {user_name} nope, too high.\n")
        else:
            print(f"Oops {user_name}! That number is not within the range. Please try again.\n")
    except ValueError:
        print(f"""Sorry {user_name}, that's not a valid number. Please enter a whole number between {min_range} and {max_range}.\n""")


print(f"Congrats {user_name}! You got it!")
