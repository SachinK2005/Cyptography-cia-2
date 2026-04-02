# main.py
# Running Key Cipher implementation
# cipher assigned: Running Key (roll number mod 10 = 5)

from hash_function import fnv1a_hash

# running key - passage from Pride and Prejudice
KEY = "It is a truth universally acknowledged that a single man in possession of a good fortune must be in want of a wife however little known the feelings or views of such a man may be on his first entering a neighbourhood this truth is so well fixed in the minds of the surrounding families"


def remove_non_alpha(text):
    out = ""
    for c in text:
        if c.isalpha():
            out += c.upper()
    return out


def running_key_encrypt(plaintext, key):
    plain = remove_non_alpha(plaintext)
    k     = remove_non_alpha(key)

    if len(k) < len(plain):
        print("ERROR: key too short")
        return ""

    result = ""
    for i in range(len(plain)):
        p = ord(plain[i]) - 65
        ki = ord(k[i]) - 65
        c = (p + ki) % 26
        result += chr(c + 65)
    return result


def running_key_decrypt(ciphertext, key):
    cipher = remove_non_alpha(ciphertext)
    k      = remove_non_alpha(key)

    if len(k) < len(cipher):
        print("ERROR: key too short")
        return ""

    result = ""
    for i in range(len(cipher)):
        c  = ord(cipher[i]) - 65
        ki = ord(k[i]) - 65
        p  = (c - ki + 26) % 26
        result += chr(p + 65)
    return result


def print_example(title, plaintext):
    plain  = remove_non_alpha(plaintext)
    enc    = running_key_encrypt(plain, KEY)
    digest = fnv1a_hash(enc)
    dec    = running_key_decrypt(enc, KEY)
    print(f"\n{title}")
    print(f"  Plaintext  : {plain}")
    print(f"  Key used   : {remove_non_alpha(KEY)[:len(plain)]}")
    print(f"  Ciphertext : {enc}")
    print(f"  FNV1a Hash : {digest}")
    print(f"  Decrypted  : {dec}")


if __name__ == "__main__":
    print("=========================================")
    print("        Running Key Cipher")
    print("=========================================")
    print(f"\nKey (Pride and Prejudice excerpt):\n  \"{KEY[:55]}...\"")

    print_example("Example 1:", "HELLO WORLD")
    print_example("Example 2:", "DATA SECURITY")

    print("\n=========================================")
    print("          Encrypt / Decrypt")
    print("=========================================")

    while True:
        print("\n1. Encrypt")
        print("2. Decrypt")
        print("3. Quit")
        ch = input("Choice: ").strip()

        if ch == "1":
            msg = input("Enter message: ").strip()
            enc = running_key_encrypt(msg, KEY)
            if enc:
                print("Ciphertext :", enc)
                print("FNV1a Hash :", fnv1a_hash(enc))

        elif ch == "2":
            msg = input("Enter ciphertext: ").strip()
            dec = running_key_decrypt(msg, KEY)
            if dec:
                print("Plaintext  :", dec)

        elif ch == "3":
            break
        else:
            print("Invalid option.")
