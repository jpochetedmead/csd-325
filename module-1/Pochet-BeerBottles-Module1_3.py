# Name: Julio Pochet Edmead
# Date: 01/12/2025
# Assignment: Module 1.3 - On the Wall + Flowchart

# Purpose: This program counts down bottles of beer on the wall, 
# adjusting the lyrics dynamically and reminding the user to buy more beer at the end.

def countdown_bottles(start_bottles):
    """
    Function to count down bottles of beer on the wall.
    Dynamically adjusts lyrics for singular/plural grammar.
    """
    while start_bottles > 0:
        if start_bottles > 1:
            # Plural case for multiple bottles
            print(f"{start_bottles} bottles of beer on the wall, {start_bottles} bottles of beer.")
            print(f"Take one down and pass it around, {start_bottles - 1} bottle(s) of beer on the wall.\n")
        else:
            # Singular case for the last bottle
            print(f"{start_bottles} bottle of beer on the wall, {start_bottles} bottle of beer.")
            print("Take it down and pass it around, 0 bottle(s) of beer on the wall.\n")
        start_bottles -= 1
    # Final message after countdown is complete
    print("Time to buy more bottles of beer!")

def main():
    """
    Main function to prompt user for input and start the countdown process.
    Handles input validation.
    """
    try:
        # Prompt user for number of bottles
        user_input = int(input("Enter the number of bottles of beer on the wall: "))
        if user_input <= 0:
            print("Please enter a positive number greater than 0.")
        else:
            countdown_bottles(user_input)
    except ValueError:
        # Handle invalid input
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()