# file decryptor using fernet
# falkensmz : date of creation : 01/24/22

from cryptography.fernet import Fernet

try:
    name = input("enter file name to decrypt > ")
    file = open(name, "rb")
    encrypted_file = file.read()

    key = input("provide key to decrypt > ")
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_file)
    final = open("decrypted_file.txt", "wb")
    final.write(decrypted)
    final.close()
except KeyboardInterrupt:
    print("")
    print("[!] Ctrl+C detected. Closing script ...")
    exit()