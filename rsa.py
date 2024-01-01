import random
import math

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2+1):
        if number  % i == 0:
            return False
    return True

def generate_prime(min_value, max_value):
    prime = random.randint(min_value, max_value)
    while not is_prime(prime):
        prime = random.randint(min_value, max_value)
    return prime

def mod_inverse(e, phi):
    for d in range (3, phi):
        if (d * e) % phi == 1:
            return d
    raise ValueError("mod_inverse does not exist")

x, y = generate_prime(10000, 15000), generate_prime(10000, 15000)

while x == y:
    y = generate_prime(10000, 15000)

n = x * y
phi_n = (x-1) * (y-1)

e = random.randint(3, phi_n-1)
while math.gcd(e, phi_n) !=1:
    e = random.randint(3, phi_n-1)


d = mod_inverse (e, phi_n)


print("Public key: ", e)
print("Private key: ", d)
print("n: ", n)
print("Phi of n: ", phi_n)
print("x: ", x)
print("y: ", y)

message = "Hello Phillip"

message_encoded = [ord(ch) for ch in message]

## (m ^ e) mod n = c
ciphertext = [pow(ch, e, n) for ch in message_encoded]

print("This is the ciphertext: ",ciphertext)

message_encoded = [pow(ch, d, n) for ch in ciphertext]
message = "".join(chr(ch) for ch in message_encoded)

print("This is the message: ", message)