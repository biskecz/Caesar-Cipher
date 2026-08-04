# 33-letter Russian alphabet (including Ё)
RU_LOWER = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
RU_UPPER = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def encrypt_eng(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result


def decrypt_eng(text, shift):
    return encrypt_eng(text, -shift)


def encrypt_ru(text, shift):
    result = ""
    for char in text:
        if char in RU_LOWER:
            idx = (RU_LOWER.index(char) + shift) % 33
            result += RU_LOWER[idx]
        elif char in RU_UPPER:
            idx = (RU_UPPER.index(char) + shift) % 33
            result += RU_UPPER[idx]
        else:
            result += char
    return result


def decrypt_ru(text, shift):
    return encrypt_ru(text, -shift)


def brute_force(text, lang):
    max_shift = 26 if lang == "eng" else 33

    print("\n" + "=" * 40)
    print(f"  BRUTE-FORCE RESULTS ({lang.upper()})")
    print("=" * 40)

    for shift in range(1, max_shift):
        if lang == "eng":
            decrypted_text = decrypt_eng(text, shift)
        else:
            decrypted_text = decrypt_ru(text, shift)

        print(f"[Shift {shift:2d}] -> {decrypted_text}")
        print("-" * 50)

    print("=" * 40 + "\n")


# --- Main Menu ---
def main():
    print("\n" + "=" * 50)
    print(" Welcome to the Caesar Cipher Program! ")
    print("- -" * 17 + "\n")

    lang_choice = input("Which language do you want to use? (eng/ru): ").strip().lower()
    choice = input("Do you want to encrypt, decrypt, brute force? (e/d/b): ").strip().lower()

    if lang_choice == "eng":
        text = input("Enter the English text: ")

        if choice in ["e", "d"]:
            shift = int(input("Enter the shift value (1-25): "))
            if choice == "e":
                print("Encrypted text:", encrypt_eng(text, shift))
            elif choice == "d":
                print("Decrypted text:", decrypt_eng(text, shift))
        elif choice == "b":
            brute_force(text, "eng")
        else:
            print("Invalid operation choice.")

    elif lang_choice == "ru":
        text = input("Enter the Russian text: ")

        if choice in ["e", "d"]:
            shift = int(input("Enter the shift value (1-32): "))
            if choice == "e":
                print("Encrypted text:", encrypt_ru(text, shift))
            elif choice == "d":
                print("Decrypted text:", decrypt_ru(text, shift))
        elif choice == "b":
            brute_force(text, "ru")
        else:
            print("Invalid operation choice.")
    else:
        print("Invalid language choice.")


if __name__ == "__main__":
    main()