import random

p = int(input("Enter P value : ")) 
q = int(input("Enter Q value : "))

def prime_or_not_for_a(p):
    if p <= 1:
        return False
    if p == 2:
        return True
    for i in range(2, p):
        if p % i == 0:
            print("The given number of P is not a prime number")
            return False
    return True

def prime_or_not_for_b(q):
    if q <= 1:
        return False
    if q == 2:
        return True
    for i in range(2, q): 
        if q % i == 0:
            print("The given number of Q is not a prime number")
            return False
    return True

a = prime_or_not_for_a(p)
b = prime_or_not_for_b(q)

# Ensure both numbers are prime
if a and b: 
    n = p * q
    pi = (p - 1) * (q - 1)  

    print("n value is : ", n)
    print("pi value is : ", pi)

    # To find the factors of pi
    list_1_equal = []
    list_2_not_factors = []

    def factors(numbers):
        for i in range(2, numbers):
            if numbers % i == 0:
                list_1_equal.append(i)
            else:
                list_2_not_factors.append(i)
        print(list_1_equal)
        return list_2_not_factors

    numbers = pi
    print(factors(numbers))
    remaining = []
    for j in list_2_not_factors:
        if all(j % i != 0 for i in list_1_equal):
            remaining.append(j)
    print("remaining : ",remaining[1])

    if remaining:
        e = random.choice(list(set(remaining)))
        print("e value is : ", e)
        public_key = (e, n)
        print("public key: ", public_key)

        # To find d value
        
        d = ""
        for i in range(1, pi):
            mul = e * i
            if mul % pi == 1:
                d = str(i)
                break 

        private_key = (int(d), n)
        print("private key:", private_key)
        plaintext = random.randint(public_key[0], public_key[1])
        print("plaintext : ", plaintext)

        # Encryption function 
        def encryption(plaintext):
            return (plaintext ** e) % n

        cipher_text = encryption(plaintext)
        print("cipher text : ", cipher_text)

        # Decryption function
        def decryption(cipher_text):
            return (cipher_text ** int(d)) % n

        plain_text = decryption(cipher_text)
        print("plain text : ", plain_text)
    else:
        print("No valid 'e' value found.")
        
else:
    print("Both numbers should be prime.")