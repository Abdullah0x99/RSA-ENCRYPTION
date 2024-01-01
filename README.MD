An algorithm for asymmetric encryption, simply means we have a public key and a private key for encryption and decryption instead of one key for both encryption and decryption.

Basic knowledge
-----------------------
Modular operations

Prime numbers: Numbers divisible by 1 and Itself.

Greatest common divisor

How Encryption and Decryption works
---------------------------------------
Let's say John wants to send a message to Phillips and doesn't want Gabriel to see what's written in the message, then we'll have to encrypt the message in a way that only John and Phillips can know what the message says.
So what John will do is encrypt the message:
let's say c= ciphertext, E = Enrypt, m = message, D = Decrypt

So John will use the function E(m) = c to encrypt the message into a ciphertext so anyone listening can't understand what the message says. Where E is the encryption algorithm being used and m is the message being encrypted and c is the ciphertext.

Then Phillip will use the function D(c) = m to Decrypt the message where D is equal to the decryption algorithm being used and c is the cipher-text being decrypted and m is the message that was sent by John.

How Symmetric Encryption works
--------------------------------
This will be John and Phillips both having a shared secret key, let's call it K, then John can encrypt the message by using the function E(K,m) = c. Where E is the encryption algorithm being used and K is the secret key and m is the message being encrypted and c is the ciphertext.

To decrypt the ciphertext that was sent to John, Phillips will have to use the function D(K,c) = m. Where D is the decryption algorithm being used and K is the shared private key and c is the cipher-text being decrypted and m is the message.

How Asymmetric Encryption Works
--------------------------------
This method involves both the sender and receiver having a key pair(Public key and Private/secret key). This means John will have a Public key and a private key, and Phillip will also have a public key and a private key. The main gist here is Public key can be known by everyone but the private key needs to remain private. 

The main getaway here is whenever John wants to send a message to Phillips, he encrypts the message with Phillips public key using the function E(PubK.Ph, m) = c. Where E is the encryption algorithm, PubK is the Public key, Ph is Phillips, m is the message and c is the ciphertext.

For Philiphs to decrypt the cipher text, he'll do that using his private key using the decryption function D(PriK.Ph, c) = m. Where D is the decryption function, PriK is the private key, Ph is Phillips, c is the ciphertext, and m is the message.

Using Asymmetric encryption, the only way to decrypt a cipher-text is by using the receiver private key(in our case, Phillips private key)

Also if John wants to send a clear text message to Phillips and wants Phillips to know that the message came from him without any alteration to the message, John needs to add a signature to the message using his private key then Phillips will use John's Public key to verify that the message came from John. 


How do we come up with a Public key and Private key using RSA encryption?
----------------------------
PRIME NUMBERS! 
Yes, to generate a Private and Public key, we need to use LARGE prime numbers but in this tutorial, we'll be making use of small prime numbers so we can understand this easily.

Let's Generate a Private key for John
--------------------------------------
We'll get the products two prime numbers, let's say X and Y where X = 11 and Y = 13.
n = X * Y  
n = 11 * 13
n = 143
where n is the product of two numbers X * Y which simply means n cannot be prime since it's divisible by 2.

The next thing we have to do is calculate Euler's totient function, what this function does is tell us numbers that are smaller than n that are co-prime to n. 

Co-prime: Two numbers are said to be "co-prime" (or "relatively prime") if their greatest common divisor (GCD) is 1

Phi(n) =  Phi(X*Y)
       =  Phi(X) * Phi(Y)
        Now to calculate Phi(n), this is what we need to do.
       =  (X-1) * (Y-1)
       In this case, our Phi(n) is
           = (11-1) * (13-1)
           = 10 * 12
     Phi(n) = 120
         
So these following keys are going to stay secret X, Y, Phi(n) because if they are known, the other values can easily be  cracked. The Phi(n) is what we are going to use to generate our public key.
 
N can be known by others as it doesn't affect anything.

To generate our public key "e" we simply use

2 < e < Phi(n) where the gcd(e, Phi(n)) = 1 : in other words, Co-prime.

So with this, the number e that we are going to pick doesn't have anything that divides it that also divides Phi(n).

Let's say e = 7
e is a prime number and our Phi(n) is not divisible by e so they are co-prime.
Where e is greater than 2 and less than Phi(n) and therefore a co-prime to 120.
Our public key is 7

To get our private key, we multiply e by d where d is our private key, and get a remainder of 1 if we divide by Phi(n).

In our case,
e * d = 1 mod 120
our d is going to be 103
Therefore,
7 * 103 = 721
so d/Phi(n) which is 721/120 = 6 mod 1
From this, it is very difficult to find what d is based on n and e because they don't have Phi(n).
This calculation is easy if Phi(n) is known
 e = 7 --> Public key
 d = 103-> Private key
 Now we've generated a Public and Private key for John, Phillips will go through the same steps to generate his own Public and private keys with different Large prime numbers.

NB: We are using small prime numbers for the sake of understanding this tutorial.

How do we use these keys to Encrypt and decrypt messages?
--------------------------------------------------------
Let's say Phillips wants to send an encrypted message(m = 15) to John.

Phillip applies the encryption formula c = m^e mod n; where c is the cipher text, m is the message and e is the public key.
Remember, Phillips knows the value of 
e = 7
n = 143; since they are all public information.
Therefore, Phillips will use this calculation to get the cipher-text
c = 15^7 mod 143
c = 115

For John to get Phillip's message from the cipher-text, he uses this formula
m = c^d mod n
m = 115^103 mod 143
m = 15

How do we use these keys to add a signature to the message?
 Let's say John wants to add a signature to a message(m = 15) before sending it to Phillip
    S = m^d mod n
        = 15^103 mod 143
        = 141
   
Phillips will verify the signature with the public key.
    m = S^e mod n
    m = 141^7 mod 143
    m = 15
    
So that's how encryption, decryption, and signature works. Now let's code this using Python

 

Learning Materials:
[YOUTUBE](https://www.youtube.com/watch?v=D_PfV_IcUdA)
