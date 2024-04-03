def rot13(message):
    # Define an empty string to store the result
    result = ""

    # Iterate through each character in the input text
    for char in message:
        # Check if the character is a letter
        if char.isalpha():
            # Determine the case (uppercase or lowercase) of the character
            if char.isupper():
                # Rotate uppercase letters
                rotated_char = chr((ord(char) - 65 + 13) % 26 + 65)
            else:
                # Rotate lowercase letters
                rotated_char = chr((ord(char) - 97 + 13) % 26 + 97)
        else:
            # Non-letter characters remain unchanged
            rotated_char = char
        
        # Append the rotated character to the result
        result += rotated_char

    return result

# Example usage
message = "Hello, World!"
ciphered_text = rot13(message)
print("Original text:", message)
print("Ciphered text:", ciphered_text)