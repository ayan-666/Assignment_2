def encrypt_text(text, n, m):
    encrypted = []
    for char in text:
        if 'a' <= char <= 'z':
            # Lowercase letters
            if char <= 'm':
                # First half (a-m): shift forward by n*m
                shifted = ord(char) + (n * m)
                while shifted > ord('z'):
                    shifted -= 26
                encrypted_char = chr(shifted)
            else:
                # Second half (n-z): shift backward by n+m
                shifted = ord(char) - (n + m)
                while shifted < ord('a'):
                    shifted += 26
                encrypted_char = chr(shifted)
        elif 'A' <= char <= 'Z':
            # Uppercase letters
            if char <= 'M':
                # First half (A-M): shift backward by n
                shifted = ord(char) - n
                while shifted < ord('A'):
                    shifted += 26
                encrypted_char = chr(shifted)
            else:
                # Second half (N-Z): shift forward by m^2
                shifted = ord(char) + (m ** 2)
                while shifted > ord('Z'):
                    shifted -= 26
                encrypted_char = chr(shifted)
        else:
            # Special characters and numbers remain unchanged
            encrypted_char = char
        encrypted.append(encrypted_char)
    return ''.join(encrypted)


def decrypt_text(text, n, m):
    decrypted = []
    for char in text:
        if 'a' <= char <= 'z':
            # Lowercase letters
            if (ord(char) - (n * m)) <= ord('m'):
                # First half was shifted forward by n*m, so we shift back
                shifted = ord(char) - (n * m)
                while shifted < ord('a'):
                    shifted += 26
                decrypted_char = chr(shifted)
            else:
                # Second half was shifted backward by n+m, so we shift forward
                shifted = ord(char) + (n + m)
                while shifted > ord('z'):
                    shifted -= 26
                decrypted_char = chr(shifted)
        elif 'A' <= char <= 'Z':
            # Uppercase letters
            if (ord(char) + n) <= ord('M'):
                # First half was shifted backward by n, so we shift forward
                shifted = ord(char) + n
                while shifted > ord('Z'):
                    shifted -= 26
                decrypted_char = chr(shifted)
            else:
                # Second half was shifted forward by m^2, so we shift back
                shifted = ord(char) - (m ** 2)
                while shifted < ord('A'):
                    shifted += 26
                decrypted_char = chr(shifted)
        else:
            # Special characters and numbers remain unchanged
            decrypted_char = char
        decrypted.append(decrypted_char)
    return ''.join(decrypted)


def check_correctness(original, decrypted):
    return original == decrypted


def main():
    # Get user inputs
    try:
        n = int(input("Enter the first encryption parameter (n): "))
        m = int(input("Enter the second encryption parameter (m): "))
    except ValueError:
        print("Please enter valid integers for n and m.")
        return

    # Read the original file
    try:
        with open("raw_text.txt", "r") as file:
            original_text = file.read()
    except FileNotFoundError:
        print("Error: raw_text.txt not found.")
        return

    # Encrypt the text
    encrypted_text = encrypt_text(original_text, n, m)

    # Write encrypted text to file
    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted_text)

    # Decrypt the text
    decrypted_text = decrypt_text(encrypted_text, n, m)

    # Check correctness
    is_correct = check_correctness(original_text, decrypted_text)

    print("\nEncryption and decryption completed!")
    print(f"Original and decrypted texts match: {is_correct}")

    # Optionally show samples
    print("\nSample comparison:")
    print("Original (first 50 chars):", original_text[:50])
    print("Decrypted (first 50 chars):", decrypted_text[:50])


if __name__ == "__main__":
    main()