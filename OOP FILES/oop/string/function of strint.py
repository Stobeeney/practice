# finding length of string
length = len("computer Engineering")
print(length)  # Output will be 20


# String Concatenation
print("CMPE" + "103")

# String Repeat
print("A" * 4)

# Substring Tests

# Example string
string = "computer Engineering"

# First 3 characters
first_three = string[:3]
print("First 3 characters:", first_three)

# Last 3 characters
last_three = string[-3:]
print("Last 3 characters:", last_three)

# Middle of the string (from index 4 to 8)
middle_substring = string[4:9]
print("Middle substring (index 4 to 8):", middle_substring)

# Extract "computer"
computer_substring = string[:8]
print("Extract 'computer':", computer_substring)

# Extract "Engineering"
engineering_substring = string[9:]
print("Extract 'Engineering':", engineering_substring)

# Length of the string
length_of_string = len(string)
print("Length of the string:", length_of_string)
