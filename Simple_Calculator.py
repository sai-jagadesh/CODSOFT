def calculator():
    while True:
        # Get the first number.
        first_number = float(input("Enter the first number: "))

        # Get the second number.
        second_number = float(input("Enter the second number: "))

        # Get the operation.
        operation = int(input("Choices:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\nEnter Here(in numbers): "))

        # Perform the operation.
        if operation == 1:
            result = first_number + second_number
            print(first_number,"+",second_number,"=",result)
        elif operation == 2:
            result = first_number - second_number
            print(first_number,"-",second_number,"=",result)
        elif operation == 3:
            result = first_number * second_number
            print(first_number,"*",second_number,"=",result)
        elif operation == 4:
            result = first_number / second_number
            print(first_number,"/",second_number,"=",result)
        else:
            print("Invalid operation.")
            continue


        # Check if the user wants to exit.
        choice = input("Do you want to continue (y/n)? ")
        if choice == "n":
            break


if __name__ == "__main__":
    calculator()
