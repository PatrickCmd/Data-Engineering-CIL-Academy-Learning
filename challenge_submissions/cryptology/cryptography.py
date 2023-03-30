import random, time


def encrypt(plaintext, key):
    """A basic encryption algorithm to cipher a text with a given key number"""
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = ""
    for i in range(0, len(plaintext)):
        character = plaintext[i]
        ciphertext = ciphertext + character
        for j in range(0, key):
            ciphertext = ciphertext + random.choice(alphabet)

    return ciphertext


def decrypt(ciphertext, key):
    """Given a key, decrypt a given ciphertext"""
    plaintext = ""
    cipher_len = len(ciphertext)
    i = 0
    while i < cipher_len:
        plaintext = plaintext + ciphertext[i]
        i += key + 1

    return plaintext


def print_menu():
    menu = """
    Choose either 1 or 2 to carry out any of the procedures
    0 to exit
    
    1. Cipher(Encrypt) text
    2. Decrypt text
    0. Exit
    """
    print(menu)


if __name__ == "__main__":
    while True:
        print_menu()

        try:
            choice = int(input("Please select choice from the menu: "))
        except ValueError as e:
            print(str(e))
            continue

        if choice == 0:
            break
        elif choice == 1:
            plaintext = input("Enter a message to encrypt (plaintext): ")
            key = int(input("Input a key as a number between 1 and 10: "))

            while not (key >= 1 and key <= 10):
                print("Invalid key, try again!")
                key = int(input("Input a key as a number between 1 and 10: "))

            print("....")
            time.sleep(1)
            print("Encrypting plaintext...")
            time.sleep(1)
            print("....")
            time.sleep(1)
            ciphertext = encrypt(plaintext, key)
            print(f"Ciphertext: {ciphertext}")
        elif choice == 2:
            ciphertext = input("Enter a text to decrypt (ciphertext): ")
            key = int(input("Input a key as a number between 1 and 10: "))

            while not (key >= 1 and key <= 10):
                print("Invalid key, try again!")
                key = int(input("Input a key as a number between 1 and 10: "))

            print("....")
            time.sleep(1)
            print("Decrypting Ciphertext...")
            time.sleep(1)
            print("....")
            time.sleep(1)
            plaintext = decrypt(ciphertext, key)
            print(f"Plaintext: {plaintext}")
        else:
            print("Invalid choice, please try again!")
