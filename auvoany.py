try:
    number = int(input("Enter a number: "))
    print ("The number is:", number)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")