import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special_chars=True):
    
    character_pool = string.ascii_lowercase  

    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_digits:
        character_pool += string.digits
    if use_special_chars:
        character_pool += string.punctuation

    if length <= 0:
        return "Password length must be greater than 0."

    
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    
    length = int(input("Enter the desired length of the password: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    
    password = generate_password(length, use_uppercase, use_digits, use_special_chars)

    print(f"Generated Password: {password}")


if __name__ == "__main__":
    main()
