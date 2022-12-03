import random
from Crypto.Util import number

# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a


def modInverse(A, M):
    for X in range(1, M):
        if (((A % M) * (X % M)) % M == 1):
            return X
    return -1


def part1():
    p = number.getPrime(2018)
    q = number.getPrime(2018)

    n = p * q
    fn = (p-1) * (q-1)

    e = 65537
    # d = modInverse(e, fn)
    d = pow(e, -1, fn)

    public_key = (e, n)
    private_key = (d, n)
    print("public key: ", public_key)
    print("private key: ", private_key)

    message = random.randrange(100, 1000)
    print("message is: ", message)

    ciphertext = pow(message, e, n) 
    print("Encripted cipher: ", ciphertext)

    plaintext = pow(ciphertext, d, n) 
    print("plaintext: ", plaintext, end="\n\n")


def part2():
    n = 14
    e = 5
    d = 11

    # bob
    s = 2
    c_bob = pow(s, e, n)  # sentt
    print("Bob sent c ", c_bob)

    # mal
    random = 3
    c_mal = c_bob * pow(random, e, n)  # sent
    print("Mal sent c' ", c_mal)

    # ali
    s_ali = pow(c_mal, d, n)  # sent
    print("Alice sent back ", s_ali)

    # mal (decrypts)
    res = (s_ali * modInverse(random, n)) % n
    print("Mal decrypt original message as ", res)


if __name__ == "__main__":
    part1()
    part2()
