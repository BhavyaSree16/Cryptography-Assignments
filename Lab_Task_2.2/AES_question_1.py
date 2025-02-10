from Crypto.Cipher import AES
from secrets import token_bytes


key = token_bytes(16)

def aes_encrypt(msg):
    
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('utf-8'))
    return nonce, ciphertext, tag

def aes_decrypt(nonce, ciphertext, tag):
    
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('utf-8')
    except:
        return False

print("1. Encrypt a text message")
print("2. Encrypt a file")

ip = int(input('Choose an option: '))

if ip == 1:
    message = input("Enter a message to encrypt: ")
    nonce, ciphertext, tag = aes_encrypt(message)
    plaintext = aes_decrypt(nonce, ciphertext, tag)

    print(f"\nEncrypted Data Saved to 'Encrypted_File.txt'")
    
    with open("./Cryptography_assignment-1/Lab_Task_3/Encrypted_File.txt", 'wb') as enc_file:
        enc_file.write(nonce + ciphertext + tag)

    with open("./Cryptography_assignment-1/Lab_Task_3/Decrypted_File.txt", 'w') as dec_file:
        dec_file.write(plaintext if plaintext else "Message is corrupted")

elif ip == 2:
    filename = input('Enter filename (including path & extension): ')
    
    try:
        with open(f'./Cryptography_assignment-1/Lab_Task_3/{filename}', 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print("File not found! Please check the filename.")
        exit()

    nonce, ciphertext, tag = aes_encrypt(content)
    plaintext = aes_decrypt(nonce, ciphertext, tag)

    
    with open("./Cryptography_assignment-1/Lab_Task_3/Encrypted_File.txt", 'wb') as enc_file:
        enc_file.write(nonce + ciphertext + tag)

    
    with open("./Cryptography_assignment-1/Lab_Task_3/Decrypted_File.txt", 'w', encoding='utf-8') as dec_file:
        dec_file.write(plaintext if plaintext else "Message is corrupted")

    print(f"\n Encrypted Data saved to 'Encrypted_File.txt'")
    print(f" Decrypted Data saved to 'Decrypted_File.txt'")

else:
    print(" Enter a valid option")