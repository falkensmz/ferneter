# file encryptor using fernet
# falkensmz : date of creation : 01/24/22

from cryptography.fernet import Fernet
try:
    name = input("enter file name > ")
    file = open(name, "r")
    code = file.read()

    key = Fernet.generate_key()
    f = Fernet(key)
    print("")
    print("[!] Make sure to save this key > ", key)
    code_in_bytes = bytes(code, 'utf-8')
    token = f.encrypt(code_in_bytes)
    encrypted_file = open("encrypted_file.txt", "wb")
    encrypted_file.write(token)
    encrypted_file.close()
except KeyboardInterrupt:
    print("")
    print("[!] Ctrl+C detected. Closing script ...")
    exit()
