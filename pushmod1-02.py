# Get a string input from the user
user_input = input("Enter a string: ")

# Initialize empty strings for lowercase and uppercase letters
lowercase_letters = ""
uppercase_letters = ""

# Remove spaces and separate lowercase and uppercase letters
for char in user_input:
    if char.islower():
        lowercase_letters += char
    elif char.isupper():
        uppercase_letters += char

# Combine the lowercase and uppercase letters without spaces
result_string = lowercase_letters + uppercase_letters

# Print the modified string
print("Modified string:", result_string)