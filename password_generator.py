import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4.")
        return None
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("Password Generator")
    try:
        length = int(input("Enter desired password length: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    password = generate_password(length)
    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
