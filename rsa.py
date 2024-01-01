import random
import math

#function to check if a number is prime
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2+1):
        if number  % i == 0:
            return False
    return True

#function to generate a random prime number
def generate_prime(min_value, max_value):
    prime = random.randint(min_value, max_value)
    while not is_prime(prime):
        prime = random.randint(min_value, max_value)
    return prime

#function to find the modular inverse of e modulo phi
def mod_inverse(e, phi):
    for d in range (3, phi):
        if (d * e) % phi == 1:
            return d
    raise ValueError("mod_inverse does not exist")

#Generate two distinct prime numbers x and y
x, y = generate_prime(10000, 15000), generate_prime(10000, 15000)

#making sure x and y are distinct
while x == y:
    y = generate_prime(10000, 15000)

#calculate the product of x and y and Euler's totient function (phi_n)
n = x * y
phi_n = (x-1) * (y-1)


#Generate a random public key e such that 1 < e < phi_n and gcd(e, phi_n) = 1

e = random.randint(3, phi_n-1)
while math.gcd(e, phi_n) !=1:
    e = random.randint(3, phi_n-1)

#Calculate the private key d using the modular inverse of e modulo phi_n

d = mod_inverse (e, phi_n)

#Public and Private key components
print("Public key: ", e)
print("Private key: ", d)
print("n: ", n)
print("Phi of n: ", phi_n)
print("x: ", x)
print("y: ", y)

#Encrypting message

message = "Hello Phillip"
message_encoded = [ord(ch) for ch in message]

## (m ^ e) mod n = c
ciphertext = [pow(ch, e, n) for ch in message_encoded]

print("This is the ciphertext: ",ciphertext)

#Decrypting the message

message_encoded = [pow(ch, d, n) for ch in ciphertext]
message = "".join(chr(ch) for ch in message_encoded)

print("This is the message: ", message)
