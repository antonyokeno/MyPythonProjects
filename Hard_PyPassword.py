
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# Create an empty list to store the password characters
password_chars = []

# Add random letters to the password
for _ in range(nr_letters):
    password_chars.append(random.choice(letters))

# Add random symbols to the password
for _ in range(nr_symbols):
    password_chars.append(random.choice(symbols))

# Add random numbers to the password
for _ in range(nr_numbers):
    password_chars.append(random.choice(numbers))

# Shuffle the password list to ensure random order
random.shuffle(password_chars)

# Join the list into a string to form the final password
password = ''.join(password_chars)

# Print the generated password
print(f"Your password is: {password}")
