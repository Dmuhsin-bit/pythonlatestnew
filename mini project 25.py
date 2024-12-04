def get_valid_integer():
    while True:
        arshad = input("Enter a valid integer: ")
        try:
            valid_int = int(arshad)
            print(f"Thank you! You entered a valid integer: {valid_int}")
            return valid_int
        except ValueError:
            print("Invalid input. Please try again.")
get_valid_integer()
