# Define the correct password
correct_password = "12345"

# Initialize user input variable
user_input = ""

# Keep asking for the password until the correct one is entered
while user_input != correct_password:
    user_input = input("Enter the password: ")
    
    # Check if the entered password is incorrect
    if user_input != correct_password:
        print("Incorrect password. Try again.")

# Display success message when the correct password is entered
print("Access granted.")
