try:
    n=int(input("Enter your age:"))
    if n < 0:
        print("Age cannot be negative!")
    else:
        print("Your age is:", n)
except ValueError:
    print("Invalid input! Please enter a valid integer for age.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    