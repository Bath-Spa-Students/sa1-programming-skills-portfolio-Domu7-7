def check_even_odd(number):
    """Determines if a number is even or odd and returns a message."""
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

def main():
    # Ask the user for a number
    try:
        user_input = int(input("Enter a number: "))
        # Call the function and print the result
        result = check_even_odd(user_input)
        print(result)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()
