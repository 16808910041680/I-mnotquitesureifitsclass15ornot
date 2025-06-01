try:
    number = int(input("Enter a number: "))
    if number < 0:
        print("What is this? I thought this was a random number generator, not a random negative number generator!")
    else:
        print("The number is:", number)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")