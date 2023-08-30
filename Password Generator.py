import random
import string
import time as t

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("-"*45)
    print("Welcome to the Password Generator Application!")
    print("-"*45)

    while True:
        try:
            password_length = int(input("How many characters you need in your password?\n[Enter in Digits] (or enter 0 to exit): "))
            
            if password_length == 0:
                print("-"*45)
                print("Exiting the Password Generator Application. Goodbye!")
                print("-"*45)
                break
            
            if password_length < 0:
                raise ValueError("Password length should be a non-negative integer.")
            
            password = generate_password(password_length)
            print("Generated Password:", password)
            print("*"*30)
            t.sleep(1.0)
        except ValueError as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
