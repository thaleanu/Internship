# Submitted By Aniket Sominath Thale (Batch 11)
# Task 2: Random Password Generator


import random
import string

def generate_random_password(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Check if the desired length is valid
    if length <= 0:
        return "Password length must be a positive integer."
    
    # Generate a random password by selecting characters randomly
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

if __name__ == "__main__":
    try:
        password_length = int(input("Enter the desired password length: "))
        random_password = generate_random_password(password_length)
        print("Generated Password:", random_password)
    except ValueError:
        print("Please enter a valid integer for password length.")
