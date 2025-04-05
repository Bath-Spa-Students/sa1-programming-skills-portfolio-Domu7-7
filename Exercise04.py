# Ask the user a question
answer = input("What is the capital of France? ")

# Check the answer and provide feedback (ignoring capitalization)
if answer.strip().lower() == "paris":
    print("Correct!")
else:
    print("Wrong! The correct answer is Paris.")