# Function to encrypt text using Caesar Cipher
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine base ASCII value for uppercase or lowercase letters
            shift_base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around using modulo
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    return result


# Function to decrypt text using Caesar Cipher
def decrypt(text, shift):
    result_1 = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            # Shift back character and wrap around using modulo
            result_1 += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            result_1 += char
    return result_1


# Display welcome banner
print(
    "\n",
    "=" * 50,
    "\n Welcome to the Caesar Cipher Encryption Program! \n",
    "- -" * 17,
    "\n",
)

# Get user input
choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
text = input("Enter the text: ")
shift = int(input("Enter the shift value (1-25): "))

print("-" * 50, "\n")

# Execute action based on user selection
if choice == "e":
    print("Encrypted text:", encrypt(text, shift))
elif choice == "d":
    print("Decrypted text:", decrypt(text, shift))
else:
    print(
        "Invalid choice. Please enter 'e' for encryption or 'd' for decryption."
    )