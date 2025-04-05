# Create a dictionary mapping month numbers to days
month_days = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

# Ask the user for a month number
month = input("Enter a month number (1-12): ")

# Check if input is valid and print the corresponding days
if month.isdigit():  # Check if input is a number
    month = int(month)
    if 1 <= month <= 12:
        print(f"Month {month} has {month_days[month]} days.")
    else:
        print("Invalid month number. Please enter a number between 1 and 12.")
else:
    print("Invalid input. Please enter a number.")