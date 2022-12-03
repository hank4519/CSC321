import random
from Crypto.Hash import SHA256

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def part1():
    p = 37
    g = 5

    x = random.randint(1, p - 2)
    y = random.randint(1, p - 2)
    print("p = " + str(p))
    print("g = " + str(g))
    print("x = " + str(x))
    print("y = " + str(y))

    A = pow(g, x) % p
    B = pow(g, y) % p
    print("\n")
    print("A = " + str(A))
    print("B = " + str(B))

    s1 = pow(A, y) % p
    s2 = pow(B, x) % p
    print("\n")
    print("s1 = " + str(s1))
    print("s2 = " + str(s2))

    k = SHA256.new()
    k.update(bytes(s1))
    truncate_k = bytes(k.hexdigest()[0:16], encoding='utf8')
    print("The key is " + truncate_k.decode('utf8'))

    iv = get_random_bytes(16)
    alice_message = pad(bytes("Hi Bob!", encoding='utf8'), AES.block_size)
    bob_message = pad(bytes("Hi Alice!", encoding='utf8'), AES.block_size)
    print("\n")
    print(unpad(alice_message, AES.block_size))
    print(unpad(bob_message, AES.block_size))

    cipher = AES.new(truncate_k, AES.MODE_CBC, iv)
    alice_ciphertext = cipher.encrypt(alice_message)
    print("\n")
    print("Alice's ciphertext: ", end="")
    print(alice_ciphertext)

    cipher = AES.new(truncate_k, AES.MODE_CBC, iv)
    bob_ciphertext = cipher.encrypt(bob_message)
    print("Bob's ciphertext: ", end="")
    print(bob_ciphertext)

    cipher = AES.new(truncate_k, AES.MODE_CBC, iv)
    bob_message = cipher.decrypt(bob_ciphertext)
    print("\n")
    print("Bob's message: ", end="")
    print(unpad(bob_message, AES.block_size))

    cipher = AES.new(truncate_k, AES.MODE_CBC, iv)
    alice_message = cipher.decrypt(alice_ciphertext)
    print("Alice's message: ", end="")
    print(unpad(alice_message, AES.block_size))

def part2():
    p = "B10B8F96A080E01DDE92DE5EAE5D54EC52C99FBCFB06A3C69A6A9DCA52D23B616073E28675A23D189838EF1E2EE652C013ECB4AEA906112324975C3CD49B83BFACCBDD7D90C4BD7098488E9C219A73724EFFD6FAE5644738FAA31A4FF55BCCC0A151AF5F0DC8B4BD45BF37DF365C1A65E68CFDA76D4DA708DF1FB2BC2E4A4371"
    g = "A4D1CBD5C3FD34126765A442EFB99905F8104DD258AC507FD6406CFF14266D31266FEA1E5C41564B777E690F5504F213160217B4B01B886A5E91547F9E2749F4D7FBD7D3B9A92EE1909D0D2263F80A76A6A24C087A091F531DBF0A0169B6A28AD662A4D18E73AFA32D779D5918D08BC8858F4DCEF97C2A24855E6EEB22B3B2E5"
    p = int.from_bytes(bytes(p, encoding="utf8"), "big")
    g = int.from_bytes(bytes(g, encoding="utf8"), "big")

    x = random.randint(1, p - 2)
    y = random.randint(1, p - 2)

    A = pow(g, x, p)
    B = pow(g, y, p)
    print("\n")
    print("A = " + str(A))
    print("B = " + str(B))

    s1 = pow(A, y, p)
    s2 = pow(B, x, p)
    print("\n")
    print("s1 = " + str(s1))
    print("s2 = " + str(s2))

    k = SHA256.new(bytes(str(s1), encoding='utf8'))
    truncate_k = bytes(k.hexdigest()[0:16], encoding='utf8')
    print("The key is " + truncate_k.decode('utf8'))

    iv = get_random_bytes(16)
    alice_message = pad(bytes("Hi Bob!", encoding='utf8'), AES.block_size)
    bob_message = pad(bytes("Hi Alice!", encoding='utf8'), AES.block_size)
    print("\n")
    print(unpad(alice_message, AES.block_size))
    print(unpad(bob_message, AES.block_size))

    cipher = AES.new(truncate_k, AES.MODE_CBC, iv)
    alice_ciphertext = cipher.encrypt(alice_message)
    print("\n")
    print("Alice's ciphertext: ", end="")
    print(alice_ciphertext)

    cipher = AES.new(truncate_k, AES.MODE_CBC, iv)
    bob_ciphertext = cipher.encrypt(bob_message)
    print("Bob's ciphertext: ", end="")
    print(bob_ciphertext)

    cipher = AES.new(truncate_k, AES.MODE_CBC, iv)
    bob_message = cipher.decrypt(bob_ciphertext)
    print("\n")
    print("Bob's message: ", end="")
    print(unpad(bob_message, AES.block_size))

    cipher = AES.new(truncate_k, AES.MODE_CBC, iv)
    alice_message = cipher.decrypt(alice_ciphertext)
    print("Alice's message: ", end="")
    print(unpad(alice_message, AES.block_size))

if __name__ == "__main__":

    part1()
    part2()

